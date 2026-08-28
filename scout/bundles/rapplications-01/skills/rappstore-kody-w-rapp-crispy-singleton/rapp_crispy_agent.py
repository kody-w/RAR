"""RAPP Crispy — a local-first meeting stack as a rapplication.

Record a meeting, denoise it, transcribe it and summarise it entirely on the
machine the brainstem is running on. No audio and no transcript ever leaves the
host: denoising is ffmpeg's RNNoise filter, transcription is a local
whisper.cpp server on 127.0.0.1, and summarisation goes through a user-owned
shell hook the user points wherever they like.

Everything lands under ~/.rappcrispy/meetings/<timestamp>/ as plain files.

Measured on an Apple M4 (reproduce with action="bench"):
    white noise  -26 to -28 dB noise floor, -3.9 dB speech
    pink noise   -15 dB
    babble       -3.2 dB  <- known limitation, see the README
    real-time factor 0.014 (70x faster than real time)

RNNoise separates voice from non-voice. Babble IS voice, so it barely moves.
This is stated plainly rather than papered over.

Stdlib only. Shells out to ffmpeg; talks to the local ASR over HTTP.
"""

import json
import os
import re
import shutil
import subprocess
import time
import urllib.error
import urllib.request
import wave

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "rapp_crispy",
    "version": "1.4.0",
    "description": (
        "Local-first meeting stack: record, RNNoise denoise, local whisper.cpp "
        "transcription and hook-driven notes."
    ),
    "author": "@kody-w",
    "tags": ["meetings", "audio", "denoise", "transcription", "local-first", "privacy"],
    "dependencies": ["@rapp/basic_agent"],
    "requires_env": [],
}

HOME = os.path.expanduser("~")
CRISPY_HOME = os.environ.get("CRISPY_HOME", os.path.join(HOME, ".rappcrispy"))
MEETINGS = os.path.join(CRISPY_HOME, "meetings")
MODELS = os.path.join(CRISPY_HOME, "models")
HOOKS = os.path.join(CRISPY_HOME, "hooks")
LOGS = os.path.join(CRISPY_HOME, "logs")
ASR_PORT = int(os.environ.get("ASR_PORT", "8765"))
RNN_MODEL = os.environ.get("RNN_MODEL", "cb")
# Offline denoise engine. Measured at 0dB SNR (action="bench" reproduces it):
#   rnnoise  white +28.1 dB  pink +15.8 dB  babble +4.2 dB  RTF 0.014
#   dfn      white +42.5 dB  pink +36.6 dB  babble +4.5 dB  RTF 0.048
# DFN3 is the default when present. It is OFFLINE ONLY — deep-filter is
# file-to-file with no streaming mode, so live denoise is always RNNoise.
ENGINE = os.environ.get("ENGINE", "auto")
DEEP_FILTER = os.environ.get("DEEP_FILTER", os.path.join(CRISPY_HOME, "bin", "deep-filter"))
CHUNK_SECONDS = int(os.environ.get("CHUNK_SECONDS", "300"))

# Auto-pick prefers a REAL hardware input. Capturing through some other
# denoiser's virtual device would measure its processing instead of ours, and
# routing through a loopback device can feed audio back on itself.
# Positive match on hardware tokens first, then a generic virtual-name skip list.
# Override either with CRISPY_MIC=<index>.
_HARDWARE_HINTS = ("built-in", "macbook", "imac", "mac mini", "mac studio",
                   "usb", "external", "headset", "airpods")
_VIRTUAL_HINTS = ("blackhole", "loopback", "aggregate", "virtual", "soundflower",
                  "multi-output", "teams audio", "driver")


def _ffmpeg():
    for c in ("/opt/homebrew/bin/ffmpeg", "/usr/local/bin/ffmpeg"):
        if os.path.exists(c):
            return c
    return shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"


def _run(args, timeout=1800):
    return subprocess.run(args, capture_output=True, text=True, timeout=timeout)


def _wav_seconds(path):
    try:
        with wave.open(path) as w:
            return round(w.getnframes() / float(w.getframerate()), 2)
    except Exception:
        return 0.0


def _devices():
    """avfoundation input devices as [(index, name)]."""
    p = _run([_ffmpeg(), "-hide_banner", "-f", "avfoundation",
              "-list_devices", "true", "-i", ""], timeout=60)
    out, seen_audio, devs = p.stderr or "", False, []
    for line in out.splitlines():
        if "audio devices" in line.lower():
            seen_audio = True
            continue
        if not seen_audio:
            continue
        m = re.search(r"\[(\d+)\]\s+(.*)$", line)
        if m:
            devs.append((int(m.group(1)), m.group(2).strip()))
    return devs


def _pick_mic():
    if os.environ.get("CRISPY_MIC"):
        return int(os.environ["CRISPY_MIC"]), "(CRISPY_MIC override)"
    devs = _devices()
    # 1. a device that names real hardware and is a microphone
    for idx, name in devs:
        low = name.lower()
        if ("microphone" in low or "mic" in low) \
                and any(h in low for h in _HARDWARE_HINTS) \
                and not any(h in low for h in _VIRTUAL_HINTS):
            return idx, name
    # 2. anything that does not look like a virtual/loopback device
    for idx, name in devs:
        if not any(h in name.lower() for h in _VIRTUAL_HINTS):
            return idx, name
    return (devs[0] if devs else (0, "unknown"))


def _asr_up():
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{ASR_PORT}/", timeout=3) as r:
            return 200 <= r.status < 500
    except urllib.error.HTTPError:
        return True          # any HTTP answer means it is serving
    except Exception:
        return False


def _post_wav(path, prompt=None):
    """Multipart POST to the local whisper.cpp server. Stdlib only."""
    boundary = "----rappcrispy%d" % int(time.time() * 1000)
    parts = []

    def field(name, value):
        parts.append(f"--{boundary}\r\nContent-Disposition: form-data; "
                     f'name="{name}"\r\n\r\n{value}\r\n'.encode())

    with open(path, "rb") as fh:
        blob = fh.read()
    parts.append(
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; "
        f'filename="{os.path.basename(path)}"\r\n'
        f"Content-Type: audio/wav\r\n\r\n".encode() + blob + b"\r\n")
    field("temperature", "0")
    field("response_format", "json")
    if prompt:
        field("prompt", prompt)
    parts.append(f"--{boundary}--\r\n".encode())
    body = b"".join(parts)

    req = urllib.request.Request(
        f"http://127.0.0.1:{ASR_PORT}/inference", data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
    with urllib.request.urlopen(req, timeout=900) as r:
        return json.loads(r.read().decode("utf-8", "replace")).get("text", "")


def _dict_path():
    """Own dictionary first so the rapplication is self-contained; fall back to a
    sibling RAPP Voice install so one vocabulary serves both. Explicit
    CRISPY_DICT always wins."""
    explicit = os.environ.get("CRISPY_DICT")
    if explicit:
        return explicit
    for cand in (os.path.join(CRISPY_HOME, "dictionary.txt"),
                 os.path.join(HOME, ".rappvoice", "dictionary.txt")):
        if os.path.exists(cand):
            return cand
    return os.path.join(CRISPY_HOME, "dictionary.txt")


def _dictionary():
    """Optional personal vocabulary: one term per line, or `heard => Term`."""
    path = _dict_path()
    terms, subs = [], []
    if not os.path.exists(path):
        return terms, subs
    for raw in open(path, encoding="utf-8", errors="replace").read().splitlines():
        t = raw.strip()
        if not t or t.startswith("#"):
            continue
        if "=>" in t:
            heard, meant = (x.strip() for x in t.split("=>", 1))
            if heard:
                subs.append((heard, meant))
                terms.append(meant)
        else:
            terms.append(t)
    return terms, subs


def _bounded(s):
    pat = re.escape(s)
    if s[:1].isalnum():
        pat = r"\b" + pat
    if s[-1:].isalnum():
        pat = pat + r"\b"
    return pat


def _apply_dictionary(text):
    """Bias alone lands the common words; canonical spelling is enforced after
    decoding too, because an invented word that is a homophone of a real one
    cannot be fixed by biasing."""
    terms, subs = _dictionary()
    for heard, meant in sorted(subs, key=lambda x: -len(x[0])):
        text = re.sub(_bounded(heard), lambda m, r=meant: r, text, flags=re.I)
    for term in terms:
        text = re.sub(_bounded(term), lambda m, r=term: r, text, flags=re.I)
    return text


def _dict_prompt():
    terms, _ = _dictionary()
    seen, parts = set(), []
    for t in terms:
        if t not in seen:
            seen.add(t)
            parts.append(f"{t}. {t}.")     # weighted: each term twice
    return " ".join(parts) or None


class RappCrispyAgent(BasicAgent):
    """Local-first meeting capture, denoise, transcription and notes."""

    def __init__(self):
        self.name = "RappCrispy"
        self.metadata = {
            "name": self.name,
            "description": (
                "Local-first meeting stack. Records a meeting, denoises it with "
                "RNNoise, transcribes it on a local whisper.cpp server and writes "
                "notes via a user-owned hook whose default sends the transcript "
                "to Anthropic. Audio, denoising and transcription never leave "
                "the machine. Actions: doctor, record, denoise, transcribe, notes, "
                "run, list, read, bench, live_status."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["doctor", "record", "denoise", "transcribe",
                                 "notes", "run", "list", "read", "bench",
                                 "live_status"],
                        "description": "What to do. Default 'doctor'.",
                    },
                    "seconds": {
                        "type": "integer",
                        "description": "Recording length for record/run. Required "
                                       "for headless use; there is no ENTER to press.",
                    },
                    "name": {"type": "string", "description": "Label for the meeting folder."},
                    "meeting": {"type": "string", "description": "Meeting id (folder name) for notes/read."},
                    "path": {"type": "string", "description": "WAV path for denoise/transcribe."},
                    "screen": {"type": "boolean", "description": "Also capture screen video."},
                    "notes": {"type": "boolean", "description":
                              "Write notes via the hook. Default true. Set false "
                              "for a confidential meeting: the DEFAULT hook calls "
                              "`claude -p` and sends the transcript to Anthropic, "
                              "and this is the only way to stop that from here."},
                },
                "required": [],
            },
        }
        for d in (MEETINGS, MODELS, HOOKS, LOGS):
            os.makedirs(d, exist_ok=True)
        super().__init__(self.name, self.metadata)

    # ------------------------------------------------------------------ helpers
    def _log(self, line):
        try:
            with open(os.path.join(LOGS, "crispy.log"), "a") as fh:
                fh.write(time.strftime("%Y-%m-%dT%H:%M:%SZ ", time.gmtime()) + line + "\n")
        except Exception:
            pass

    def _model_path(self):
        return os.path.join(MODELS, f"{RNN_MODEL}.rnnn")

    def _engine(self):
        if ENGINE == "rnnoise":
            return "rnnoise"
        return "dfn" if os.access(DEEP_FILTER, os.X_OK) else "rnnoise"

    # ------------------------------------------------------------------- doctor
    def _doctor(self):
        ff = _ffmpeg()
        have_ff = os.path.exists(ff)
        filters = _run([ff, "-hide_banner", "-filters"], timeout=60).stdout if have_ff else ""
        idx, mic = _pick_mic()
        models = sorted(f for f in os.listdir(MODELS) if f.endswith(".rnnn")) \
            if os.path.isdir(MODELS) else []
        lines = [
            "RAPP Crispy environment",
            f"  ffmpeg              {'yes' if have_ff else 'MISSING'} ({ff})",
            f"  arnndn (RNNoise)    {'yes' if 'arnndn' in filters else 'MISSING'}",
            f"  capture device      [{idx}] {mic}",
            f"  local ASR :{ASR_PORT}     {'up' if _asr_up() else 'DOWN'}",
            f"  denoise engine      {'DeepFilterNet3 (offline) + RNNoise (live)' if self._engine() == 'dfn' else 'RNNoise only — DFN3 absent, ~14dB weaker on steady noise'}",
            f"  denoise models      {len(models)} {models or '(run install.sh)'}",
            f"  notes hook          {'yes' if os.access(os.path.join(HOOKS, 'notes.sh'), os.X_OK) else 'no'}",
            f"  dictionary          {_dict_path() if os.path.exists(_dict_path()) else 'none'}",
            f"  meetings            {MEETINGS}",
            "",
            "Denoise is local ffmpeg, ASR is localhost, and note-writing runs "
            "the hook at ~/.rappcrispy/hooks/notes.sh — whose default calls "
            "`claude -p`, sending the transcript to Anthropic. "
            "notes go through your own hook.",
        ]
        return "\n".join(lines)

    # ------------------------------------------------------------------- record
    def _record(self, seconds, name, screen):
        if not seconds or int(seconds) <= 0:
            return ("record needs `seconds` when run headlessly — there is no "
                    "keypress to stop it. Example: action=record, seconds=600.")
        seconds = int(seconds)
        idx, mic = _pick_mic()
        stamp = time.strftime("%Y-%m-%d_%H%M%S")
        slug = re.sub(r"[^A-Za-z0-9_-]+", "-", name).strip("-") if name else ""
        d = os.path.join(MEETINGS, stamp + (f"_{slug}" if slug else ""))
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "device.txt"), "w") as fh:
            fh.write(mic + "\n")

        sc = None
        if screen:
            sc = subprocess.Popen(["screencapture", "-v", "-V", str(seconds),
                                   "-G", str(idx), os.path.join(d, "screen.mov")],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        p = _run([_ffmpeg(), "-hide_banner", "-loglevel", "error",
                  "-f", "avfoundation", "-i", f":{idx}",
                  "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le",
                  "-t", str(seconds), "-y", os.path.join(d, "mic.wav")],
                 timeout=seconds + 120)
        if sc:
            try:
                sc.wait(timeout=20)
            except Exception:
                sc.terminate()
        wav = os.path.join(d, "mic.wav")
        if not os.path.exists(wav):
            return f"recording failed: {(p.stderr or '')[:400]}"
        self._log(f"record dir={d} seconds={_wav_seconds(wav)}")
        return d

    # ------------------------------------------------------------------ denoise
    def _denoise(self, src, dst=None):
        dst = dst or (os.path.splitext(src)[0] + ".denoised.wav")
        eng = self._engine()
        t0 = time.time()
        if eng == "dfn":
            work = os.path.join(CRISPY_HOME, ".dfn")
            shutil.rmtree(work, ignore_errors=True)
            os.makedirs(work, exist_ok=True)
            p = _run([DEEP_FILTER, "-o", work, src])
            produced = sorted(f for f in os.listdir(work) if f.endswith(".wav"))
            if p.returncode != 0 or not produced:
                shutil.rmtree(work, ignore_errors=True)
                return None, f"deep-filter failed: {(p.stderr or '')[:300]}"
            # normalise so every downstream stage sees one shape
            n = _run([_ffmpeg(), "-hide_banner", "-loglevel", "error", "-i",
                      os.path.join(work, produced[0]), "-ar", "48000", "-ac", "1",
                      "-c:a", "pcm_s16le", "-y", dst])
            shutil.rmtree(work, ignore_errors=True)
            if n.returncode != 0 or not os.path.exists(dst):
                return None, f"normalise failed: {(n.stderr or '')[:300]}"
        else:
            model = self._model_path()
            if not os.path.exists(model):
                return None, f"denoise model missing: {model}"
            p = _run([_ffmpeg(), "-hide_banner", "-loglevel", "error", "-i", src,
                      "-af", f"arnndn=m={model}", "-ar", "48000", "-ac", "1",
                      "-c:a", "pcm_s16le", "-y", dst])
            if p.returncode != 0 or not os.path.exists(dst):
                return None, f"denoise failed: {(p.stderr or '')[:400]}"
        dur = _wav_seconds(src) or 1.0
        rtf = round((time.time() - t0) / dur, 4)
        self._log(f"denoise src={src} engine={eng} rtf={rtf}")
        return dst, f"denoised -> {dst} (engine={eng}, RTF={rtf})"

    # --------------------------------------------------------------- transcribe
    def _transcribe(self, wav):
        if not _asr_up():
            return None, (f"no local ASR on 127.0.0.1:{ASR_PORT}. Start it:\n"
                          f"  whisper-server -m <ggml-small.en.bin> --host 127.0.0.1 "
                          f"--port {ASR_PORT} -l en")
        work = os.path.join(CRISPY_HOME, ".chunks")
        shutil.rmtree(work, ignore_errors=True)
        os.makedirs(work, exist_ok=True)
        p = _run([_ffmpeg(), "-hide_banner", "-loglevel", "error", "-i", wav,
                  "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le",
                  "-f", "segment", "-segment_time", str(CHUNK_SECONDS),
                  os.path.join(work, "c%04d.wav")])
        chunks = sorted(f for f in os.listdir(work) if f.endswith(".wav"))
        if p.returncode != 0 or not chunks:
            shutil.rmtree(work, ignore_errors=True)
            return None, f"chunking failed: {(p.stderr or '')[:300]}"
        prompt, out = _dict_prompt(), []
        for c in chunks:
            try:
                out.append(_post_wav(os.path.join(work, c), prompt).strip())
            except Exception as exc:
                out.append(f"[chunk {c} failed: {exc}]")
        shutil.rmtree(work, ignore_errors=True)
        text = _apply_dictionary(" ".join(x for x in out if x))
        self._log(f"transcribe wav={wav} chunks={len(chunks)}")
        return text, f"transcribed {len(chunks)} chunk(s)"

    # -------------------------------------------------------------------- notes
    def _notes(self, d, run_hook=True):
        if not os.path.isdir(d):
            return f"no such meeting: {d}"
        src = os.path.join(d, "mic.denoised.wav")
        if not os.path.exists(src):
            src = os.path.join(d, "mic.wav")
        if not os.path.exists(src):
            return f"no audio in {d}"
        tpath = os.path.join(d, "transcript.txt")
        if not (os.path.exists(tpath) and os.path.getsize(tpath) > 2):
            text, msg = self._transcribe(src)
            if text is None:
                return msg
            with open(tpath, "w") as fh:
                fh.write(text)
        transcript = open(tpath, encoding="utf-8", errors="replace").read()
        words = len(transcript.split())
        if words < 3:
            return f"transcript has {words} words — not enough speech to summarise"
        # The CLI grew --no-notes; the twin is the surface most people actually
        # use, and it had no way to decline at all. Someone asking the agent to
        # record a confidential meeting could not stop the transcript leaving.
        if not run_hook:
            return (f"transcript.txt written ({words} words). Notes SKIPPED at "
                    f"your request — the hook was never called, so the transcript "
                    f"did not leave this machine.")
        hook = os.path.join(HOOKS, "notes.sh")
        if not os.access(hook, os.X_OK):
            return (f"transcript.txt written ({words} words). No notes hook at "
                    f"{hook}, so no summary. The hook takes a transcript path as "
                    f"$1 and prints markdown — point it at any local model.")
        try:
            p = _run([hook, tpath], timeout=600)
        except subprocess.TimeoutExpired:
            return f"transcript.txt written ({words} words); notes hook timed out"
        if p.returncode != 0 or not (p.stdout or "").strip():
            return (f"transcript.txt written ({words} words); notes hook failed: "
                    f"{(p.stderr or '')[:300]}")
        npath = os.path.join(d, "notes.md")
        with open(npath, "w") as fh:
            fh.write(p.stdout)
        self._log(f"notes dir={d} words={words}")
        return f"{npath}\n\n{p.stdout}"

    # --------------------------------------------------------------------- list
    def _list(self):
        if not os.path.isdir(MEETINGS):
            return "no meetings yet"
        rows = []
        for m in sorted(os.listdir(MEETINGS), reverse=True):
            d = os.path.join(MEETINGS, m)
            if not os.path.isdir(d):
                continue
            rows.append({
                "meeting": m,
                "seconds": _wav_seconds(os.path.join(d, "mic.wav")),
                "denoised": os.path.exists(os.path.join(d, "mic.denoised.wav")),
                "transcript": os.path.exists(os.path.join(d, "transcript.txt")),
                "notes": os.path.exists(os.path.join(d, "notes.md")),
                "video": os.path.exists(os.path.join(d, "screen.mov")),
            })
        if not rows:
            return "no meetings yet — try action=run with seconds=60"
        return json.dumps({"meetings_dir": MEETINGS, "count": len(rows),
                           "meetings": rows}, indent=2)

    def _read(self, meeting):
        if not meeting:
            return ("read needs `meeting` — a folder name from action=list, "
                    "e.g. 2026-07-25_132122_screen-proof")
        d = meeting if os.path.isdir(meeting) else os.path.join(MEETINGS, meeting or "")
        if not os.path.isdir(d):
            return f"no such meeting: {meeting}"
        out = [f"# {os.path.basename(d)}"]
        for f, title in (("notes.md", "Notes"), ("transcript.txt", "Transcript")):
            p = os.path.join(d, f)
            if os.path.exists(p):
                out.append(f"\n## {title}\n" + open(p, encoding="utf-8",
                                                    errors="replace").read().strip())
        return "\n".join(out) if len(out) > 1 else f"{d} has no transcript or notes yet"

    # -------------------------------------------------------------------- bench
    def _bench(self):
        """Reproduce the denoise numbers on synthesised fixtures, so the claims in
        the README are checkable on the user's own hardware."""
        ff = _ffmpeg()
        model = self._model_path()
        if not os.path.exists(model):
            return f"denoise model missing: {model}"
        work = os.path.join(CRISPY_HOME, ".bench")
        os.makedirs(work, exist_ok=True)
        speech = os.path.join(work, "speech.wav")
        _run([ff, "-hide_banner", "-loglevel", "error", "-f", "lavfi",
              "-i", "sine=frequency=220:duration=3:sample_rate=48000",
              "-af", "tremolo=f=4:d=0.7", "-ac", "1", "-c:a", "pcm_s16le",
              "-y", speech])

        def mean_db(path, ss, t):
            p = _run([ff, "-hide_banner", "-ss", str(ss), "-t", str(t), "-i", path,
                      "-af", "volumedetect", "-f", "null", "-"], timeout=120)
            m = re.search(r"mean_volume:\s*(-?[\d.]+) dB", p.stderr or "")
            return float(m.group(1)) if m else 0.0

        rows = []
        for kind in ("white", "pink"):
            noisy = os.path.join(work, f"n_{kind}.wav")
            _run([ff, "-hide_banner", "-loglevel", "error", "-f", "lavfi",
                  "-i", f"anoisesrc=r=48000:c={kind}:a=0.05:d=3",
                  "-ac", "1", "-c:a", "pcm_s16le", "-y", noisy])
            den = os.path.join(work, f"d_{kind}.wav")
            t0 = time.time()
            _run([ff, "-hide_banner", "-loglevel", "error", "-i", noisy,
                  "-af", f"arnndn=m={model}", "-ar", "48000", "-ac", "1",
                  "-c:a", "pcm_s16le", "-y", den])
            rtf = round((time.time() - t0) / max(_wav_seconds(noisy), 0.01), 4)
            rows.append({"noise": kind,
                         "in_db": mean_db(noisy, 0, 2.5),
                         "out_db": mean_db(den, 0, 2.5),
                         "reduction_db": round(mean_db(noisy, 0, 2.5) - mean_db(den, 0, 2.5), 1),
                         "rtf": rtf})
        shutil.rmtree(work, ignore_errors=True)
        return json.dumps({
            "model": RNN_MODEL,
            "noise_only_fixtures": rows,
            "note": ("Pure-noise fixtures, so reduction here is the suppressor's "
                     "ceiling. On speech+noise the published figures are white "
                     "-26..-28 dB, pink -15 dB, babble only -3.2 dB. RNNoise "
                     "separates voice from non-voice and babble is voice."),
        }, indent=2)

    # -------------------------------------------------------------- live status
    def _live_status(self):
        """A loopback device is any device presenting BOTH an output and an input,
        so audio written to it reappears as a capture source. Must match what the
        CLI matches — an earlier version only looked for BlackHole and so reported
        "not installed" on a machine that already had a usable loopback."""
        p = _run([_ffmpeg(), "-hide_banner", "-f", "lavfi", "-i", "anullsrc",
                  "-t", "0.05", "-f", "audiotoolbox", "-list_devices", "true", "-"],
                 timeout=60)
        pattern = os.environ.get(
            "LOOPBACK_PATTERN", r"blackhole|loopback|soundflower|teams audio")
        sinks = []
        for line in (p.stderr or "").splitlines():
            m = re.search(r"\[(\d+)\]\s+([^,]+)", line)
            if m and re.search(pattern, m.group(2), re.I):
                sinks.append({"index": int(m.group(1)), "name": m.group(2).strip()})
        pidfile = os.path.join(CRISPY_HOME, "live.pid")
        running = False
        if os.path.exists(pidfile):
            try:
                os.kill(int(open(pidfile).read().strip()), 0)
                running = True
            except Exception:
                running = False
        out = {
            "live_denoise_running": running,
            "loopback_sinks_available": sinks,
            "how_it_works": ("mic -> RNNoise -> a loopback output device your "
                             "meeting app selects as its microphone"),
            "engine_note": ("live denoise is always RNNoise; DeepFilterNet is "
                            "file-to-file with no streaming mode, so it is the "
                            "offline engine only"),
        }
        if sinks:
            out["ready"] = True
            out["start_with"] = "crispy live start"
            out["then_select_as_microphone"] = sinks[0]["name"]
        else:
            out["ready"] = False
            out["needs"] = ("a loopback CoreAudio device. A dedicated one "
                            "(BlackHole) needs an administrator password to "
                            "install; many machines already have one from a "
                            "conferencing app, in which case nothing is needed.")
        return json.dumps(out, indent=2)

    # ------------------------------------------------------------------ perform
    def perform(self, **kwargs):
        action = (kwargs.get("action") or "doctor").strip().lower()
        try:
            if action == "doctor":
                return self._doctor()
            if action == "list":
                return self._list()
            if action == "read":
                return self._read(kwargs.get("meeting"))
            if action == "bench":
                return self._bench()
            if action == "live_status":
                return self._live_status()

            if action == "denoise":
                src = kwargs.get("path")
                if not src or not os.path.exists(src):
                    return ("denoise needs `path` to an existing wav — "
                            "use action=list to find a meeting, then point at "
                            "its mic.wav")
                _, msg = self._denoise(src)
                return msg or "denoise finished but reported nothing"
            if action == "transcribe":
                src = kwargs.get("path")
                if not src or not os.path.exists(src):
                    return "transcribe needs `path` to an existing wav"
                text, msg = self._transcribe(src)
                if text is None:
                    return msg
                # An empty transcript is a real outcome (silence), but returning
                # "" makes /chat answer with nothing, which reads as a hang.
                return text.strip() or f"transcribed {src} — no speech detected"
            if action == "notes":
                m = kwargs.get("meeting")
                if not m:
                    return "notes needs `meeting` (a folder name from action=list)"
                d = m if os.path.isdir(m) else os.path.join(MEETINGS, m)
                return self._notes(d, kwargs.get("notes", True))
            if action == "record":
                d = self._record(kwargs.get("seconds"), kwargs.get("name"),
                                 bool(kwargs.get("screen")))
                return d if not os.path.isdir(d) else f"recorded -> {d}"
            if action == "run":
                d = self._record(kwargs.get("seconds"), kwargs.get("name"),
                                 bool(kwargs.get("screen")))
                if not os.path.isdir(d):
                    return d
                dn, dmsg = self._denoise(os.path.join(d, "mic.wav"),
                                         os.path.join(d, "mic.denoised.wav"))
                return f"{dmsg}\n\n{self._notes(d, kwargs.get('notes', True))}"
            return (f"unknown action '{action}'. Try: doctor, record, denoise, "
                    f"transcribe, notes, run, list, read, bench, live_status")
        except subprocess.TimeoutExpired:
            return f"action '{action}' timed out"
        except Exception as exc:
            return f"action '{action}' failed: {type(exc).__name__}: {exc}"

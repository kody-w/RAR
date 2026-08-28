---
name: "rappstore-kody-w-rapp-crispy-singleton"
description: "Local-first meeting stack. Records a meeting, denoises it with RNNoise, transcribes it on a local whisper.cpp server and writes notes via a user-owned hook whose default sends the transcript to Anthropic. Audio, denoising and transcription never leave the machine. Actions: doctor, record, denoise, transcribe, notes, run, list, read, bench, live_status."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-crispy-singleton", "rar_sha256": "4229fed6d82f92d9561fd291f4bb61e7862c710f24d0b03b43f514745f665f72", "source_kind": "federated-rapplication", "source_commit": null, "version": "1.4.0", "author": "@kody-w", "tags": ["meetings", "audio", "denoise", "transcription", "local-first", "privacy"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rapp-crispy-singleton`. The original RAPP
agent is preserved byte-for-byte in `rapp_crispy_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

RAPP Crispy — a local-first meeting stack as a rapplication.

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

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "What to do. Default 'doctor'.",
      "enum": [
        "doctor",
        "record",
        "denoise",
        "transcribe",
        "notes",
        "run",
        "list",
        "read",
        "bench",
        "live_status"
      ],
      "type": "string"
    },
    "meeting": {
      "description": "Meeting id (folder name) for notes/read.",
      "type": "string"
    },
    "name": {
      "description": "Label for the meeting folder.",
      "type": "string"
    },
    "notes": {
      "description": "Write notes via the hook. Default true. Set false for a confidential meeting: the DEFAULT hook calls `claude -p` and sends the transcript to Anthropic, and this is the only way to stop that from here.",
      "type": "boolean"
    },
    "path": {
      "description": "WAV path for denoise/transcribe.",
      "type": "string"
    },
    "screen": {
      "description": "Also capture screen video.",
      "type": "boolean"
    },
    "seconds": {
      "description": "Recording length for record/run. Required for headless use; there is no ENTER to press.",
      "type": "integer"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_crispy_agent.py` and embedded as the fenced Python below (sha256 4229fed6d82f92d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_crispy_agent.py` first:

```bash
python3 rapp_crispy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_crispy_agent.py   # or on stdin
python3 rapp_crispy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

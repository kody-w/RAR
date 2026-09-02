---
name: "rappstore-kody-w-rapp-crispy-singleton"
description: "Local-first meeting stack. Records a meeting, denoises it with RNNoise, transcribes it on a local whisper.cpp server and writes notes via a user-owned hook whose default sends the transcript to Anthropic. Audio, denoising and transcription never leave the machine. Actions: doctor, record, denoise, transcribe, notes, run, list, read, bench, live_status."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-crispy-singleton", "rar_sha256": "4229fed6d82f92d9561fd291f4bb61e7862c710f24d0b03b43f514745f665f72", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_crispy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rapp-crispy-singleton:9d2568cc6e7def7d01d80b3f4ca0446e5016b629552396735eedaccdd20fcc9a", "kind": "skill"}, "version": "1.4.0", "author": "@kody-w", "tags": ["meetings", "audio", "denoise", "transcription", "local-first", "privacy"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rapp-crispy-singleton`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_crispy_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

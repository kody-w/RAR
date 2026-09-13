---
name: "rappstore-kody-w-rapp-crispy-singleton"
description: "Local-first meeting stack. Records a meeting, denoises it with RNNoise, transcribes it on a local whisper.cpp server and writes notes via a user-owned hook whose default sends the transcript to Anthropic. Audio, denoising and transcription never leave the machine. Actions: doctor, record, denoise, transcribe, notes, run, list, read, bench, live_status."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-crispy-singleton", "rar_sha256": "d3133031a2e4ffc3be0ed282c2df7b73ca49e46e07b259dc704539904aaefe74", "source_kind": "federated-rapplication", "source_commit": null, "version": "1.5.1", "author": "@kody-w", "tags": ["meetings", "audio", "denoise", "transcription", "local-first", "privacy"]}
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

Record, enhance and transcribe locally. Prefer installed native app controls
for capture; keep the legacy headless algorithms available explicitly.
Optional notes require provider consent: the example claude hook sends the
transcript to Anthropic. Neither missing consent nor a provider blocks local
audio or transcription.

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
      "description": "Request provider notes. Default false. Even when true, legacy hooks require CRISPY_NOTES_CONSENT=1 after reviewing the provider; the example hook sends transcripts to Anthropic. Native consent is configured separately in the graphical app.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_crispy_agent.py` and embedded as the fenced Python below (sha256 d3133031a2e4ffc3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_crispy_agent.py` first:

```bash
python3 rapp_crispy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_crispy_agent.py   # or on stdin
python3 rapp_crispy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""RAPP Crispy — a local-first meeting stack as a rapplication.

Record, enhance and transcribe locally. Prefer installed native app controls
for capture; keep the legacy headless algorithms available explicitly.
Optional notes require provider consent: the example claude hook sends the
transcript to Anthropic. Neither missing consent nor a provider blocks local
audio or transcription.

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
import plistlib
import re
import shutil
import subprocess
import time
import urllib.error
import urllib.request
from urllib.parse import quote, urlencode
import wave

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "rapp_crispy",
    "version": "1.5.1",
    "description": (
        "Secondary integration for the RAPP Crispy native macOS app, with "
        "preserved optional legacy processing and consent-gated provider notes."
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


def _native_app():
    """Discover a real signed-or-development bundle, never a PATH shell launcher.

    CRISPY_BACKEND=legacy preserves headless/CLI workflows. A native record/run
    request only prepares visible controls; the user must press Record in-app.
    """
    backend = os.environ.get("CRISPY_BACKEND", "auto")
    if backend == "legacy":
        return None
    if backend not in ("auto", "native"):
        raise ValueError("CRISPY_BACKEND must be auto, native, or legacy")
    explicit = os.environ.get("RAPP_CRISPY_APP")
    candidates = [explicit] if explicit else [
        "/Applications/RAPP Crispy.app", "/Applications/RAPPCrispy.app",
        os.path.join(HOME, "Applications", "RAPP Crispy.app"),
        os.path.join(HOME, "Applications", "RAPPCrispy.app"),
    ]
    for candidate in candidates:
        try:
            with open(os.path.join(candidate, "Contents", "Info.plist"), "rb") as handle:
                info = plistlib.load(handle)
            binary = os.path.join(candidate, "Contents", "MacOS", "RAPPCrispy")
            if info.get("CFBundleIdentifier") == "io.rapp.crispy" \
                    and info.get("CFBundleExecutable") == "RAPPCrispy" \
                    and os.path.isfile(binary) and os.access(binary, os.X_OK):
                return os.path.abspath(candidate), os.path.abspath(binary)
        except (OSError, ValueError, plistlib.InvalidFileException):
            continue
    if explicit or backend == "native":
        raise RuntimeError("No valid RAPP Crispy native app found. Install the complete app or explicitly select CRISPY_BACKEND=legacy.")
    return None


def _native_recording_url(kwargs):
    name = kwargs.get("name") or ""
    seconds = kwargs.get("seconds")
    screen = kwargs.get("screen", False)
    if not isinstance(name, str) or len(name) > 200 or any(ord(c) < 32 or ord(c) == 127 for c in name):
        raise ValueError("name must be at most 200 characters without control characters")
    if seconds is not None and (type(seconds) is not int or not 1 <= seconds <= 86400):
        raise ValueError("seconds must be an integer between 1 and 86400")
    if type(screen) is not bool:
        raise ValueError("screen must be a boolean")
    query = {"name": name, "screen": "true" if screen else "false"}
    if seconds is not None:
        query["seconds"] = str(seconds)
    return "rappcrispy://prepare-recording?" + urlencode(query, quote_via=quote)


def _meeting_audio(directory):
    candidates = []
    metadata = os.path.join(directory, "native-meeting.json")
    if os.path.exists(metadata):
        with open(metadata, encoding="utf-8") as handle:
            record = json.load(handle)
        candidates.extend([record.get("enhancedAudioFilename"), record.get("audioFilename")])
    candidates.extend(["mic.denoised.wav", "mic.wav", "mic.voiceprocessed.wav", "microphone.caf"])
    for name in candidates:
        if not isinstance(name, str) or not name or name != os.path.basename(name) or name in (".", ".."):
            continue
        path = os.path.join(directory, name)
        if os.path.dirname(os.path.realpath(path)) == os.path.realpath(directory) and os.path.isfile(path):
            return path
    return None


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
    with open(path, encoding="utf-8", errors="replace") as handle:
        lines = handle.read().splitlines()
    for raw in lines:
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
                              "Request provider notes. Default false. Even when "
                              "true, legacy hooks require CRISPY_NOTES_CONSENT=1 "
                              "after reviewing the provider; the example hook "
                              "sends transcripts to Anthropic. Native consent is "
                              "configured separately in the graphical app."},
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
    def _notes(self, d, run_hook=False):
        if not os.path.isdir(d):
            return f"no such meeting: {d}"
        src = _meeting_audio(d)
        if not src:
            return f"no audio in {d}"
        tpath = os.path.join(d, "transcript.txt")
        if not (os.path.exists(tpath) and os.path.getsize(tpath) > 2):
            text, msg = self._transcribe(src)
            if text is None:
                return msg
            with open(tpath, "w") as fh:
                fh.write(text)
        with open(tpath, encoding="utf-8", errors="replace") as handle:
            transcript = handle.read()
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
        if os.environ.get("CRISPY_NOTES_CONSENT") != "1":
            return (f"transcript.txt kept ({words} words). Notes DISABLED: review "
                    f"{hook} and its destination, then explicitly set "
                    "CRISPY_NOTES_CONSENT=1 to authorize that provider.")
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
        if os.path.isfile(npath):
            revisions = os.path.join(d, ".revisions")
            os.makedirs(revisions, exist_ok=True)
            shutil.copy2(npath, os.path.join(revisions, f"notes.{time.time_ns()}.md"))
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
                "seconds": _wav_seconds(_meeting_audio(d) or os.path.join(d, "mic.wav")),
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
    def _native_dispatch(self, action, kwargs):
        if action not in ("doctor", "live_status", "record", "run"):
            return None
        installation = _native_app()
        if not installation:
            return None
        app, binary = installation
        if action in ("doctor", "live_status"):
            response = _run([binary, "--diagnostics-json"], timeout=20)
            if response.returncode != 0:
                return f"native diagnostics failed: {(response.stderr or '')[:400]}"
            json.loads(response.stdout)  # malformed output is an error, never an empty success
            return response.stdout
        url = _native_recording_url(kwargs)
        response = _run(["/usr/bin/open", "-a", app, url], timeout=20)
        if response.returncode != 0:
            return f"could not open native recording controls: {(response.stderr or '')[:400]}"
        return ("Opened RAPP Crispy recording controls. Capture has NOT started. "
                "Review the selected microphone, explicitly choose any screen/window, "
                "then press Record in the app. Notes remain disabled unless approved "
                "and requested there. For existing headless workflows explicitly use "
                "CRISPY_BACKEND=legacy.")

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "doctor").strip().lower()
        try:
            native = self._native_dispatch(action, kwargs)
            if native is not None:
                return native
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
                return self._notes(d, kwargs.get("notes", False))
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
                return f"{dmsg}\n\n{self._notes(d, kwargs.get('notes', False))}"
            return (f"unknown action '{action}'. Try: doctor, record, denoise, "
                    f"transcribe, notes, run, list, read, bench, live_status")
        except subprocess.TimeoutExpired:
            return f"action '{action}' timed out"
        except Exception as exc:
            return f"action '{action}' failed: {type(exc).__name__}: {exc}"
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9W8WberRtom+Ff2OnWRdmMfMQ+u+mo1iFliEJOAci0nM4h5EkLZ2b+9Q3vv47S/tDOr1uqLbl0cC4h44413fJ7YRn/7Eq1L2U9ffvryf9Z9uv+4ffnhS5rNyVQNS9V34P65T6Lmx7ya5uWtzbKl6oq3eYmS+uublSX9lM5v0bcHP7ylWddXcza/VcvbVi3lm6Xrrxs/vC1T1L3kxh8P+w5Ma16y37aymods+poMw9ucTfdseou69G2bqgWM7frXv/cqAuNX8PjHfuuy9K3s+xrM7OcMrJlHa7OAuR1QZimzX9calrelf2O7pZz6oUq+vrFrWvXftHzt5LXQP0aDHb912UuBJovu2busNkrKqsvA3OT1fP7pLe2TpZ9+eJvet//rnn+7xR8+1AZj1u6Ht6aal9fwCAyOsy4pX7fu2S/AjMs6fwUmzx5ROzTZ/OWn//E/f/hSge9ffvrbl6SJZnDrixUNw3ECRtrZIusWML6JugI8GHbgvA5cA/Pl/dSCW8AYb59X381Zk//w9n/8H/UWTcX8/U8/d2+fn+h9L2//8fbdx7OvRbZ89/OXj9s/f/n+rZ/efv7ysVFw+XVegHm++/5r02/Z9N33/xC0TPtvxL4+XbSAvQHRr9W//vJx+UsKtI+WpPzuY4kf3j51+v3cKv82vXp3/Jved9l/kv/6TNmyTt3n2H8S8W1z//GbLfy5kA81P8Z99/2/FPby478X9Rr1bwS9QuHfC3qN+r1/PtMMeORfy38Psn+/wPuwf7vnXwP1f2Xrvw5+if3XnvnImj8UOk8JCKDfbR1ED9jR9/889hUzIFJeU0DQvr7289fX6K/ZA3hi/g48+f4P1viN8t/9qg3I/gzUkL++5v/1VTui7u1dzKtWbNH97ecVhREcqP/HAr99fv4CStXndv/jFRAvWXkFis1vaiWoLt3b0Ffd8hYt/wsiq2V+a0EVA3r8oSV++eGtnYtfM+9zS+/7/1O/vSZ85PqnAYCS1VyCAhuvCxg09NMCLoBZy/fA+5cu/Uf9+/+CV3+rz7/z6x8Zf8key+8t+g95f2JUoPVr1qt6/Unl+r3p//n5fwHd6i1rh2X/bROrXj0WlIPmrV+XpG+zt+/mqgHZm33/w6ejXiJfHvoDiWBzX0Abq0EbPSQlCDUgF5Txj/786dkfXl04Kd+bFFjstV4JeszXPw2c1z6/tYWXi/Lfmjt9+xsw0N+/ZUvXv4EGnwHxabZkCQiofxNI783zD2Oo/c8R9I+S+KdB1P67OPmAGJ8h8inwr2/fRW9536TAUF0ELJ5PffvbjP7+j2ImBeq1r3W/RWs1p9X0Xfv9W9aA5Pp29waS/jtNEBxFl2wQY9//m7r6ruB36Q+/3/qnlX54EyMg/Pt/13JeYOUPbZr+GuAfg37fc2ZwD+AqYOD/vDywyuvuvy5b75+475v/JDWZsuyFNL7/872n3xz4e2Omn8bMv20KhNuP//3tb+nf/01UASz2/4/9/8m2/3UYp3+wMYCz0j9qCb+LQxBWII1+7Sv/K/v59vljOZ+rpJ8C/9zBwIN/e+n3958BVvi5+9ufB/tf3m/+5ddQ/ydXf+vkQOTa1R3gCN9c/5e/fXz5+1++vjkArf45fP+zDvy70va/g+x/V5SyR5KBUj6v8TD1STbPX52qzUA9Fx5DNWXpT3+4ofwbKP/NPt4WMDF9tYLfavwpX3j/z2sCKOLg3v+G2DwCPSX96e1vyz5k34G533/95ZdXlP/yy9/BXXADmP3L3wE/6UDhXz/oEKAc/+W/vGlVMvVzny9vdtK/+tHavZR8QUAHsLtXA3txqenFreYqbrLPccAUt+xDkT5/++snBz1MgPD8mLwznh9fNK3Jlr77K/AfkNFPVVF1oBVarGn+3EUvRvSSP0zZO3kEyGVfsh8BAfrx9eWt6t7++pL3y4e8X94nfB32v75zP/D0pZh1VN6SaJjXJvv6Uvr6gmYfKibvUCFLViDrg6/mwEyvAMjmvnkniWD1ua6a5g3kafYKrv1dNjDCTy9hf/3rX+NoLn/uPuga9vbR1ecDGPCrOm8//gh2kDdVUS4/d6BX9sA1wCn/19u/mvUu/LWGCZjip4mBhqpt6G8gedYWDAPWB/4CIfpu4r/9/dOOQEwHehtwSJVX2cfkpupq0Jw/jWrL7I8oQYLABsYEhmxfYPAFmKrl65uSv/2q7ydOfAcNPcC6aTYAKg7SAYAYgDd+7n615DumA6xtzvcfXmz+fdW/xlP0rmL7ywue/PVNO5oAo/XNC6gBNd8Hgcl9VwHz/+ryj/uvI4G/zG/cNxFf3/R3Aj9EwOnlFH2ukUcffgFI5dv0FwoETX/7uXvx7exlqugViR/mAYOAZZJPl/748vkbQF5t9Dpj+Fz7fUz0wsdOH4HFp5+7+TOaoyl7LzBAlf2tWKs0AmDtv36G1Fz2a5O+2w9o+pL06YX00yvvMfiK77cP2v8NSH2emPzRacwHZnsFegOs9L6PdyGfRS7rypcGvzvviD8Dutm/vpkfurxsCG68EP8HDwfywLa7Zeqb+ecOxMErTUAJAXups2z4iJqsiICrSxBiIDGAGk0BknQpW/D1DmpK9Mr37PFSrFrAYj93xnuFAoH6gbymbFyBmV/V4F69ABdYcQbu+Old/OfZyFvSRGuafRz8/HrU83P3p2c9egZ0AMLaan4/6vkUCtYEMfCPtWJgg3r+sASIrdcB0StKfnco9G5K4eXLd7D81rxHwdq95v/fh68vq39Ul8OnT+bDf3vVP2DMdvjvh5dvhgYE6EfpeJemZdEMzJi+H4R1b+zw2qKGv30Hcmnq0xX46h2ffyLOXzn9NxQA4DooSB+c7e1HlHxt/keUfku5z5t507+63I/YV+Z18wOAf8wdQJp/m/r2I0KA5x8P4ih++erjA2air5lv/+3Ht4+O2lRt9ZEjPwAPfCSWJbC8JnxMf9WeH1/7/ky3N/jrK2q/o+AHuPNKkFc96D5q1Gvc+xnB5wkhkPjK2ffDvr5KPgE3SPof3y+/vnEfyin2x3OgQv86SIxBqjX7WwtS7WXZb+3m1YGBdd/NDh4DweW35YdoyN4tf//MNHtJmyoGnnhlgl1mTTO/uus7Z8/bISv+6xvIChAk4MZ7wL+3Ada23kW8yY5jvg7xQHxnIMS+/NStTfPDOz783eHd65wO7LAFHGiaX+d7wNFAk6XK3q8+PP369vsD2OuLsoGV0/7rG/951PmXDxDzl/ezw25tv/z0Pz6PusCND2DzfpD77mTw7R8pDy7ek+41bu3etZ6X90nRa8p7lL3f/RXFfPmfYD5ABECVF9/rihcE+Izzf9ZW+yxKVQrA2D/o0/dv+QePz0ADA0u9FP8noR8W+88Sz1GcNe/T349jP+V/yP5jMe/7+yc5FqgyICP/kfnv4/5h0/wFLb++gTTvQHaBfwDGAVH2rbqBsvOPSnW0FNsMftENR7B/ORq6LejOfyBvUf6KcYByqmx7KflS+Nty//V3xey3VezXSjP/5wr2UYO/FS4Q1eBrXhXvdeNbuoDg/taOXh3v1SJfVfs3lnmxjyzqXqZ5ofU/iDDWe3s9eTfyZ9Ac/hEyf2jkDwLzz7LYBqTlZ494+xj09tp//8cKfbKrP/LWK4jfi23WFZ+6fUT2CwG9/vjw7or0/cGvvQfAgXdDT59HyG/AMYL1susLH86/UQIAgKzIpi9///sr+D9kfRy/fw7o4xc0fbdaEy0fx+t/A4G/RGm0RJ/5+4lewfApmn6cX+39gHyFXwkVTR8w7R9/W/ljXPs5di4jALZeJ/gYgmEwhkRohud5gsUZnKUojSZomlMxhSURzmQ4mcFUjBJMmlAwTmAMA+NRBHo4hQN5c79OSfbLC69Uy7d69Hmzrjqwzy95ln5glx9/ixnerfErkn6vSh9b+NuXmMTBNBmfFfbjczzQCEP5cWyocZE/abG5ucRQ9fbZmXMvQl1tNQUHRK5wm7u0Se83SLdcW+1nF7Wk4bRTskQ9n0/BXAVoT3GTZS+D2ygjGpsTTKCVbbDH9Vzh2MYmj0NDQ0brZOoiQvkjOxiHw6E5HEVMIOlMzyTJI5RraIuNuJ/z87FjNsXEc7N1wGhGFs6kAtN+iJrzoraFlyqhMXTwXtOqzopqmxOqNkv1LIkLQ+GN1l6IVj2x4iWxN76+HIXrXhw6HMwtrVBaEyoIR7Vy6Ls4NLR6JetOWarjja8XByJExBw4Stb6y+GRhoP48C/SjUoh0bzfruxAlBR6OrblRKC70eX6rY5s8Sm47QHTrNA7a/Phgh5H1oFFfK1RlYWNa2oSM18I3XzelGFoG1KBuKk2TF92UDezpZPHbe3Dsc4E2KtAJnZWHLewkTIFD1xHKnZ2t8NhjthCXRM4ZnnetYeCVRpPiCs6wjSqn4etb5hYHq3A8A5U1yrUpdOfAxlV2PPe7KfIdvlbbBIkD6W1fF8sZVaUmjU2s+4P3GETlRoptNkpZTbH6LjZtK1ljmWwWfC9X+9sh5q3i5Qstda5ZPGAuZxeBk8oggthnRW/l8+YfLkHRm7lnHS/PG+6hpL9PdeghwE9jdR2xtBNLbzRqbElDfRQaAc4X3cz8Smch/o04LGHDR8S1ah3wRfgauuroSILPz25OY9Dpjngztl9HmNbwR9umXLlBTnkJPQ8Bt1hwOhjcGeFWRQ40hOQamV3i8jqKd0NP3lie13oM1y0knx1Rl6uAgZaW1Vn9meNmRC/op1SjcVGtBpFu/Pd9Wi/3m++xh9YnRYV1dt4j+aoxsbMPO/qkjXmrXASERcS5yIxRzPsYKaRjaTyLZ4pDXE+j0x+9IrjhXO2Yi7iyNWSrqNb1jgzj8TtYjp9dCqaRnxozvCZNl3aOYTPFio6xbShQslhqj70Q7eTpxMfHcTWCJitnmUTluDIzkWk1jR+D8NrcwWl5szN5VwyxxYrxCMbSyMm02sgNwhtGReX64NWuB+8ldj0nI6Q2llvOUy3/bMvSYrmGjrFhzXtUrEnqhTwaVS3WqWX21vb+dveOGYuXQpZhCUzWg9LhqHdztBOvscI8pDuQg6rtFrwVib7eQaJC3nIOeY0G/dbS1XVKGo4kZyFmj7rVCAexbtGKgp73RVSlSs4GZeb/1TRvNvPO3lXx0RYArqmOi0ehELnGFsWnjq7E89QNU5hbq9trMD7fmwJR2Zv64jf96qNgvgGxVmsn2/3c35VjneaLJnMv62B4ZTpmSUOXAnzdjE78nG+c+Ijih/E4Xk+j6J5G3yu8Z6BomxzKNfcHdfp+NE9o8sw3svJHM7q2YpEBqcpAzqYZknx4SkgBAF+MAF72IjCL7jOh6LcQf2OgjKHhhlGCu22lyWf5SOmwZ3p6kFVUt5lTBeGJGdzZnGqGwx1c85v0P1WEIfcIBD75C0Fx6mBVo8yh6bmo3QxoSDL4nx/0hSEefw1vMRX0+HRKDQexwZhuZgmdTMktrnneadDblJhQmZyMJ/O/khwW+JmBRowlo41ndw2ydV4E6+emrLfLHYQOVD9JkjqVHxXaPZucShB5/chXEVQl5UdZg3CL2QHZ8Pm0d8LqsLbjnsyFEQ7epUnB8w/lHXkXM7mYUhofzYRiA4oQneBPfHwWvX8dqBFInBVkmFE6tqf9613ngcpYpO7szBls4UemhQXjLZYZg3tlRdXs7K3Uus4Hz9kh3zd6G6YnYI65CzmtvTRBUWWlDRXFgWjFrmZ6XsX2zuuPTksJUjZUz6mStFeAqV8INdFsMZKOJsY5R/LEIfgpDvgoYSMqWRS7E6pSuCRxq2nD7eUTPNzgR+WxwUzAds4bKMUoLdSzXDJOtq7fsfyZ8ekvgUiIZ4Zo6LL+DKGFi/NGJ6Tm4Lyo3Q2U+4el0erP0HlVuQ2pBgB1LQbpwkKayTni8HE8KJcLmRhnSOyK47aBa6akxUcb4LqL8W663OrcCZ/vCx7JTRQXfH18a6yvQDPA+D0t0i5loRSIFzQhoTI1PVF0aTjNA+IKDuQVXpu4SFsq+CNcLMG6WypKF+wIiX1l6QwR48YuBLTwq7Sn0alTKhl26QiYJHVgwwQQMsKuVBPDYY6SQ8hL02dC4a0lAvpUgV8WaGuUldwT8Y9TncxbtPWrEEUQBUGaWIlQRoHucMheYIPRoyxti+l9EVtJy15Hk9qzWsbL+867o0MO7tbdQg3/6lLen2WoU5woUd33vm6YEsWhnpyTGzoPOWDo8MbGz7XCqtp2gd+oAM5uXG1pcNItV+kY+KO2ETCe+VrSn4scrw9ZUUbKMbKWmMEjbqGG55kesW950628QSFfBBPIcfu1bGk1ue8nRVPQSLFP3lMfe9Ni2UZdDPDFVT7uhy6ZKrl5UzJliUrWHU2mbqkUYt2eXM/X+r7vMlOQ80Oubd940p0pd7uVx6JYtPgTjXZTdGp6qcpx6yevl13e+0QmH9E6s4lWk7dDwlFLpLu77dKbprk6i83rrxt+DKz2d4W5869bWMCjQwnn+ZSIY6c1LWFZhEiFFiwrR4Q3NlJp3UuNqVlZ04Lh4MWnlru1mpKcDlmdoXh5F0uzGJLGDHYTc7hDnCrWMPp3Op4es+fMGRafXQOYqRlHkEoL3eTeLLbTKw1r+7O4zGe7fqGY6xZjvPlYvXNmAQKN1mqp5E3U1ClicRYj3Y819Mu83Z1H/eIhS2lVxQ8u+mdoyDB9VFY10Q/rtZYcFf+EbhBOxgXZx8YgVBDtI+cRReQ+s7vfVTvLUeSylqtBhI5/NP1eJqYk3MWPE9pDD9NPtpqThS8XZorxm6N+ZQiUrjU9EWefLsutNNtLI6JphTHuRslvFH9O33OJKQqEKF8XK/jnOFZY4eH+zUdV46qWjFO7c0kVpb3h8gPdU68yti9I8lxRSZ4QvsgM2nErPph95Vpvc/FuUL3ul9Rssk9zZc6+NwoDcrLcaGyjXNDt3vEPWCfOcIwG8igcF+39iiqbniRj+FRQpesM0dux12qSc6sp/P0KLVGHGN4ZYSyaDGGaFGaTkULMkuUTjm9A7OriAiBcpnbvmdseNSYwa3OZxi2y373vCsvp9hpP+k80fdcmHs1byv0fW/kBoCRRM4xtduPvCcx6uHQ5j2l5wa5Kl60OJeDKRs5iVli1a0HVdevHrvHq9px+dF01k5MR8RrV6w7Sw6hR2YPcWl5NKVjfTwtOV4Q+GiXV8EJR4G7pP1sdZJqDCZ+F6rL3Z7RJOxP0cSrZG1116CoJNOK0/FiTcRek5owAlAGX/PpyBnFIWkUOMFUsw6eOnmaqjKvsVHEb5p5TtvdP515D3X7SioWGgQsxz2LkyP5uuF1XnYi42ycY04drkWSXk+wsBaAhkHzceKnvluI1To6AFQ+8ogcTwvWSnDLnIKb3698XjI5lAAcfIBl0mYgIaENWvXJY2w88gPnjD53efi+1uLhdJUDLi0EOrhpDnw0uVRQPcmpVaMbXeWsQY2lyv12mY/cpuPDQ8F2bCUY1fOfd1JDb3dUamiMyw68gCyZ+SQI37gFvIVdrQS9u1SwBmJme/UsZHcK4SPuNN0VMxJCjYM5zvEy9BGbgDGeTnVxcD2Oozj9njGcIRE4aSY0nwr0PAigCNRF3Q/bZWAYwlcMem5M9zFey6laer6+8b1ut+kph+XLE2WGSwWDjD6MkJGJA7l42xGTvDsCFSjd53DIXx6EpwV1QE1cKbEnTy00XJOS5LFHVXCWEYpIr+GdLEexHzM2g4rjWcr6YXmMGRcgjaDqOXwxzcsmFyyagpqK5i3pX/FNITkURav9sbciEclJXfh3dfFvzNhybKIU+CWh1OkkTJSgQkyme75PP2oVCXVTci2rwe0DdH0eVTx8ojaHZANCeEeA/XN2QHDhycAeZ+BkWzMLWSjts9Dz0SGlmTqcjulOGQksz9fTpIbJg9bWLCSfTjde1AfMTpGgF8ujJmE2jJrpYJUry3EHCN6ldjmchkFPWtzdPGmHu4OutCbLEwrlzzFbAIA5KyKHiXIjDKKrkz4foc0oawmRKjrcArJVPpfdRDXuVoqHPcLG0xODYLa1kJ4Ia+HOyfGJGhgMuk/OpN2UOJtPOXS1jihVzN3Sx5tu+DEMVz7l15jcRJleO50mqy3f0BFeet3diXT2NodQPfIlf2Z4rY5msYm1KMpkqb+tIrVsImqbDF3ccXH3kFU+mwUddFV7qm8sRrYnuc5l7R5vSqhGj1gMqyW6E0KEy3SpHZuLIpy3fOkT1ufK9QTLNzWqNvzKkecsu5iJtApuF/BGz0uUPFYevq7T2SvrZGOjKmJ8sw9bYw1pyLcPlkJT/k5Ag3IAdT43DvRxox3D8+LTxPbuHOgtJyuh+EQaDaIjW8JWqtIs0qJlOeEysZdKLGoUIdqX8ZKmYWUWetmr9+MYx7pkqig9hdWZH6dpOK/Y0YOLQ3xvj33t9JnRb1tUD2eAHrA7XjA3+LLRPePVDyZsasLYIo3CZzjDnL0Jn3YtXNyTMUlZEl73huJLwXAgATPvIMwR6EQ5RwvU+dr013veXYIz66z8aVlchBYzWIGiI4kuWqlejvjxRJFrOITd41RcsoyttJ46Cdvx6E3yTZCOhtE/FjdVrWd8OrR1ukkVPtVOwCy5TJwRxjuLyEpRqjk4sHU0Bj/mMDVSOYtWo+QuUMc8JA2Rtq/LvA6jox/5jraxC6Cioqxf+voYM/0xzu4rzz1QItMfT7ugkNu5pJClpLyTzvU0TN/Owno5z975MDAtLscXtzdx0qjTCJ+V9rKrgOAIZ8F1gqucK12mipwC0AiHe3uIATIYV0lbiWg0XMjIxHu8bpoUcAOTmN0L4dGDcSMr8WG7e63Sxm09jGxINoh5MVC/dRLuqjyZiChqKpR2+lpdgO8RNLtzPjk+TLZOaCWMONT0N3k/BjLtQXfyUAMitogCJSqwwnkdnZwErBUbD6sIu78bkaA4DtaLy+GgqowdOl3vJ8IUarnsHwWOn6b+GhN7MUDenTr618dC8s8if+BpqTiHnOSvx/y4Dpg1q5o9YvMU6DnpJeKEpuXeBY8ysaVBw8WBB9R9s2IGOutOc97I0UToJAMUIx5L2LNuVjUN8rHYzSRNRz9OUdaJvULHigxmKam8GpLDBDJ/mSGW5tykhxxicGydrS/nJQxPF5YBHVjbGt72FWJrZZyQoztaLFq/u0fPQSDqWkTxzN1EH2X8yTdl99qx6blHZTFwd5eNbiPnJ8dOWg/404QQFa1TAW9tV4ovqoInA1opfBifhPsIYKSSmY218XbY7GdBoTQy02OG1DV99zXiFqKJ0+NmrjomJZD7U7otoCKpgXNu41PWCzvuX4ZoWwepJm4YHDhkzreFREJwe9OYDa+OsViZzrMes+TsipDF2bUVUSzk1UTyCCgVX4nr44m6kr9fLtrJ7+uL6bp1F7AelD2wKgke9i3etTsiQY4w6tvK9c29Epebl3HiLaCn3IRJjlBEc+5yFSRu0sU7Ax9lS03Yhy/t+oEZx+twGs8TdLxeW2y8oUwoZksVSlfIPJ1W+ozqwYI4bb5XoSqSzoW9WkxfNCTyUPutWbpiTfcKfYYhLa/xubPto39UOo46Vdb9YnHB3kKiD/fJAKIXNNMRpkXofDzc0Axt6dnwBvhxmFiEHSlUESryetIs1D02OogCZPZYAy14Z4em4cCChtZqkEwE6kA31aW/nBj8npJwWqO3oxQ+RdBC6atxPLGgSUJI3TD+ky54j+RWttt0CNpIE91gPBUDacLbMM56EbCpFK79LYgBHYRXJj8aUcff/cC5iPmaikkCbV6JVLbe3pzmtiAGH0gh8FZ4HDw6WVR4ZIRp6FtFRGNj3NVLMG6PhLJHibx6NycLHBlDz4OTw8nEHQj3Ssh7dm69xbJP1YlGr9r9dsO9NO6py+HqaeKhw85iF43U1lbkdpzuVHQVqHOaOC1dPeWTnqTIdhrDHXBSdt4p56yVOe4ORr2ViOHxdbCeqk3WG7bU8M2yBUE+VsiRbCPjSAbKahKJlRNab2bbah/nvrL4YN3ZMR5uGto+Wf5SeKAK19IUKp1XnKc7bow4Nj/KiaxShL1jUL9PMXuetwAw3FxoxjQsfE1M46myFtwMMBrlu8dDf7BMeury4uKV8/MpNLcTI4LC9eSvHOcuHhISiOVEtV4EFY5zqIcDqErAZp+FKmphlRMKVY+jS3BqIuVQjo61SvYKncaOBQQyDwwcMArbvMJH39LtAeHH0+RiUiqyGGM9M/JWqrcDQE+Vkchh1SKjIZiPSOtojily6WmdJQ82A3+QitvgkJF2l07D08UWzAo85/IMm8PZcK5KrkDdhVUy72Ri9tnRHjvib70tyP7JHVPZ2x0qix7jtiRad8SYIu0RgNM0rydOqh2Ugh1mUX9SVYeZ20GcOJq40J5vNEpRiE6TocsYku2mZKgupyZhjZcrfjm0vORAXnmG+MvFs4kAoYfDcDgpLRLfbswRfR5PmsA7LME+UZQuZEEtbPhiPGUrOIRRfR/QJhsmKOxkb7oOfeEtZsBT11xQsk5AjImmB0KZZDhG3dv92DQgK4b5cLwgNQ4JgnTyW3+hJahoHbHtDb5Ya4SdYd8e3G0qDVbe+d3ZY+t89YtbWuo4cu0RLKE4RALKFDvEX8d6Y5D2RIvqA4P8mlTK9tLpClGNxV3P5ceg+0rmqM168JDhaIRMou/pI3FrVekRILqh4uNcHJphz5J05+NLxFvSxl1zyBqee0XcxAN2lohndDmbzkTpBylZfJE4bB5nPS9+yJF4XVnkTr56zRTl1QOKryqFomJS+vf0HN/JNkk5zcLp23VOGCV2rN6hi/CUFlTUcbju2NVjJxY/4ESnaLTWCLbhVtMPwbK3C9YYPj4bj4ube2M5h9dLfjhLmuOOFNGVpdSbBMU3Cy1eCSqc8FHhpMJnQ01IZcM4Sd65knU9z6SyB870EYQ2c1QcOFgaBkr1p36CVQFTVomRHoCcXPnW2MrQT2BCHBxdNVFIfgbLLB3YmExCOx/O+GM7bcWxJ3njQo6qkUAxqSrHikOefjA6YoFlpOGy/kCmnUib3UClXW+EfJdg2243Isom5R1E6f20Y8h12idqhMs6DuxuUAsA8BoGfbjdtt5Sr5EgybZdPtKnvct9Az9XGXMOezn3A0CE7TCX9VPVXq8IPvgJzUkjdoHvjwdz5kvXOj2LkXFIYcpY/egxfFaMFJtfNGR8nGZyaA7Kpl9c75kEQS4xdsX0yfPidrImYpomyYVnJosjXJe49BRotRiBIu6HQsVEUsL7Jt7wexRJXsov5MFcEnPHE1x8QhubDGlOjAyRF4wxWGjvGLTEuYFTH+UsO5wwLNRDSmg2OnMYnO7kjTCfeRkMfKYnT2a43hbCPXY1JAbIvpC7xk0q1a2R78MrfmGGs+vpc8vjUBY3/PT0It3ambPQ7gdOG2Ld6NktfF6gbWGvXhxr6kPSCZO4rpAu4LbaPx/X03w30Ha5DMs4INzME9NsOS49lJlXQH7KzJKkhENhdENm+At7sA72QrTwacOpBg1wwLvuMq4Zm5bfjOHaW6myg2rQX42mdK/4fhIG1w0JABNxKy+757nlnUWElVsdYGPNhZAtywgmGMiRifa+vxhLqZO7QQVjZPW9RcWLuGugffnE7mTjwz2gkufxVASoqE+JsclG6CCRbIUYsUTuHIFS6BVa8ZONBXRHQDn76IK8zOdL2UMp17HQ7ZiwtzGb+xr3sCNxwMornRBuO10iko2C68MeZ8eHfP7JTjckr9gsqkaXJO7p6XQab9w5i13JMhlPhHHjfp+iq0khAeJKtSe7M5XDVmmEuaitx+a+wsraU1m1jgWRYgFRXRB8bqiuUe3ncV+e3vO6nJDjyZSIoB8Q41BWje/ldHJgCFoIZtWtRF5DTmiFPJ/UsiJYGLh2iEk6TB5O5+dRut0c+NivOzlLFgwSTB2Gh1BfyUv9tO7KIF1WPUnIY9ykXivv5JXsnh1fuAdN2QdORsPn0kvEti1rbh84VcMnuJvZE3qdH350KBCZzhvnfmx1Dhf9q4qb1nnWDdCcJZMRubmPcAE9kdMZtXQBpbhgHNbDHjKxS99qqbqRBc/e8mCiZQIg44GiGYgijueL3UzT4x5ErEqtJGPN92kwRZijdtwmo3CevH22OdwQdRMT2ueUu4S92V4E8DGoShzXKFjotWN3Ci10JsrhYVRNG9mW2PpPakd4WEKv00g/HrVbqIxP+LpPdGAZ//aMn4hxQqj40ZrplajzjN4in42DfPCFi1gupRI+qN7Jp6gilYiTOo/Zd2RI9ucyZ48ptat6c4orPme6P+2HuZNVKEWTg1ytnWOEM9XkADsfFux+8LIDQ6YWBfVD5ZWymkQDCDC6V7zTYSJJj8XGPSCben4w2Ta1A6+TmxzkhlsHGcmzV03SKctpxcKFFXPWiGA8iZehQ6MHI82wA8R5O6dQlZQ9I7eSz0EhRAhRnKVyOd4XIY8HVxx7Ow0sbQd99ZCF8OnR6dgVTgSBuj/JPnIFqVtGAdaOXYBVO5M6g4/iXH2+Nn2aP3vonDt37IkXGlLUrcwPjzNxJUO5uOM5DuABulSKm/AtFoR6FF5G86nC3HgJFtGBxxDrzENO5dF0hHYKI/16p6VGPkgXdL+n+WNSREuUch4rMQow4uspGXVI9U8kR/IOIJhbzjiDh0azhK+1Lz5YS7fUDWQXN0vqvEiby+FbY13qFiau0yNG0r3O4AcSNgCzWXybhVtmVEEuzxbUSNolgGUEJlwsxRafJTPmsPg36hqwXBuvN7w/6t2m+AV8N6Wy7iCNcpjontpEyxwssQGOav0rzc7L7ayq3mYRqnvVqjUI8EQ9BNEuiZ5cewzOiTTdyu4zYw+E/fRRbNL9ui1Ue7kRIbogzDM9h8Tkd5XdG6h9mqUsHdLJhBhWMU+IN9gomjyvgThzin/xLTEFZLG19uEog5BJ01BP0x5PQ29opMdVhTNqwmq0P64j0jfmhBeoZBtBjngBvm13S8U7bNFM4nYpkO6Qx3B64fPrfHpCrKyOWe4rT+PxPDLB3KC5RyQK3LUcQP5bh4+XY/HssECp78KTqlnBn/UQ6ID0GTdQz9GB7kPbdzlRNtq+rLVde1Jr0NHxUe3nlrrV3X1hW8pLo6XlT/NMLvcBmerkCteupNOwxFNT7TIj5GuNbESxenOQbNPmldVUik/ccU19CO7E9JDAeF+OF4gBJWWa3fBBo3QtSadw8sy53J0U9emtYxFEPJB3gd5JJmdktYFuqXwfRJxv9Oi5TrDwKBIfu/v4gG8TXN+lrHXHU8JCNbuSMeuUKR0/nZPoIdPGbzQrQ5nnGLdV4A9mYgUXOsdVum2DQZoK4VLpxERf+Lvce9MFulWGjWv93WA6Zbm659bdVpdSg2oa+zLiY19g6GhIOqlE5xRWI2VwH76z8nJj7L0UcCCjI8ciSdZm/X48RiwmUEzi04fKvxE8ts09YWh9BvrHJU05NBwAro79njSQM5/6ZzweZjIcj4caam3SbpkNZSjSBg14QQEed+ijNi3myiAMVGCh2dTuOjFNeKwOLr3d/Ho506ctH3R9uPHu2Wid52Ai2dhpXikZWG55TfggK7xNBMymlei8G5uEOERbPm/8aVvlAMYmyWvSKyYvS1tjqYNZrabolDScT8O+wjHvCRup3vM0NsUoel5LfeOz6Qo/0iM59JDCZaeU4xiLvJujZEWujTfRU4RRFEHQ8HIaK0nO0rAM73JCqxVXQxsPmcep4ZOCeiaEmQ7qeT5zR24UQYmQqAwKSa5/4FTn3jPnRnvXLZ1E+aYcQbO6PPE10DmgqMKq1+Jpm3Ix0V493rCjJq1c7A8tIRynOE+z2YfKK7/gWIGrGmJzPm8BNogmaJTvm7Qsq3NFeoSPoxOq3/Vs30/mob5PToTJlzHKUbx/GvRychfW7SIuReSg6LVkmFaImfrNw8+unF9abL5ecQdNfA1Tkask01sQPsPyLkLI8yzHnqiem2sdt3Nl8Fdqb1GCPB6qa3LXriSi965meoDFea520Fy8HQUEvnFjOgK4i2veTLSZ5xq4ibfKyIUkmqqYqtr7ohqYdV05t0KVUM0HgOR2qwzYozmW1bnRtS1nu1V0H/cpL84O292w0A50eruwAo2HpL1kthCsFqR4bCNkr78mq4OYt/qtkrciJMRoFh2nbHJXD0TZSfjroKtK5PMYWoX9aaXEPmdFQddCknRWj8qeDkXM51A7qe1em8emWDODe9jnPng+fZiGcqeHNsAkI8QoL7tg5F7l0asxNcIamDMpdzo7PBqUYdF0eVYez9tKZrSpLXbVOmlkvKgBqjua66TC09rSQ2dO6IEMGT30XLkp1J69stx0afj20Afqo+U4QFs4CIJ8jtZFbjBJmM/n4wME3gjStqCLE1Nhjnt+oADLtd1QIA+nBh11Jeq+0a0iRh7HCTOMgxLdQ2U8Kw0T3RafVKBLw8Gm7+r2jZ2rBr7cKX81m5vunV3u9uitW4UTyuleEie6POCpHhNN64pCeUIvCJkGZUbsbSaz+hkd8+WRDKjimqE1kye6sUZC2dpgsr2z0kH2dNKIDD3g0llOMV27LZPC61kJuIXuoRt0OWES6k5ymLpOY7MkNfN9utAoGrpZFKNrGk8xotN27rYxYqSeWazJo9YgRKsTOzMtWa5cf5hqx2MZmvEGhrYjrb2nsztgXeQADmSu9hHrg0BQEZ/NbhxTNYa1EoQsIbsT1wefLFJBZ7gNG6mC9pwevnAa7ukGMS7OMRUlgMMh+0y3PHd/4r7jB3J7fV4PzU6fQPlHAVFlrg9Yikcr8m2V5xMbXbnQ6GyjUxUUEZ4RvZpdeKolWoSz50ZfDycYwalzpByc5xKR0nBHqDnSE2qa0GEYd327u4Ta8VEbhj6BP1wI7afcCa7HxY1gKWBwfCk42MmYtRQ1Hb1duLPZGWLFT0vNOhcVoe5sc92vUtSLxyP9CC+UVj74hLpVBS8ZKXoqmi7fV0InZ60KMuJC3HD8Fq8rsMDcTbNJ9I+7pp4fm2nbVoldzFIX9OsEo+oBEXJnn032VS4FnaDw+uHw7HMpaxJUpNryytQFTQk7LcNmY6jtjurpMJIzPh1BfZ0QVgk87DE5vc2cKGa2uAPENdOBcSiIFyPzEG45xW1B1Y1bthsFvMh9db6O9+5EtVJW20nESCjTeIsIKuQzD68OEaVPlQQIkicu0ZZtHAfLAzxO22LFe1OZgPedgzoThOx0PoX4anoIZ9F3gEtDMnqO1sFDBDmO6JuPADBmcN3BaqCLLHEyIrqXS9zdGh/EiLiSaAbjY74v1zmtaz9Picm21j7gRSWT7B4AmmCAVDa4tLYYwCEqj2cAqqiDVUT5hcndI+xETZKZ9vNcK+nj0MzTrSs3SCA6VZjD1tS05Frv+Szc14vbb9XNoPd9D+BUxzsmUgN+D63TPLUXyziq9uv/m9Wfl5ujD0GBj9gMEwqMpyN6QYkToYYMXkXnlNk0fO5RjE/Fu8CmNqOJhzsC1LhJ0o0m5gMCaAeyeqMOaMPuzDlEpSUicytAC2bTmsLJvtzMoUsAKjGgXi+2PCV5ldaTebxLkJjVJ+EkQjjMlSNn0mUojTmfmCUtsE8Kq5lcRviiADTzoE0nUdD2xw2ze/Q432peARjm4QyLjvR7YeopYav7cdANu+pxo37wM5OLLvGMdBHl6j1QwM56TcVnnOgu0L7dkglKrkjAVP1TeGya5B+EDGNIyPe3851sG5mToM0gfJ7kJv7Y7VuHuZH0wLJHv8vP9RFPkJ9ZxtALSra2Jz6swlMMjbW+is7aQrXL6eeeTQQaqW8ISJfJjk8lftAyHN32p1qMHKGVDHouWKhD/I0VzXY5R+JyroNeihIbmeWQHSAaxSsAB2BxygA1uiDH2mCSfTVol0ZonyJSlXeEeIOK54EmF4mrYbYp0UxP1eGhlv5TnOTzVSzRErl5Jaa0FzMy5t6axUC4o6thctmk64XsVRMS9VzXGpuVeFpxLwVr7jzpYurURVulUTofcncRj8LxUe6s+disiOGZkegm62hebnqzgubWLbOm3eTj7eFWE+tOHkWS7WZoITvj3UnXHRDyKN6yF7WzIRAzBUE4YRepJMyd8HQP9q3QBVOWrie2ezTcWtxC+6xdb6TLqE7C6jen7BWfuDvcxGG0fn5C2oieF6jfgFvS3GOMyX5aOsYTQ62fWqxAFqi0CkLhnNS2nCfVnjyvh5q4cSWoUnKs1++reNYed1doTHEnzltoXuFuZWwGiSw20q4H47xQt6ON0DKekPWgmvmOyE22KF0XeGJnPWTp5s3niTkb2VmYUQj3bQv3vad8ELf4TEBhXcf4mDXopvMGIDZJzSpoYbHJxZE6ajrfjER3CEJICrZktvged23+uG2qpXjPZH3OqGLF/nTrab52T6vDyp12eLYFL7ghRMubCrczMlVDROlJEpGz0KWxkOuX6nKqFjvSUfdchgSkVEk/w7ckH+TLqi+DvnW+OyA2vZiXqyAhpDljvXb1r0P+LCgIt2VCoSEZMCtZpqHSjXZ6iJIcvbkHzSA5KMmZ0sXE23o2VPQ2vF6GxuK0LWM3WW/rY9DX8wG6HfHJ25sWgwDN7Xt0n+fTMY+DJbvvdL0FTnMJL3s1k5RV4YCFPNa8VwpAb5MKa82ePq4tNx0Sr5+VgjlJDQVwqCo0UqQRB25N4hNRBiRKAl11Qhe1FMYrJkbHYcVsHNDT6NJKK7nIp57Oghqi4scsrTd1Piqj3Z5B1x373qkGYrzA44XoOwBTg8WigyLJRW0yaxTwlCLow5tux3HpD3EW7ZqJ6xIZusvjQrvrydnJIF0ZZqCsxrLo4+X6sC6bcB0THoGZBXefXB1KOIkyaba743WnsW6Li1i+x9KDtqunirPwEUEQ834UXNBVxEMTwAnsTqRQ8WgNco3BrHK7DCLsJ2TWksI98o5RD9FCYIU4ICRbfhsrU4Dou2GV/omUWJFKlvawro6YUW67xrfrtk9hW5zrO+DGU2taT+9+wQpy0WjzEY0ly3WlrXrIZX1IzDSIu5y5FZd0PYcVmDTv0e2RH/GRoM06WLCLpe+J6iusxUHHRW3FxabF0B6Ym7cWdRTebpc9sk9PUfYE36IkpYRSvm1yQLbiO8RP851NmHCYMAuFsPTa1GXZzrP2fELIPOZ4MiTF1i6PhoWWEZAI35MIwvWsc0dPEwWPzz3bnc0eZTETwg1FVOZ63eTmBBmOHeReNhPuWYr2vd1l56aWcZPtJG/rsUaO3iXnyhUOcrhJPCNGMsFsitmwRF1rqJQ93QnnOhgwWsQXdJTndH1G/QmJXaDPpOxTAdN62NWZkecuuXjBktwFDtGejFSvUmFgKgQPeVhft/XWm/mMNaBdEdTaACqVaAh6ihWlX5f9StLhterETKQPryO0Pj+2KAJBat5K2xHG5ceUc0vS0M0JFSjEvi0I/sxTDyTCyCeP7mmwp9PimycQOFM6293p2RFEqp0T2VpUHCq3Dif4xvY3wPvT+Y7OHQrvbeT2spuS0y1qKBtlaTI+x8lExO4E8TfKOBCdkQqDo0oewfHlJnoBwZ65EzTKqHFyWj1EXWJSS7saXC07GbDKUBbheZYzjLzhnM/Y8dHfUNmKzhdystJUyqMOPclVdjtAq3a+i8LMutcwtyPPyFZzmiy709Sp2itYOWFj15fUQpHQE+emp39p2wTCpAxnxkXzRHLj4VaJWoqE2VUxx0iNDanm4Ju+SZrqtDOLK50rYeylHIg8TEh2Z5+3SZHPh4BVR942FvkajMdboC2ddby2FFMeW8dhHaKpJ4Hxbr0dp+7pFBv6lQqKIBtW+iHeyqINUe4md5OMUoR1bQj7LJzzQ1/rVbETAsGM1/nakuSDTGk9UNv5IZ94adFdaEV0J3CkcjNV/bCG4xabcYxMhjdunXqXz8hQ3V1Fl556g7uPzqg80Aqf6SMM9wNkEjBk4Mth2y4kHyWHHMZeHUnF0NW+I61jpg5ZlO481IYJhc7NcmTuSDqpfGTC1uCRm7M9j6KYI6IgknxZWU3rZA9zD3OhkWlQ9rBuPnVuIgXlvtcIY9ASHvgZbwR4rG3VCD0evf7YuwiaC3XLtfB8NILGuj7r8TY/xkE6UVerQp/MxeECgOmUvqXMfq1nuE8aTrZrdt2VC7gmcAL0Db0XV0bzTqmjTZS+xOejo8xcjzLI9XS89dxwl8YdxTiLsGJVlEu4Z5ZNu147+DlF/RF7WFGqJ3yOHOabnIY2ry/O4bGbmTGv9+TOH/eOY6lLG6EyyOOF8AdNnGti8uMWZwItwc+xnVb35jIiCP+I3eGcGxrAK+esDzH5cCuTNHFErPQv0BruVyR8FEh3ujKP5Hx+Pu0uOW16vy98Fq2HRBp4aRp9yj4JrdxJaspvkRn1epqAJNpEZpYZZwt6lmX/4z++/PDl9a745zvEf/T7Fa/X/P5fe2Xw47W//g4W7JLs9Tbx6yXdn97X+ukPV/+fP3yZkgqs/fG249ysxaei89JP2Y8fbzz++GdvPM77x+899N3rh6S+vaK4RMXrJxC/vV38ekn5/YX8P3yX+eNN0R++/OYnEV5vWE/VPUre9Xv/rZH3dzORr8RX5Mvf/x/pb2qn7lIAAA== -->

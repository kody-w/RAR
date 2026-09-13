---
name: "rappstore-kody-w-rapp-crispy-singleton"
description: "Local-first meeting stack. Records a meeting, denoises it with RNNoise, transcribes it on a local whisper.cpp server and writes notes via a user-owned hook whose default sends the transcript to Anthropic. Audio, denoising and transcription never leave the machine. Actions: doctor, record, denoise, transcribe, notes, run, list, read, bench, live_status."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-crispy-singleton", "rar_sha256": "bb90598a858eef6dbf8c231782496f596669f92706bca1454f8fd9821302a2be", "source_kind": "federated-rapplication", "source_commit": null, "version": "1.5.0", "author": "@kody-w", "tags": ["meetings", "audio", "denoise", "transcription", "local-first", "privacy"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_crispy_agent.py` and embedded as the fenced Python below (sha256 bb90598a858eef6d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_crispy_agent.py` first:

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
    "version": "1.5.0",
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

<!-- rci-capsule:v1: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 -->

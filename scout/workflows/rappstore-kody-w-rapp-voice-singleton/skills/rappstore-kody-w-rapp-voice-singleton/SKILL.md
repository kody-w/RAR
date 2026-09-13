---
name: "rappstore-kody-w-rapp-voice-singleton"
description: "Local hold-to-talk dictation. Speech recognition runs on-device via whisper.cpp; audio never leaves the machine. Actions: doctor, dictionary, add_term, stats, process."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-voice-singleton", "rar_sha256": "a04c1100a70545f13b0cdce6c39e24c34f55daae4aeaf8fde6b6e9e1d5b1e785", "source_kind": "federated-rapplication", "source_commit": null, "version": "1.1.0", "author": "@kody-w", "tags": ["dictation", "speech", "whisper", "local-first", "privacy"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rapp-voice-singleton`. The original RAPP
agent is preserved byte-for-byte in `rapp_voice_agent.py` and in the RCI capsule.

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

RAPP Voice: native typed actions first, legacy Hammerspoon fallback.

The native executable accepts the existing five actions as JSON on stdin. None
can record audio, inject keys, or invoke a polish provider. When no native app
is installed, the legacy hs / localhost backend remains available. A native
failure is reported, not retried through a second backend with side effects.
Stdlib only; no protocol, manifest identity, or egg changes.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "What to do. Default doctor.",
      "enum": [
        "doctor",
        "dictionary",
        "add_term",
        "stats",
        "process"
      ],
      "type": "string"
    },
    "app": {
      "description": "Frontmost app to format for; terminals and editors get unformatted text.",
      "type": "string"
    },
    "term": {
      "description": "Vocabulary entry for add_term. Either a bare term, or 'heard text => Canonical Term'.",
      "type": "string"
    },
    "text": {
      "description": "Text to run through post-processing.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_voice_agent.py` and embedded as the fenced Python below (sha256 a04c1100a70545f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_voice_agent.py` first:

```bash
python3 rapp_voice_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_voice_agent.py   # or on stdin
python3 rapp_voice_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""RAPP Voice: native typed actions first, legacy Hammerspoon fallback.

The native executable accepts the existing five actions as JSON on stdin. None
can record audio, inject keys, or invoke a polish provider. When no native app
is installed, the legacy hs / localhost backend remains available. A native
failure is reported, not retried through a second backend with side effects.
Stdlib only; no protocol, manifest identity, or egg changes.
"""

import json
import os
import shutil
import subprocess
import urllib.error
import urllib.request

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "rapp_voice",
    "version": "1.1.0",
    "description": ("Local hold-to-talk dictation. whisper.cpp on-device, filler "
                    "stripping, app-aware formatting, weighted personal dictionary."),
    "author": "@kody-w",
    "tags": ["dictation", "speech", "whisper", "local-first", "privacy"],
    "dependencies": ["@rapp/basic_agent"],
    "requires_env": [],
}

HOME = os.path.expanduser("~")
VOICE_HOME = os.environ.get("RAPPVOICE_HOME", os.path.join(HOME, ".rappvoice"))
DICT = os.path.join(VOICE_HOME, "dictionary.txt")
LOG = os.path.join(VOICE_HOME, "logs", "rappvoice.log")
ASR_PORT = int(os.environ.get("ASR_PORT", "8765"))


def _native():
    override = os.environ.get("RAPPVOICE_NATIVE_CLI")
    if override:
        return override if os.path.isfile(override) and os.access(override, os.X_OK) else None
    candidates = [
        "/Applications/RAPPVoice.app/Contents/MacOS/RAPPVoice",
        "/Applications/RAPP Voice.app/Contents/MacOS/RAPPVoice",
        os.path.join(HOME, "Applications/RAPPVoice.app/Contents/MacOS/RAPPVoice"),
        os.path.join(HOME, "Applications/RAPP Voice.app/Contents/MacOS/RAPPVoice"),
        shutil.which("RAPPVoice"),
    ]
    return next((path for path in candidates if path and os.path.isfile(path)
                 and os.access(path, os.X_OK)), None)


def _native_action(action, kwargs):
    executable = _native()
    if not executable:
        if os.environ.get("RAPPVOICE_NATIVE_CLI"):
            return "Native RAPP Voice override is not executable; legacy fallback was not invoked."
        return None
    request = {"action": action}
    if action == "process":
        request["text"] = kwargs.get("text")
        request["app"] = kwargs.get("app") or "TextEdit"
    elif action == "add_term":
        request["term"] = kwargs.get("term")
    try:
        encoded = json.dumps(request)
        if len(encoded.encode("utf-8")) > 65536:
            return "Native action refused: request exceeds 64 KiB."
        result = subprocess.run(
            [executable, "--action"], input=encoded, capture_output=True,
            text=True, timeout=30,
        )
        response = json.loads(result.stdout)
        if (not isinstance(response, dict) or response.get("runtime") != "native"
                or response.get("action") != action
                or not isinstance(response.get("text"), str)
                or not isinstance(response.get("ok"), bool)):
            return "Invalid native response; legacy fallback was not invoked."
        if result.returncode != 0 or not response["ok"]:
            return "Native RAPP Voice action failed: " + response["text"]
        return response["text"]
    except (OSError, subprocess.SubprocessError, ValueError, TypeError) as exc:
        return f"Native RAPP Voice action failed: {type(exc).__name__}: {exc}. Legacy fallback was not invoked."


def _hs():
    for c in (os.environ.get("HS_CLI"), shutil.which("hs"),
              "/opt/homebrew/bin/hs", "/usr/local/bin/hs"):
        if c and os.access(c, os.X_OK):
            return c
    return None


# Allowlist: name -> the exact Lua expression. Nothing here interpolates input.
_LUA = {
    "healthy": 'print(require("rappvoice")._serverHealthy())',
    "hotkey": 'print(require("rappvoice").CONFIG.hotkey)',
    "dictpath": 'print(require("rappvoice").CONFIG.dictionary)',
    "accessibility": "print(hs.accessibilityState())",
    "mode": 'print(require("rappvoice")._stateMode())',
}


def _lua(key, timeout=30):
    exe = _hs()
    if not exe or key not in _LUA:
        return None
    try:
        p = subprocess.run([exe, "-c", _LUA[key]], capture_output=True,
                           text=True, timeout=timeout)
    except Exception:
        return None
    out = (p.stdout or "").strip().splitlines()
    return out[-1].strip() if out else None


def _asr_up():
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{ASR_PORT}/", timeout=3) as r:
            return 200 <= r.status < 500
    except urllib.error.HTTPError:
        return True
    except Exception:
        return False


def _read_dict():
    if not os.path.exists(DICT):
        return [], []
    terms, subs = [], []
    for raw in open(DICT, encoding="utf-8", errors="replace").read().splitlines():
        t = raw.strip()
        if not t or t.startswith("#"):
            continue
        (subs if "=>" in t else terms).append(t)
    return terms, subs


class RappVoiceAgent(BasicAgent):
    """Local dictation actions, preferring the native app over legacy hs."""

    ACTIONS = ("doctor", "dictionary", "add_term", "stats", "process")

    def __init__(self):
        self.name = "RappVoice"
        self.metadata = {
            "name": self.name,
            "description": ("Local hold-to-talk dictation. Speech recognition runs "
                            "on-device via whisper.cpp; audio never leaves the machine. "
                            "Actions: doctor, dictionary, add_term, stats, process."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["doctor", "dictionary", "add_term",
                                        "stats", "process"],
                               "description": "What to do. Default doctor."},
                    "term": {"type": "string",
                             "description": "Vocabulary entry for add_term. Either a bare "
                                            "term, or 'heard text => Canonical Term'."},
                    "text": {"type": "string",
                             "description": "Text to run through post-processing."},
                    "app": {"type": "string",
                            "description": "Frontmost app to format for; terminals and "
                                           "editors get unformatted text."},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    # ------------------------------------------------------------------ actions
    def _doctor(self):
        terms, subs = _read_dict()
        hs_present = _hs() is not None
        lines = [
            "RAPP Voice environment",
            f"  Hammerspoon CLI    {'yes' if hs_present else 'MISSING — hotkey state unknown'}",
        ]
        if hs_present:
            acc = _lua("accessibility")
            lines += [
                f"  Accessibility      {acc or 'unknown'}"
                f"{'' if acc == 'true' else '  <- hotkey and paste will NOT work'}",
                f"  hotkey             {_lua('hotkey') or 'unknown'}",
                f"  state              {_lua('mode') or 'unknown'}",
            ]
        lines += [
            f"  speech server      {'up' if _asr_up() else 'DOWN'} on 127.0.0.1:{ASR_PORT}",
            f"  dictionary         {len(terms)} term(s), {len(subs)} rewrite(s) — {DICT}",
            "",
            "Audio is captured to a temp file, transcribed locally and discarded. "
            "The opt-in polish hook is the one path off this machine: its default "
            "implementation calls `claude -p`.",
        ]
        return "\n".join(lines)

    def _dictionary(self):
        terms, subs = _read_dict()
        if not terms and not subs:
            return f"no dictionary at {DICT} — add one with action=add_term"
        out = [f"{DICT}", ""]
        if terms:
            out += ["terms (bias + enforced spelling):"] + [f"  {t}" for t in terms]
        if subs:
            out += ["", "rewrites (for homophones bias cannot fix):"] + [f"  {s}" for s in subs]
        out += ["", "Biasing alone cannot fix a word that is a homophone of a real one, "
                    "and the mis-hearing shifts with context — so a rewrite is per "
                    "mis-hearing. There is deliberately no fuzzy matching: it would "
                    "corrupt genuine uses of the real word."]
        return "\n".join(out)

    def _add_term(self, term):
        if not term or not term.strip():
            return "add_term needs `term`"
        term = term.strip()
        if "\n" in term:
            return "one term per call"
        terms, subs = _read_dict()
        if term in terms or term in subs:
            return f"{term!r} is already in the dictionary"
        os.makedirs(os.path.dirname(DICT), exist_ok=True)
        with open(DICT, "a", encoding="utf-8") as fh:
            if os.path.getsize(DICT) if os.path.exists(DICT) else 0:
                fh.write("\n" if not open(DICT).read().endswith("\n") else "")
            fh.write(term + "\n")
        return (f"added {term!r} to {DICT}\n"
                "It takes effect on your next dictation — no reload needed.")

    def _stats(self):
        if not os.path.exists(LOG):
            return f"no log at {LOG} yet"
        dictations, total_ms, engines = 0, [], {}
        for line in open(LOG, encoding="utf-8", errors="replace"):
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("event") == "dictation":
                dictations += 1
                if isinstance(d.get("total_ms"), int):
                    total_ms.append(d["total_ms"])
                engines[d.get("engine") or "?"] = engines.get(d.get("engine") or "?", 0) + 1
        if not dictations:
            return "no dictations recorded yet"
        total_ms.sort()
        med = total_ms[len(total_ms) // 2] if total_ms else 0
        return (f"{dictations} dictation(s)\n"
                f"  median total_ms   {med}   (key release -> text ready)\n"
                f"  fastest / slowest {total_ms[0]} / {total_ms[-1]}\n"
                f"  engines           {engines}")

    def _process(self, text, app):
        if not text:
            return "process needs `text`"
        exe = _hs()
        if not exe:
            return "Hammerspoon CLI not found — cannot reach the post-processing pipeline"
        # The one call that must carry data. Passed as a Lua long-bracket literal
        # so quotes and backslashes in the text cannot terminate the string, and
        # the payload is refused outright if it contains the closing delimiter.
        payload, appname = str(text), str(app or "TextEdit")
        if "]==]" in payload or "]==]" in appname:
            return "text contains the Lua long-bracket delimiter and was refused"
        lua = ('print(require("rappvoice")._processFor([==[%s]==], [==[%s]==]))'
               % (payload, appname))
        try:
            p = subprocess.run([exe, "-c", lua], capture_output=True, text=True, timeout=60)
        except Exception as exc:
            return f"post-processing failed: {type(exc).__name__}: {exc}"
        out = (p.stdout or "").strip().splitlines()
        return out[-1].strip() if out else (p.stderr or "no output").strip()

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "doctor").strip().lower()
        try:
            if action not in self.ACTIONS:
                return "unknown action '%s'. Try: %s" % (action, ", ".join(self.ACTIONS))
            native = _native_action(action, kwargs)
            if native is not None:
                return native
            if action == "doctor":
                return self._doctor()
            if action == "dictionary":
                return self._dictionary()
            if action == "add_term":
                return self._add_term(kwargs.get("term"))
            if action == "stats":
                return self._stats()
            if action == "process":
                return self._process(kwargs.get("text"), kwargs.get("app"))
            return "unknown action '%s'. Try: %s" % (action, ", ".join(self.ACTIONS))
        except Exception as exc:
            return "action '%s' failed: %s: %s" % (action, type(exc).__name__, exc)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

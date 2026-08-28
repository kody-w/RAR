---
name: "rappstore-kody-w-rapp-voice-singleton"
description: "Local hold-to-talk dictation. Speech recognition runs on-device via whisper.cpp; audio never leaves the machine. Actions: doctor, dictionary, add_term, stats, process."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-voice-singleton", "rar_sha256": "cc241dc84953742d1e6925db17f4b20065573687c7d4b71e53699a3c0df2618c", "source_kind": "federated-rapplication", "source_commit": null, "author": "@kody-w", "tags": ["dictation", "speech", "whisper", "local-first", "privacy"]}
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

RAPP Voice — hold a key, speak, release, and cleaned text appears at your cursor.

Speech recognition is whisper.cpp bound to 127.0.0.1. Audio is captured to a
temporary file, transcribed and discarded; it is never uploaded and never kept.

Unlike the other RAPP apps this one has no CLI — the hotkey, capture and
insertion live in Hammerspoon. So this agent talks to the running Hammerspoon
over its local `hs` IPC socket, and to the speech server over HTTP on localhost.
Both are on-machine.

Every Lua call is a fixed, parameterless entry point on the module. The agent
never builds Lua from user input, so it cannot be talked into evaluating
arbitrary code inside Hammerspoon.

Stdlib only.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_voice_agent.py` and embedded as the fenced Python below (sha256 cc241dc84953742d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_voice_agent.py` first:

```bash
python3 rapp_voice_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_voice_agent.py   # or on stdin
python3 rapp_voice_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""RAPP Voice — hold a key, speak, release, and cleaned text appears at your cursor.

Speech recognition is whisper.cpp bound to 127.0.0.1. Audio is captured to a
temporary file, transcribed and discarded; it is never uploaded and never kept.

Unlike the other RAPP apps this one has no CLI — the hotkey, capture and
insertion live in Hammerspoon. So this agent talks to the running Hammerspoon
over its local `hs` IPC socket, and to the speech server over HTTP on localhost.
Both are on-machine.

Every Lua call is a fixed, parameterless entry point on the module. The agent
never builds Lua from user input, so it cannot be talked into evaluating
arbitrary code inside Hammerspoon.

Stdlib only.
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
    "version": "1.0.0",
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
    """Local hold-to-talk dictation, driven through Hammerspoon."""

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

---
name: "rappstore-kody-w-rapp-voice-singleton"
description: "Local hold-to-talk dictation. Speech recognition runs on-device via whisper.cpp; audio never leaves the machine. Actions: doctor, dictionary, add_term, stats, process."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-voice-singleton", "rar_sha256": "cc241dc84953742d1e6925db17f4b20065573687c7d4b71e53699a3c0df2618c", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_voice_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rapp-voice-singleton:992933de2a060117d5437af90b339e95923921f0c567b37c7971f30d270bbc86", "kind": "skill"}, "author": "@kody-w", "tags": ["dictation", "speech", "whisper", "local-first", "privacy"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rapp-voice-singleton`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_voice_agent.py` is
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

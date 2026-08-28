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

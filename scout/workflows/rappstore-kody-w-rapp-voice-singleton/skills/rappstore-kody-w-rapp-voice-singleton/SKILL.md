---
name: "rappstore-kody-w-rapp-voice-singleton"
description: "Local hold-to-talk dictation. Speech recognition runs on-device via whisper.cpp; audio never leaves the machine. Actions: doctor, dictionary, add_term, stats, process."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-voice-singleton", "rar_sha256": "39028adae65b34b524fc615ca4bb7a135d4bf5720c7a5bccb51328891f52b398", "source_kind": "federated-rapplication", "source_commit": null, "version": "1.1.1", "author": "@kody-w", "tags": ["dictation", "speech", "whisper", "local-first", "privacy"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_voice_agent.py` and embedded as the fenced Python below (sha256 39028adae65b34b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_voice_agent.py` first:

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
    "version": "1.1.1",
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/7V6d5PjVpLnV2HUxoSkRXcThnCa0MXBkTAECEcC4PaGBA8QlvCkdr77PbCqtZrVaOb+uGNFVcEk0ucv8+Hx1zd/HLKme/vx7X8XTfT4PL99eoviPuzydsibGlw/NqFfbrKmjD4PzefBL4tNlIeDv97+srHaOA6zTReHTVrn67VNN9b9pqk/R/GUh/Fmyv3NnOV9G3dfwrb968Yfo7zZ1PEUd5sy9qe43wxZvKn8MMvr+MuGCVc2/Y+bqAmHpvv0Egeu+N3j08aPop+HuKs+bXqgQv9p03ZNGPf9F6B3vPhVW8b924//8Z+f3nJw/Pbjr29h6ffg0pvpt+2lARoxaVwPgLz06xRcbx/AATU4BwomTVeBS1GcbD7Ovu/jMvm0+fd/L2a/S/sffvxabz4+/kurzU+b79/vfUnj4fuvb++Xv779sGm6zde3dyPA6Zd+AE79/ocvZTPH3fc//DejoXv8ju36yZNv3Otm2OT1ZtXiC8PZ0kmz/gft+uniYexqIG2si7qZ629Pf/eX/rsvGxvw3/yl//q2+cvm+/c7nwDt+vvl1uT197/n/sMPf8++BoGeYmDlz+9HP78z+I3Ph1/+oP/Hc3n/MkFr6vjP9X6n/TMX/PTT79z450xeRvz8Tvf9D/+c2W8J9X/B8Dfaf8H0W2b+a5bfKP8+b96f/eGfC3kl/b+W8CL7F/p+FM6/ZvZB+D+1XQag7bf4f8v9tv2jCf+fkjNewrgdNsLr38rP79drP/6J8N8J3SR+XsbRKvaPoodHG38P+Pzw5WeQ8VX888+fVrY/vP0NQEoNanh8hycAE//2bxs1D7umb5JhY4XNOKzYN+QVSOWvtQ0wb03/Fdu6Fez6PCjjDzrg01v8rlGTbH75wN5tBxz4eVpB6nOf12kZD039C/ARYNF0eZrXAIlNRte/1v4KYiv7tov7uJviaBM8hvgzwKzP68EKGr+s7H5+sfv5Rf+lffyy8etovbmqZXLSJvTbfizjL6vKThbXHwqGfg3MjsMRsCpfHSABPgN4C8Q1JSjsYTWvL/KyBPgM4B9U3ePFG7jgx5XZL7/8Evh99rV+B1hs895U+i0g+E2dzefPwICkzNNs+FqDTtJsvvv1b99t/mvzz556MV9l6ADaPxwMNJStk7YB2ThWgAz4HkQr9qOXg3/924cbAZsa9B0QjjzJPzpPmddFHH3zqSUyn1Gc2AQx8CXwY9U23QCCscmHLxsp2fymLxC63uo3PuiO/bCJ4jauo7gOH4CrD8z5zZMrAvYA4/oEdLCxj19Sfwk6/6Vi9XMIyH/ZqJy+GZqmBH9WNV9E4OGmzoH7f4v4+3XApPuu37DfWHzZaK9+2vog5lnnf8hI/Pe4gE707XHA3AfNd/5arw0yXl310cpX9wAi4JnwI6Sf15hvwqaqQGD7b7JfNP4AMs5ufCC8+1r3H7nsd/FrFACqPDbpmEd+HcZ//UipPmvGMnr5D2i6cvqIQvQRlVcOrum9efXpH7/1kLUkow/U6EEedv3wCUwOqQ88LfpVBUqrbYD0xC/LwA+LL+/lF397/j2P/bX6/HBFi/ewx0vevwKbrETf2AMUeeUR4NcPUQ78svaur/VaEKtpXfQ+wHwC7lhLeFPED1AWwMN5PTUFYLRpmzLvs7XGpzwCZm1edVU33/RZUbLO3xMUqBxHn97T8N2irN9s30vulVWrQfFaVnG1xnrjTwC8VlvAoPRb41wBbexe3fY9KVeea9YB+OtWBw9Z14xpBpQDoWoAu29s53zINj1QcxMnCTCnB86zhqjMA+CB8vHXVW1gyNCETfkJzGh1nsRAK/AAALrh8TI8TtMNSOE6jV9jWAliBzLi7cd6LMtPbyuI/n78WictkKVVDDKnXwc0wB4MW0Mev87e47Ae/f0Y6oAaWSsjar5s+Djxx3L4GBBfo189gsHtPz7GhHWG/a1tg5NvDRccvjrjqsJ7U3sDg+KaXkDAOp6BgRDAPND0j/L3XVMP1RoRcHtVZJ0OgUrg3183K/MVnPsXAsZRDpToQaEMm7F+p1vLZe2Zq7J/EPjS7Q8SLyAHgrEEJmyAs8HfZC3jD1O+bAQQOVBHPggliPz7TAwIvstiv3uXtfnpf224bwCysQHFd38ifhn+KN5eOfwGRe/p0wL7P3+4Djz8D7gBdl18HwF8RO9j+Mf9JliLZZXWlv7wPmf/+gaSwI/8wf9Ig4+WCMg7v/vcr6ixRb7AQAo4f0f//16o/MNm+UHaZz6AcECL0TBKARExgQfYLsDRXRISCB76uyAgfQTDo12Q4CQKh6SPB2EY4AiGUhSNJDgaYDS1ZkwzdqCBriiYD9+S+uNikdfAzLckjt4R8fOqE8j/F6K+nPFbe37l9rsFv74FxA48Ju56iXn/cFvy4seYfhsyceviFOfF18OV08yps/ConZvOPeG4tsSkPHmTax9gK505r1IVTyoNfpuf/TBpWmiuCYvkdsx0dnfFmcZCh1HYJSBmiO73erglt+ONjrdXtm2F3ZWvXSK4pNB9Z6jxybQrZ0S5ZiivxGwrCx6pSUz1yKFU7oZahV1dOa5+bBST0J/m8XbZlVcBLODcymCswsph79axu4vdanuKn5zBFKBY2SZuT0sGq/nuTWO21zx87pWThCvwubBQ7paXKu45NdTvUnhcZMzv5YILoAk3XcPzXPXcOnPT2q5vPZVCR41cfpZwJ/I5qpyVNp+0I9Pt0nLxiIu8l8fFFjzKImyLl85mbCxBgOUKtseemqDJRn0tCA9x1L11SVNRO2fWAxHSR7m0EGFL+ymuilI7E0zknS2GP4uaE1y4SGWumtrtvfTGtOL12Z3gYjT0biJFsTgogaVe+Wt2wIlamQVqTpaw3d5PLRt0mtdb9Z3aH3WPCp6molEpDyG1jImo+6gR2/Jdu9Pxi2scaUu5EfHlUvUi3DxKxZmCvbU9njjyHN8uVoHdFIjlzEsctpeDte1YUrem8JRKJuzf8EhepsvjcQr6RE2ynVK0TB3tMgq+z8vVdJ4IcWBpUtDVLW6CMn2gA2zqSXHIZm1ijGRKn1m9jHrmdcqg8aChQrQxnx7mIVguat9WeqUsTlWczjsJPaPWPZVC6dEoZ92A90M8L4YdCsdHdmUJkxQpig28nqt5l7NOVfDMvYRzj3wU+2ZFC2NBMnS6SCmEZwk9W9pol26c7stSi4mz5Sgqm3SVSWkkskhVDl1uLLWLHDXOdG8wmdyauOBq3rdFPZwI086fhKx21B6Zzs5wY5TQgkxTSZ/7iWDy6wOxkYtutlXRIvtjgTzTy9LFNziabJImmME3FI4g7LM2O7pEdfK5SyA8dG88EYodDfXoXM3RHWaP6JglXhvzhp3yiIg78RW/EScmDDO1MtTDbN26HZ3UZIw2u0LjrrcYvp8gJOTZkdYmEXkYVsSXC58agalznDKTp2mAoISEY3oenoGb4DRML/fLFhpP3RPncFDfjkJ6sEnDOl+UkzA95uWgk4U+1yaUiCK9612SIrMWWS7B/b5fSEdPvaXJu2eWy6e+VkrutljQCTdnlQHZw97u+yNyUuqdSE32NF/Uq3D3QqkqJMc+gMkDOat8bQboTXv29zx/aA81Od/YtBL9gz3JPr40Kg3tcLFFE82AwKKB9p/XBRRckyUzcpxt+djHtqndmWeGCY48OAP5qI5ntaTGoHMnae49IctoKzmhbMiN2qEdUN6bk5RGU5h00Vve9q4xS7aOYaLWhvds2hZPbx9azRBIEAp3HEX5Se1o+Vi1lXbCW0wXZLEmPSHk7ovdL4cgMZN+Mi/O1n4isBLlHIe5zHNBbfSk20RLXNHoOgaqetmZ9V0Ch0ekKZukO+Iip1ayjU6J8ZBnyann6zFm0vSKm5Xp27xXG49x4FV3mY/qU9vhndjYLX2fj4E08s/HqUTu5woVKk98uJyZwvbp9ujKYp9eyEMhBlWpH/lRa86PLi7SzstUXCSjWm62Uxu3l8TW4UPoIdDjgtM0PQ0uj3dmWELK3rJ46Mg7Y5drmZRe4u1ZpLsEvu+I60V2sot5T4Xr9ULWITo6WcgI5BAdumGAOeGCmERQVvF8KO4piy6l7B6o5PQQWvUk25Z9cDwCM3JP225pwz6VwZlj7mRh2RXIcV6888dCY1yXezRklegyZ3rpctvZE1JQzXI9IdiVW/YAlUWJuSW8KeqSfkep8+VEjT1xtJWEpf1+F1+H+3Bi+NGdA9V9PIYwBgvH/TjjsJrgWri1UGHfDtsZvy4J7NuXIVdk5Bwz/ILvbnEjUkd55zvK8pSyTMS2tic/EA4vbWymkjTE7Mq46Vv6NGvpyMoolujEfYuiRhxfQhnSd6GfB7uDo6pMdYWLCbuHpDv2g7h4omQf5fiY4q50bJ7czEcVaWKXHoYPubg/sgFrZsrQsCd0q9snLqZZOWqGVoaVC+XE2VW6JWDWN7Ce6uH6cRb6g39RqlAwaSSF1SI6W9DRPMPKgTQ77dSKNC02Huafr4l08G93jY6zQ3+q3KHeCXiwx/ZeNLFRZglBui3sjm1ukunIMgugMBNvRntQNfm0v0PQdjDPu75Iq5AYPQ1WDS/kfd4wqmPio+I5ZOp0vxxd56lf+Z2ysBEnI3uO0bsjQce1rFFJklXXcTJNnkUDpH0goyqy2nxK4ek8PxXGX5obexbuEQAqQ72ntURLQqfx1xnLdpc9HVHZUnGmBhML1dzJRlXJ5ObPzCTs4wzXzw92WTrHEejyrpP85FVUQVcKFj7Yh6E8TcYGVMaY6nJOeXYI673aMh2poZmY2gnMbi2oRjWPqZ5EFsJBqZdsdjFGaGJcQ7md4HLeLfaNcaHqSITjvoIjhkM8jNPwe60MD8d0x5OYnA0a5YNaiOeCkpErtKVANHNKv5Inp07mWd9p2+OMDS5WLbXbj8xewZQ50ndEKLAQejw9Mj5qLsee2wbX+bwP9BgZjeQGsmGml4CKXP8Q12CICp43iYSNifUgl9CjUzwOtn2BFekM2gW/O5xwKy0ld2tWBVOzNoC0u1CloScKA5QiuGwVmiLsTrUkHdWjnXPC1VSe/t4/3uQTO5tXYqmwncHTTJgSMBncpEAGo5g0p3jkNwZCk5AKJQ2R6kX5vD9dClIN+qzzlYt1Ui+eL0WOMVV6VZKSxlxlLjUihR9dZpHi6FleJR5uJgQT48KLeUxesbNr3NxK7uf8KHTsiTJc0bWxk+6ZkuihvA3yrOWlwLkhoBe1j6iOeYJyhKt/nsacc9zdnQpY9IQyx+ul9c2cEbOUwBnyqAlbJByLrvARn+iVRPLPe2N/R+I9iUHna8PXZ6+DNKiOyr4jqgpuYP+Jzn19OWDZdD/7KOfMonK5P+Ghde/2mCb7rtRjssDpoL5H5/3OZxOt8y73+rDgbJGBsQa3dJAxpyoSoVZzrOrG1bFhHRsxhHumghODT/fBLCAhG5JcEpHos5WcG8tyxtRbbkeer7HG3aRWQESiJnYz4rnBFCKGvXBQ1JKqbNtOu3cPtErHtK2Jd/0STDWCieJy4rQo2+4hi193HmqCp2vX651F5KU+G3C0kpuWlokpS0hHpNjLkehVXIoNtqn4uUVsg7rFxslgW+jYC9l4xdoTcu40iYzDZaeEj7a2FbyEHsjz4cZeK+LsUt1YyBIMHgvw0LTQ5XzEHw+AdrGlODVSyUx4o3RHKbbV7gyxNMU0mhdMXMcYTN5XsjdvpyqUas434N3toM+96Pa53e+Pe+Y0P+9dqLX3/TlxUpvR+K6jApQmx3qsA7nMnFBo6Y5H/DkKhMXZpYMn4t4zoJ8m5HpyKwUzLuk0i8FYGoiRaQudKxgpM0mP2YkctDrcySx7yijIKeVRtZdrcLXQipsmZUTLMCQ0BDcMSJy3SXa680JFsJ5eKqKILWhSm2iSqBMEwHGr7lXufJwvnuZ0rkYWOxTpcvgcHG2rGMeU2fGYkqEcdZlN2MJ2N/wR0cYV9kwILa9TGlvxaQnqNHDEZiu248FprKg7CoeYj9H5dkSXyJRzG09CxrGwu3ldCvz0pCvtqFAE1QV4H05+jfVWWD3im6TGPqUVN1ERHwe+pObcXOLUxCPhJPdoUA38qCo75Vw0Gqog3HQj6Z1jUUs0qZJlQLv9oqFV5y0UERluG5xSH0o7JTInAZ459ow7Z+Vy3SkPFRuFsEZzd6IxOBaOMcegJ6ldJn7veZqWulHmsPeLrkZNNNf6Xe302969XQQAk4Ubsg8mxqZOMQqKbaK2QwVbUehZ8Iw+NAZ1XxL9hVe5hrUV8aidFf5JlQ+W1KK9VjANlM++LmWVtGWuxOD1h2o5b7OdXi61LyUhRYcczrLojnvACZji+fPpedJUOK2hOXX4MrKVB+oGfcukNwmTXJk7W/blDMtlc1K2i1XrouG5FWvOWx9BZ5+LQoHbRqQraGPH1pBuTOfHDdUbcWanomDuJ06GV50h3kApdrckTapHBLHsnUZUon3to6jpPLDGHTFp7ubqKkm4EDiWYd2W4yAmQrgPLkrwHAKl60utKpuUujSFnrkG6KI8TmRT1ua7o4dBhztjdgBCeie4haK742JPFdTI3l4jkpBk7lLVfnP32DoyraDhhof19ATn4DH60FqmKYOlwYAet517OLrq7WSfKUU0MeVa7rlaBfMlJTuIBW0xdX+FxdRD6tQz5PmOzuF1EnLnajh7jTXHvZsiYAhuLgQuMbJ0Ls09wS/zwa8N2KT2+GFBBQ4swlAqe04jTgySkQWeQGLKHpGV/W4ORrbe8qSNkHUugSESqmAa1k510mswnNhCJp51MMKTeC2CFTfJE7GPMTsqlLopDHERv16po6BzEWxwtLYDw03nFtkAsed8vBzJzukZfdmDNaEtLEdK6HHzjDQ7eQyI5FLq3G6gx2ujBZoygiVq1zLsmDdwue0vIyySISE/LqqYkSOuMWCVfjug/RF2F+QYMcseD469p0NHjb2Iz7jgCrk437eN1R+2VgQjUPaEWePenlUivAmnNodyFNVnY2DH8A6ddmpLF7gjR9h+GBo3PvBgCXXmjlgtHYK9jdVXSJl0QnG4HbK1wZJuSJMdr+Nyk5+op9/fxuxAXLuoZ4YhMiiHUPi8XoYivrGZ3lr0DFsLmoOBbxjtVDTlrVON44IcGg/RaIQ80o/KJ7Z0Etxp3rp3PZ2FxybrTHXHuq6BkqSqhvtjxzo69cCx2jjuEcdx5NPs5tj54kcEjp66BS3HUVvMRJt7d0SuObJ4ZyCO9HN63sII2tdnUc/QSEMFgcEm9EHCllaqp+x5kPj7fHuW2Rimu52IxFLjBB6PetcxGTCbgwEMFAlzveko4ck5wNlHhmEpocGYeJiDIGUNvoXpp1bNYQjWnze5CM2b790p62w/Qo06XEZ/Yhm4WsIcWvZXTz4Lul6pXcG7BNnBZ8I5LNmkF8AHtUfe9ZtdGkdoGLMgTiR0e2XqGB+1ALtoV/sZTA7w6EOWOywiyitBIJAYKbSQ5TX6AGtErZM4T5LAYkGKYO50Fttsjmv4dLkbDD4wkQ9JSY+px/EmbA81B9/PHM5oOzY7SJFIHjGXK6lh0ViBJkomkH37QR8TQTON2eIc9fHcFy6jT1AvnyQyKOniwpYud0En4TIUQTj2pEsxVi/VbUc9Zu88pLmhTITe2AfagPt+z+mDksjQyWi4KhbUyTsdYUVWCzVUGt6VPK2MDlkmX2EwAHqXPqlsxd3dSOROD9MVM5cFlSB34R8hD9bZYmecMxSt8QP1jPOTXo0nyx12CTqVgTcfSqtDHwtE1Z3mbGHfAdVEJdOek7yTYYzdZNj8WO8o93miOhnNBIwq7Bv9oBkAXcGAglXkNRYBJCZBWeKkQhWIS9oTIcRbGVoSGwZrRTA3U9e0ZXe5xQjBQ4MMspA1idV6VwOsn1MyRLhEjXDYz0fDZGAUoowxiZiQ0QPYIXdLml2hdOt1dW0+NAI/j9PJ7YP+Wkz1RHr1bvBPLpEuCLcw9RExxOmuxwSlKs+9bXaGzNJo4d8hEW+Andq1xji8G2IMVaslmRbCqWVOhKMlZnqLJp7egV/2915Hbot8B+sCVWAREjrkpougDnncSbSp4aHLLxxK8XFG3fop9zBLTUsAhhie+2RAeftmC03EE64nMR/IuJOo4jgExybwSYBau6O5nRmwemz0oy0wDPPTT2+f3tbNtI/NkH+wMbu+af5/9tb6/c1zMwF5dRivGyNd7Ec/vmT9+I+E/+enty7Mgej31+19OaYfavZD08Wf31+5f/6TV+79430bs6nftxLe35EPftq/9mS+fVtopXx9XQgcfHwjaN0uWre6Pr929V77Mvnkhy+FXlvmr90A5Av4efvb/wGQ//a+rSQAAA== -->

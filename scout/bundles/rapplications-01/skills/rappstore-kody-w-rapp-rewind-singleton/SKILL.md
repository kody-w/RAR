---
name: "rappstore-kody-w-rapp-rewind-singleton"
description: "Searchable local memory of what has been on screen. Capture, OCR and search all happen on this machine. Actions: doctor, search, stats, capture, timeline, prune, bench."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-rewind-singleton", "rar_sha256": "65e86577bd45dc30713a5b1ebb103ec411d0d2b0fa32721bec66425ee92ba947", "source_kind": "federated-rapplication", "source_commit": null, "version": "1.2.1", "author": "@kody-w", "tags": ["screen", "ocr", "search", "memory", "local-first", "privacy"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rapp-rewind-singleton`. The original RAPP
agent is preserved byte-for-byte in `rapp_rewind_agent.py` and in the RCI capsule.

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

RAPP Rewind — A local, searchable memory of everything that has been on your screen. Capture, OCR and search all run on
this machine; this agent has no network egress of its own.

Runs entirely on the machine the brainstem is running on. This agent is a thin,
allowlisted wrapper over the rewind CLI that ships in the same repository: every
action maps to one subcommand with validated arguments, so the agent cannot be
talked into running arbitrary shell.

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
        "search",
        "stats",
        "capture",
        "timeline",
        "prune",
        "bench"
      ],
      "type": "string"
    },
    "app": {
      "description": "Restrict a search to an app name.",
      "type": "string"
    },
    "days": {
      "description": "Retention in days for prune.",
      "type": "integer"
    },
    "limit": {
      "description": "Max results.",
      "type": "integer"
    },
    "query": {
      "description": "Search text, required for search.",
      "type": "string"
    },
    "since": {
      "description": "e.g. 30m, 6h, 2d.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_rewind_agent.py` and embedded as the fenced Python below (sha256 65e86577bd45dc30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_rewind_agent.py` first:

```bash
python3 rapp_rewind_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_rewind_agent.py   # or on stdin
python3 rapp_rewind_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""RAPP Rewind — A local, searchable memory of everything that has been on your screen. Capture, OCR and search all run on
this machine; this agent has no network egress of its own.

Runs entirely on the machine the brainstem is running on. This agent is a thin,
allowlisted wrapper over the rewind CLI that ships in the same repository: every
action maps to one subcommand with validated arguments, so the agent cannot be
talked into running arbitrary shell.

Stdlib only.
"""

import os
import plistlib
import shutil
import subprocess

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "rapp_rewind",
    "version": "1.2.1",
    "description": "A local, searchable memory of everything that has been on your screen.",
    "author": "@kody-w",
    "tags": ["screen", "ocr", "search", "memory", "local-first", "privacy"],
    "dependencies": ["@rapp/basic_agent"],
    "requires_env": [],
}

HOME = os.path.expanduser("~")
_CANDIDATES = [
    os.environ.get("REWIND_CLI"),
    shutil.which("rewind"),
    os.path.join(HOME, ".local", "bin", "rewind"),
    "/opt/homebrew/bin/rewind",
    "/usr/local/bin/rewind",
    "/usr/local/bin/rewind",
    # Last resort only: the author's own checkout layout. Kept so a dev box works
    # without installing, but it must never be the primary path — for anyone else
    # it is simply a dead entry.
    os.path.join(HOME, "Documents", "Fable5", "rapp-rewind", "rewind"),
]

_NATIVE_APPS = [
    os.environ.get("REWIND_NATIVE_APP"),
    "/Applications/RAPP Rewind.app",
    "/Applications/RAPPRewind.app",
    os.path.join(HOME, "Applications", "RAPP Rewind.app"),
    os.path.join(HOME, "Applications", "RAPPRewind.app"),
]


def _native():
    for candidate in _NATIVE_APPS:
        if not candidate or not candidate.lower().endswith(".app"):
            continue
        bundle = os.path.realpath(os.path.expanduser(candidate))
        executable = os.path.join(bundle, "Contents", "MacOS", "RAPPRewind")
        if not os.path.realpath(executable).startswith(bundle + os.sep):
            continue
        try:
            with open(os.path.join(bundle, "Contents", "Info.plist"), "rb") as handle:
                info = plistlib.load(handle)
            if info.get("CFBundleIdentifier") == "io.rapp.rewind" and os.access(executable, os.X_OK):
                return executable, bundle
        except (OSError, ValueError, plistlib.InvalidFileException):
            continue
    return None


def _cli():
    for c in _CANDIDATES:
        if c and os.access(c, os.X_OK):
            return c
    return None


def _run(args, timeout=900):
    native = None if os.environ.get("REWIND_CLI") else _native()
    exe = native[0] if native else _cli()
    if not exe:
        return None, ("RAPP Rewind was not found. Install the native app in Applications, "
                      "set REWIND_NATIVE_APP to its .app path, or install the compatibility "
                      "`rewind` CLI / set REWIND_CLI.")
    try:
        if native:
            assessment = subprocess.run(
                ["/usr/sbin/spctl", "--assess", "--type", "execute", native[1]],
                capture_output=True, text=True, timeout=30)
            if assessment.returncode != 0:
                return None, ("macOS has not approved this RAPP Rewind app for execution. "
                              "Open the installed app normally and resolve its signing/"
                              "Gatekeeper warning, or explicitly select your compatibility "
                              "CLI with REWIND_CLI. No security setting was changed.")
        command = [exe] + (["--rewind-command"] if native else []) + args
        p = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
    except FileNotFoundError as exc:
        # A traceback is not an answer. Say what is missing and how to fix it.
        return None, (f"{exe} could not be executed ({exc.strerror}). The tool is "
                      f"installed but a component it shells out to is missing — run "
                      f"./install.sh in that repo to build the shims.")
    out = (p.stdout or "").strip()
    err = (p.stderr or "").strip()
    if p.returncode != 0 and not out:
        return None, err or f"`{os.path.basename(exe)} {' '.join(args)}` failed with no output"
    if not out and not err:
        # /chat must never answer with nothing — the estate contract says the
        # answer lives in `response`, and an empty response reads as a hang.
        return f"`{os.path.basename(exe)} {' '.join(args)}` completed and produced no output.", None
    return out or err, None


class RappRewindAgent(BasicAgent):
    """A local, searchable memory of everything that has been on your screen."""

    ACTIONS = ("doctor", "search", "stats", "capture", "timeline", "prune", "bench")

    def __init__(self):
        self.name = "RappRewind"
        self.metadata = {
            "name": self.name,
            "description": "Searchable local memory of what has been on screen. Capture, OCR and search all happen on this machine. Actions: doctor, search, stats, capture, timeline, prune, bench.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["doctor", "search", "stats", "capture",
                                        "timeline", "prune", "bench"],
                               "description": "What to do. Default doctor."},
                    "query": {"type": "string", "description": "Search text, required for search."},
                    "app": {"type": "string", "description": "Restrict a search to an app name."},
                    "since": {"type": "string", "description": "e.g. 30m, 6h, 2d."},
                    "limit": {"type": "integer", "description": "Max results."},
                    "days": {"type": "integer", "description": "Retention in days for prune."},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "doctor").strip().lower()
        try:
            if action == "search":
                q = kwargs.get("query")
                if not q:
                    return "search needs `query` — the text you remember seeing"
                args = ["search"] + str(q).split()
                if kwargs.get("app"):
                    args += ["--app", str(kwargs["app"])]
                if kwargs.get("since"):
                    args += ["--since", str(kwargs["since"])]
                args += ["--limit", str(int(kwargs.get("limit") or 20))]
                out, err = _run(args)
                return out if out is not None else err
            if action == "timeline":
                out, err = _run(["timeline", "--since", str(kwargs.get("since") or "1d"),
                                 "--limit", str(int(kwargs.get("limit") or 400))])
                return out if out is not None else err
            if action == "prune":
                # ALWAYS a dry run from the agent surface. `confirm` used to be an
                # LLM-settable boolean that became `--yes`, which turned the CLI's
                # deliberate irreversible-delete guard into a parameter a model
                # fills in from "free up space, don't ask me again". Deleting a
                # user's screen history is not a thing a sentence should do.
                args = ["prune", "--days", str(int(kwargs.get("days") or 30))]
                out, err = _run(args)
                if out is not None:
                    out += ("\n\nThis was a DRY RUN and nothing was deleted. I cannot "
                            "delete your screen history — deleting is irreversible, so "
                            "it needs your hand on it:\n"
                            f"    rewind prune --days {int(kwargs.get('days') or 30)} --yes")
                return out if out is not None else err
            if action in ("doctor", "stats", "capture", "bench"):
                out, err = _run([action])
                return out if out is not None else err
            return "unknown action '%s'. Try: %s" % (action, ", ".join(self.ACTIONS))
        except subprocess.TimeoutExpired:
            return "action '%s' timed out" % action
        except Exception as exc:
            return "action '%s' failed: %s: %s" % (action, type(exc).__name__, exc)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

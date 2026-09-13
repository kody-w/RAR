---
name: "rappstore-kody-w-rapp-rewind-singleton"
description: "Searchable local memory of what has been on screen. Capture, OCR and search all happen on this machine. Actions: doctor, search, stats, capture, timeline, prune, bench."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-rewind-singleton", "rar_sha256": "8125b7a918528e76ff0449d9e1d66208c1e5bdc5d8e7746f3a42d64f9827250d", "source_kind": "federated-rapplication", "source_commit": null, "version": "1.2.0", "author": "@kody-w", "tags": ["screen", "ocr", "search", "memory", "local-first", "privacy"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_rewind_agent.py` and embedded as the fenced Python below (sha256 8125b7a918528e76…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_rewind_agent.py` first:

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
    "version": "1.2.0",
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

---
name: "rappstore-kody-w-rapp-rewind-singleton"
description: "Searchable local memory of what has been on screen. Capture, OCR and search all happen on this machine. Actions: doctor, search, stats, capture, timeline, prune, bench."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-rewind-singleton", "rar_sha256": "8074e7acdeb4877ba705b9ffdab99dabd4b57464b27ad38d4eb77b35e9f2dac3", "source_kind": "federated-rapplication", "source_commit": null, "version": "1.1.0", "author": "@kody-w", "tags": ["screen", "ocr", "search", "memory", "local-first", "privacy"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_rewind_agent.py` and embedded as the fenced Python below (sha256 8074e7acdeb4877b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_rewind_agent.py` first:

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
import shutil
import subprocess

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "rapp_rewind",
    "version": "1.1.0",
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


def _cli():
    for c in _CANDIDATES:
        if c and os.access(c, os.X_OK):
            return c
    return None


def _run(args, timeout=900):
    exe = _cli()
    if not exe:
        return None, ("rewind CLI not found. Install rapp-rewind so that `rewind` is on PATH, "
                      "or set REWIND_CLI.")
    try:
        p = subprocess.run([exe] + args, capture_output=True, text=True, timeout=timeout)
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

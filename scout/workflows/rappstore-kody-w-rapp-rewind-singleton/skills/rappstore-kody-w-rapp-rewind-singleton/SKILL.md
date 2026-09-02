---
name: "rappstore-kody-w-rapp-rewind-singleton"
description: "Searchable local memory of what has been on screen. Capture, OCR and search all happen on this machine. Actions: doctor, search, stats, capture, timeline, prune, bench."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-rewind-singleton", "rar_sha256": "8074e7acdeb4877ba705b9ffdab99dabd4b57464b27ad38d4eb77b35e9f2dac3", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_rewind_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rapp-rewind-singleton:cc07181bf1e48015be1235a0270baf92d87f59dd947a09d07ff5087598c8e9fa", "kind": "skill"}, "version": "1.1.0", "author": "@kody-w", "tags": ["screen", "ocr", "search", "memory", "local-first", "privacy"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rapp-rewind-singleton`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_rewind_agent.py` is
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

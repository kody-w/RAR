---
name: "rappstore-kody-w-rapp-shot-singleton"
description: "Screenshots that are safe to share. Captures, reads text with on-device OCR, and redacts credentials opaquely before sharing. Actions: doctor, capture, ocr, redact, annotate, list."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-shot-singleton", "rar_sha256": "5284459ecf14f9b7faa80f26ebefa7de33a346919ef7d32773712fa71f01b907", "source_kind": "federated-rapplication", "source_commit": null, "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_shot_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rapp-shot-singleton:1958d66a5c246abd055b40c1f0ab3cbeef7c07b8c68e34c649ce99095d8ac51f", "kind": "skill"}, "version": "1.2.0", "author": "@kody-w", "tags": ["screenshot", "ocr", "redaction", "privacy", "local-first"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rapp-shot-singleton`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_shot_agent.py` is
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

RAPP Shot — Capture, annotate and redact screenshots on-device. Finds credentials with OCR and paints them out opaquely.

Runs entirely on the machine the brainstem is running on. This agent is a thin,
allowlisted wrapper over the shot CLI that ships in the same repository: every
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
        "capture",
        "ocr",
        "redact",
        "annotate",
        "list"
      ],
      "type": "string"
    },
    "auto": {
      "description": "Redaction: find secrets by OCR.",
      "type": "boolean"
    },
    "box": {
      "description": "Manual region as x,y,w,h.",
      "type": "string"
    },
    "copy": {
      "description": "Put the result on the clipboard.",
      "type": "boolean"
    },
    "dry_run": {
      "description": "Redaction: report without painting.",
      "type": "boolean"
    },
    "image": {
      "description": "Shot name or path; defaults to the most recent.",
      "type": "string"
    },
    "limit": {
      "description": "Max rows for list.",
      "type": "integer"
    },
    "mode": {
      "description": "Capture mode. Only screen works headlessly.",
      "enum": [
        "region",
        "window",
        "screen"
      ],
      "type": "string"
    },
    "name": {
      "description": "Label for the capture.",
      "type": "string"
    },
    "text": {
      "description": "Annotation text as x,y,message.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_shot_agent.py` and embedded as the fenced Python below (sha256 5284459ecf14f9b7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_shot_agent.py` first:

```bash
python3 rapp_shot_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_shot_agent.py   # or on stdin
python3 rapp_shot_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""RAPP Shot — Capture, annotate and redact screenshots on-device. Finds credentials with OCR and paints them out opaquely.

Runs entirely on the machine the brainstem is running on. This agent is a thin,
allowlisted wrapper over the shot CLI that ships in the same repository: every
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
    "name": "rapp_shot",
    "version": "1.2.0",
    "description": "Capture, annotate and redact screenshots on-device. Finds credentials with OCR and paints them out opaquely.",
    "author": "@kody-w",
    "tags": ["screenshot", "ocr", "redaction", "privacy", "local-first"],
    "dependencies": ["@rapp/basic_agent"],
    "requires_env": [],
}

HOME = os.path.expanduser("~")
_CANDIDATES = [
    os.environ.get("SHOT_CLI"),
    shutil.which("shot"),
    os.path.join(HOME, ".local", "bin", "shot"),
    "/opt/homebrew/bin/shot",
    "/usr/local/bin/shot",
    "/usr/local/bin/shot",
    # Last resort only: the author's own checkout layout. Kept so a dev box works
    # without installing, but it must never be the primary path — for anyone else
    # it is simply a dead entry.
    os.path.join(HOME, "Documents", "Fable5", "rapp-shot", "shot"),
]


def _cli():
    for c in _CANDIDATES:
        if c and os.access(c, os.X_OK):
            return c
    return None


def _run(args, timeout=900):
    exe = _cli()
    if not exe:
        return None, ("shot CLI not found. Install rapp-shot so that `shot` is on PATH, "
                      "or set SHOT_CLI.")
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


class RappShotAgent(BasicAgent):
    """Capture, annotate and redact screenshots on-device. Finds credentials with OCR and paints them out opaquely."""

    ACTIONS = ("doctor", "capture", "ocr", "redact", "annotate", "list")

    def __init__(self):
        self.name = "RappShot"
        self.metadata = {
            "name": self.name,
            "description": "Screenshots that are safe to share. Captures, reads text with on-device OCR, and redacts credentials opaquely before sharing. Actions: doctor, capture, ocr, redact, annotate, list.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["doctor", "capture", "ocr", "redact",
                                        "annotate", "list"],
                               "description": "What to do. Default doctor."},
                    "image": {"type": "string", "description": "Shot name or path; defaults to the most recent."},
                    "mode": {"type": "string", "enum": ["region", "window", "screen"],
                             "description": "Capture mode. Only screen works headlessly."},
                    "name": {"type": "string", "description": "Label for the capture."},
                    "auto": {"type": "boolean", "description": "Redaction: find secrets by OCR."},
                    "dry_run": {"type": "boolean", "description": "Redaction: report without painting."},
                    "copy": {"type": "boolean", "description": "Put the result on the clipboard."},
                    "box": {"type": "string", "description": "Manual region as x,y,w,h."},
                    "text": {"type": "string", "description": "Annotation text as x,y,message."},
                    "limit": {"type": "integer", "description": "Max rows for list."},
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "doctor").strip().lower()
        try:
            if action == "capture":
                mode = kwargs.get("mode") or "screen"
                if mode not in ("region", "window", "screen"):
                    return "mode must be region, window or screen"
                if mode in ("region", "window"):
                    return ("region and window capture open an interactive picker, so they cannot "
                            "run headlessly. Use mode='screen', or the Hammerspoon hotkeys.")
                args = ["capture", "--mode", "screen"]
                if kwargs.get("name"):
                    args += ["--name", str(kwargs["name"])]
                if kwargs.get("auto"):
                    args.append("--auto-redact")
                if kwargs.get("copy"):
                    args.append("--copy")
                out, err = _run(args)
                return out if out is not None else err
            if action == "ocr":
                args = ["ocr"]
                if kwargs.get("image"):
                    args.append(str(kwargs["image"]))
                if kwargs.get("copy"):
                    args.append("--copy")
                out, err = _run(args)
                return out if out is not None else err
            if action == "redact":
                args = ["redact"]
                if kwargs.get("image"):
                    args.append(str(kwargs["image"]))
                if kwargs.get("auto", True):
                    args.append("--auto")
                if kwargs.get("box"):
                    args += ["--box", str(kwargs["box"])]
                if kwargs.get("dry_run"):
                    args.append("--dry-run")
                if kwargs.get("copy"):
                    args.append("--copy")
                out, err = _run(args)
                return out if out is not None else err
            if action == "annotate":
                args = ["annotate"]
                if kwargs.get("image"):
                    args.append(str(kwargs["image"]))
                for k, flag in (("box", "--box"), ("crop", "--crop"), ("arrow", "--arrow")):
                    if kwargs.get(k):
                        args += [flag, str(kwargs[k])]
                if kwargs.get("text"):
                    args += ["--text", str(kwargs["text"])]
                if not any(kwargs.get(k) for k in ("box", "crop", "arrow", "text")):
                    return "annotate needs at least one of box, crop, arrow or text"
                if kwargs.get("copy"):
                    args.append("--copy")
                out, err = _run(args)
                return out if out is not None else err
            if action == "list":
                out, err = _run(["list", "--limit", str(int(kwargs.get("limit") or 20))])
                return out if out is not None else err
            if action == "doctor":
                out, err = _run(["doctor"])
                return out if out is not None else err
            return "unknown action '%s'. Try: %s" % (action, ", ".join(self.ACTIONS))
        except subprocess.TimeoutExpired:
            return "action '%s' timed out" % action
        except Exception as exc:
            return "action '%s' failed: %s: %s" % (action, type(exc).__name__, exc)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

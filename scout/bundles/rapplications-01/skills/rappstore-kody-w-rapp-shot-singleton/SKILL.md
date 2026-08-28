---
name: "rappstore-kody-w-rapp-shot-singleton"
description: "Screenshots that are safe to share. Captures, reads text with on-device OCR, and redacts credentials opaquely before sharing. Actions: doctor, capture, ocr, redact, annotate, list."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-shot-singleton", "rar_sha256": "5284459ecf14f9b7faa80f26ebefa7de33a346919ef7d32773712fa71f01b907", "source_kind": "federated-rapplication", "source_commit": null, "version": "1.2.0", "author": "@kody-w", "tags": ["screenshot", "ocr", "redaction", "privacy", "local-first"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rapp-shot-singleton`. The original RAPP
agent is preserved byte-for-byte in `rapp_shot_agent.py` and in the RCI capsule.

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

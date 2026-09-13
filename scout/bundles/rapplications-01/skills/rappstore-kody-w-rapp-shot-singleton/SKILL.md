---
name: "rappstore-kody-w-rapp-shot-singleton"
description: "Screenshots for review before sharing. Native capture/edit/OCR requests are staged in an installed RAPP Shot app; a user starts capture and approves the final preview before copy/export. Local OCR and opaque redaction can miss credentials. Explicit SHOT_CLI keeps the legacy backend. Actions: doctor, capture, ocr, redact, annotate, list."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-shot-singleton", "rar_sha256": "7ea3d9383ed9cd998d41ff64275a3b668683fe885bb8fdc56c92900c2e9bcb95", "source_kind": "federated-rapplication", "source_commit": null, "version": "1.3.0", "author": "@kody-w", "tags": ["screenshot", "ocr", "redaction", "privacy", "local-first"]}
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

Optional integration for an already-installed RAPP Shot app or legacy shot CLI.
Native capture/edit/OCR requests are staged for user review, never silently
captured or copied. Legacy CLI actions remain allowlisted subcommands; no shell
is used. Installing this Python file does not install the native application.

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
      "description": "Request clipboard output. Native mode requires final preview approval; the legacy CLI retains its copy behavior.",
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
      "description": "Native app: all modes require user confirmation. Legacy CLI: only screen works headlessly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_shot_agent.py` and embedded as the fenced Python below (sha256 7ea3d9383ed9cd99…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_shot_agent.py` first:

```bash
python3 rapp_shot_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_shot_agent.py   # or on stdin
python3 rapp_shot_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""RAPP Shot — Capture, annotate and redact screenshots on-device. Finds credentials with OCR and paints them out opaquely.

Optional integration for an already-installed RAPP Shot app or legacy shot CLI.
Native capture/edit/OCR requests are staged for user review, never silently
captured or copied. Legacy CLI actions remain allowlisted subcommands; no shell
is used. Installing this Python file does not install the native application.

Stdlib only.
"""

import os
import plistlib
import shutil
import subprocess
from urllib.parse import quote, urlencode

from agents.basic_agent import BasicAgent

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "rapp_shot",
    "version": "1.3.0",
    "description": "Capture and edit screenshots locally, with opaque credential redaction and preview review. Native requests require user confirmation; detection is not an all-clear.",
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


def _native_app():
    if os.environ.get("SHOT_CLI"):
        return None
    candidates = [
        os.environ.get("RAPP_SHOT_APP"),
        "/Applications/RAPPShot.app",
        "/Applications/RAPP Shot.app",
        os.path.join(HOME, "Applications", "RAPPShot.app"),
        os.path.join(HOME, "Applications", "RAPP Shot.app"),
    ]
    for app in candidates:
        if not app:
            continue
        executable = os.path.join(app, "Contents", "MacOS", "RAPPShot")
        if not os.access(executable, os.X_OK):
            continue
        try:
            with open(os.path.join(app, "Contents", "Info.plist"), "rb") as stream:
                info = plistlib.load(stream)
                if isinstance(info, dict) and info.get("CFBundleIdentifier") == "io.rapp.shot":
                    return app
        except (OSError, ValueError, plistlib.InvalidFileException):
            continue
    return None


def _native_command(app, args):
    action = args[0]
    executable = os.path.join(app, "Contents", "MacOS", "RAPPShot")
    if action == "doctor":
        return [executable, "--diagnose"], None
    if action == "list":
        limit = int(args[2]) if len(args) == 3 and args[1] == "--limit" else 20
        if not 1 <= limit <= 100:
            raise ValueError("native list limit must be 1 through 100")
        return [executable, "--agent-list", "--limit", str(limit)], None
    if action not in ("capture", "ocr", "redact", "annotate"):
        raise ValueError("unsupported native action")
    values = {"auto": "false"}
    value_flags = {"--mode": "mode", "--name": "name", "--box": "box",
                   "--arrow": "arrow", "--crop": "crop", "--text": "text"}
    flags = {"--auto": "auto", "--auto-redact": "auto",
             "--copy": "copy", "--dry-run": "dry_run"}
    index = 1
    while index < len(args):
        argument = args[index]
        if argument in flags:
            values[flags[argument]] = "true"
        elif argument in value_flags:
            index += 1
            if index >= len(args):
                raise ValueError("missing value for " + argument)
            values[value_flags[argument]] = args[index]
        elif not argument.startswith("-") and "image" not in values:
            path = os.path.expanduser(argument)
            if not os.path.isabs(path) and not os.path.exists(path):
                root = os.path.expanduser(os.environ.get("SHOT_HOME") or "~/.rappshot")
                path = os.path.join(root, "shots", path if path.endswith(".png") else path + ".png")
            values["image"] = os.path.abspath(path)
        else:
            raise ValueError("unsupported native argument: " + argument)
        index += 1
    url = "rappshot://action/" + action + "?" + urlencode(values, quote_via=quote)
    if len(url.encode("utf-8")) > 16384:
        raise ValueError("native action exceeds the 16 KB limit")
    return ["/usr/bin/open", "-a", app, url], (
        "Opened RAPP Shot with a staged " + action + " request. "
        "Review & Apply in the app; capture requires clicking Capture, and "
        "copy/export requires reviewing the final preview. "
        "No capture, clipboard write, or export was performed by this request.")


def _run(args, timeout=900):
    app = _native_app()
    notice = None
    if app:
        command, notice = _native_command(app, args)
        exe = command[0]
    else:
        exe = _cli()
        command = [exe] + args if exe else []
    if not exe:
        return None, ("RAPP Shot not found. Install RAPPShot.app in /Applications "
                      "(or set RAPP_SHOT_APP), or install the legacy shot CLI / set SHOT_CLI.")
    try:
        p = subprocess.run(command, capture_output=True, text=True,
                           timeout=min(timeout, 30) if app else timeout)
    except FileNotFoundError as exc:
        # A traceback is not an answer. Say what is missing and how to fix it.
        return None, (f"{exe} could not be executed ({exc.strerror}). The tool is "
                      f"installed but a component it shells out to is missing — run "
                      f"./install.sh in that repo to build the shims.")
    out = (p.stdout or "").strip()
    err = (p.stderr or "").strip()
    if p.returncode != 0:
        return None, f"{os.path.basename(exe)} exited {p.returncode}: " + (err or out or "no output")
    if notice:
        return notice, None
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
            "description": "Screenshots for review before sharing. Native capture/edit/OCR requests are staged in an installed RAPP Shot app; a user starts capture and approves the final preview before copy/export. Local OCR and opaque redaction can miss credentials. Explicit SHOT_CLI keeps the legacy backend. Actions: doctor, capture, ocr, redact, annotate, list.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["doctor", "capture", "ocr", "redact",
                                        "annotate", "list"],
                               "description": "What to do. Default doctor."},
                    "image": {"type": "string", "description": "Shot name or path; defaults to the most recent."},
                    "mode": {"type": "string", "enum": ["region", "window", "screen"],
                             "description": "Native app: all modes require user confirmation. Legacy CLI: only screen works headlessly."},
                    "name": {"type": "string", "description": "Label for the capture."},
                    "auto": {"type": "boolean", "description": "Redaction: find secrets by OCR."},
                    "dry_run": {"type": "boolean", "description": "Redaction: report without painting."},
                    "copy": {"type": "boolean", "description": "Request clipboard output. Native mode requires final preview approval; the legacy CLI retains its copy behavior."},
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
                if mode in ("region", "window") and not _native_app():
                    return ("region and window capture open an interactive picker, so they cannot "
                            "run headlessly with the CLI. Install the native RAPP Shot app, "
                            "use mode='screen', or use the legacy Hammerspoon hotkeys.")
                args = ["capture", "--mode", mode]
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

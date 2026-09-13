---
name: "rappstore-kody-w-rapp-shot-singleton"
description: "Screenshots for review before sharing. Native capture/edit/OCR requests are staged in an installed RAPP Shot app; a user starts capture and approves the final preview before copy/export. Local OCR and opaque redaction can miss credentials. Explicit SHOT_CLI keeps the legacy backend. Actions: doctor, capture, ocr, redact, annotate, list."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp-shot-singleton", "rar_sha256": "bc817f0fdf172cb4e16bbba507e8381838f444033cc0b277d0f55c679d72f61d", "source_kind": "federated-rapplication", "source_commit": null, "version": "1.3.1", "author": "@kody-w", "tags": ["screenshot", "ocr", "redaction", "privacy", "local-first"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_shot_agent.py` and embedded as the fenced Python below (sha256 bc817f0fdf172cb4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_shot_agent.py` first:

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
    "version": "1.3.1",
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

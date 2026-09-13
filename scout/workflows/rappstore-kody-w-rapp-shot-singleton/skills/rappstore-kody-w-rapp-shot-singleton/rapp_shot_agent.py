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

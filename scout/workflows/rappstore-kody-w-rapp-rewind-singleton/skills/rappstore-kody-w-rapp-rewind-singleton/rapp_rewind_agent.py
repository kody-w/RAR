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

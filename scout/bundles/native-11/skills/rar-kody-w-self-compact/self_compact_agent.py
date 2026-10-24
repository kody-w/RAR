"""self_compact_agent.py — the brainstem compacts its own context. One agent file; the grail is untouched.

Drop into a brainstem's ``agents/`` folder. It works on a stock (grail) brainstem with no restart:
agents are discovered on every request.

Ported from the Pi "self-compact" extension. A chat client resends the conversation on every
turn, and the web UI silently drops the oldest turns past its budget (40 messages / 60k
characters). This agent lets the model see that coming and write its own handoff first:

  gauge     Every /chat request is measured: the conversation added since the last saved note,
            against a budget. Phases: ok, notice, warning, cutoff.
  hints     Past the notice and warning lines, a short hint joins the system prompt for that
            request only (never the history).
  cutoff    Past the cutoff, every tool except SelfCompact is withheld from the model until it
            writes its note. Tools come back the moment the note is saved.
  handoff   SelfCompact(note_to_self) saves the note per session; it returns in the system prompt
            on every later turn, so it survives when the client drops the old turns.
  view      SelfCompact(action="view") reports how full the conversation is.

The cutoff works because an agent runs inside the kernel process: on load, this file wraps the
running kernel's ``call_copilot`` and ``call_copilot_stream`` in memory (once per process), the
same way agents already extend the running brainstem. No file is changed; delete this file and
restart to remove it completely.

Settings (environment, optional):
  SELF_COMPACT_BUDGET_TOKENS  default 15000 (the web UI's 60k-char budget / 4)
  SELF_COMPACT_NOTICE_PCT     default 50
  SELF_COMPACT_WARN_PCT       default 70
  SELF_COMPACT_FORCE_PCT      default 85 (capped at 90)
  SELF_COMPACT_DIR            default <brainstem>/.brainstem_data/self_compact
                              (inside the data folder, so notes travel with snapshots)
"""

import hashlib
import json
import os
import re
import sys
import threading
import types
from datetime import datetime, timezone

try:
    from agents.basic_agent import BasicAgent
except ImportError:  # pragma: no cover — standalone / other hosts
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:  # minimal stand-in so the file runs on its own
            def __init__(self, name=None, metadata=None):
                self.name, self.metadata = name, metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/self_compact_agent",
    "display_name": "SelfCompact",
    "version": "1.0.0",
    "description": (
        "The brainstem compacts its own context: a gauge on every chat, hints as it fills, and at the "
        "cutoff every other tool waits until the model writes a note to itself that survives when old "
        "turns drop out."
    ),
    "author": "@kody-w",
    "tags": ["context", "memory", "compaction", "handoff", "long-conversations", "pi"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "based_on": "disler/self-compact-pi-agent",
    "example_call": {"args": {"action": "view"}},
}

TOOL_NAME = "SelfCompact"
NOTE_MAX_CHARS = 4000
_BRAINSTEM_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The kernel re-imports agent files on every request, so anything that must outlive one
# request (the per-request state the tool filter reads, the "already wrapped" flag) lives in
# one stable module in sys.modules.
_SHARED = sys.modules.setdefault("_rapp_self_compact_shared", types.ModuleType("_rapp_self_compact_shared"))
if not hasattr(_SHARED, "local"):
    _SHARED.local = threading.local()
    _SHARED.hooks = []
    _SHARED.reason = "not attached yet"


def _env_int(key, default):
    try:
        return int((os.getenv(key) or str(default)).strip().rstrip("%"))
    except ValueError:
        return default


def _settings():
    return {
        "budget_tokens": max(_env_int("SELF_COMPACT_BUDGET_TOKENS", 15000), 1),
        "notice_pct": _env_int("SELF_COMPACT_NOTICE_PCT", 50),
        "warn_pct": _env_int("SELF_COMPACT_WARN_PCT", 70),
        "force_pct": min(_env_int("SELF_COMPACT_FORCE_PCT", 85), 90),
        "note_max_chars": NOTE_MAX_CHARS,
    }


def _dir():
    d = os.getenv("SELF_COMPACT_DIR") or os.path.join(_BRAINSTEM_DIR, ".brainstem_data", "self_compact")
    os.makedirs(d, exist_ok=True)
    return d


def _path(session_id):
    return os.path.join(_dir(), re.sub(r"[^A-Za-z0-9_.-]", "_", session_id or "default")[:120] + ".json")


def _load_note(session_id):
    try:
        with open(_path(session_id), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def _fingerprint(text):
    return hashlib.sha256((text or "").strip().encode("utf-8")).hexdigest()[:16]


def _gauge(history, user_input, saved=None):
    """Measure the conversation added since the turn that wrote the saved note."""
    msgs = [m for m in (history or []) if isinstance(m, dict)]
    if saved and saved.get("checkpoint"):
        for i in range(len(msgs) - 1, -1, -1):
            if msgs[i].get("role") == "user" and _fingerprint(msgs[i].get("content")) == saved["checkpoint"]:
                msgs = msgs[i + 1:]
                break
    used = (sum(len(m.get("content") or "") for m in msgs) + len(user_input or "")) // 4
    s = _settings()
    pct = round(100 * used / s["budget_tokens"])
    phase = ("cutoff" if pct >= s["force_pct"] else "warning" if pct >= s["warn_pct"]
             else "notice" if pct >= s["notice_pct"] else "ok")
    return {"used_tokens": used, "pct": pct, "phase": phase, **s, "cycle": (saved or {}).get("cycle", 0)}


def _guidance(g):
    numbers = (f"{g['used_tokens']} tokens of new conversation since your last note ({g['pct']}% of a "
               f"{g['budget_tokens']}-token budget; warning at {g['warn_pct']}%, cutoff at {g['force_pct']}%)")
    if g["phase"] == "notice":
        return (f"[self-compact · notice] {numbers}. Heads-up only; nothing is required. When the moment is "
                f"right you can call {TOOL_NAME} with a note_to_self.")
    if g["phase"] == "warning":
        return (f"[self-compact · WARNING] {numbers}. Older messages will soon drop out of this conversation. "
                f"Finish the current step, then call {TOOL_NAME} with your note_to_self (goal, done, in "
                "progress, decisions, exact next step last), then answer the user.")
    if g["phase"] == "cutoff":
        return (f"[self-compact · CUTOFF] {numbers}. Every other tool is withheld until you call {TOOL_NAME} "
                "with your note_to_self. Call it first, then answer the user.")
    return None


def _filter_tools(tools):
    """At the cutoff, before the note is written, the model may only call SelfCompact."""
    req = getattr(_SHARED.local, "req", None)
    if not tools or not req or req["gauge"]["phase"] != "cutoff" or req["compacted"]:
        return tools
    only = [t for t in tools if (t.get("function") or {}).get("name") == TOOL_NAME]
    return only or tools


def _find_kernel():
    for mod in list(sys.modules.values()):
        d = getattr(mod, "__dict__", None)
        if d and all(k in d for k in ("app", "load_agents", "call_copilot")):
            return mod
    return None


def _attach():
    """Wrap the kernel's model calls in memory, once per process."""
    kernel = _find_kernel()
    if kernel is None:
        _SHARED.reason = "kernel module not found"
        return
    if getattr(kernel, "_self_compact_agent_attached", False):
        return
    orig_call = kernel.call_copilot

    def call_copilot(messages, tools=None, *a, **k):
        return orig_call(messages, _SHARED.filter(tools), *a, **k)
    kernel.call_copilot = call_copilot
    hooks = ["call_copilot"]
    if hasattr(kernel, "call_copilot_stream"):
        orig_stream = kernel.call_copilot_stream

        def call_copilot_stream(messages, tools=None, *a, **k):
            return orig_stream(messages, _SHARED.filter(tools), *a, **k)
        kernel.call_copilot_stream = call_copilot_stream
        hooks.append("call_copilot_stream")
    kernel._self_compact_agent_attached = True
    _SHARED.hooks, _SHARED.reason = hooks, ""


_SHARED.filter = _filter_tools        # the wrappers call whatever the newest import provides
try:
    _attach()
except Exception as _e:               # never break agent loading
    _SHARED.reason = f"attach failed: {_e}"


class SelfCompactAgent(BasicAgent):
    def __init__(self):
        self.name = "SelfCompact"
        self.metadata = {
            "name": "SelfCompact",
            "description": (
                "Your context gauge and handoff note. action='save' (default) saves a note_to_self so "
                "nothing is lost when older messages drop out of this conversation; call it when the "
                "[self-compact] guidance in your instructions asks you to, or when the user asks you to "
                "checkpoint. The note is shown back to you, word for word, on every later turn. "
                "action='view' returns how full the conversation is (use it when the user asks)."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string", "enum": ["save", "view"], "description": "save (default) or view"},
                    "note_to_self": {"type": "string", "description": (
                        f"For save: up to {NOTE_MAX_CHARS} characters. Merge your previous note (if any) and "
                        "cover: the user's goal, what is DONE (exact names, values, results), what is IN "
                        "PROGRESS, key decisions and preferences, and the exact NEXT step last.")},
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def system_context(self):
        """Runs inside every /chat request: measure, remember for this request, return the hint."""
        try:
            from flask import request
            data = request.get_json(force=True, silent=True)
        except Exception:
            return None
        if not isinstance(data, dict):
            return None
        session_id = data.get("session_id") or "default"
        user_input = data.get("user_input") if isinstance(data.get("user_input"), str) else ""
        history = data.get("conversation_history")
        saved = _load_note(session_id)
        g = _gauge(history if isinstance(history, list) else [], user_input, saved)
        _SHARED.local.req = {"session_id": session_id, "checkpoint": _fingerprint(user_input), "gauge": g,
                             "compacted": False}
        parts = []
        if saved and saved.get("note"):
            parts.append(
                f'<self_compact_note cycle="{saved.get("cycle", 1)}" saved="{saved.get("saved_at", "")}">\n'
                f'{saved["note"]}\n</self_compact_note>\n'
                "This is the note you wrote to yourself at your last checkpoint. Older messages may no "
                "longer be in this conversation; trust this note for what came before.")
        hint = _guidance(g)
        if hint:
            parts.append(hint)
        return "\n\n".join(parts) or None

    def perform(self, action="save", note_to_self="", **kwargs):
        req = getattr(_SHARED.local, "req", None)
        if action == "view":
            saved = _load_note(req["session_id"]) if req else None
            return json.dumps({
                "gauge": (req or {}).get("gauge") or _settings(),
                "note": ({"cycle": saved.get("cycle"), "saved_at": saved.get("saved_at"),
                          "chars": len(saved.get("note", ""))} if saved else None),
                "cutoff_enforced": bool(_SHARED.hooks), "reason": _SHARED.reason,
            })
        if action not in ("save", None, ""):
            return f"Error: unknown action {action!r}; use 'save' or 'view'."
        note = (note_to_self or "").strip()
        if not note:
            return f"Error: note_to_self is empty. Write the note, then call {TOOL_NAME} again."
        if len(note) > NOTE_MAX_CHARS:
            return (f"Error: note_to_self is {len(note)} characters; the limit is {NOTE_MAX_CHARS}. "
                    f"Shorten it and call {TOOL_NAME} again.")
        req = req or {"session_id": "default", "checkpoint": None, "gauge": {"cycle": 0}, "compacted": False}
        record = {"note": note, "checkpoint": req.get("checkpoint"), "cycle": req["gauge"].get("cycle", 0) + 1,
                  "saved_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        path = _path(req["session_id"])
        with open(path + ".tmp", "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2)
        os.replace(path + ".tmp", path)
        req["compacted"] = True       # tools come back for the rest of this request
        return (f"Note saved (cycle {record['cycle']}). It will be shown to you on every later turn of this "
                "session, even after older messages drop out. Now continue with the user's request.")


if __name__ == "__main__":
    # Standalone: show the gauge for an empty conversation (no brainstem needed).
    print(SelfCompactAgent().perform(action="view"))

---
name: "rar-kody-w-self-compact"
description: "The brainstem compacts its own context: a gauge on every chat, hints as it fills, and at the cutoff every other tool waits until the model writes a note to itself that survives when old turns drop out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/self_compact_agent", "rar_sha256": "ad47db5e49459bdc85e90cf7a6a1fa7201061b358925ae5d7290b8c32a790c9e", "source_kind": "rar-agent", "source_commit": "acb65718b1e8ae07ce85ae5b6ea25cfc874f1bcf", "author": "@kody-w", "tags": ["context", "memory", "compaction", "handoff", "long-conversations", "pi"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/self_compact_agent`. The original RAPP
agent is preserved byte-for-byte in `self_compact_agent.py` and in the RCI capsule.

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

self_compact_agent.py — the brainstem compacts its own context. One agent file; the grail is untouched.

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

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `self_compact_agent.py` and embedded as the fenced Python below (sha256 ad47db5e49459bdc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `self_compact_agent.py` first:

```bash
python3 self_compact_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 self_compact_agent.py   # or on stdin
python3 self_compact_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

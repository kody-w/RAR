---
name: "rar-kody-w-self-compact"
description: "The brainstem compacts its own context: a gauge on every chat, hints as it fills, and at the cutoff every other tool waits until the model writes a note to itself that survives when old turns drop out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/self_compact_agent", "rar_sha256": "4e3d29f41ac869e4eaf99a8c499d27f37a811bd019d61c1551d8c5adb98585a8", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "@kody-w", "tags": ["context", "memory", "compaction", "handoff", "long-conversations", "pi"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `self_compact_agent.py` and embedded as the fenced Python below (sha256 4e3d29f41ac869e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `self_compact_agent.py` first:

```bash
python3 self_compact_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 self_compact_agent.py   # or on stdin
python3 self_compact_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/self_compact_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/self_compact_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/self_compact_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

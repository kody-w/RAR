---
name: "rar-kody-w-self-compact"
description: "The brainstem compacts its own context: a gauge on every chat, hints as it fills, and at the cutoff every other tool waits until the model writes a note to itself that survives when old turns drop out."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/self_compact_agent", "rar_sha256": "4e3d29f41ac869e4eaf99a8c499d27f37a811bd019d61c1551d8c5adb98585a8", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "@kody-w", "tags": ["context", "memory", "compaction", "handoff", "long-conversations", "pi"]}
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

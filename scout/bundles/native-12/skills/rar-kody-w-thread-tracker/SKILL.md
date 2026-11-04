---
name: "rar-kody-w-thread-tracker"
description: "Routes remarks into durable local topic threads, lists open work, and parks or closes threads without deleting their history."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/thread_tracker_agent", "rar_sha256": "c6768a7a25c21f3047e8cb47a96528f83f126742bdbafb9f13e4df4ebb30aad5", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "kody-w", "tags": ["threads", "notes", "routing", "append-only", "offline"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/thread_tracker_agent`. The original RAPP
agent is preserved byte-for-byte in `thread_tracker_agent.py` and in the RCI capsule.

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

Thread Tracker — local append-only topic routing that keeps work from getting lost.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "place",
        "open",
        "list",
        "topics",
        "close",
        "park",
        "show"
      ],
      "type": "string"
    },
    "reason": {
      "type": "string"
    },
    "text": {
      "type": "string"
    },
    "thread": {
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `thread_tracker_agent.py` and embedded as the fenced Python below (sha256 c6768a7a25c21f30…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `thread_tracker_agent.py` first:

```bash
python3 thread_tracker_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 thread_tracker_agent.py   # or on stdin
python3 thread_tracker_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/thread_tracker_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/thread_tracker_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/thread_tracker_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Thread Tracker — local append-only topic routing that keeps work from getting lost."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/thread_tracker_agent",
    "version": "1.0.0",
    "display_name": "Thread Tracker",
    "description": "Routes remarks into durable local topic threads, lists open work, and parks or closes threads without deleting their history.",
    "author": "kody-w",
    "tags": ["threads", "notes", "routing", "append-only", "offline"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import threading
import uuid

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:
        class BasicAgent:
            def __init__(self, name=None, metadata=None):
                if name is not None:
                    self.name = name
                if metadata is not None:
                    self.metadata = metadata

            def perform(self, **kwargs):
                return "Not implemented."


_LOCK = threading.RLock()
_WORDS = re.compile(r"[a-z0-9][a-z0-9_-]{1,}")
_STOP = {
    "about", "after", "again", "also", "been", "being", "from", "have",
    "into", "just", "more", "that", "their", "then", "this", "what", "when",
    "where", "which", "with", "would", "your",
}


def _store():
    configured = os.environ.get("RAPP_THREAD_STORE")
    if configured:
        return Path(configured).expanduser()
    return Path.home() / ".rapp" / "agent_data" / "thread_tracker.jsonl"


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _terms(text):
    return {
        word for word in _WORDS.findall(text.casefold())
        if word not in _STOP
    }


def _load():
    path = _store()
    if not path.exists():
        return []
    events = []
    previous = ""
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            event = json.loads(line)
            payload = {key: value for key, value in event.items() if key != "hash"}
            expected = hashlib.sha256(
                json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest()
            if event.get("previous") != previous or event.get("hash") != expected:
                raise ValueError(f"thread record is corrupt at line {number}")
            events.append(event)
            previous = event["hash"]
    return events


def _append(kind, payload):
    with _LOCK:
        events = _load()
        path = _store()
        path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        if os.name != "nt":
            path.parent.chmod(0o700)
        event = {
            "utc": _now(),
            "kind": kind,
            "payload": payload,
            "previous": events[-1]["hash"] if events else "",
        }
        event["hash"] = hashlib.sha256(
            json.dumps(event, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, sort_keys=True) + "\n")
        if os.name != "nt":
            path.chmod(0o600)
        return event


def _threads():
    threads = {}
    for event in _load():
        payload = event["payload"]
        identifier = payload.get("thread")
        if not identifier:
            continue
        item = threads.setdefault(identifier, {
            "thread": identifier,
            "topic": "",
            "notes": [],
            "state": "open",
            "opened": event["utc"],
            "touched": event["utc"],
            "terms": set(),
        })
        item["touched"] = event["utc"]
        if event["kind"] == "thread.opened":
            item["topic"] = payload["topic"]
            item["terms"].update(payload.get("terms", []))
        elif event["kind"] == "thread.note":
            item["notes"].append(payload["note"])
            item["terms"].update(payload.get("terms", []))
        elif event["kind"] == "thread.closed":
            item["state"] = "closed"
            item["reason"] = payload.get("reason", "")
        elif event["kind"] == "thread.parked":
            item["state"] = "parked"
    return threads


def _best_match(terms, threads, floor=2):
    candidates = []
    for item in threads.values():
        if item["state"] == "closed":
            continue
        score = len(terms & item["terms"])
        candidates.append((score, item["touched"], item["thread"], item))
    if not candidates:
        return None, 0
    score, _, _, item = max(candidates)
    return (item, score) if score >= floor else (None, score)


class ThreadTrackerAgent(BasicAgent):
    def __init__(self):
        self.name = "ThreadTracker"
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": [
                            "place", "open", "list", "topics",
                            "close", "park", "show",
                        ],
                    },
                    "text": {"type": "string"},
                    "thread": {"type": "string"},
                    "reason": {"type": "string"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        action = str(kwargs.get("action") or "list").strip().lower()
        threads = _threads()
        text = str(kwargs.get("text") or "").strip()
        if action in ("place", "open"):
            if not text:
                return "Provide a remark or topic."
            terms = _terms(text)
            match, score = (None, 0) if action == "open" else _best_match(
                terms, threads
            )
            if match:
                _append("thread.note", {
                    "thread": match["thread"],
                    "note": text[:1000],
                    "terms": sorted(terms),
                })
                return (
                    f"Placed on thread {match['thread']} "
                    f"({score} shared terms): {match['topic'][:100]}"
                )
            identifier = uuid.uuid4().hex[:10]
            _append("thread.opened", {
                "thread": identifier,
                "topic": text[:500],
                "terms": sorted(terms),
            })
            return f"Opened thread {identifier}: {text[:120]}"
        if action in ("close", "park"):
            identifier = str(kwargs.get("thread") or "").strip()
            if identifier not in threads:
                return f"No thread {identifier}."
            _append(
                "thread.closed" if action == "close" else "thread.parked",
                {
                    "thread": identifier,
                    "reason": str(kwargs.get("reason") or "")[:500],
                },
            )
            return f"Thread {identifier} {action}d. History was preserved."
        if action == "show":
            identifier = str(kwargs.get("thread") or "").strip()
            item = threads.get(identifier)
            if not item:
                return f"No thread {identifier}."
            safe = {**item, "terms": sorted(item["terms"])}
            return json.dumps(safe, indent=2, sort_keys=True)
        if action == "topics":
            if not threads:
                return "Nothing tracked yet."
            latest_day = max(item["touched"][:10] for item in threads.values())
            items = [
                item for item in threads.values()
                if item["touched"][:10] == latest_day
            ]
            counts = Counter()
            for item in items:
                counts.update(item["terms"])
            lines = [f"Covered on {latest_day}:"]
            lines.extend(
                f"[{item['state']}] {item['thread']} {item['topic'][:100]}"
                for item in sorted(items, key=lambda value: value["touched"])
            )
            recurring = [
                term for term, count in counts.most_common(8) if count > 1
            ]
            if recurring:
                lines.append("Recurring terms: " + ", ".join(recurring))
            return "\n".join(lines)
        active = [
            item for item in threads.values() if item["state"] != "closed"
        ]
        if not active:
            return "No open threads."
        return "\n".join(
            f"{item['thread']} [{item['state']}] "
            f"{len(item['notes'])} note(s): {item['topic'][:100]}"
            for item in sorted(active, key=lambda value: value["touched"])
        )


if __name__ == "__main__":
    print(ThreadTrackerAgent().perform(action="list"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

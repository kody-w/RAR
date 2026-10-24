---
name: "rar-kody-w-thread-tracker"
description: "Routes remarks into durable local topic threads, lists open work, and parks or closes threads without deleting their history."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/thread_tracker_agent", "rar_sha256": "dcf4d630cab0eaa9a6919e052cb14429416a1607f4e581a397a58430c7f8ad98", "source_kind": "rar-agent", "source_commit": "82c64ab86138c5d021d69d1a32df1731b399b231", "author": "kody-w", "tags": ["threads", "notes", "routing", "append-only", "offline"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `thread_tracker_agent.py` and embedded as the fenced Python below (sha256 dcf4d630cab0eaa9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `thread_tracker_agent.py` first:

```bash
python3 thread_tracker_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 thread_tracker_agent.py   # or on stdin
python3 thread_tracker_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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

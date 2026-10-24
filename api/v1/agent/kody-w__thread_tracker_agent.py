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

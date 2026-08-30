"""Parallel Dimensions — append-only what-if branches with deterministic merging."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/parallel_dimensions_agent",
    "version": "1.0.0",
    "display_name": "Parallel Dimensions",
    "description": "Tracks independent what-if branches, detects conflicting assertions, and merges only compatible dimensions using an append-only local record.",
    "author": "kody-w",
    "tags": ["planning", "what-if", "branches", "append-only", "offline"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

import hashlib
import json
import os
from pathlib import Path
import threading
from datetime import datetime, timezone
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


def _store():
    configured = os.environ.get("RAPP_DIMENSION_STORE")
    if configured:
        return Path(configured).expanduser()
    return Path.home() / ".rapp" / "agent_data" / "parallel_dimensions.jsonl"


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _load():
    path = _store()
    if not path.exists():
        return []
    events = []
    previous = ""
    with path.open(encoding="utf-8", errors="strict") as handle:
        for number, line in enumerate(handle, 1):
            event = json.loads(line)
            payload = {key: value for key, value in event.items() if key != "hash"}
            expected = hashlib.sha256(
                json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest()
            if event.get("previous") != previous or event.get("hash") != expected:
                raise ValueError(f"dimension record is corrupt at line {number}")
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


def _dimensions():
    dimensions = {}
    for event in _load():
        payload = event["payload"]
        identifier = payload.get("dimension")
        if not identifier:
            continue
        state = dimensions.setdefault(identifier, {
            "dimension": identifier,
            "about": "",
            "steps": [],
            "assertions": {},
            "state": "open",
            "opened": event["utc"],
            "merged_into": None,
        })
        if event["kind"] == "dimension.branched":
            state["about"] = payload["about"]
        elif event["kind"] == "dimension.step":
            state["steps"].append(payload.get("step", ""))
            state["assertions"].update(payload.get("assertions", {}))
        elif event["kind"] == "dimension.amended":
            state["steps"].append(f"AMENDED: {payload.get('reason', '')}")
            state["assertions"].update(payload.get("assertions", {}))
        elif event["kind"] == "dimension.merged":
            state["state"] = "merged"
            state["merged_into"] = payload["into"]
        elif event["kind"] == "dimension.parked":
            state["state"] = "parked"
    return dimensions


def _conflicts(left, right):
    shared = set(left["assertions"]) & set(right["assertions"])
    return {
        key: (left["assertions"][key], right["assertions"][key])
        for key in shared
        if left["assertions"][key] != right["assertions"][key]
    }


class ParallelDimensionsAgent(BasicAgent):
    def __init__(self):
        self.name = "ParallelDimensions"
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
                            "branch", "explore", "compatible", "merge",
                            "amend", "show", "list",
                        ],
                    },
                    "about": {"type": "string"},
                    "dimension": {"type": "string"},
                    "other": {"type": "string"},
                    "step": {"type": "string"},
                    "assertions": {"type": "object"},
                    "reason": {"type": "string"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        action = str(kwargs.get("action") or "list").strip().lower()
        dimensions = _dimensions()
        if action == "branch":
            about = str(kwargs.get("about") or "").strip()
            if not about:
                return "Provide the possibility this dimension should explore."
            identifier = uuid.uuid4().hex[:10]
            _append("dimension.branched", {
                "dimension": identifier,
                "about": about[:500],
            })
            return f"Opened dimension {identifier}: {about[:120]}"
        if action == "explore":
            identifier = str(kwargs.get("dimension") or "").strip()
            if identifier not in dimensions:
                return f"No dimension {identifier}."
            assertions = kwargs.get("assertions") or {}
            if not isinstance(assertions, dict):
                return "assertions must be an object."
            clean = {
                str(key)[:80]: str(value)[:300]
                for key, value in assertions.items()
            }
            _append("dimension.step", {
                "dimension": identifier,
                "step": str(kwargs.get("step") or "")[:500],
                "assertions": clean,
            })
            return f"Recorded a step in dimension {identifier}."
        if action in ("compatible", "merge"):
            left_id = str(kwargs.get("dimension") or "").strip()
            right_id = str(kwargs.get("other") or "").strip()
            if left_id not in dimensions or right_id not in dimensions:
                return "Provide two existing dimension identifiers."
            conflicts = _conflicts(dimensions[left_id], dimensions[right_id])
            if conflicts:
                details = "; ".join(
                    f"{key}: {values[0]!r} vs {values[1]!r}"
                    for key, values in sorted(conflicts.items())
                )
                if action == "merge":
                    _append("dimension.parked", {
                        "dimension": right_id,
                        "reason": f"conflicts with {left_id}",
                    })
                    return f"Not merged. Conflicts: {details}"
                return f"Incompatible. Conflicts: {details}"
            if action == "compatible":
                return "Compatible. No conflicting assertions."
            _append("dimension.merged", {
                "dimension": right_id,
                "into": left_id,
            })
            return f"Merged {right_id} into {left_id}."
        if action == "amend":
            identifier = str(kwargs.get("dimension") or "").strip()
            if identifier not in dimensions:
                return f"No dimension {identifier}."
            assertions = kwargs.get("assertions") or {}
            if not isinstance(assertions, dict):
                return "assertions must be an object."
            _append("dimension.amended", {
                "dimension": identifier,
                "reason": str(kwargs.get("reason") or "")[:500],
                "assertions": {
                    str(key)[:80]: str(value)[:300]
                    for key, value in assertions.items()
                },
            })
            return f"Appended an amendment to dimension {identifier}."
        if action == "show":
            identifier = str(kwargs.get("dimension") or "").strip()
            state = dimensions.get(identifier)
            return (
                json.dumps(state, indent=2, sort_keys=True)
                if state else f"No dimension {identifier}."
            )
        if not dimensions:
            return "No dimensions yet."
        return "\n".join(
            f"{item['dimension']} [{item['state']}] "
            f"{len(item['steps'])} step(s): {item['about'][:80]}"
            for item in sorted(dimensions.values(), key=lambda value: value["opened"])
        )


if __name__ == "__main__":
    print(ParallelDimensionsAgent().perform(action="list"))

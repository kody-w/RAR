---
name: "rar-kody-w-parallel-dimensions"
description: "Tracks independent what-if branches, detects conflicting assertions, and merges only compatible dimensions using an append-only local record."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/parallel_dimensions_agent", "rar_sha256": "ad3d5af03678ded14558a1f449a5ba4002e15dbb1ee101c37349da16ba7b2c2b", "source_kind": "rar-agent", "source_commit": "50a570ba43b2a106e3f146533693846fa657df36", "author": "kody-w", "tags": ["planning", "what-if", "branches", "append-only", "offline"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/parallel_dimensions_agent`. The original RAPP
agent is preserved byte-for-byte in `parallel_dimensions_agent.py` and in the RCI capsule.

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

Parallel Dimensions — append-only what-if branches with deterministic merging.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "about": {
      "type": "string"
    },
    "action": {
      "enum": [
        "branch",
        "explore",
        "compatible",
        "merge",
        "amend",
        "show",
        "list"
      ],
      "type": "string"
    },
    "assertions": {
      "type": "object"
    },
    "dimension": {
      "type": "string"
    },
    "other": {
      "type": "string"
    },
    "reason": {
      "type": "string"
    },
    "step": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `parallel_dimensions_agent.py` and embedded as the fenced Python below (sha256 ad3d5af03678ded1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `parallel_dimensions_agent.py` first:

```bash
python3 parallel_dimensions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 parallel_dimensions_agent.py   # or on stdin
python3 parallel_dimensions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

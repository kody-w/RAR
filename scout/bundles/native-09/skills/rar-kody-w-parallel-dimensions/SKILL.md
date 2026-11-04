---
name: "rar-kody-w-parallel-dimensions"
description: "Tracks independent what-if branches, detects conflicting assertions, and merges only compatible dimensions using an append-only local record."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/parallel_dimensions_agent", "rar_sha256": "d1e6ed9c0a69f581b705a4e8ee01440d5a0e3b5ad9efa9a78fcd156eb4ac1aad", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "kody-w", "tags": ["planning", "what-if", "branches", "append-only", "offline"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `parallel_dimensions_agent.py` and embedded as the fenced Python below (sha256 d1e6ed9c0a69f581…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `parallel_dimensions_agent.py` first:

```bash
python3 parallel_dimensions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 parallel_dimensions_agent.py   # or on stdin
python3 parallel_dimensions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/parallel_dimensions_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/parallel_dimensions_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/parallel_dimensions_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

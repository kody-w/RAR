---
name: "rar-kody-w-parallel-dimensions"
description: "Tracks independent what-if branches, detects conflicting assertions, and merges only compatible dimensions using an append-only local record."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/parallel_dimensions_agent", "rar_sha256": "d1e6ed9c0a69f581b705a4e8ee01440d5a0e3b5ad9efa9a78fcd156eb4ac1aad", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "kody-w", "tags": ["planning", "what-if", "branches", "append-only", "offline"]}
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

---
name: "rar-kody-w-hologram-dogg"
description: "Lists the public RAR hologram DOGG channel and asks a local RAPP Zoo to summon a named, hash-verified character or data projection. Downloads data only; the zoo owns the sandboxed renderer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/hologram_dogg", "rar_sha256": "d775ce5751134da02ee2d825ef0a74d79192691d3f5f8a3621c13c8bddfd8bf2", "source_kind": "rar-agent", "source_commit": "0313216c95b75e5aa168f655108622ba549a6481", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "hologram_dogg_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/hologram-dogg:443d153d5b820f0fe56ea4666ec44234b0d4cf9f3ef6e69f39a5a291b5fe60a0", "kind": "skill"}, "version": "1.1.0", "author": "Kody Wildfeuer", "tags": ["hologram", "dogg", "rar", "rapp-zoo", "three-js", "summon"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/hologram_dogg`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `hologram_dogg_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

List and summon data-only hologram DOGGs through a local RAPP Zoo.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "List, dimension-match, catch one DOGG, or inspect local bottles.",
      "enum": [
        "list",
        "match",
        "summon",
        "status"
      ],
      "type": "string"
    },
    "frame_json": {
      "description": "Optional RAPP frame whose payload supplies match dimensions.",
      "type": "string"
    },
    "hologram_id": {
      "description": "RAR DOGG id, for example holo-avatar.",
      "type": "string"
    },
    "query": {
      "description": "Natural-language dimensions to match against cached bottles.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hologram_dogg_agent.py` and embedded as the fenced Python below (sha256 d775ce5751134da0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hologram_dogg_agent.py` first:

```bash
python3 hologram_dogg_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hologram_dogg_agent.py   # or on stdin
python3 hologram_dogg_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""List and summon data-only hologram DOGGs through a local RAPP Zoo."""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request

try:
    from agents.basic_agent import BasicAgent
except Exception:
    try:
        from basic_agent import BasicAgent
    except Exception:
        try:
            from openrappter.agents.basic_agent import BasicAgent
        except Exception:
            class BasicAgent:
                def __init__(self, name=None, metadata=None):
                    if name is not None:
                        self.name = name
                    if metadata is not None:
                        self.metadata = metadata

                def perform(self, **kwargs):
                    del kwargs
                    return "Not implemented."

                def to_tool(self):
                    return {
                        "type": "function",
                        "function": {
                            "name": self.name,
                            "description": self.metadata.get("description", ""),
                            "parameters": self.metadata.get("parameters", {}),
                        },
                    }


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/hologram_dogg",
    "version": "1.1.0",
    "display_name": "HologramDOGG",
    "description": (
        "Lists the public RAR hologram DOGG channel and asks a local RAPP Zoo "
        "to summon a named, hash-verified character or data projection. "
        "Downloads data only; the zoo owns the sandboxed renderer."
    ),
    "author": "Kody Wildfeuer",
    "tags": ["hologram", "dogg", "rar", "rapp-zoo", "three-js", "summon"],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


RAR_CATALOG = os.environ.get(
    "RAR_HOLOGRAM_INDEX_URL",
    "https://raw.githubusercontent.com/kody-w/RAR/main/doggs/holograms/index.json",
)
ZOO_BASE = os.environ.get("RAPP_ZOO_URL", "http://127.0.0.1:7070")
MAX_BYTES = 256 * 1024


def _json_request(url: str, *, payload: dict | None = None) -> dict:
    body = None
    headers = {
        "Accept": "application/json",
        "User-Agent": "hologram-dogg-agent/1.0",
    }
    method = "GET"
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
        method = "POST"
    request = urllib.request.Request(
        url,
        data=body,
        headers=headers,
        method=method,
    )
    with urllib.request.urlopen(request, timeout=12) as response:
        raw = response.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError("response exceeds the hologram DOGG byte limit")
    parsed = json.loads(raw.decode("utf-8"))
    if not isinstance(parsed, dict):
        raise ValueError("response is not a JSON object")
    return parsed


class HologramDOGGAgent(BasicAgent):
    def __init__(self):
        self.name = "HologramDOGG"
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["list", "match", "summon", "status"],
                        "description": "List, dimension-match, catch one DOGG, or inspect local bottles.",
                    },
                    "hologram_id": {
                        "type": "string",
                        "description": "RAR DOGG id, for example holo-avatar.",
                    },
                    "query": {
                        "type": "string",
                        "description": "Natural-language dimensions to match against cached bottles.",
                    },
                    "frame_json": {
                        "type": "string",
                        "description": "Optional RAPP frame whose payload supplies match dimensions.",
                    },
                },
                "required": [],
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        action = kwargs.get("action") or "list"
        hologram_id = kwargs.get("hologram_id") or ""
        try:
            if action in {"list", "match"}:
                catalog = _json_request(RAR_CATALOG)
                entries = catalog.get("entries") or []
                if action == "match":
                    if not entries:
                        raise ValueError("RAR hologram bottle index is empty")
                    tokens = set(re.findall(
                        r"[a-z0-9]+",
                        (kwargs.get("query") or "").lower(),
                    ))
                    frame_json = kwargs.get("frame_json") or ""
                    if frame_json:
                        frame = json.loads(frame_json)
                        tokens.update(re.findall(
                            r"[a-z0-9]+",
                            json.dumps(frame.get("payload") or {}).lower(),
                        ))
                    ranked = []
                    for entry in entries:
                        dimensions = set(entry.get("dimensions") or [])
                        matches = sorted(dimensions & tokens)
                        ranked.append((
                            len(matches),
                            entry.get("id") or "",
                            matches,
                            entry,
                        ))
                    ranked.sort(key=lambda item: (-item[0], item[1]))
                    score, _, matches, entry = ranked[0]
                    return json.dumps({
                        "status": "ok",
                        "mode": "dimensional" if score else "nearest-static",
                        "score": score,
                        "matched_dimensions": matches,
                        "bottle": entry,
                    })
                return json.dumps({
                    "status": "ok",
                    "source": RAR_CATALOG,
                    "count": len(entries),
                    "holograms": [
                        {
                            "id": entry.get("id"),
                            "name": entry.get("name"),
                            "kind": entry.get("kind"),
                            "rappid": entry.get("rappid"),
                            "bottle": entry.get("bottle"),
                            "dimensions": entry.get("dimensions") or [],
                        }
                        for entry in entries
                    ],
                })
            if action == "status":
                local = _json_request(f"{ZOO_BASE}/api/holograms")
                return json.dumps({
                    "status": "ok",
                    "zoo": ZOO_BASE,
                    "holograms": local.get("holograms") or [],
                })
            if action == "summon":
                if not hologram_id:
                    return json.dumps({
                        "status": "error",
                        "message": "hologram_id is required for summon.",
                    })
                result = _json_request(
                    f"{ZOO_BASE}/api/holograms/summon",
                    payload={"id": hologram_id},
                )
                return json.dumps({
                    "status": "ok",
                    "message": f"Caught hologram DOGG bottle {hologram_id}.",
                    "result": result,
                })
            return json.dumps({
                "status": "error",
                "message": "action must be list, match, summon, or status.",
            })
        except (OSError, ValueError, urllib.error.URLError) as exc:
            return json.dumps({
                "status": "error",
                "action": action,
                "message": str(exc),
                "hint": (
                    "Start RAPP Zoo for local status/summon, or verify that the "
                    "public RAR hologram DOGG catalog is reachable."
                ),
            })


if __name__ == "__main__":
    print(HologramDOGGAgent().perform(action="list"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-kody-w-hologram-dogg"
description: "Lists the public RAR hologram DOGG channel and asks a local RAPP Zoo to summon a named, hash-verified character or data projection. Downloads data only; the zoo owns the sandboxed renderer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/hologram_dogg", "rar_sha256": "d4ad3769e2ef14bdef527072bdda1f2d126905bfbe52f30e74ba72ca953c11ee", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.0", "author": "Kody Wildfeuer", "tags": ["hologram", "dogg", "rar", "rapp-zoo", "three-js", "summon"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/hologram_dogg`. The original RAPP
agent is preserved byte-for-byte in `hologram_dogg_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hologram_dogg_agent.py` and embedded as the fenced Python below (sha256 d4ad3769e2ef14bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hologram_dogg_agent.py` first:

```bash
python3 hologram_dogg_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hologram_dogg_agent.py   # or on stdin
python3 hologram_dogg_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/hologram_dogg_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/hologram_dogg_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/hologram_dogg/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

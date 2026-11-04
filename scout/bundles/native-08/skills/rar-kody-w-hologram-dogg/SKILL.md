---
name: "rar-kody-w-hologram-dogg"
description: "Lists the public RAR hologram DOGG channel and asks a local RAPP Zoo to summon a named, hash-verified character or data projection. Downloads data only; the zoo owns the sandboxed renderer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/hologram_dogg", "rar_sha256": "d4ad3769e2ef14bdef527072bdda1f2d126905bfbe52f30e74ba72ca953c11ee", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.1.0", "author": "Kody Wildfeuer", "tags": ["hologram", "dogg", "rar", "rapp-zoo", "three-js", "summon"]}
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

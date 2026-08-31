"""List and summon data-only hologram DOGGs through a local RAPP Zoo."""

from __future__ import annotations

import json
import os
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
    "version": "1.0.0",
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
                        "enum": ["list", "summon", "status"],
                        "description": "List the RAR channel, summon one DOGG, or inspect local holograms.",
                    },
                    "hologram_id": {
                        "type": "string",
                        "description": "RAR DOGG id, for example holo-avatar.",
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
            if action == "list":
                catalog = _json_request(RAR_CATALOG)
                entries = catalog.get("entries") or []
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
                    "message": f"Summoned hologram DOGG {hologram_id}.",
                    "result": result,
                })
            return json.dumps({
                "status": "error",
                "message": "action must be list, summon, or status.",
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

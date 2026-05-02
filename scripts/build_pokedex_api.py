#!/usr/bin/env python3
"""
build_pokedex_api.py — generate the static RAR Pokédex API.

Mirrors kody-w/RAPP_Store/scripts/build_pokedex_api.py (same shape,
applied to bare agents instead of rapplications). Modeled on PokeAPI:
predictable static URLs at raw.githubusercontent.com, no backend.

URL shape (relative to repo root, all under api/v1/):

    api/v1/index.json                    — paginated list + counts
    api/v1/agent/<id>.json               — single agent entry
    api/v1/agent/<id>.card               — the .card holocard (.py + magic comment)
    api/v1/agent/<id>.py                 — the bare singleton .py
    api/v1/sprite/<id>.svg               — deterministic generative sprite

Where <id> is the URL-safe agent name with @publisher/ replaced by
publisher__ (e.g. @rapp/learn_new → rapp__learn_new) so the path stays
flat and HTTP-safe. The original namespaced name lives inside the JSON.

The zoodex's Discover tab fetches index.json from this endpoint AND
from RAPP_Store's + RAPP_Sense_Store's, then renders the union. One
unified Pokédex; three federated source repos.

Reads registry.json (already built by build_registry.py) — that's the
source of truth for what's in the catalog. Each entry's _file points
at the actual .py file under agents/@<publisher>/<file>.py.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import time
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
_REGISTRY = _REPO / "registry.json"
_AGENTS_ROOT = _REPO / "agents"
_API = _REPO / "api" / "v1"

SCHEMA_API_INDEX = "rar-pokedex-api/1.0"
SCHEMA_API_AGENT = "rar-pokedex-agent/1.0"
RAW_PREFIX = "https://raw.githubusercontent.com/kody-w/RAR/main"


def _now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _slug(name: str) -> str:
    """@publisher/agent_name → publisher__agent_name (URL-safe)."""
    if name.startswith("@"):
        name = name[1:]
    return name.replace("/", "__").replace(".", "_")


# ── Sprite generator (matches the rapp_store one byte-for-byte) ────────────

PALETTES = {
    "core":       ["#d29922", "#ffa657", "#7d4e00"],
    "platform":   ["#79c0ff", "#58a6ff", "#0969da"],
    "integrations": ["#ffa657", "#f78166", "#bc4c00"],
    "creative":   ["#b58ddf", "#a78bfa", "#8250df"],
    "b2b_sales":  ["#79c0ff", "#58a6ff", "#0969da"],
    "b2c_sales":  ["#3fb950", "#56d364", "#1a7f37"],
    "default":    ["#58a6ff", "#79c0ff", "#0969da"],
}


def _sprite_svg(seed: str, category: str = "default") -> str:
    h = abs(int(hashlib.sha256(seed.encode()).hexdigest()[:8], 16))
    palette = PALETTES.get(category, PALETTES["default"])
    fg = palette[h % 3]
    bg = palette[(h >> 4) % 3]
    rects = []
    for y in range(6):
        for x in range(3):
            bit = (h >> ((y * 3 + x) % 28)) & 1
            if bit:
                rects.append(f'<rect x="{x*8}" y="{y*8}" width="8" height="8" fill="{fg}"/>')
                rects.append(f'<rect x="{(5-x)*8}" y="{y*8}" width="8" height="8" fill="{fg}"/>')
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="192" height="192" shape-rendering="crispEdges">\n'
        f'  <rect width="48" height="48" fill="{bg}" opacity="0.25"/>\n'
        + "  " + "\n  ".join(rects) + "\n</svg>\n"
    )


# ── Per-agent entry ────────────────────────────────────────────────────────

def _build_entry(agent: dict) -> dict:
    """Translate a registry.json agent entry into a Pokédex entry."""
    name = agent["name"]                       # e.g. @rapp/learn_new
    slug = _slug(name)                          # e.g. rapp__learn_new
    publisher = name.split("/")[0] if "/" in name else "@anon"
    file_rel = agent.get("_file", "")           # agents/@rapp/learn_new_agent.py
    has_card = bool(agent.get("_has_card"))
    sha256 = agent.get("_sha256") or ""
    rappid = f"rappid:v2:agent:{publisher}/{name.split('/')[-1]}:{(sha256 or _slug(name))[:32]}"

    # File-on-disk references (publisher-namespaced under agents/)
    py_url = f"{RAW_PREFIX}/{file_rel}" if file_rel else None
    # If a .card file is shipped alongside, link it too. The registry
    # uses `_card_sha256`; the file lives at <_file>.card.
    card_url = py_url + ".card" if (py_url and has_card) else None
    # The Pokédex API also serves a fetch-friendly mirror under api/v1/agent/
    api_card_url = f"{RAW_PREFIX}/api/v1/agent/{slug}.card" if has_card else None
    api_py_url = f"{RAW_PREFIX}/api/v1/agent/{slug}.py"

    return {
        "schema": SCHEMA_API_AGENT,
        "id": slug,
        "name": agent.get("display_name", name.split("/")[-1]),
        "rar_name": name,                       # original @publisher/slug
        "rappid": rappid,
        "version": agent.get("version", "0.0.0"),
        "publisher": publisher,
        "category": agent.get("category"),
        "tags": agent.get("tags", []),
        "description": agent.get("description"),
        "author": agent.get("author"),
        "quality_tier": agent.get("quality_tier"),
        "requires_env": agent.get("requires_env", []),
        "dependencies": agent.get("dependencies", []),
        "lines": agent.get("_lines"),
        "size_kb": agent.get("_size_kb"),
        "sha256": sha256,
        "has_card": has_card,
        "added_at": agent.get("_added_at"),

        # Lineage
        "parent_rappid": "rappid:v2:prototype:@rapp/origin:0b635450c04249fbb4b1bdb571044dec@github.com/kody-w/RAPP",

        # Asset URLs
        "sprite_url":  f"{RAW_PREFIX}/api/v1/sprite/{slug}.svg",
        "py_url":      py_url,
        "card_url":    card_url,
        "api_py_url":  api_py_url,
        "api_card_url": api_card_url,

        # Self-reference + browse-back
        "self_url":    f"{RAW_PREFIX}/api/v1/agent/{slug}.json",
        "github_url":  f"https://github.com/kody-w/RAR/blob/main/{file_rel}" if file_rel else None,
    }


# ── Main build ─────────────────────────────────────────────────────────────

def main():
    if not _REGISTRY.is_file():
        print(f"err: registry.json not found at {_REGISTRY}", file=sys.stderr)
        sys.exit(1)

    if _API.exists():
        shutil.rmtree(_API)
    (_API / "agent").mkdir(parents=True)
    (_API / "sprite").mkdir(parents=True)

    with open(_REGISTRY) as f:
        registry = json.load(f)

    entries = []
    for agent in registry.get("agents", []):
        entry = _build_entry(agent)
        slug = entry["id"]
        entries.append(entry)

        # Per-agent JSON
        (_API / "agent" / f"{slug}.json").write_text(
            json.dumps(entry, indent=2) + "\n"
        )

        # Sprite SVG
        sprite = _sprite_svg(entry["rappid"], entry.get("category") or "default")
        (_API / "sprite" / f"{slug}.svg").write_text(sprite)

        # Mirror the .py + .card under api/v1/agent/ for stable URLs
        # (the originals stay at agents/@<publisher>/...; the API copies
        # are slug-named for HTTP-friendly fetching).
        file_rel = agent.get("_file", "")
        if file_rel:
            src_py = _REPO / file_rel
            if src_py.is_file():
                (_API / "agent" / f"{slug}.py").write_bytes(src_py.read_bytes())
            src_card = _REPO / f"{file_rel}.card"
            if src_card.is_file():
                (_API / "agent" / f"{slug}.card").write_bytes(src_card.read_bytes())

    # Index — paginated summary tiles (matches RAPP_Store's shape)
    index = {
        "schema": SCHEMA_API_INDEX,
        "name": "RAR Pokédex API",
        "description": (
            "Static catalog API for bare RAPP agents (single-file Python, "
            "BasicAgent subclass, perform()). Mirrors the RAPP_Store API "
            "shape so the rapp-zoo can browse all federation stores with "
            "the same client code. Each entry has a sprite, a downloadable "
            ".py (and .card holocard if shipped), lineage back to the "
            "species root, and stats (lines, size, sha256)."
        ),
        "version": "1.0.0",
        "generated_at": _now_iso(),
        "count": len(entries),
        "self_url":  f"{RAW_PREFIX}/api/v1/index.json",
        "agents": [
            {
                "id":        e["id"],
                "name":      e["name"],
                "rar_name":  e["rar_name"],
                "publisher": e["publisher"],
                "category":  e["category"],
                "version":   e["version"],
                "has_card":  e["has_card"],
                "url":       e["self_url"],
                "sprite":    e["sprite_url"],
                "py":        e["api_py_url"],
                "card":      e["api_card_url"],
            }
            for e in entries
        ],
    }
    (_API / "index.json").write_text(json.dumps(index, indent=2) + "\n")

    print(f"  → wrote {len(entries)} agent entries to {_API.relative_to(_REPO)}/")
    print(f"  → index: api/v1/index.json")


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_pokedex_api


def slug(name: str) -> str:
    return name.lstrip("@").replace("/", "__").replace(".", "_")


def test_card_urls_exist_only_for_shipped_card_artifacts():
    registry = json.loads(
        (ROOT / "registry.json").read_text(encoding="utf-8")
    )
    for agent in registry["agents"]:
        file_rel = agent.get("_file", "")
        if not file_rel:
            continue
        source = ROOT / file_rel
        card_source = (
            source
            if file_rel.endswith(".card")
            else ROOT / f"{file_rel}.card"
        )
        api_path = (
            ROOT
            / "api"
            / "v1"
            / "agent"
            / f"{slug(agent['name'])}.json"
        )
        api = json.loads(api_path.read_text(encoding="utf-8"))
        mirror = api_path.with_suffix(".card")
        if card_source.is_file():
            assert api["card_url"]
            assert api["api_card_url"]
            assert mirror.is_file()
            assert mirror.read_bytes() == card_source.read_bytes()
        else:
            assert api["card_url"] is None
            assert api["api_card_url"] is None
            assert not mirror.exists()


def test_pokedex_builder_projects_canonical_tiles_and_legacy_cards():
    registry = json.loads(
        (ROOT / "registry.json").read_text(encoding="utf-8")
    )
    tile_index = json.loads(
        (ROOT / "tiles" / "v1" / "index.json").read_text(encoding="utf-8")
    )["tiles"]
    build_pokedex_api._TILES = tile_index
    for agent in registry["agents"]:
        entry = build_pokedex_api._build_entry(agent)
        assert entry["has_tile"] is True
        assert entry["tile_url"] == tile_index[agent["name"]]["url"]
        assert entry["tile_url"].endswith(".tile")

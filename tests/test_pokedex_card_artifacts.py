from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


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

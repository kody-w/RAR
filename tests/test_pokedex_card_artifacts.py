from __future__ import annotations

import json
from pathlib import Path
from scripts import build_pokedex_api


ROOT = Path(__file__).resolve().parents[1]

def test_rebuilding_agent_mirrors_preserves_other_api_feeds(tmp_path, monkeypatch):
    registry = tmp_path / "registry.json"
    registry.write_text(json.dumps({"agents": []}))
    api = tmp_path / "api" / "v1"
    foreign = {
        "skills.json": b'{"skills":[]}\n',
        "stats/downloads.json": b'{"downloads":42}\n',
        "front.json": b'{"items":[]}\n',
    }
    for relative, content in foreign.items():
        path = api / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    monkeypatch.setattr(build_pokedex_api, "_REPO", tmp_path)
    monkeypatch.setattr(build_pokedex_api, "_REGISTRY", registry)
    monkeypatch.setattr(build_pokedex_api, "_API", api)
    build_pokedex_api.main()
    for relative, content in foreign.items():
        assert (api / relative).read_bytes() == content
    assert json.loads((api / "index.json").read_text())["count"] == 0


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

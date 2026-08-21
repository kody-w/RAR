from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import urllib.parse
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SDK = ROOT / "rapp_sdk.py"
CARD_ROOT = ROOT / "cards" / "v2"
CARD_INDEX_PATH = CARD_ROOT / "index.json"
TILE_ROOT = ROOT / "tiles" / "v1"
TILE_INDEX_PATH = TILE_ROOT / "index.json"

sys.path.insert(0, str(ROOT))
import rapp_sdk


def _path_from_url(root: Path, marker: str, url: str) -> Path:
    parsed = urllib.parse.urlparse(url)
    relative = urllib.parse.unquote(parsed.path.split(marker, 1)[1])
    return root / relative


def _agent_source() -> bytes:
    return b"\r\n".join([
        b'"""Tile fixture."""',
        b"",
        b"__manifest__ = {",
        b'    "schema": "rapp-agent/1.0",',
        b'    "name": "@test/tile_fixture",',
        b'    "version": "1.0.0",',
        b'    "display_name": "Tile Fixture",',
        b'    "description": "Exercises rappid-tile/1.0.",',
        b'    "author": "RAR Tests",',
        b'    "tags": ["tile"],',
        b'    "category": "devtools",',
        b'    "quality_tier": "community",',
        b'    "requires_env": [],',
        b'    "dependencies": ["@rapp/basic_agent"],',
        b"}",
        b"",
        b"raise RuntimeError('transport verification must not execute payloads')",
        b"",
    ])


def _pack_fixture(tmp_path: Path, *, pin: bool = False) -> tuple[Path, dict]:
    agent = tmp_path / "tile_fixture_agent.py"
    agent.write_bytes(_agent_source())
    text = tmp_path / "prompt.txt"
    text.write_bytes(b"line one\r\nline two\r\n")
    binary = tmp_path / "weights.bin"
    binary.write_bytes(bytes(range(256)) + b"\x00\xffRAPPID")
    output = tmp_path / "tile_fixture_agent.py.tile"
    rapp_sdk.pack_tile(
        agent,
        resources=[text, binary],
        pin_url=agent.as_uri() if pin else None,
        output_path=output,
    )
    return output, {
        agent.name: agent.read_bytes(),
        text.name: text.read_bytes(),
        binary.name: binary.read_bytes(),
    }


def test_generated_index_has_frozen_cards_and_canonical_tiles_sections():
    index = json.loads(TILE_INDEX_PATH.read_text(encoding="utf-8"))
    assert index["schema"] == "rappid-tile-index/1.0"
    assert index["cards"] == {
        "schema": "rar-card/2.0",
        "index": (
            "https://raw.githubusercontent.com/kody-w/RAR/main/"
            "cards/v2/index.json"
        ),
        "frozen": True,
    }
    assert isinstance(index["tiles"], dict)
    assert len(index["tiles"]) >= 20


def test_every_frozen_card_migrates_without_identity_drift():
    cards = json.loads(CARD_INDEX_PATH.read_text(encoding="utf-8"))
    tile_index = json.loads(TILE_INDEX_PATH.read_text(encoding="utf-8"))["tiles"]
    assert set(tile_index) == set(cards)
    for agent_id, card_entry in cards.items():
        card_path = _path_from_url(CARD_ROOT, "/cards/v2/", card_entry["url"])
        tile_path = _path_from_url(
            TILE_ROOT,
            "/tiles/v1/",
            tile_index[agent_id]["url"],
        )
        card = json.loads(card_path.read_text(encoding="utf-8"))
        tile = json.loads(tile_path.read_text(encoding="utf-8"))
        assert tile["seed"] == card["seed"] == tile_index[agent_id]["seed"]
        assert tile["face"] == card["face"]
        assert tile["key"] == card["incantation"] == tile_index[agent_id]["key"]
        assert tile["payload"][0]["role"] == "primary"
        assert all(
            item["role"] == "resource" for item in tile["payload"][1:]
        )
        assert (
            hashlib.sha256(tile_path.read_bytes()).hexdigest()
            == tile_index[agent_id]["sha"]
        )
        assert rapp_sdk.verify_tile(tile, fetch_payloads=False)["valid"]


def test_tile_pack_unpack_preserves_crlf_text_and_binary(tmp_path):
    tile_path, originals = _pack_fixture(tmp_path)
    verified = rapp_sdk.verify_tile(tile_path)
    assert verified["offline"]["status"] == "offline: ready"
    assert [item["role"] for item in verified["tile"]["payload"]] == [
        "primary",
        "resource",
        "resource",
    ]
    destination = tmp_path / "unpacked"
    written = rapp_sdk.unpack_tile(tile_path, destination)
    assert {Path(path).name for path in written} == set(originals)
    for filename, expected in originals.items():
        assert (destination / filename).read_bytes() == expected


def test_tile_rejects_tampered_payload_and_face(tmp_path):
    tile_path, _ = _pack_fixture(tmp_path)
    tile = json.loads(tile_path.read_text(encoding="utf-8"))
    payload_tamper = copy.deepcopy(tile)
    payload_tamper["payload"][0]["inline"] += "# tampered\r\n"
    assert rapp_sdk.tile_offline_readiness(payload_tamper)["ready"] is False
    with pytest.raises(ValueError, match="sha256_lf_v1 mismatch"):
        rapp_sdk.verify_tile(payload_tamper)

    face_tamper = copy.deepcopy(tile)
    face_tamper["face"]["seed"] += 1
    with pytest.raises(ValueError, match="face.seed"):
        rapp_sdk.verify_tile(face_tamper)


def test_unsatisfiable_footprint_names_failed_requirement(tmp_path):
    tile_path, _ = _pack_fixture(tmp_path)
    tile = json.loads(tile_path.read_text(encoding="utf-8"))
    tile["stands_on"]["kernel"] = "rapp/999"
    with pytest.raises(ValueError, match=r"stands_on\.kernel unsatisfied"):
        rapp_sdk.verify_tile(tile)

    tile = json.loads(tile_path.read_text(encoding="utf-8"))
    tile["stands_on"]["python"] = ">=999.0"
    tile["manifest"]["python"] = ">=999.0"
    with pytest.raises(ValueError, match=r"stands_on\.python unsatisfied"):
        rapp_sdk.verify_tile(tile)


def test_python_footprint_supports_compatible_and_wildcard_specifiers():
    major, minor = sys.version_info[:2]
    assert rapp_sdk._python_requirement_satisfied(f"~={major}.{minor}")
    assert rapp_sdk._python_requirement_satisfied(f"=={major}.*")
    assert rapp_sdk._python_requirement_satisfied(f"!={major + 1}.*")


def test_pinned_tile_is_never_reported_offline_ready(tmp_path):
    tile_path, _ = _pack_fixture(tmp_path, pin=True)
    verified = rapp_sdk.verify_tile(tile_path)
    assert verified["offline"] == {
        "ready": False,
        "pinned_payloads": 1,
        "invalid_payloads": 0,
        "status": "offline: needs 1 pinned payload(s)",
    }


def test_from_card_writes_tile_and_legacy_card_still_loads(tmp_path):
    card = CARD_ROOT / "@rapp" / "basic_agent.py.card"
    output = tmp_path / "basic_agent.py.tile"
    migrated = Path(rapp_sdk.tile_from_card(card, output))
    assert migrated == output
    card_result = rapp_sdk.verify_card(card)
    tile_result = rapp_sdk.verify_tile(migrated)
    assert tile_result["tile"]["seed"] == card_result["card"]["seed"]
    assert tile_result["tile"]["face"] == card_result["card"]["face"]
    assert tile_result["tile"]["key"] == card_result["card"]["incantation"]


def test_from_card_maps_table_to_arena_without_inventing_lineage():
    card_path = CARD_ROOT / "@rapp" / "basic_agent.py.card"
    card = json.loads(card_path.read_text(encoding="utf-8"))
    card["table"] = {"seat": 4, "faceUp": False}
    tile = rapp_sdk.card_to_tile(card, fetch_payloads=False)
    assert tile["arena"] == {"seat": 4, "faceUp": False}
    assert "lineage" not in tile
    assert "table" not in tile


def test_tile_cli_exposes_all_protocol_verbs_and_card_alias_warns():
    help_result = subprocess.run(
        [sys.executable, str(SDK), "tile", "--help"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert help_result.returncode == 0
    for verb in ("pack", "unpack", "verify", "scan", "from-card"):
        assert verb in help_result.stdout

    legacy = subprocess.run(
        [
            sys.executable,
            str(SDK),
            "card",
            "verify",
            str(CARD_ROOT / "@rapp" / "basic_agent.py.card"),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert legacy.returncode == 0, legacy.stdout + legacy.stderr
    assert "DEPRECATED" in legacy.stderr
    assert "Schema: rar-card/2.0" in legacy.stdout


def test_tile_schema_and_registry_projection_are_published():
    schema = json.loads(
        (ROOT / "schema" / "rappid-tile-1.0.json").read_text(encoding="utf-8")
    )
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert set(schema["required"]) == rapp_sdk.TILE_REQUIRED_FIELDS
    assert schema["properties"]["schema"]["const"] == "rappid-tile/1.0"
    registry = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
    assert all(agent["_has_tile"] for agent in registry["agents"])
    indexed = json.loads(TILE_INDEX_PATH.read_text(encoding="utf-8"))["tiles"]
    for agent in registry["agents"]:
        entry = indexed[agent["name"]]
        assert agent["_tile_sha256"] == entry["sha"]
        assert agent["_tile_url"] == entry["url"]
        assert agent["_tile_key"] == entry["key"]


def test_tile_generation_is_idempotent_and_card_generation_is_frozen():
    tile_check = subprocess.run(
        [sys.executable, "scripts/migrate_tiles_v1.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=180,
    )
    assert tile_check.returncode == 0, tile_check.stdout + tile_check.stderr
    assert "0 changed, 0 stale removed" in tile_check.stdout

    card_check = subprocess.run(
        [sys.executable, "scripts/migrate_cards_v2.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=180,
    )
    assert card_check.returncode == 0, card_check.stdout + card_check.stderr
    assert "0 changed, 0 stale removed" in card_check.stdout

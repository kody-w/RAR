from __future__ import annotations

import functools
import hashlib
import http.server
import json
import subprocess
import sys
import threading
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SDK = ROOT / "rapp_sdk.py"
V1_PATH = ROOT / "cards" / "holo_cards.json"
V2_ROOT = ROOT / "cards" / "v2"
V2_INDEX_PATH = V2_ROOT / "index.json"
REGISTRY_PATH = ROOT / "registry.json"

sys.path.insert(0, str(ROOT))
import rapp_sdk


@pytest.fixture(scope="module")
def v1_cards() -> dict:
    return json.loads(V1_PATH.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def v2_index() -> dict:
    return json.loads(V2_INDEX_PATH.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def registry() -> dict:
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return {agent["name"]: agent for agent in data["agents"]}


def _face_bytes(face: dict) -> bytes:
    return json.dumps(face, ensure_ascii=True, separators=(",", ":")).encode()


def _fixture_agent_bytes() -> bytes:
    lines = [
        '"""Offline card fixture."""',
        "",
        "__manifest__ = {",
        '    "schema": "rapp-agent/1.0",',
        '    "name": "@test/card_fixture",',
        '    "version": "1.0.0",',
        '    "display_name": "Card Fixture",',
        '    "description": "Tests inert card transport.",',
        '    "author": "RAR Tests",',
        '    "tags": ["offline", "card"],',
        '    "category": "devtools",',
        '    "quality_tier": "community",',
        '    "requires_env": [],',
        '    "dependencies": ["@rapp/basic_agent"],',
        "}",
        "",
        "raise RuntimeError('a scan must never execute this payload')",
        "",
    ]
    return "\r\n".join(lines).encode("utf-8")


def _pack_fixture(tmp_path: Path, *, with_egg: bool = False) -> tuple[Path, Path, Path | None]:
    agent = tmp_path / "card_fixture_agent.py"
    agent.write_bytes(_fixture_agent_bytes())
    egg = tmp_path / "fixture.egg" if with_egg else None
    if egg is not None:
        egg.write_bytes(bytes(range(256)) + b"\x00RAR-CARD\xff")
    card = tmp_path / "card_fixture.card"
    command = [
        sys.executable,
        str(SDK),
        "card",
        "pack",
        str(agent),
        "--inline",
        "--output",
        str(card),
    ]
    if egg is not None:
        command[5:5] = ["--egg", str(egg)]
    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    return card, agent, egg


def test_every_v1_face_round_trips_byte_for_byte(v1_cards, v2_index):
    assert set(v2_index) == set(v1_cards)
    for agent_id, v1_face in v1_cards.items():
        card_path = V2_ROOT / f"{agent_id}.card"
        v2 = json.loads(card_path.read_text(encoding="utf-8"))
        assert _face_bytes(v2["face"]) == _face_bytes(v1_face), agent_id
        assert _face_bytes(rapp_sdk.to_v1(v2)) == _face_bytes(v1_face), agent_id


def test_every_v2_seed_and_index_hash_recomputes(v1_cards, v2_index, registry):
    assert set(v2_index) == set(v1_cards) == set(registry)
    for agent_id, entry in v2_index.items():
        path = V2_ROOT / f"{agent_id}.card"
        raw = path.read_bytes()
        card = json.loads(raw)
        manifest = card["manifest"]
        seed = rapp_sdk.forge_seed(
            manifest["name"],
            manifest.get("category", "general"),
            manifest.get("quality_tier", "community"),
            manifest.get("tags", []),
            manifest.get("dependencies", []),
        )
        assert card["seed"] == entry["seed"] == seed, agent_id
        assert entry["name_seed"] == rapp_sdk.seed_hash(agent_id), agent_id
        assert entry["incantation"] == rapp_sdk.seed_to_words(seed), agent_id
        assert entry["sha"] == hashlib.sha256(raw).hexdigest(), agent_id
        assert card["dimension"] is None and card["state"] == "dormant"
        assert card["scan"]["url"] == entry["url"]
        assert rapp_sdk.verify_card(card, fetch_payloads=False)["valid"]


def test_migrated_payloads_are_revision_pinned(v2_index, registry):
    for agent_id in v2_index:
        card = json.loads((V2_ROOT / f"{agent_id}.card").read_text(encoding="utf-8"))
        item = card["payload"][0]
        expected = registry[agent_id].get("_sha256") or registry[agent_id].get(
            "_stub_sha256"
        )
        revision = card["provenance"]["rar_revision"]
        assert item["sha256_lf_v1"] == expected
        assert f"/{revision}/" in item["url"]
        assert "/main/" not in item["url"]
        assert "inline" not in item


def test_tampered_payload_hash_is_refused(tmp_path):
    card_path, _, _ = _pack_fixture(tmp_path)
    card = json.loads(card_path.read_text(encoding="utf-8"))
    card["payload"][0]["inline"] += "# tampered\r\n"
    card_path.write_bytes(rapp_sdk._card_json_bytes(card))
    with pytest.raises(ValueError, match="sha256_lf_v1 mismatch"):
        rapp_sdk.verify_card(card_path)


@pytest.mark.parametrize(
    "mutate",
    [
        lambda card: card["face"].__setitem__("seed", card["seed"] + 1),
        lambda card: card["face"].__setitem__("title", "A forged face"),
    ],
)
def test_face_and_seed_disagreement_is_refused(tmp_path, mutate):
    source = V2_ROOT / "@aibast-agents-library" / "account_intelligence.card"
    card = json.loads(source.read_text(encoding="utf-8"))
    mutate(card)
    tampered = tmp_path / "tampered.card"
    tampered.write_bytes(rapp_sdk._card_json_bytes(card))
    with pytest.raises(ValueError, match="face"):
        rapp_sdk.verify_card(tampered)


def test_cli_pack_unpack_preserves_crlf_text_and_binary(tmp_path):
    card, agent, egg = _pack_fixture(tmp_path, with_egg=True)
    verify = subprocess.run(
        [sys.executable, str(SDK), "card", "verify", str(card)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert verify.returncode == 0, verify.stdout + verify.stderr
    assert "sha256-lf-v1:" in verify.stdout
    assert "sha256:" in verify.stdout

    output = tmp_path / "unpacked"
    unpack = subprocess.run(
        [sys.executable, str(SDK), "card", "unpack", str(card), str(output)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert unpack.returncode == 0, unpack.stdout + unpack.stderr
    assert (output / agent.name).read_bytes() == agent.read_bytes()
    assert b"\r\n" in (output / agent.name).read_bytes()
    assert egg is not None
    assert (output / egg.name).read_bytes() == egg.read_bytes()


def test_card_scan_accepts_local_file_url_without_execution(tmp_path):
    card, _, _ = _pack_fixture(tmp_path)
    marker = tmp_path / "payload-executed"
    result = subprocess.run(
        [sys.executable, str(SDK), "card", "scan", card.as_uri()],
        cwd=marker.parent,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Card Fixture" in result.stdout
    assert "sha256-lf-v1:" in result.stdout
    assert not marker.exists()


def test_card_scan_accepts_directory_served_url_offline(tmp_path):
    card, _, _ = _pack_fixture(tmp_path)

    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, _format, *_args):
            pass

    handler = functools.partial(QuietHandler, directory=str(tmp_path))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        url = f"http://127.0.0.1:{server.server_port}/{card.name}"
        result = subprocess.run(
            [sys.executable, str(SDK), "card", "scan", url],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30,
        )
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Verified: @test/card_fixture" in result.stdout


def test_migration_is_idempotent():
    result = subprocess.run(
        [sys.executable, "scripts/migrate_cards_v2.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=180,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "0 changed, 0 stale removed" in result.stdout


def test_schema_is_draft_2020_12_and_models_sealed_payloads():
    schema = json.loads(
        (ROOT / "schema" / "rar-card-2.0.json").read_text(encoding="utf-8")
    )
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert set(schema["required"]) == rapp_sdk.CARD_REQUIRED_FIELDS
    assert schema["properties"]["state"]["enum"] == ["dormant", "active"]
    payload = schema["$defs"]["payload"]
    assert set(payload["properties"]["kind"]["enum"]) == {"agent.py", "egg"}
    assert len(payload["oneOf"]) == 2


def test_site_and_api_publish_v2_cards_with_local_qr():
    api = json.loads((ROOT / "api.json").read_text(encoding="utf-8"))
    assert api["endpoints"]["cards_v2"]["url"].endswith("/cards/v2/index.json")
    assert api["endpoints"]["card_file"]["url"].endswith(
        "/cards/v2/{publisher}/{slug}.card"
    )
    pages = {
        name: (ROOT / name).read_text(encoding="utf-8")
        for name in ("store.html", "grail.html", "incantation-hero.html")
    }
    assert "cards/v2/index.json" in pages["store.html"]
    assert "_v2CardIndex" in pages["store.html"]
    assert "envelope.face" in pages["grail.html"]
    assert "CARD_V2" in pages["incantation-hero.html"]
    for name, page in pages.items():
        assert "api.qrserver.com" not in page, name
    assert "rarQrSvg" in pages["store.html"]
    assert "rarQrSvg" in pages["grail.html"]
    assert "renderQR" in pages["incantation-hero.html"]

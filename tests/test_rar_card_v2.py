from __future__ import annotations

import functools
import hashlib
import http.server
import json
import copy
import shutil
import subprocess
import sys
import threading
import urllib.parse
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SDK = ROOT / "rapp_sdk.py"
V1_PATH = ROOT / "cards" / "holo_cards.json"
V2_ROOT = ROOT / "cards" / "v2"
V2_INDEX_PATH = V2_ROOT / "index.json"
TILE_ROOT = ROOT / "tiles" / "v1"
TILE_INDEX_PATH = TILE_ROOT / "index.json"
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


def _v2_card_path(agent_id: str, index: dict) -> Path:
    url = index[agent_id]["url"]
    relative = urllib.parse.unquote(
        urllib.parse.urlparse(url).path.split("/cards/v2/", 1)[1]
    )
    return V2_ROOT / relative


def _fixture_agent_bytes() -> bytes:
    lines = [
        '"""Offline rappid tile fixture."""',
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
    card = tmp_path / "card_fixture_agent.py.tile"
    command = [
        sys.executable,
        str(SDK),
        "tile",
        "pack",
        str(agent),
        "--inline",
        "--out",
        str(card),
    ]
    if egg is not None:
        command[5:5] = ["--resource", str(egg)]
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
    assert set(v2_index) <= set(v1_cards)
    for agent_id in v2_index:
        v1_face = v1_cards[agent_id]
        card_path = _v2_card_path(agent_id, v2_index)
        v2 = json.loads(card_path.read_text(encoding="utf-8"))
        assert _face_bytes(v2["face"]) == _face_bytes(v1_face), agent_id
        assert _face_bytes(rapp_sdk.to_v1(v2)) == _face_bytes(v1_face), agent_id


def test_every_v2_seed_and_index_hash_recomputes(v1_cards, v2_index, registry):
    assert set(v2_index) <= set(v1_cards) == set(registry)
    for agent_id, entry in v2_index.items():
        path = _v2_card_path(agent_id, v2_index)
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
        path = _v2_card_path(agent_id, v2_index)
        card = json.loads(path.read_text(encoding="utf-8"))
        item = card["payload"][0]
        expected = registry[agent_id].get("_sha256") or registry[agent_id].get(
            "_stub_sha256"
        )
        revision = card["provenance"]["rar_revision"]
        assert item["sha256_lf_v1"] == expected
        assert f"/{revision}/" in item["url"]
        assert "/main/" not in item["url"]
        assert "inline" not in item
        assert path.name == f"{item['filename']}.card"
        readiness = rapp_sdk.card_offline_readiness(card)
        assert readiness["status"] == "offline: needs 1 pinned payload(s)"


def test_tampered_payload_hash_is_refused(tmp_path):
    card_path, _, _ = _pack_fixture(tmp_path)
    card = json.loads(card_path.read_text(encoding="utf-8"))
    card["payload"][0]["inline"] += "# tampered\r\n"
    card_path.write_bytes(rapp_sdk._tile_json_bytes(card))
    with pytest.raises(ValueError, match="sha256_lf_v1 mismatch"):
        rapp_sdk.verify_tile(card_path)


def test_pack_pin_must_resolve_to_the_local_agent(tmp_path):
    agent = tmp_path / "card_fixture_agent.py"
    agent.write_bytes(_fixture_agent_bytes())
    packed = tmp_path / "card_fixture_agent.py.tile"
    result = rapp_sdk.pack_tile(
        agent,
        pin_url=agent.as_uri(),
        output_path=packed,
    )
    assert Path(result) == packed
    assert rapp_sdk.verify_tile(packed)["valid"]

    wrong = tmp_path / "wrong.py"
    wrong.write_text("not the same agent\n", encoding="utf-8")
    with pytest.raises(ValueError, match="does not match the local agent"):
        rapp_sdk.pack_tile(
            agent,
            pin_url=wrong.as_uri(),
            output_path=tmp_path / "card_fixture_agent.py.tile",
        )


def test_deprecated_card_pack_alias_emits_tile_and_warns(tmp_path):
    agent = tmp_path / "card_fixture_agent.py"
    agent.write_bytes(_fixture_agent_bytes())
    result = subprocess.run(
        [
            sys.executable,
            str(SDK),
            "card",
            "pack",
            str(agent),
            "--out",
            str(tmp_path / "card_fixture_agent.py.tile"),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    card = tmp_path / "card_fixture_agent.py.tile"
    assert f"Packed rappid tile: {card}" in result.stdout
    assert "DEPRECATED" in result.stderr
    packed = json.loads(card.read_text(encoding="utf-8"))
    assert packed["payload"]
    assert all("inline" in item and "url" not in item for item in packed["payload"])
    assert rapp_sdk.verify_tile(card)["offline"]["status"] == "offline: ready"


@pytest.mark.parametrize(
    "mutate",
    [
        lambda card: card["face"].__setitem__("seed", card["seed"] + 1),
        lambda card: card["face"].__setitem__("title", "A forged face"),
    ],
)
def test_face_and_seed_disagreement_is_refused(
    tmp_path, mutate, v2_index,
):
    source = _v2_card_path(
        "@aibast-agents-library/account_intelligence",
        v2_index,
    )
    card = json.loads(source.read_text(encoding="utf-8"))
    mutate(card)
    tampered = tmp_path / source.name
    tampered.write_bytes(rapp_sdk._card_json_bytes(card))
    with pytest.raises(ValueError, match="face"):
        rapp_sdk.verify_card(tampered)


def test_cli_pack_unpack_preserves_crlf_text_and_binary(tmp_path):
    card, agent, egg = _pack_fixture(tmp_path, with_egg=True)
    verify = subprocess.run(
        [sys.executable, str(SDK), "tile", "verify", str(card)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert verify.returncode == 0, verify.stdout + verify.stderr
    assert "sha256-lf-v1:" in verify.stdout
    assert "sha256:" in verify.stdout
    assert "offline: ready" in verify.stdout

    output = tmp_path / "unpacked"
    unpack = subprocess.run(
        [sys.executable, str(SDK), "tile", "unpack", str(card), str(output)],
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


def test_cli_verify_and_scan_label_pinned_tile_not_offline_ready(v2_index):
    agent_id = "@aibast-agents-library/account_intelligence"
    card = _v2_card_path(agent_id, v2_index)
    incantation = v2_index[agent_id]["incantation"]
    commands = [
        [sys.executable, str(SDK), "card", "verify", str(card)],
        [sys.executable, str(SDK), "card", "scan", incantation],
    ]
    for command in commands:
        result = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert result.returncode == 0, result.stdout + result.stderr
        assert "offline: needs 1 pinned payload(s)" in result.stdout


def test_offline_path_tile_is_offline_ready(tmp_path, monkeypatch):
    trailhead = tmp_path / "trailhead"
    offline = tmp_path / "offline"
    trailhead.mkdir()
    offline.mkdir()
    card, agent, egg = _pack_fixture(trailhead, with_egg=True)
    copied_card = Path(shutil.copy2(card, offline / card.name))

    def reject_network(*_args, **_kwargs):
        raise AssertionError("the offline path must not fetch")

    monkeypatch.setattr(rapp_sdk.urllib.request, "urlopen", reject_network)
    verified = rapp_sdk.verify_tile(copied_card)
    assert verified["offline"] == {
        "ready": True,
        "pinned_payloads": 0,
        "invalid_payloads": 0,
        "status": "offline: ready",
    }

    unpacked = offline / "unpacked"
    rapp_sdk.unpack_tile(copied_card, unpacked)
    assert (unpacked / agent.name).read_bytes() == agent.read_bytes()
    assert egg is not None
    assert (unpacked / egg.name).read_bytes() == egg.read_bytes()


def test_unpack_without_directory_strips_final_dot_tile_suffix(tmp_path):
    card, agent, egg = _pack_fixture(tmp_path, with_egg=True)
    agent_bytes = agent.read_bytes()
    egg_bytes = egg.read_bytes() if egg is not None else b""
    agent.unlink()
    assert egg is not None
    egg.unlink()

    written = rapp_sdk.unpack_tile(card)

    assert {Path(path) for path in written} == {agent, egg}
    assert agent.read_bytes() == agent_bytes
    assert egg.read_bytes() == egg_bytes


@pytest.mark.parametrize("operation", ["verify", "scan"])
def test_reader_refuses_sleeve_name_disagreement(
    tmp_path, operation, v2_index,
):
    source = _v2_card_path(
        "@aibast-agents-library/account_intelligence",
        v2_index,
    )
    wrong_name = tmp_path / "wrong.tile"
    shutil.copy2(source, wrong_name)
    reader = rapp_sdk.verify_tile if operation == "verify" else rapp_sdk.scan_tile
    with pytest.raises(ValueError, match="rappid tile filename.*disagrees"):
        reader(wrong_name)


@pytest.mark.parametrize("operation", ["verify", "scan"])
def test_reader_refuses_encoded_url_separator(
    tmp_path, monkeypatch, operation,
):
    card, _, _ = _pack_fixture(tmp_path)
    raw = card.read_bytes()
    monkeypatch.setattr(
        rapp_sdk,
        "_read_url_bytes",
        lambda _url, max_bytes=None: raw,
    )
    source = (
        "https://example.invalid/not-the-sleeve%2F"
        "card_fixture_agent.py.tile"
    )
    reader = rapp_sdk.verify_tile if operation == "verify" else rapp_sdk.scan_tile
    with pytest.raises(ValueError, match="must not encode a path separator"):
        reader(source)


def test_pack_out_rejects_wrong_sleeve_basename(tmp_path):
    agent = tmp_path / "card_fixture_agent.py"
    agent.write_bytes(_fixture_agent_bytes())
    with pytest.raises(ValueError, match="Output filename must be"):
        rapp_sdk.pack_tile(
            agent,
            output_path=tmp_path / "wrong.tile",
        )


def test_remote_unpack_keeps_sleeve_subdirectory(
    tmp_path, monkeypatch,
):
    packed_dir = tmp_path / "packed"
    receiver = tmp_path / "receiver"
    packed_dir.mkdir()
    receiver.mkdir()
    card, agent, _ = _pack_fixture(packed_dir)
    raw = card.read_bytes()
    expected = agent.read_bytes()
    monkeypatch.setattr(
        rapp_sdk,
        "_read_url_bytes",
        lambda _url, max_bytes=None: raw,
    )
    monkeypatch.chdir(receiver)

    written = rapp_sdk.unpack_tile(
        "https://example.invalid/card_fixture_agent.py.tile"
    )

    restored = receiver / "card_fixture_agent.py" / "card_fixture_agent.py"
    assert written == [str(restored)]
    assert restored.read_bytes() == expected


def test_card_scan_command_accepts_local_file_url_without_execution(tmp_path):
    card, _, _ = _pack_fixture(tmp_path)
    marker = tmp_path / "payload-executed"
    result = subprocess.run(
        [sys.executable, str(SDK), "tile", "scan", card.as_uri()],
        cwd=marker.parent,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Card Fixture" in result.stdout
    assert "sha256-lf-v1:" in result.stdout
    assert "offline: ready" in result.stdout
    assert not marker.exists()


def test_card_scan_command_accepts_directory_served_url_offline(tmp_path):
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
            [sys.executable, str(SDK), "tile", "scan", url],
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
    assert "Verified rappid tile: @test/card_fixture" in result.stdout


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


def test_migration_rejects_a_nonexistent_revision():
    result = subprocess.run(
        [
            sys.executable,
            "scripts/migrate_cards_v2.py",
            "--revision",
            "0" * 40,
            "--check",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 1
    assert "does not exist" in result.stderr


@pytest.mark.parametrize(
    ("path", "value", "message"),
    [
        (("scan", "qr"), 7, "scan.qr"),
        (("manifest", "display_name"), 7, "manifest.display_name"),
        (("manifest", "dependencies"), [7], "manifest.dependencies"),
        (("origin", "parkedAt"), 7, "origin.parkedAt"),
        (("face", "avatar_svg"), 7, "face.avatar_svg"),
    ],
)
def test_verify_enforces_normative_property_types(
    path, value, message, v2_index,
):
    source = _v2_card_path(
        "@aibast-agents-library/account_intelligence",
        v2_index,
    )
    card = json.loads(source.read_text(encoding="utf-8"))
    target = card
    for key in path[:-1]:
        if target.get(key) is None:
            target[key] = {}
        target = target[key]
    target[path[-1]] = value
    with pytest.raises(ValueError, match=message):
        rapp_sdk.verify_card(copy.deepcopy(card), fetch_payloads=False)


def test_scan_refuses_oversized_rappid_tile_document(tmp_path):
    oversized = tmp_path / "oversized.card"
    oversized.write_bytes(b"{" + b" " * rapp_sdk.CARD_MAX_DOCUMENT_BYTES + b"}\n")
    with pytest.raises(ValueError, match="exceeds"):
        rapp_sdk.scan_card(oversized.as_uri())


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


def test_site_and_api_publish_rappid_tiles_with_local_qr():
    api = json.loads((ROOT / "api.json").read_text(encoding="utf-8"))
    assert api["endpoints"]["tiles"]["url"].endswith("/tiles/v1/index.json")
    assert api["endpoints"]["tile_file"]["url"].endswith(
        "/tiles/v1/{publisher}/{primary_payload_filename}.tile"
    )
    assert api["endpoints"]["cards_v2"]["url"].endswith("/cards/v2/index.json")
    assert api["endpoints"]["card_file"]["url"].endswith(
        "/cards/v2/{publisher}/{primary_payload_filename}.card"
    )
    pages = {
        name: (ROOT / name).read_text(encoding="utf-8")
        for name in ("store.html", "grail.html", "incantation-hero.html")
    }
    assert "tiles/v1/index.json" in pages["store.html"]
    assert "cards/v2/index.json" in pages["store.html"]
    assert "_v2CardIndex" in pages["store.html"]
    assert "parseRappidTile" in pages["store.html"]
    assert "parseRarCardV2" in pages["store.html"]
    assert "envelope.face" in pages["grail.html"]
    assert "TILE_V1" in pages["incantation-hero.html"]
    assert "CARD_V2" in pages["incantation-hero.html"]
    for name, page in pages.items():
        assert "api.qrserver.com" not in page, name
    assert "rarQrSvg" in pages["store.html"]
    assert "rarQrSvg" in pages["grail.html"]
    assert "renderQR" in pages["incantation-hero.html"]
    assert "cardFileUrlForAgent" in pages["store.html"]
    assert "CARD_INDEX_URL" in pages["grail.html"]
    assert "_install_filename" in pages["store.html"]
    assert "cardEnvelope?.scan?.url" in pages["grail.html"]


def test_user_copy_uses_rappid_tile_and_lowercase_rapplication():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    spec = (ROOT / "spec" / "rar-card-v2.md").read_text(encoding="utf-8")
    api = (ROOT / "api.json").read_text(encoding="utf-8")
    pages = [
        (ROOT / name).read_text(encoding="utf-8")
        for name in ("store.html", "grail.html", "incantation-hero.html")
    ]
    assert "RAPPlication" not in readme
    assert "rapplication" in readme
    assert "## Rappid tiles" in readme
    assert spec.startswith("# Rappid tiles (rar-card/2.0)\n")
    assert "pinned-only rappid tile" in readme
    assert "never called\noffline-ready" in readme
    assert "Rappid tile index" in api
    legacy_name = "RAR " + "card"
    assert legacy_name not in "\n".join([readme, spec, api, *pages])


@pytest.mark.parametrize(
    "workflow_name",
    ["approve-agent.yml", "approve-agent-batch.yml"],
)
def test_admission_commits_source_before_pinning_and_pushes_after_tests(
    workflow_name,
):
    workflow = (
        ROOT / ".github" / "workflows" / workflow_name
    ).read_text(encoding="utf-8")
    source_commit = workflow.index('git commit \\\n')
    frozen_check = workflow.index(
        "python scripts/migrate_cards_v2.py --check",
        source_commit,
    )
    migrate = workflow.index("python scripts/migrate_tiles_v1.py", frozen_check)
    tests = workflow.index("python -m pytest -q", migrate)
    push = workflow.index("git push origin HEAD:main", tests)
    assert source_commit < frozen_check < migrate < tests < push

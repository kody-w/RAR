"""Static 1.1 frames are byte-addressed, append-only and reproducible."""

import hashlib
import json
from pathlib import Path

import pytest

from scripts.static_api import json_bytes, publish_frame, stable_document, write_json


def test_frame_matches_exact_bytes_and_never_rewrites(tmp_path):
    content = b"first\r\n"
    frame = publish_frame("@test/example", ".py.stub", content, tmp_path)
    digest = hashlib.sha256(content).hexdigest()
    assert frame == {
        "sha256": digest, "sha8": digest[:12],
        "path": f"versions/@test/example/{digest[:12]}.py.stub",
    }
    path = tmp_path / frame["path"]
    before = path.stat().st_mtime_ns
    assert publish_frame("@test/example", ".py.stub", content, tmp_path) == frame
    assert path.stat().st_mtime_ns == before
    next_frame = publish_frame("@test/example", ".py.stub", b"second", tmp_path)
    assert path.read_bytes() == content
    assert (tmp_path / next_frame["path"]).read_bytes() == b"second"


def test_corrupt_existing_frame_is_an_error_not_an_overwrite(tmp_path):
    frame = publish_frame("item", ".json", b"{}", tmp_path)
    path = tmp_path / frame["path"]
    path.write_bytes(b"corrupt")
    with pytest.raises(ValueError, match="collision or corruption"):
        publish_frame("item", ".json", b"{}", tmp_path)
    assert path.read_bytes() == b"corrupt"


@pytest.mark.parametrize("name", ["../outside", "/absolute"])
def test_frame_name_cannot_escape_store(tmp_path, name):
    with pytest.raises(ValueError, match="invalid frame name"):
        publish_frame(name, ".py", b"", tmp_path)


def test_stable_timestamp_and_stable_write(tmp_path):
    path = tmp_path / "status.json"
    original = {"schema": "test/1.0", "generated": "2026-01-01T00:00:00Z", "count": 1}
    write_json(path, original)
    before = path.stat().st_mtime_ns
    newer = {**original, "generated": "2026-11-05T00:00:00Z"}
    assert stable_document(path, newer) == original
    write_json(path, newer)
    assert path.read_bytes() == json_bytes(original)
    assert path.stat().st_mtime_ns == before
    write_json(path, {**newer, "count": 2})
    assert json.loads(path.read_bytes())["generated"] == newer["generated"]


def test_published_status_hashes_describe_exact_endpoint_bytes():
    root = Path(__file__).resolve().parent.parent
    status = json.loads((root / "api/v1/status.json").read_text())
    for endpoint in status["endpoints"]:
        content = (root / "api/v1" / f"{endpoint['name']}.json").read_bytes()
        assert endpoint["sha8"] == hashlib.sha256(content).hexdigest()[:12]


def test_every_agent_has_a_verifiable_immutable_fallback():
    root = Path(__file__).resolve().parent.parent
    registry = json.loads((root / "registry.json").read_text())
    for agent in registry["agents"]:
        frame = agent["_version"]
        content = (root / frame["path"]).read_bytes()
        assert content == (root / agent["_file"]).read_bytes()
        assert hashlib.sha256(content).hexdigest() == frame["sha256"]
        assert frame["sha8"] == frame["sha256"][:12]


def test_exported_inputs_accept_explicit_reproducible_time(monkeypatch):
    from scripts.static_api import commit_timestamp

    commit_timestamp.cache_clear()
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "0")
    try:
        assert commit_timestamp() == "1970-01-01T00:00:00Z"
    finally:
        commit_timestamp.cache_clear()


def test_status_pins_resolve_to_identical_live_bytes():
    root = Path(__file__).resolve().parent.parent
    status = json.loads((root / "api/v1/status.json").read_text())
    for endpoint in status["endpoints"]:
        assert (root / endpoint["version_path"]).read_bytes() == (
            root / "api/v1" / f"{endpoint['name']}.json"
        ).read_bytes()


def test_pokedex_rebuild_keeps_retired_urls(tmp_path, monkeypatch):
    from scripts import build_pokedex_api as builder

    api = tmp_path / "api/v1"
    agent_dir = api / "agent"
    sprite_dir = api / "sprite"
    agent_dir.mkdir(parents=True)
    sprite_dir.mkdir()
    retired = agent_dir / "retired.json"
    retired.write_bytes(b'{"rappid": "legacy:retired", "legacy_field": true}\n')
    sprite = sprite_dir / "retired.svg"
    sprite.write_bytes(b"<svg/>")
    registry = tmp_path / "registry.json"
    registry.write_text(json.dumps({
        "agents": [{
            "name": "@test/current", "_sha256": "a" * 64,
            "display_name": "Current",
        }],
    }))
    monkeypatch.setattr(builder, "_REPO", tmp_path)
    monkeypatch.setattr(builder, "_REGISTRY", registry)
    monkeypatch.setattr(builder, "_API", api)
    builder.main()
    assert retired.read_bytes() == b'{"rappid": "legacy:retired", "legacy_field": true}\n'
    assert sprite.read_bytes() == b"<svg/>"
    first = {p.relative_to(api): p.read_bytes() for p in api.rglob("*") if p.is_file()}
    builder.main()
    assert {p.relative_to(api): p.read_bytes() for p in api.rglob("*") if p.is_file()} == first

"""Article XXVI — eggs: one file, one brainstem. The catalog admits only safe organism eggs."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("build_eggs_catalog", ROOT / "scripts" / "build_eggs_catalog.py")
cat = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cat)
rapp1 = cat.rapp1

RID = "rappid:@example/test-desk:" + "b" * 64
UTC = "2026-09-23T12:00:00.000Z"


def organism(files=None, rappid=RID, variant="organism", payload=None):
    base = {
        "rappid.json": rapp1.canonical({"schema": "rapp/1", "rappid": rappid}).encode(),
        "soul.md": b"# Test Desk\nA test brainstem.\n",
        "agents/desk_agent.py": b"# agent\n",
    }
    if files is not None:
        base.update(files)
    if variant == "session":
        return rapp1.pack_egg("session", rappid, UTC, payload={"runtime": "x", "transcript": []})
    return rapp1.pack_egg(variant, rappid, UTC, files=base,
                          payload=payload or {"engine": {"name": "rapp-brainstem", "version": "1.0.0",
                                                         "source": "grail", "commit": ""}})


@pytest.fixture
def repo(tmp_path, monkeypatch):
    monkeypatch.setattr(cat, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(cat, "EGGS_DIR", tmp_path / "eggs")
    return tmp_path


def put(repo, rel, blob):
    p = repo / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(blob)
    return p


def test_valid_egg_is_indexed(repo):
    put(repo, "eggs/@example/test-desk.egg", organism())
    catalog, problems = cat.build()
    assert problems == []
    [entry] = catalog["eggs"]
    assert entry["name"] == "@example/test-desk"
    assert entry["agents"] == ["desk_agent.py"]
    assert entry["soul_summary"] == "Test Desk"
    assert entry["memory_included"] is False
    assert entry["hatch"].endswith("eggs/@example/test-desk.egg")


def test_path_must_match_rappid(repo):
    put(repo, "eggs/@someone-else/test-desk.egg", organism())
    _, problems = cat.build()
    assert any("path must match" in p for p in problems)


def test_tampered_egg_is_rejected(repo):
    blob = bytearray(organism())
    i = blob.find(b"A test brainstem.")
    blob[i] ^= 1
    put(repo, "eggs/@example/test-desk.egg", bytes(blob))
    _, problems = cat.build()
    assert any("verification" in p for p in problems)


def test_engine_code_is_rejected(repo):
    put(repo, "eggs/@example/test-desk.egg", organism({"brainstem.py": b"print('engine')\n"}))
    _, problems = cat.build()
    assert any("engine code" in p for p in problems)


@pytest.mark.parametrize("secret", [".env", ".copilot_token", ".brainstem_secret", "agents/.env"])
def test_secrets_are_rejected(repo, secret):
    put(repo, "eggs/@example/test-desk.egg", organism({secret: b"x"}))
    _, problems = cat.build()
    assert any("secret" in p for p in problems)


def test_only_organism_eggs_are_listed(repo):
    put(repo, "eggs/@example/test-desk.egg", organism(variant="session"))
    _, problems = cat.build()
    assert any("only 'organism'" in p for p in problems)


def test_memory_is_reported_from_contents(repo):
    put(repo, "eggs/@example/test-desk.egg", organism({".brainstem_data/shared_memories/memory.json": b"{}"}))
    catalog, problems = cat.build()
    assert problems == [] and catalog["eggs"][0]["memory_included"] is True


def test_committed_catalog_is_current():
    catalog, problems = cat.build()
    assert problems == []
    committed = json.loads((ROOT / "api" / "v1" / "eggs.json").read_text())
    assert committed == catalog, "run python scripts/build_eggs_catalog.py"


def test_vendored_reference_implementation_is_verbatim():
    vendor = json.loads((ROOT / "scripts" / "rapp1.vendor.json").read_text())
    assert hashlib.sha256((ROOT / "scripts" / "rapp1.py").read_bytes()).hexdigest() == vendor["sha256"]

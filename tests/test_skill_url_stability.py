"""Permanent URL checks for accepted skill metadata paths."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "check_skill_url_stability.py"
sys.path.insert(0, str(ROOT / "scripts"))


def manifest(name: str = "@tester/workspace-refresh") -> dict:
    source = b"---\nname: workspace-refresh\ndescription: Test.\n---\n"
    return {
        "schema": "rar-skill/1.0",
        "artifact_type": "skill",
        "name": name,
        "version": "1.0.0",
        "display_name": "Workspace Refresh",
        "description": "Test skill.",
        "author": "Tester",
        "tags": ["workspace"],
        "source": {
            "repository": "tester/tools",
            "revision": "a" * 40,
            "entrypoint": "skills/workspace-refresh/SKILL.md",
            "files": [
                {
                    "path": "skills/workspace-refresh/SKILL.md",
                    "sha256": hashlib.sha256(source).hexdigest(),
                }
            ],
        },
        "install": {
            "strategy": "copy-files",
            "destination": "skills/workspace-refresh",
        },
        "protocol_conformance": {
            "profile": None,
            "status": "not_assessed",
            "evidence": [],
        },
    }


@pytest.fixture
def checker(tmp_path, monkeypatch):
    spec = importlib.util.spec_from_file_location("_skill_url_check", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    skills = tmp_path / "skills"
    path = skills / "@tester" / "workspace-refresh" / "manifest.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(manifest(), indent=2), encoding="utf-8")
    ledger = tmp_path / "state" / "published_skill_paths.json"
    ledger.parent.mkdir()
    monkeypatch.setattr(module, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(module, "SKILLS_DIR", skills)
    monkeypatch.setattr(module, "LEDGER_PATH", ledger)

    state = module.load_ledger()
    module.do_update(state)
    module.save_ledger(state)
    assert module.do_check(module.load_ledger())["ok"]
    return module, path


def test_published_skill_path_remains_stable(checker):
    module, _path = checker
    assert module.do_check(module.load_ledger())["ok"]


def test_skill_manifest_deletion_is_detected(checker):
    module, path = checker
    path.unlink()
    result = module.do_check(module.load_ledger())
    assert not result["ok"]
    assert result["missing"][0]["path"].endswith(
        "skills/@tester/workspace-refresh/manifest.json"
    )


def test_skill_manifest_move_is_detected(checker):
    module, path = checker
    moved = path.parent.parent / "renamed" / "manifest.json"
    moved.parent.mkdir()
    path.rename(moved)
    result = module.do_check(module.load_ledger())
    assert not result["ok"]
    assert result["missing"]


def test_skill_identity_change_is_detected(checker):
    module, path = checker
    value = json.loads(path.read_text())
    value["name"] = "@tester/other-skill"
    path.write_text(json.dumps(value), encoding="utf-8")
    result = module.do_check(module.load_ledger())
    assert not result["ok"]
    assert result["malformed"] or result["renamed_manifest"]

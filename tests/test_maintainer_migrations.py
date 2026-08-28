"""One-time maintainer migrations are exact and idempotent."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "apply_maintainer_migrations.py"
CONFIG = ROOT / "state" / "maintainer_migrations.json"


def load_script():
    spec = importlib.util.spec_from_file_location("_maintainer_migrations", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def test_repository_migration_inputs_match_exact_pre_or_post_hashes():
    config = json.loads(CONFIG.read_text())
    assert config["schema"] == "rar-maintainer-migrations/1.0"
    assert len(config["migrations"]) == 4
    for migration in config["migrations"]:
        path = ROOT / migration["path"]
        current = digest(path.read_bytes())
        assert current in {
            migration["expected_sha256"],
            migration["target_sha256"],
        }


def test_migration_is_hash_pinned_atomic_and_idempotent(tmp_path, monkeypatch):
    module = load_script()
    root = tmp_path / "repo"
    path = root / "agents" / "@demo" / "demo_agent.py"
    path.parent.mkdir(parents=True)
    before = b'__manifest__ = {"version": "1.0.0"}\n'
    after = b'__manifest__ = {"version": "1.0.1"}\n'
    path.write_bytes(before)
    config = tmp_path / "migrations.json"
    config.write_text(json.dumps({
        "schema": "rar-maintainer-migrations/1.0",
        "migrations": [{
            "agent": "@demo/demo",
            "path": "agents/@demo/demo_agent.py",
            "expected_sha256": digest(before),
            "target_sha256": digest(after),
            "replacements": [{
                "old": "\"version\": \"1.0.0\"",
                "new": "\"version\": \"1.0.1\"",
            }],
        }],
    }))

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "apply_maintainer_migrations.py",
            "--repo-root",
            str(root),
            "--config",
            str(config),
            "--check",
        ],
    )
    assert module.main() == 0
    assert path.read_bytes() == before

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "apply_maintainer_migrations.py",
            "--repo-root",
            str(root),
            "--config",
            str(config),
        ],
    )
    assert module.main() == 0
    assert path.read_bytes() == after
    assert module.main() == 0
    assert path.read_bytes() == after

    path.write_text("unexpected", encoding="utf-8")
    with pytest.raises(ValueError, match="unexpected source hash"):
        module.main()

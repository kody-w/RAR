from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_controller_continuity as continuity


def write_registry(path: Path, github_id: int) -> None:
    path.write_text(
        json.dumps({
            "agents": [{
                "name": "@publisher/example",
                "_controller": {
                    "github_id": github_id,
                    "github_login": "publisher",
                },
            }]
        }),
        encoding="utf-8",
    )


def test_controller_check_uses_explicit_repository_and_base(tmp_path):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(
        ["git", "config", "user.email", "test@example.com"],
        cwd=tmp_path,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Test"],
        cwd=tmp_path,
        check=True,
    )
    write_registry(tmp_path / "registry.json", 100)
    subprocess.run(["git", "add", "registry.json"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "base"], cwd=tmp_path, check=True)
    base = subprocess.check_output(
        ["git", "rev-parse", "HEAD"],
        cwd=tmp_path,
        text=True,
    ).strip()

    write_registry(tmp_path / "registry.json", 100)
    assert continuity.main(tmp_path, base) == 0

    write_registry(tmp_path / "registry.json", 200)
    assert continuity.main(tmp_path, base) == 1

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_changed_rappids_preserve_committed_identity_bridge():
    for path in (ROOT / "api" / "v1" / "agent").glob("*.json"):
        previous = subprocess.run(
            [
                "git",
                "show",
                f"HEAD:{path.relative_to(ROOT).as_posix()}",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if previous.returncode != 0:
            continue
        try:
            old = json.loads(previous.stdout)
            current = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        old_rappid = old.get("rappid")
        current_rappid = current.get("rappid")
        if old_rappid and current_rappid and old_rappid != current_rappid:
            assert old_rappid in current.get(
                "_migrated_from_all",
                [],
            ), (
                f"{path.name} lost committed RAPPID {old_rappid}"
            )

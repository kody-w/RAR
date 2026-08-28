#!/usr/bin/env python3
"""Apply exact, hash-pinned one-time maintainer migrations."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = ROOT / "state" / "maintainer_migrations.json"


def canonical_sha256(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def atomic_write(path: Path, data: bytes) -> None:
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=str(path.parent),
    )
    try:
        with os.fdopen(descriptor, "wb") as temporary:
            temporary.write(data)
            temporary.flush()
            os.fsync(temporary.fileno())
        os.replace(temporary_name, path)
    finally:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)


def apply_migration(root: Path, migration: dict, check: bool) -> dict:
    path = (root / migration["path"]).resolve()
    if root != path and root not in path.parents:
        raise ValueError(f"{migration['agent']}: path escapes repository")
    if not path.is_file():
        raise FileNotFoundError(f"{migration['agent']}: missing {path}")
    current = path.read_bytes()
    current_hash = canonical_sha256(current)
    if current_hash == migration["target_sha256"]:
        return {
            "agent": migration["agent"],
            "path": migration["path"],
            "status": "already-applied",
            "sha256": current_hash,
        }
    if current_hash != migration["expected_sha256"]:
        raise ValueError(
            f"{migration['agent']}: unexpected source hash {current_hash}; "
            f"expected {migration['expected_sha256']} or "
            f"{migration['target_sha256']}"
        )

    text = current.decode("utf-8")
    for replacement in migration.get("replacements") or []:
        old = replacement["old"]
        new = replacement["new"]
        count = text.count(old)
        if count != 1:
            raise ValueError(
                f"{migration['agent']}: expected one occurrence of {old!r}, "
                f"found {count}"
            )
        text = text.replace(old, new, 1)
    target = text.encode("utf-8")
    target_hash = canonical_sha256(target)
    if target_hash != migration["target_sha256"]:
        raise ValueError(
            f"{migration['agent']}: transformed hash {target_hash} does not "
            f"match target {migration['target_sha256']}"
        )
    if not check:
        atomic_write(path, target)
    return {
        "agent": migration["agent"],
        "path": migration["path"],
        "status": "would-apply" if check else "applied",
        "sha256": target_hash,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    parser.add_argument("--repo-root", default=str(ROOT))
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    config = json.loads(
        Path(args.config).resolve().read_text(encoding="utf-8")
    )
    if (
        config.get("schema") != "rar-maintainer-migrations/1.0"
        or not isinstance(config.get("migrations"), list)
    ):
        raise SystemExit("maintainer migration config has the wrong schema")

    results = [
        apply_migration(root, migration, args.check)
        for migration in config["migrations"]
    ]
    changed = [
        result
        for result in results
        if result["status"] in {"applied", "would-apply"}
    ]
    print(json.dumps({
        "status": "ok",
        "check": args.check,
        "changed": len(changed),
        "results": results,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

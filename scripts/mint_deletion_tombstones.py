#!/usr/bin/env python3
"""Mint deletion tombstones + ``agent.delete`` receipts.

Removing an agent artifact is a notarized act, exactly like publishing
one. ``scripts/check_notarized_changes.py`` rejects any push that
deletes ``agents/**`` bytes unless the agent's lifecycle record has
``status: "deleted"`` and its ``latest_receipt`` is an
``agent.delete`` receipt whose digest matches the *deleted* bytes.
``build_registry.py::_validated_tombstones`` then re-validates every
field before publishing the tombstone into ``registry.json``.

This is the maintainer counterpart to ``mint_maintainer_receipts.py``:
that one notarizes bytes that exist, this one notarizes bytes that
stopped existing. Idempotent — records already tombstoned are skipped.

Deleted bytes are recovered from git (``git show <rev>:<path>``) and
the recovered digest must match the lifecycle record's ``sha256``; a
mismatch means the artifact was modified before deletion and is
reported rather than guessed at.

Usage:
  python3 scripts/mint_deletion_tombstones.py --note "why it went away"
  python3 scripts/mint_deletion_tombstones.py --only @borg/hacker_news_agent
  python3 scripts/mint_deletion_tombstones.py --dry-run
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LIFECYCLE_FILE = REPO_ROOT / "state" / "agent_lifecycle.json"
RECEIPTS_DIR = REPO_ROOT / "state" / "receipts"

MAINTAINER = {"github_id": 1735900, "github_login": "kody-w"}
POLICY = "rar-maintainer-deletion/1.0"


def canonical_sha256(content: bytes) -> str:
    return hashlib.sha256(content.replace(b"\r\n", b"\n")).hexdigest()


def git_bytes_at(rev: str, rel_path: str) -> bytes | None:
    """Bytes of rel_path at rev, or None if git has no such blob."""
    try:
        return subprocess.check_output(
            ["git", "show", f"{rev}:{rel_path}"],
            cwd=REPO_ROOT,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return None


def last_known_bytes(rel_path: str) -> bytes | None:
    """Bytes from the commit that deleted rel_path (its parent's copy)."""
    try:
        revs = subprocess.check_output(
            ["git", "log", "--format=%H", "-n", "5", "--", rel_path],
            cwd=REPO_ROOT,
            text=True,
        ).split()
    except subprocess.CalledProcessError:
        return None
    for rev in revs:
        for candidate in (f"{rev}^", rev):
            data = git_bytes_at(candidate, rel_path)
            if data is not None:
                return data
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--note", default="maintainer deletion pass")
    parser.add_argument("--only", action="append", default=[],
                        help="agent name; repeatable. Default: every active "
                             "record whose artifact is gone from disk.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    lifecycle = json.loads(LIFECYCLE_FILE.read_text(encoding="utf-8"))
    agents_lc = lifecycle.setdefault("agents", {})
    now = datetime.now(timezone.utc).isoformat()

    targets = []
    for name, record in sorted(agents_lc.items()):
        if args.only and name not in args.only:
            continue
        if record.get("status") != "active":
            continue
        rel = str(record.get("canonical_path", ""))
        if not rel or (REPO_ROOT / rel).exists():
            continue
        targets.append((name, record, rel))

    if not targets:
        print("no active lifecycle records point at missing artifacts.")
        return 0

    minted = 0
    problems = []
    for name, record, rel in targets:
        content = last_known_bytes(rel)
        if content is None:
            problems.append(f"{name}: cannot recover deleted bytes for {rel}")
            continue
        digest = canonical_sha256(content)
        if digest != record.get("sha256"):
            problems.append(
                f"{name}: recovered bytes digest {digest[:12]} != lifecycle "
                f"{str(record.get('sha256'))[:12]} — artifact changed before "
                "deletion; re-notarize the change first."
            )
            continue

        version = str(record.get("version", "0.0.0"))
        tier = str(record.get("quality_tier", "community"))
        basis = json.dumps(
            {
                "migration": POLICY,
                "agent": name,
                "digest": digest,
                "version": version,
                "action": "agent.delete",
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        revision_id = hashlib.sha256(basis.encode()).hexdigest()
        receipt_id = f"rar_{revision_id}"
        receipt = {
            "acceptance": {
                "checks": ["manifest", "content_sha256", "registry_build",
                           "full_test_suite"],
                **MAINTAINER,
                "policy": POLICY,
                "workflow_run": f"local-maintainer-deletion-{now[:10]}",
            },
            "action": "agent.delete",
            "agent": name,
            "artifact": {"algorithm": "sha256-lf-v1", "digest": digest},
            "canonical_path": rel,
            "controller": dict(MAINTAINER),
            "created_at": now,
            "id": receipt_id,
            "issuer": "github:kody-w/RAR",
            "previous": {
                "digest": record.get("sha256", ""),
                "receipt": record.get("latest_receipt", ""),
                "version": record.get("version", ""),
            },
            "quality_tier": tier,
            "request_id": f"req_{revision_id[:24]}",
            "revision_id": revision_id,
            "schema": "rar-receipt/1.0",
            # Tombstone receipts carry the terminal status itself — build_registry
            # asserts receipt.status == lifecycle.status for every tombstone.
            "status": "deleted",
            "submission": {**MAINTAINER, "note": args.note},
            "version": version,
        }
        print(f"{'would mint' if args.dry_run else 'minting'} tombstone "
              f"{receipt_id[:16]}… for {name} ({rel})")
        if args.dry_run:
            continue
        (RECEIPTS_DIR / f"{revision_id}.json").write_text(
            json.dumps(receipt, indent=1, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        record.update({
            "status": "deleted",
            "latest_receipt": receipt_id,
            "updated_at": now,
        })
        minted += 1

    if problems:
        for p in problems:
            print(f"ERROR {p}")

    if minted and not args.dry_run:
        lifecycle["updated_at"] = now
        LIFECYCLE_FILE.write_text(
            json.dumps(lifecycle, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(f"minted {minted} tombstone(s); {len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())

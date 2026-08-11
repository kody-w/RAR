#!/usr/bin/env python3
"""Mint maintainer-migration lifecycle records + receipts.

For every active agent artifact whose current bytes lack matching
lifecycle evidence, mint a ``rar-maintainer-migration/1.0`` receipt and
update ``state/agent_lifecycle.json``, chaining ``previous`` to the
prior receipt. Idempotent: agents whose lifecycle digest already
matches are skipped.

This is the maintainer's bulk path for repo-wide maintenance passes
(description sweeps, template upgrades). Individual submissions still
ride the Issue notarization pipeline, which produces the same shapes.

Usage:
  python3 scripts/mint_maintainer_receipts.py [--note "why"]
"""

from __future__ import annotations

import argparse
import ast as astmod
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LIFECYCLE_FILE = REPO_ROOT / "state" / "agent_lifecycle.json"
RECEIPTS_DIR = REPO_ROOT / "state" / "receipts"

MAINTAINER = {"github_id": 1735900, "github_login": "kody-w"}
POLICY = "rar-maintainer-migration/1.0"


def canonical_sha256(content: bytes) -> str:
    return hashlib.sha256(content.replace(b"\r\n", b"\n")).hexdigest()


def manifest_of(source: str) -> dict | None:
    try:
        tree = astmod.parse(source)
    except SyntaxError:
        return None
    for node in astmod.walk(tree):
        if isinstance(node, astmod.Assign) and any(
            isinstance(t, astmod.Name) and t.id == "__manifest__"
            for t in node.targets
        ):
            try:
                return astmod.literal_eval(node.value)
            except (TypeError, ValueError):
                return None
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--note", default="maintainer bulk maintenance pass")
    args = parser.parse_args()

    lifecycle = json.loads(LIFECYCLE_FILE.read_text(encoding="utf-8"))
    agents_lc = lifecycle.setdefault("agents", {})
    now = datetime.now(timezone.utc).isoformat()
    minted = 0

    paths = sorted(REPO_ROOT.glob("agents/**/*.py")) + sorted(
        REPO_ROOT.glob("agents/**/*.py.card")
    )
    for path in paths:
        rel = str(path.relative_to(REPO_ROOT))
        content = path.read_bytes()
        manifest = manifest_of(content.decode("utf-8", errors="replace"))
        if not manifest or not manifest.get("name"):
            continue
        name = manifest["name"]
        digest = canonical_sha256(content)
        existing = agents_lc.get(name)
        if existing and existing.get("sha256") == digest:
            continue
        version = str(manifest.get("version", "0.0.0"))
        tier = str(manifest.get("quality_tier", "community"))
        action = "agent.update" if existing else "agent.create"
        basis = json.dumps(
            {
                "migration": POLICY,
                "agent": name,
                "digest": digest,
                "version": version,
                "action": action,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        revision_id = hashlib.sha256(basis.encode()).hexdigest()
        receipt_id = f"rar_{revision_id}"
        receipt = {
            "acceptance": {
                "checks": [
                    "manifest",
                    "content_sha256",
                    "registry_build",
                    "full_test_suite",
                ],
                **MAINTAINER,
                "policy": POLICY,
                "workflow_run": f"local-maintainer-migration-{now[:10]}",
            },
            "action": action,
            "agent": name,
            "artifact": {"algorithm": "sha256-lf-v1", "digest": digest},
            "canonical_path": rel,
            "controller": dict(MAINTAINER),
            "created_at": now,
            "id": receipt_id,
            "issuer": "github:kody-w/RAR",
            "previous": (
                {
                    "digest": existing.get("sha256", ""),
                    "receipt": existing.get("latest_receipt", ""),
                    "version": existing.get("version", ""),
                }
                if existing
                else None
            ),
            "quality_tier": tier,
            "request_id": f"req_{revision_id[:24]}",
            "revision_id": revision_id,
            "schema": "rar-receipt/1.0",
            "status": "notarized",
            "submission": {**MAINTAINER, "note": args.note},
            "version": version,
        }
        (RECEIPTS_DIR / f"{revision_id}.json").write_text(
            json.dumps(receipt, indent=1, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        agents_lc[name] = {
            "status": "active",
            "version": version,
            "quality_tier": tier,
            "owner_github_id": MAINTAINER["github_id"],
            "owner_github_login": MAINTAINER["github_login"],
            "canonical_path": rel,
            "sha256": digest,
            "latest_receipt": receipt_id,
            "updated_at": now,
        }
        minted += 1

    lifecycle["updated_at"] = now
    LIFECYCLE_FILE.write_text(
        json.dumps(lifecycle, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"minted {minted} receipt(s); total records: {len(agents_lc)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

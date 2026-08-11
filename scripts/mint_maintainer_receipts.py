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
  python3 scripts/mint_maintainer_receipts.py \
    --agent @publisher/agent_name --note "why"
"""

from __future__ import annotations

import argparse
import ast as astmod
import hashlib
import json
import subprocess
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


def write_lifecycle(value: dict) -> None:
    temporary = LIFECYCLE_FILE.with_suffix(".json.tmp")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    temporary.replace(LIFECYCLE_FILE)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--note", default="maintainer bulk maintenance pass")
    parser.add_argument(
        "--agent",
        help="Mint only the named @publisher/agent lifecycle record.",
    )
    parser.add_argument(
        "--collapse-unpublished",
        action="store_true",
        help=(
            "With --agent, remove only untracked receipt descendants and "
            "restore the committed lifecycle ancestor before minting."
        ),
    )
    args = parser.parse_args()
    if args.collapse_unpublished and not args.agent:
        parser.error("--collapse-unpublished requires --agent")

    lifecycle = json.loads(LIFECYCLE_FILE.read_text(encoding="utf-8"))
    agents_lc = lifecycle.setdefault("agents", {})
    if args.collapse_unpublished:
        baseline = json.loads(
            subprocess.check_output(
                [
                    "git",
                    "show",
                    "HEAD:state/agent_lifecycle.json",
                ],
                cwd=REPO_ROOT,
                text=True,
            )
        )
        baseline_record = baseline.get("agents", {}).get(args.agent)
        current_record = agents_lc.get(args.agent)
        if not baseline_record or not current_record:
            parser.error("agent lacks committed lifecycle ancestry")
        cursor = current_record.get("latest_receipt", "")
        stop = baseline_record.get("latest_receipt", "")
        removable = []
        seen = set()
        while cursor != stop:
            if not cursor.startswith("rar_") or cursor in seen:
                parser.error("unpublished receipt ancestry is invalid")
            seen.add(cursor)
            relative = Path(
                "state/receipts"
            ) / f"{cursor.removeprefix('rar_')}.json"
            receipt_path = REPO_ROOT / relative
            if not receipt_path.exists():
                parser.error(f"receipt is missing: {relative}")
            tracked = subprocess.run(
                ["git", "cat-file", "-e", f"HEAD:{relative.as_posix()}"],
                cwd=REPO_ROOT,
                capture_output=True,
            ).returncode == 0
            if tracked:
                parser.error(
                    f"refusing to remove published receipt: {relative}"
                )
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            if receipt.get("agent") != args.agent:
                parser.error("receipt ancestry crosses agent identity")
            removable.append(receipt_path)
            cursor = (receipt.get("previous") or {}).get("receipt", "")
        agents_lc[args.agent] = baseline_record
        lifecycle["updated_at"] = datetime.now(timezone.utc).isoformat()
        write_lifecycle(lifecycle)
        for path in removable:
            path.unlink()
    now = datetime.now(timezone.utc).isoformat()
    minted = 0
    matched = 0

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
        if args.agent and name != args.agent:
            continue
        matched += 1
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
                "previous": (
                    {
                        "digest": existing.get("sha256", ""),
                        "receipt": existing.get("latest_receipt", ""),
                        "version": existing.get("version", ""),
                    }
                    if existing
                    else None
                ),
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
                    "maintainer_review",
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
        receipt_path = RECEIPTS_DIR / f"{revision_id}.json"
        receipt_text = json.dumps(
            receipt,
            indent=1,
            sort_keys=True,
        ) + "\n"
        if receipt_path.exists():
            if receipt_path.read_text(encoding="utf-8") != receipt_text:
                raise RuntimeError(
                    f"refusing to overwrite different receipt {receipt_path}"
                )
        else:
            receipt_path.write_text(
                receipt_text,
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

    if args.agent and matched == 0:
        parser.error(f"agent was not found: {args.agent}")
    if minted:
        lifecycle["updated_at"] = now
        write_lifecycle(lifecycle)
    print(f"minted {minted} receipt(s); total records: {len(agents_lc)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

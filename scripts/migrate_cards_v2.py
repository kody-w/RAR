#!/usr/bin/env python3
"""Check the frozen ``rar-card/2.0`` projection without rewriting it."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
import urllib.parse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rapp_sdk import verify_card  # noqa: E402


OUTPUT_ROOT = ROOT / "cards" / "v2"
INDEX_PATH = OUTPUT_ROOT / "index.json"


def load_object(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Could not read {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def plan_migration(revision: str) -> tuple[dict[Path, bytes], list[str]]:
    if revision:
        result = subprocess.run(
            ["git", "cat-file", "-e", f"{revision}^{{commit}}"],
            cwd=ROOT,
            capture_output=True,
            timeout=30,
        )
        if result.returncode != 0:
            detail = result.stderr.decode("utf-8", errors="replace").strip()
            raise RuntimeError(
                f"revision {revision} does not exist: "
                f"{detail or 'git cat-file failed'}"
            )

    index = load_object(INDEX_PATH)
    planned: dict[Path, bytes] = {}
    for agent_id, entry in sorted(index.items()):
        if not isinstance(entry, dict):
            raise RuntimeError(f"{agent_id}: frozen card index entry must be an object")
        url = entry.get("url")
        if not isinstance(url, str):
            raise RuntimeError(f"{agent_id}: frozen card index entry has no URL")
        parsed = urllib.parse.urlparse(url)
        marker = "/cards/v2/"
        if marker not in parsed.path:
            raise RuntimeError(f"{agent_id}: frozen card URL is outside cards/v2")
        relative = Path(urllib.parse.unquote(parsed.path.split(marker, 1)[1]))
        if relative.is_absolute() or ".." in relative.parts:
            raise RuntimeError(f"{agent_id}: frozen card URL contains an unsafe path")
        card_path = OUTPUT_ROOT / relative
        try:
            raw = card_path.read_bytes()
        except OSError as exc:
            raise RuntimeError(
                f"{agent_id}: could not read {card_path.relative_to(ROOT)}: {exc}"
            ) from exc
        try:
            verified = verify_card(card_path, fetch_payloads=False)
        except ValueError as exc:
            raise RuntimeError(
                f"{agent_id}: frozen card verification failed: {exc}"
            ) from exc
        card = verified["card"]
        expected = {
            "seed": card["seed"],
            "name_seed": card["name_seed"],
            "incantation": card["incantation"],
            "sha": hashlib.sha256(raw).hexdigest(),
            "url": card["scan"]["url"],
        }
        if entry != expected:
            raise RuntimeError(f"{agent_id}: frozen card index metadata disagrees")
        if card["id"] != agent_id:
            raise RuntimeError(f"{agent_id}: frozen card identity disagrees")
        planned[card_path] = raw
    planned[INDEX_PATH] = INDEX_PATH.read_bytes()
    return planned, []


def apply_migration(planned: dict[Path, bytes], *, check: bool) -> tuple[int, int]:
    expected_cards = {path.resolve() for path in planned if path.suffix == ".card"}
    stale = (
        sorted(
            path
            for path in OUTPUT_ROOT.rglob("*.card")
            if path.resolve() not in expected_cards
        )
        if OUTPUT_ROOT.exists()
        else []
    )
    changed = [
        path
        for path, content in planned.items()
        if not path.is_file() or path.read_bytes() != content
    ]
    if not check:
        raise RuntimeError(
            "cards/v2 is frozen and cannot be rewritten; "
            "run scripts/migrate_tiles_v1.py"
        )
    if changed or stale:
        details = [
            *(f"changed: {path.relative_to(ROOT)}" for path in changed),
            *(f"stale: {path.relative_to(ROOT)}" for path in stale),
        ]
        raise RuntimeError(
            "Frozen rar-card/2.0 drift:\n  " + "\n  ".join(details)
        )
    return 0, 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check the frozen rar-card/2.0 projection",
    )
    parser.add_argument(
        "--revision",
        help="Optional full Git revision that must exist",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report frozen-card drift without writing",
    )
    args = parser.parse_args()
    if args.revision and not re.fullmatch(r"[0-9a-f]{40}", args.revision):
        parser.error("--revision must be a full 40-character lowercase Git SHA")

    try:
        planned, _ = plan_migration(args.revision or "")
        changed, removed = apply_migration(planned, check=args.check)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    card_count = sum(path.suffix == ".card" for path in planned)
    print(
        f"Frozen cards: checked {card_count} rar-card/2.0 documents; "
        f"{changed} changed, {removed} stale removed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

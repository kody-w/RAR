#!/usr/bin/env python3
"""Keep every published RAR skill manifest URL stable and namespaced."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import build_skills_catalog as skill_catalog


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
LEDGER_PATH = REPO_ROOT / "state" / "published_skill_paths.json"
LEDGER_SCHEMA = "rar-published-skill-paths/1.0"
RAW_BASE = "https://raw.githubusercontent.com/kody-w/RAR/main"


def discover_published() -> dict[str, str | None]:
    found: dict[str, str | None] = {}
    if not SKILLS_DIR.exists():
        return found
    for path in sorted(SKILLS_DIR.glob("@*/*/manifest.json")):
        relative = path.relative_to(REPO_ROOT).as_posix()
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            found[relative] = None
            continue
        errors = skill_catalog.validate_manifest(
            manifest,
            expected_path=path,
        )
        found[relative] = manifest.get("name") if not errors else None
    return found


def git_first_seen(relative: str) -> str | None:
    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "--diff-filter=A",
                "--follow",
                "--format=%aI",
                "--reverse",
                "--",
                relative,
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=20,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if result.returncode != 0:
        return None
    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return lines[0] if lines else None


def load_ledger() -> dict:
    if not LEDGER_PATH.exists():
        return {
            "schema": LEDGER_SCHEMA,
            "count": 0,
            "paths": {},
        }
    return json.loads(LEDGER_PATH.read_text(encoding="utf-8"))


def save_ledger(ledger: dict) -> None:
    ledger["schema"] = LEDGER_SCHEMA
    ledger["count"] = len(ledger.setdefault("paths", {}))
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    LEDGER_PATH.write_text(
        json.dumps(ledger, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def do_update(ledger: dict) -> tuple[int, list[str]]:
    paths = ledger.setdefault("paths", {})
    added = []
    for relative, name in sorted(discover_published().items()):
        if relative in paths:
            continue
        paths[relative] = {
            "name": name,
            "first_seen": git_first_seen(relative)
            or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        added.append(relative)
    ledger["count"] = len(paths)
    return len(added), added


def do_check(ledger: dict) -> dict:
    on_disk = discover_published()
    recorded = ledger.get("paths", {})
    by_name: dict[str, list[str]] = {}
    for relative, name in on_disk.items():
        if name:
            by_name.setdefault(name, []).append(relative)

    missing = []
    renamed_manifest = []
    malformed = []
    for relative, entry in sorted(recorded.items()):
        recorded_name = entry.get("name")
        if relative not in on_disk:
            missing.append(
                {
                    "path": relative,
                    "name": recorded_name,
                    "raw_url": f"{RAW_BASE}/{relative}",
                    "likely_moved_to": by_name.get(recorded_name, []),
                }
            )
            continue
        current_name = on_disk[relative]
        if current_name is None:
            malformed.append({"path": relative, "name": recorded_name})
        elif recorded_name and current_name != recorded_name:
            renamed_manifest.append(
                {
                    "path": relative,
                    "was": recorded_name,
                    "now": current_name,
                }
            )
    return {
        "checked": len(recorded),
        "on_disk": len(on_disk),
        "missing": missing,
        "renamed_manifest": renamed_manifest,
        "malformed": malformed,
        "unrecorded": sorted(set(on_disk) - set(recorded)),
        "ok": not missing and not renamed_manifest and not malformed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--update", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    ledger = load_ledger()
    if ledger.get("schema") != LEDGER_SCHEMA:
        print("[skills] published path ledger has the wrong schema", file=sys.stderr)
        return 1
    if args.update:
        added, paths = do_update(ledger)
        save_ledger(ledger)
        result = {"added": added, "paths": paths, "total": ledger["count"]}
        print(json.dumps(result, indent=2) if args.json else (
            f"Skill URL ledger updated: +{added}, {ledger['count']} total"
        ))
        return 0

    result = do_check(ledger)
    if args.json:
        print(json.dumps(result, indent=2))
    elif result["ok"]:
        print(
            f"Skill URL stability OK: {result['checked']} published path(s)"
        )
    else:
        print(json.dumps(result, indent=2), file=sys.stderr)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

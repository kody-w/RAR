#!/usr/bin/env python3
"""
URL Stability Check — enforces CONSTITUTION.md Article XXIII (The Permanent URL Contract).

Every published agent file path is a permanent public contract. People install
agents from this repo by URL, and those URLs live in other people's brainstems,
scripts, and products. We cannot know who depends on them and we cannot notify
them. So a published path may never be renamed, moved, or deleted.

This script is the machine check behind that promise.

    state/published_paths.json   append-only ledger of every path ever published
    check  (default)             fail if any ledger entry vanished or was renamed
    --update                     record newly published agents into the ledger

Usage:
    python scripts/check_url_stability.py            # verify (CI gate, exit 1 on break)
    python scripts/check_url_stability.py --update   # record new agents after they land
    python scripts/check_url_stability.py --json     # machine-readable result

Design notes:
  * Manifests are read via AST, never imported — same posture as build_registry.py.
  * The ledger is APPEND-ONLY. Entries are never removed by this script, because
    removing an entry is exactly the act the article forbids.
  * Seeding uses only files currently on disk, so adopting the check never starts
    from a failing state. Everything published from this point forward is bound.
"""

import argparse
import ast
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = REPO_ROOT / "agents"
LEDGER_PATH = REPO_ROOT / "state" / "published_paths.json"

LEDGER_SCHEMA = "rar-published-paths/1.0"

RAW_BASE = "https://raw.githubusercontent.com/kody-w/RAR/main"
CDN_BASE = "https://cdn.jsdelivr.net/gh/kody-w/RAR@main"

# Suffixes that constitute a published, installable artifact.
PUBLISHED_SUFFIXES = (".py",)


# ── manifest extraction (AST only, no imports) ──────────────────────────────


def extract_manifest_name(py_path: Path) -> str | None:
    """Return the __manifest__['name'] for a file, or None if absent/unparseable."""
    try:
        tree = ast.parse(py_path.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError, OSError):
        return None

    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "__manifest__":
                try:
                    manifest = ast.literal_eval(node.value)
                except (ValueError, SyntaxError):
                    return None
                if isinstance(manifest, dict):
                    name = manifest.get("name")
                    return name if isinstance(name, str) else None
    return None


def discover_published() -> dict[str, str | None]:
    """Map every agent file currently on disk to its manifest name."""
    found: dict[str, str | None] = {}
    if not AGENTS_DIR.is_dir():
        return found
    for path in sorted(AGENTS_DIR.rglob("*")):
        if not path.is_file():
            continue
        if not path.name.endswith(PUBLISHED_SUFFIXES):
            continue
        rel = path.relative_to(REPO_ROOT).as_posix()
        found[rel] = extract_manifest_name(path)
    return found


# ── git helpers ─────────────────────────────────────────────────────────────


def git_first_seen(rel_path: str) -> str | None:
    """Author date of the commit that first added rel_path, ISO-8601 UTC."""
    try:
        out = subprocess.run(
            [
                "git", "log", "--diff-filter=A", "--follow",
                "--format=%aI", "--reverse", "--", rel_path,
            ],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=20,
        )
    except (subprocess.SubprocessError, OSError):
        return None
    if out.returncode != 0:
        return None
    lines = [ln.strip() for ln in out.stdout.splitlines() if ln.strip()]
    return lines[0] if lines else None


# ── ledger I/O ──────────────────────────────────────────────────────────────


def load_ledger() -> dict:
    if not LEDGER_PATH.exists():
        return {
            "schema": LEDGER_SCHEMA,
            "article": "CONSTITUTION.md Article XXIII — The Permanent URL Contract",
            "policy": (
                "Append-only. Every path listed here has been published on main and "
                "must resolve forever. Add freely. Edit in place. Deprecate with a "
                "label. Never move, never rename, never delete."
            ),
            "raw_base": RAW_BASE,
            "cdn_base": CDN_BASE,
            "generated": None,
            "count": 0,
            "paths": {},
        }
    with LEDGER_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)


def save_ledger(ledger: dict) -> None:
    ledger["generated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    ledger["count"] = len(ledger["paths"])
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER_PATH.open("w", encoding="utf-8") as fh:
        json.dump(ledger, fh, indent=2, sort_keys=False)
        fh.write("\n")


# ── operations ──────────────────────────────────────────────────────────────


def do_update(ledger: dict) -> tuple[int, list[str]]:
    """Append any newly published agent paths. Never removes. Returns (added, names)."""
    on_disk = discover_published()
    paths = ledger.setdefault("paths", {})
    added: list[str] = []

    for rel, name in sorted(on_disk.items()):
        if rel in paths:
            # Keep the recorded name authoritative; a change is a violation, not an update.
            continue
        paths[rel] = {
            "name": name,
            "first_seen": git_first_seen(rel)
            or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        added.append(rel)

    return len(added), added


def do_check(ledger: dict) -> dict:
    """Verify every ledger entry still resolves. Returns a structured result."""
    on_disk = discover_published()
    paths = ledger.get("paths", {})

    missing: list[dict] = []
    renamed_manifest: list[dict] = []

    # Index disk state by manifest name so we can guess where a file moved to.
    by_name: dict[str, list[str]] = {}
    for rel, name in on_disk.items():
        if name:
            by_name.setdefault(name, []).append(rel)

    for rel, entry in sorted(paths.items()):
        recorded_name = entry.get("name")

        if rel not in on_disk:
            candidates = by_name.get(recorded_name, []) if recorded_name else []
            missing.append({
                "path": rel,
                "name": recorded_name,
                "raw_url": f"{RAW_BASE}/{rel}",
                "likely_moved_to": candidates,
            })
            continue

        current_name = on_disk[rel]
        if recorded_name and current_name and current_name != recorded_name:
            renamed_manifest.append({
                "path": rel,
                "was": recorded_name,
                "now": current_name,
            })

    unrecorded = sorted(set(on_disk) - set(paths))

    return {
        "checked": len(paths),
        "on_disk": len(on_disk),
        "missing": missing,
        "renamed_manifest": renamed_manifest,
        "unrecorded": unrecorded,
        "ok": not missing and not renamed_manifest,
    }


# ── reporting ───────────────────────────────────────────────────────────────


def report(result: dict) -> None:
    print(f"URL stability — Article XXIII (The Permanent URL Contract)")
    print(f"  ledger entries : {result['checked']}")
    print(f"  agents on disk : {result['on_disk']}")

    if result["missing"]:
        print()
        print(f"  ✗ {len(result['missing'])} PUBLISHED PATH(S) NO LONGER RESOLVE")
        print("    Every one of these is a live 404 for anyone who installed it.")
        for m in result["missing"]:
            print()
            print(f"    path : {m['path']}")
            print(f"    name : {m['name']}")
            print(f"    url  : {m['raw_url']}")
            if m["likely_moved_to"]:
                print(f"    NOTE : same manifest name now lives at "
                      f"{', '.join(m['likely_moved_to'])}")
                print(f"           → restore the original path. Publish the new "
                      f"location as an addition, not a replacement.")
            else:
                print(f"           → restore this file. Deprecate with a manifest "
                      f"label instead of deleting.")

    if result["renamed_manifest"]:
        print()
        print(f"  ✗ {len(result['renamed_manifest'])} MANIFEST NAME(S) CHANGED")
        print("    The manifest name is the callable tool ID. Changing it breaks callers.")
        for r in result["renamed_manifest"]:
            print(f"    {r['path']}")
            print(f"      was : {r['was']}")
            print(f"      now : {r['now']}  → revert to the published name")

    if result["unrecorded"]:
        print()
        print(f"  · {len(result['unrecorded'])} new agent(s) not yet in the ledger "
              f"(run with --update once they land on main)")
        for rel in result["unrecorded"][:10]:
            print(f"      {rel}")
        if len(result["unrecorded"]) > 10:
            print(f"      … and {len(result['unrecorded']) - 10} more")

    print()
    if result["ok"]:
        print("  ✓ OK — every published agent URL still resolves.")
    else:
        print("  ✗ FAIL — the permanent URL contract is broken. See above.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enforce the permanent URL contract for published agents."
    )
    parser.add_argument("--update", action="store_true",
                        help="append newly published agents to the ledger")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    ledger = load_ledger()

    if args.update:
        added, names = do_update(ledger)
        save_ledger(ledger)
        if args.json:
            print(json.dumps({"added": added, "paths": names,
                              "total": ledger["count"]}, indent=2))
        else:
            print(f"Ledger updated: +{added} path(s), {ledger['count']} total")
            for n in names[:20]:
                print(f"  + {n}")
            if added > 20:
                print(f"  … and {added - 20} more")
        return 0

    result = do_check(ledger)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        report(result)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

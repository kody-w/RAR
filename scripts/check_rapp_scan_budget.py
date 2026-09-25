#!/usr/bin/env python3
"""
RAPP/1 bounded-scan budget — keeps RAR inside what the RAPP/1 checker can verify.

kody-w/rapp-1's conformance checker (`rapp_check.py`, estate pin 591e014) walks a
checkout with fixed bounds. When a repository outgrows them it cannot finish its
frame discovery and reports DRIFT ("verification unavailable"), whatever the
artifacts themselves say. RAR crossed the JSON-file bound once, with more than
16,000 files; this check applies the same rules so it cannot happen silently again:

    walk       os.walk top-down in sorted order; never enters `.git` or a
               symlinked directory; at most 10,000 directories, 100,000
               entries (directories plus files) and depth 32
    discovery  every regular `*.json` file of at most 1 MiB, in sorted path
               order, except `rappid.json`, `rapp-frame-index.json`, files a
               frame index lists and numeric `frames/<n>.json`; at most 10,000
               files and 64 MiB in total

It fails at 90% of any bound, while there is still room to act, and names the
largest discovery populations. It reads no file contents except frame indexes,
and it never imports rapp-1: the rules are restated here from rapp_check.py.

Usage:
    python scripts/check_rapp_scan_budget.py          # summary; exit 1 near a bound
    python scripts/check_rapp_scan_budget.py --json   # machine-readable report
"""

import argparse
import collections
import json
import os
import re
import stat
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

MAX_WALK_ENTRIES = 100_000
MAX_WALK_DIRS = 10_000
MAX_WALK_DEPTH = 32
MAX_JSON_FILES = 10_000
MAX_JSON_BYTES = 64 * 1024 * 1024
MAX_CANONICAL_BYTES = 1024 * 1024
FAIL_FRACTION = 0.9

INDEX_NAME = "rapp-frame-index.json"
INDEX_SCHEMA = "rapp-frame-index/1"
NUMERIC_FRAME = re.compile(r"^\d+\.json$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def walk(root):
    """The checker's bounded walk: (sorted regular *.json paths, dirs, entries, depth, issues)."""
    root = os.path.abspath(root)
    found, issues, errors = [], [], []
    dirs_seen = entries_seen = max_depth = 0
    for base, dirs, files in os.walk(root, topdown=True, followlinks=False,
                                     onerror=lambda exc: errors.append(str(exc))):
        dirs_seen += 1
        relative = os.path.relpath(base, root)
        depth = 0 if relative == "." else relative.count(os.sep) + 1
        max_depth = max(max_depth, depth)
        dirs[:] = sorted(name for name in dirs
                         if name != ".git" and not os.path.islink(os.path.join(base, name)))
        if depth >= MAX_WALK_DEPTH and dirs:
            issues.append(f"depth limit reached at {relative}")
            dirs.clear()
        entries_seen += len(dirs) + len(files)
        if dirs_seen > MAX_WALK_DIRS or entries_seen > MAX_WALK_ENTRIES:
            issues.append("repository tree limit reached; tail not scanned")
            break
        for name in sorted(files):
            if name.endswith(".json"):
                path = os.path.join(base, name)
                try:
                    if stat.S_ISREG(os.lstat(path).st_mode):
                        found.append(path)
                except OSError as exc:
                    issues.append(f"cannot inspect {os.path.relpath(path, root)}: {exc}")
    issues.extend(f"cannot scan repository path: {error}" for error in errors)
    return sorted(found), dirs_seen, entries_seen, max_depth, issues


def _strict_json(path):
    if os.lstat(path).st_size > MAX_CANONICAL_BYTES:
        raise ValueError("JSON exceeds the 1 MiB input ceiling")

    def pairs(values):
        result = {}
        for key, value in values:
            if key in result:
                raise ValueError(f"duplicate JSON member: {key}")
            result[key] = value
        return result

    with open(path, "rb") as handle:
        value = json.loads(handle.read(), object_pairs_hook=pairs)
    stack = [(value, 1)]
    while stack:
        current, depth = stack.pop()
        if depth > 64:
            raise ValueError("JSON nesting depth exceeds 64")
        children = current.values() if isinstance(current, dict) else current if isinstance(current, list) else ()
        stack.extend((child, depth + 1) for child in children)
    return value


def _index_member(root, index_path, member):
    if (
        not isinstance(member, str)
        or not member
        or member.startswith("/")
        or "\\" in member
        or not member.endswith(".json")
        or any(part in ("", ".", "..") for part in member.split("/"))
    ):
        return None
    candidate = os.path.abspath(os.path.join(os.path.dirname(index_path), member))
    if os.path.commonpath((root, candidate)) != root:
        return None
    cursor = root
    parts = os.path.relpath(candidate, root).split(os.sep)
    try:
        for position, part in enumerate(parts):
            cursor = os.path.join(cursor, part)
            mode = os.lstat(cursor).st_mode
            if stat.S_ISLNK(mode) or (position < len(parts) - 1 and not stat.S_ISDIR(mode)):
                return None
        return candidate if stat.S_ISREG(os.lstat(candidate).st_mode) else None
    except OSError:
        return None


def index_members(root, index_path):
    """Paths a well-formed frame index lists; the checker verifies those instead of counting them."""
    try:
        index = _strict_json(index_path)
    except (OSError, ValueError):
        return set()
    if not isinstance(index, dict) or set(index) != {"schema", "stream_id", "frames", "head"}:
        return set()
    members, head = index["frames"], index["head"]
    if (
        index["schema"] != INDEX_SCHEMA
        or not isinstance(index["stream_id"], str)
        or not isinstance(members, list)
        or not members
        or any(not isinstance(member, str) for member in members)
        or len(members) != len(set(members))
        or not isinstance(head, dict)
        or set(head) != {"seq", "frame_hash"}
        or not isinstance(head["seq"], int)
        or isinstance(head["seq"], bool)
        or not 0 <= head["seq"] <= 2**53 - 1
        or not isinstance(head["frame_hash"], str)
        or not HEX64.fullmatch(head["frame_hash"])
    ):
        return set()
    return {path for path in (_index_member(root, index_path, m) for m in members) if path}


def measure(root=REPO_ROOT):
    """Every bound the checker applies, with RAR's current value and the fail threshold."""
    root = os.path.abspath(root)
    json_paths, dirs_seen, entries_seen, max_depth, issues = walk(root)
    excluded = {p for p in json_paths
                if os.path.basename(os.path.dirname(p)) == "frames"
                and NUMERIC_FRAME.fullmatch(os.path.basename(p))}
    for path in json_paths:
        if os.path.basename(path) == INDEX_NAME:
            excluded |= index_members(root, path)
    count = total = oversized = 0
    populations = collections.Counter()
    for path in json_paths:
        if path in excluded or os.path.basename(path) in ("rappid.json", INDEX_NAME):
            continue
        size = os.lstat(path).st_size
        if size > MAX_CANONICAL_BYTES:
            oversized += 1
            continue
        count, total = count + 1, total + size
        parts = os.path.relpath(path, root).split(os.sep)
        populations["/".join(parts[:2]) if len(parts) > 2 else parts[0]] += 1

    def bound(value, limit):
        threshold = int(limit * FAIL_FRACTION)
        return {"value": value, "limit": limit, "fail_above": threshold, "ok": value <= threshold}

    bounds = {
        "discovery_json_files": bound(count, MAX_JSON_FILES),
        "discovery_json_bytes": bound(total, MAX_JSON_BYTES),
        "walk_directories": bound(dirs_seen, MAX_WALK_DIRS),
        "walk_entries": bound(entries_seen, MAX_WALK_ENTRIES),
        "walk_depth": bound(max_depth, MAX_WALK_DEPTH),
    }
    return {
        "schema": "rar-rapp-scan-budget/1.0",
        "rules": "kody-w/rapp-1 rapp_check.py @ 591e014ad39e223b00ab343ae26e5d9a867ebeee",
        "ok": not issues and all(b["ok"] for b in bounds.values()),
        "bounds": bounds,
        "walk_issues": issues,
        "skipped_over_1_mib": oversized,
        "largest_populations": dict(populations.most_common(8)),
    }


def summary(report):
    lines = [f"RAPP/1 bounded scan ({report['rules']}): {'OK' if report['ok'] else 'NEAR OR OVER A BOUND'}"]
    for name, b in report["bounds"].items():
        mark = "ok" if b["ok"] else "FAIL"
        lines.append(f"  {name:22} {b['value']:>12,} / {b['limit']:,}  (fail above {b['fail_above']:,})  {mark}")
    lines.extend(f"  walk issue: {issue}" for issue in report["walk_issues"])
    lines.append("  largest discovery populations: " + ", ".join(
        f"{path} {n:,}" for path, n in report["largest_populations"].items()))
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--root", default=str(REPO_ROOT), help="checkout to measure (default: this repo)")
    parser.add_argument("--json", action="store_true", help="print the machine-readable report")
    args = parser.parse_args(argv)
    report = measure(args.root)
    print(json.dumps(report, indent=2) if args.json else summary(report))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())

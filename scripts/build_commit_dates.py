#!/usr/bin/env python3
"""build_commit_dates.py — commit-time truth for every agent file, as static data.

Writes state/agent_commit_dates.json mapping each agents/ path to its first
(added) and latest (updated) commit timestamps, computed from local git history.

This replaces the GitHub commits API at page-load time: index.html used to make
up to 16 unauthenticated API calls per visitor to recover these dates. CI has
the full clone (fetch-depth: 0), so the same truth is derived here for free and
served as a committed static file — pages read data, never the API.

Runs in build-registry.yml after build_registry.py. Requires full history;
refuses (exit 2) on a shallow clone rather than committing wrong dates.
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "state" / "agent_commit_dates.json"


def main():
    shallow = subprocess.run(
        ["git", "rev-parse", "--is-shallow-repository"],
        cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if shallow == "true":
        print("✗ shallow clone — refusing to derive dates from partial history (use fetch-depth: 0)")
        return 2

    # One pass over history: newest-first, so the first time we see a path is
    # its latest touch and the last time is its introduction.
    log = subprocess.run(
        ["git", "log", "--pretty=format:%cI", "--name-only", "--", "agents"],
        cwd=ROOT, capture_output=True, text=True, check=True).stdout

    dates = {}
    stamp = None
    for line in log.splitlines():
        line = line.strip()
        if not line:
            continue
        if line[0].isdigit() and "T" in line:  # a %cI timestamp line
            stamp = line
            continue
        if not line.startswith("agents/") or stamp is None:
            continue
        d = dates.setdefault(line, {"added": stamp, "updated": stamp})
        d["added"] = stamp  # newest-first walk: keep overwriting until the oldest touch wins

    live = {p: d for p, d in dates.items() if (ROOT / p).exists()}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(
        {"schema": "rar-commit-dates/1", "files": live}, indent=1, sort_keys=True) + "\n")
    print(f"✓ {OUT.relative_to(ROOT)} — {len(live)} live agent files dated from git history "
          f"({len(dates) - len(live)} deleted paths dropped)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

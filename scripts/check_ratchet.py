#!/usr/bin/env python3
"""The clutter ratchet: RAR's surface may shrink, never grow, without a ruling.

RAR is the catalog. This check counts the things a visitor (person or AI) has to wade
through before reaching it, and fails when any count is above its limit in
scripts/ratchet.json. Limits only go down:

    python scripts/check_ratchet.py            # check; exit 1 when a count is over its limit
    python scripts/check_ratchet.py --tighten  # after a tidy-up: lower limits to today's counts
    python scripts/check_ratchet.py --json     # the counts, for other tools

Raising a limit means editing scripts/ratchet.json by hand, in a pull request, with the
ruling that allows it written in that entry's "ruling" field. Nothing here raises one.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIMITS = ROOT / "scripts" / "ratchet.json"

WHAT = {
    "root_files": "files at the top level of the repo",
    "root_pages": "web pages at the top level",
    "top_folders": "folders at the top level",
    "entry_kinds": "kinds of thing the registry lists (agents, stacks, ...)",
    "quality_tiers": "quality tiers in use across the registry",
    "categories": "agent categories in use",
}


def tracked(root=ROOT):
    out = subprocess.run(["git", "-C", str(root), "ls-files"], capture_output=True, text=True, check=True).stdout
    return [line for line in out.splitlines() if line]


def measure(files, registry):
    """Counts from a file list and a registry dict. Pure, so tests can feed it anything."""
    root_files = [f for f in files if "/" not in f]
    entries = {k: v for k, v in registry.items() if isinstance(v, list) and v and isinstance(v[0], dict)
               and k not in ("releases",)}
    tiers = {e.get("quality_tier") for v in entries.values() for e in v if e.get("quality_tier")}
    categories = {e.get("category") for e in registry.get("agents", []) if e.get("category")}
    return {
        "root_files": len(root_files),
        "root_pages": len([f for f in root_files if f.endswith(".html")]),
        "top_folders": len({f.split("/", 1)[0] for f in files if "/" in f}),
        "entry_kinds": len(entries),
        "quality_tiers": len(tiers),
        "categories": len(categories),
    }


def compare(counts, limits):
    """(over, under): names whose count is above, or below, its limit."""
    over = {k: (counts[k], limits[k]["limit"]) for k in counts if counts[k] > limits[k]["limit"]}
    under = {k: (counts[k], limits[k]["limit"]) for k in counts if counts[k] < limits[k]["limit"]}
    return over, under


def main(argv):
    counts = measure(tracked(), json.loads((ROOT / "registry.json").read_text()))
    if "--json" in argv:
        print(json.dumps(counts, indent=1))
        return 0
    limits = json.loads(LIMITS.read_text())["limits"]
    over, under = compare(counts, limits)
    if "--tighten" in argv:
        if over:
            print("cannot tighten while over a limit: " + ", ".join(over))
            return 1
        for name, (now, _) in under.items():
            limits[name]["limit"] = now
        data = json.loads(LIMITS.read_text())
        data["limits"] = limits
        LIMITS.write_text(json.dumps(data, indent=1) + "\n")
        print("tightened: " + (", ".join(f"{k} to {v[0]}" for k, v in under.items()) or "nothing to tighten"))
        return 0
    for name, now in counts.items():
        limit = limits[name]["limit"]
        mark = "OVER" if now > limit else ("can tighten" if now < limit else "ok")
        print(f"  {now:>4} of {limit:<4} {WHAT[name]}  [{mark}]")
    if over:
        print("\nRAR grew where it may only shrink: " + ", ".join(f"{k} is {a}, limit {b}" for k, (a, b) in over.items()))
        print("Put the new thing in its own home, or behind an existing page or folder. A limit is raised only by")
        print("Kody's ruling, written in that entry of scripts/ratchet.json.")
        return 1
    if under:
        print("\nSmaller than the limits. Lock it in: python scripts/check_ratchet.py --tighten")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

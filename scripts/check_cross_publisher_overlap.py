#!/usr/bin/env python3
"""Cross-publisher overlap audit — a second opinion alongside
scripts/check_near_duplicates.py, focused specifically on the highest-signal
case: the same capability shipped under two different publisher namespaces.

check_near_duplicates.py is a CI *gate* on new/modified agents, and its
"stack" exemption deliberately waves through large templated batches designed
together under one publisher (see `_stack_dir`). That's correct for its job.
It is not, by itself, a ranked report of the cross-publisher case
specifically — the one a maintainer most wants to see first, because it can
never be an intentional templated-family variant (those only happen within
one publisher's own batch).

This script never merges, deprecates, or edits anything. It only ever prints
a ranked report (and, in CI, opens/updates one tracking issue). Article XXIII
makes deprecation and superseding explicit, deliberate, human acts.

Usage:
  python scripts/check_cross_publisher_overlap.py                  # local catalog.json
  python scripts/check_cross_publisher_overlap.py --source <url>    # any RAR-shaped catalog
  python scripts/check_cross_publisher_overlap.py --min-jaccard 0.6 --top-n 20 --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CATALOG = REPO_ROOT / "api" / "v1" / "catalog.json"

STOPWORDS = {
    "agent", "agents", "the", "a", "an", "and", "or", "of", "for", "to", "in", "with",
    "from", "via", "by", "on", "at", "is", "as", "into", "your", "this", "that", "it",
    "be", "use", "uses", "using", "rapp", "you", "are", "one", "any", "all", "each",
    "when", "then", "than", "not", "can", "its", "their", "them", "they", "these",
    "those", "also", "get", "gets", "return", "returns", "run", "runs", "make",
}


def tokenize(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", (text or "").lower())
            if len(t) > 2 and t not in STOPWORDS}


def signature(agent: dict) -> set[str]:
    """Token set describing what an agent DOES — id (de-slugged), display
    name, and description. Deliberately excludes `tags`: on a registry this
    size, tags are dominated by shared boilerplate within one publisher's own
    batch (e.g. a whole templated family tagged identically), which would make
    everything in that batch look like it overlaps with everything else."""
    text = " ".join([
        (agent.get("id", "") or "").replace("__", " ").replace("_", " "),
        agent.get("display_name", "") or "",
        agent.get("description", "") or "",
    ])
    return tokenize(text)


def load_catalog(source: str | None) -> dict:
    if source:
        req = urllib.request.Request(source, headers={"User-Agent": "rar-overlap-audit"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    return json.loads(DEFAULT_CATALOG.read_text(encoding="utf-8"))


def find_cross_publisher_overlap(
    agents: list[dict],
    min_jaccard: float = 0.5,
    top_n: int = 30,
) -> list[dict]:
    signatures = {a["id"]: signature(a) for a in agents}
    by_id = {a["id"]: a for a in agents}

    inverted: dict[str, set[str]] = {}
    for agent_id, sig in signatures.items():
        for tok in sig:
            inverted.setdefault(tok, set()).add(agent_id)

    universal_cutoff = max(50, len(agents) // 10)
    inverted = {tok: ids for tok, ids in inverted.items() if 2 <= len(ids) <= universal_cutoff}

    shared_counts: dict[tuple[str, str], int] = {}
    for ids in inverted.values():
        ids_sorted = sorted(ids)
        for i in range(len(ids_sorted)):
            for j in range(i + 1, len(ids_sorted)):
                key = (ids_sorted[i], ids_sorted[j])
                shared_counts[key] = shared_counts.get(key, 0) + 1

    MIN_SHARED_TOKENS = 3
    overlaps = []
    for (a_id, b_id), shared in shared_counts.items():
        if shared < MIN_SHARED_TOKENS:
            continue
        a, b = by_id[a_id], by_id[b_id]
        if a.get("publisher") == b.get("publisher"):
            continue  # this script only ever reports the cross-publisher case
        sig_a, sig_b = signatures[a_id], signatures[b_id]
        union = sig_a | sig_b
        jaccard = len(sig_a & sig_b) / len(union) if union else 0.0
        if jaccard >= min_jaccard:
            overlaps.append({
                "jaccard": round(jaccard, 3),
                "agent_a": {"id": a["id"], "name": a.get("name"), "publisher": a.get("publisher")},
                "agent_b": {"id": b["id"], "name": b.get("name"), "publisher": b.get("publisher")},
            })
    overlaps.sort(key=lambda o: -o["jaccard"])
    return overlaps[:top_n]


def format_report(overlaps: list[dict], scanned: int, min_jaccard: float) -> str:
    if not overlaps:
        return f"No cross-publisher overlap found among {scanned} scanned agents (jaccard >= {min_jaccard})."
    lines = [
        f"Found {len(overlaps)} cross-publisher overlap candidate(s) among {scanned} agents "
        f"(jaccard >= {min_jaccard}):",
        "",
    ]
    for o in overlaps:
        lines.append(
            f"- **{o['jaccard']}**  `{o['agent_a']['name']}` ({o['agent_a']['publisher']})  "
            f"⟷  `{o['agent_b']['name']}` ({o['agent_b']['publisher']})"
        )
    lines += [
        "",
        "Nothing was changed. If two of these are genuinely the same capability, the "
        "resolution is a human one — declare it in the newer agent's `__manifest__` "
        "(`\"supersedes\": [...]`) or `distinct_from` if it's deliberate, per "
        "CONSTITUTION.md Article XXIII.",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", help="URL to fetch a catalog.json from (default: local api/v1/catalog.json)")
    parser.add_argument("--min-jaccard", type=float, default=0.5)
    parser.add_argument("--top-n", type=int, default=30)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON instead of the text report")
    args = parser.parse_args()

    try:
        catalog = load_catalog(args.source)
    except (OSError, urllib.error.URLError, json.JSONDecodeError) as e:
        print(f"Could not load catalog: {e}", file=sys.stderr)
        return 2

    agents = catalog.get("agents", [])
    overlaps = find_cross_publisher_overlap(agents, args.min_jaccard, args.top_n)

    if args.json:
        print(json.dumps({
            "scanned": len(agents),
            "min_jaccard": args.min_jaccard,
            "overlap_found": len(overlaps),
            "overlaps": overlaps,
        }, indent=2))
    else:
        print(format_report(overlaps, len(agents), args.min_jaccard))

    return 0  # report-only; never fails CI


if __name__ == "__main__":
    sys.exit(main())

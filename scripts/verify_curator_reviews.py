#!/usr/bin/env python3
"""Verify durable and exported curator reviews stay in sync and 4-5 stars."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / "rappterpedia" / "rappterpedia_state.json"
EXPORT_FILE = ROOT / "state" / "curator_reviews.json"


def rating_distribution(reviews: dict) -> Counter:
    dist = Counter()
    for agent_reviews in reviews.values():
        for review in agent_reviews:
            dist[review.get("rating")] += 1
    return dist


def assert_rating_floor(label: str, reviews: dict) -> None:
    bad = []
    for agent_name, agent_reviews in reviews.items():
        for idx, review in enumerate(agent_reviews):
            rating = review.get("rating")
            if not isinstance(rating, int) or rating < 4 or rating > 5:
                bad.append((agent_name, idx, rating))
    if bad:
        preview = ", ".join(f"{a}[{i}]={r}" for a, i, r in bad[:10])
        raise AssertionError(f"{label} has ratings outside 4-5 stars: {preview}")


def main() -> int:
    state = json.loads(STATE_FILE.read_text())
    export = json.loads(EXPORT_FILE.read_text())
    state_reviews = state.get("reviews", {})
    export_reviews = export.get("agents", {})

    assert_rating_floor("rappterpedia_state.json", state_reviews)
    assert_rating_floor("curator_reviews.json", export_reviews)
    if state_reviews != export_reviews:
        raise AssertionError("state['reviews'] and curator_reviews.json agents do not match")

    print("curator review verification passed")
    print(f"state distribution: {dict(sorted(rating_distribution(state_reviews).items()))}")
    print(f"export distribution: {dict(sorted(rating_distribution(export_reviews).items()))}")
    print(f"agents: {len(state_reviews)} reviews: {sum(len(v) for v in state_reviews.values())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

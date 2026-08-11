#!/usr/bin/env python3
"""build_front_page.py — rank everything RAR knows about into one front page.

Why this exists
---------------
`scripts/crawl_sources.py` states the bet plainly: aggregating agent libraries
is only worth doing if the aggregate answers a question the individual libraries
cannot — *which of these is actually worth your time*. Indexing was step one.
This is the step that pays the bet. It reads every signal RAR already collects
and produces one ranked list, `api/v1/front.json`, with the reasoning attached
to each row so a reader can disagree with it specifically rather than distrust
it generally.

The three rules that shape everything below
-------------------------------------------
1. **Populations are never summed.** RAR's counters (curator reviews, Discussion
   upvotes, quality tier) and a source's counters (its own download numbers)
   measure different populations by different methods. They live in two blocks
   under ``signals`` and are never added into one number, because that number
   would be defensible by neither system. Consequently a score is comparable
   only *within* an origin, and the payload says so out loud.

2. **Absence of signal is not negative signal.** 158 of 279 native agents have
   no curator review and 213 of 216 Discussion threads are silent. Scoring a
   missing component as zero would rank the catalog by who happened to get
   reviewed, then present that as quality. Every missing component is filled
   with the median of the population that *does* have it, and the row says
   "not yet reviewed" in ``why`` so the reader knows the difference between
   "judged average" and "not judged".

3. **Every claim in ``why`` is backed by a number in ``signals``.** The ranking
   is only worth publishing if it can be audited from the payload itself, with
   no access to this file. `tests/test_front_page.py` enforces that mechanically.

Determinism
-----------
No network. No randomness. The freshness clock is the newest timestamp found in
the inputs, not wall time — otherwise two runs a day apart would produce
different ages and `--check` would flap in CI for reasons unrelated to the data.
``generated`` is the only field allowed to differ between two runs.

Usage
-----
    python3 scripts/build_front_page.py             # write api/v1/front.json
    python3 scripts/build_front_page.py --dry-run   # summarise, write nothing
    python3 scripts/build_front_page.py --check     # exit 1 if on disk is stale
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY = REPO_ROOT / "registry.json"
CURATOR = REPO_ROOT / "state" / "curator_reviews.json"
DISCUSSION = REPO_ROOT / "state" / "discussion_ratings.json"
AGGREGATED = REPO_ROOT / "state" / "aggregated.json"
AUDIENCE_MAP = REPO_ROOT / "api" / "v1" / "audience" / "map.json"

OUT_FILE = REPO_ROOT / "api" / "v1" / "front.json"

SCHEMA = "rar-front-page/1.0"

OWNER = "kody-w"
REPO = "RAR"
RAW_BASE = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/main"
PAGES_BASE = f"https://{OWNER}.github.io/{REPO}"

# Every other path in this repository is somebody else's. build_static_api.py
# guards its neighbours the same way; the failure this prevents — a ranking
# build quietly rewriting the catalog an application is reading — is silent and
# expensive, so it is a hard refusal rather than a review convention.
OWNED_PATHS = frozenset({OUT_FILE.resolve()})


# ── tuning constants ────────────────────────────────────────────────────────
#
# Every number here is a judgement call, so each one carries the reason. They
# are module-level and named so a disagreement can be argued about the constant
# rather than reverse-engineered out of an expression.

# Reviews are shrunk toward the population mean by this many phantom reviews.
# One five-star review is an opinion, not a track record; five of them are
# evidence. PRIOR=3 means a single review moves a score a quarter of the way.
CURATOR_PRIOR = 3.0

# Feedback saturates: the difference between 0 and 1 hands-on report is the
# whole story, the difference between 30 and 31 is noise. log1p over this scale
# encodes that. 40 is roughly "as engaged as anything in RAR has ever been".
COMMUNITY_SCALE = 40.0

# Weighted so outcomes outrank intentions. "I shipped this" is worth more than
# "I want to try this"; a reported failure subtracts but can never drive the
# component below zero, because a loud agent with mixed results still beats an
# agent nobody has ever run.
COMMUNITY_WEIGHTS = {
    "shipped": 5.0,
    "regular_use": 4.0,
    "worked": 3.0,
    "saved_time": 3.0,
    "want_to_try": 1.0,
    "did_not_work": -2.0,
    "stuck": -1.0,
}
UPVOTE_WEIGHT = 2.0
COMMENT_WEIGHT = 1.0

# The promotion path in CONSTITUTION.md is frontier -> community -> verified ->
# official. The scale mirrors it. `private` sits with frontier: it is not a
# quality statement, it is an agent the public cannot run.
TIER_SCORE = {
    "official": 1.00,
    "verified": 0.85,
    "community": 0.55,
    "private": 0.30,
    "frontier": 0.30,
}
TIER_DEFAULT = 0.55

# Half-life rather than a cliff, so nothing drops off the page overnight and
# nothing is permanently pinned by having been added first. 120 days is about
# the age of the registry itself: the oldest agent scores half of the newest.
FRESHNESS_HALF_LIFE_DAYS = 120.0

# Depth ramps and then stops. Below the floor an entry has not shown its work;
# above the ceiling more bulk is not more substance. This is the line between
# depth and the "raw file size" the payload declares it does not score.
NATIVE_DEPTH_FLOOR, NATIVE_DEPTH_CEIL = 80.0, 500.0
AGG_DEPTH_FLOOR, AGG_DEPTH_CEIL = 60.0, 400.0
HAS_CARD_SHARE = 0.45
HAS_BUNDLE_SHARE = 0.55

COMPONENTS = [
    ("curator", 0.30, "native",
     "Bayesian-shrunk mean of curator review ratings (1-5). Shrinking toward "
     "the population mean stops a single review outranking a sustained record."),
    ("community", 0.25, "native",
     "RAR's own Discussion signal: upvotes, comments and the seven hands-on "
     "outcome channels, saturating so early engagement counts and volume does "
     "not run away."),
    ("tier", 0.15, "native",
     "Quality tier along the CONSTITUTION promotion path "
     "frontier -> community -> verified -> official."),
    ("freshness", 0.15, "both",
     f"Exponential decay with a {FRESHNESS_HALF_LIFE_DAYS:.0f}-day half-life, "
     "measured against the newest entry in the inputs. Smooth, never a cliff."),
    ("depth", 0.15, "both",
     "Evidence there is something behind the entry — implementation length and "
     "a rendered card for a native agent, a published bundle and a real "
     "description for an aggregated one. Saturates early: bulk is not depth."),
    ("reach", 0.25, "aggregated",
     "The source's own download count, log-normalised WITHIN that source only. "
     "Never compared to, and never added to, any RAR counter."),
]

# Which components apply is a property of the ROW, not of the origin: a native
# agent that was also found in a third-party index carries that source's reach
# in addition to everything RAR knows about it. Every entry from the one source
# crawled so far was materialised into a real agent by the skill toaster, so in
# practice today every row is native and 76 of them also carry reach.
NATIVE_KEYS = ["curator", "community", "tier", "freshness", "depth"]
INDEXED_KEYS = ["freshness", "depth", "reach"]


def applicable_keys(row: dict) -> list[str]:
    """Reach never scores a hosted agent.

    It was briefly folded into the native score for the rows a crawler also
    found upstream, and that was wrong twice over. It made one published number
    out of RAR's counters and a third party's, which the payload's own
    `explain` denies doing. And it was a thin signal sold as a strong one: of
    the 76 crawled entries, 66 publish `downloads: 0` — the source has no
    telemetry for them — so a 25%-weighted component would have been measuring
    10 rows and quietly penalising the other 66 for a number nobody published.

    The source's counters are still carried in `signals.source` and shown on
    the page. They are provenance, not rank.
    """
    if row["origin"] != "native":
        return list(INDEXED_KEYS)
    return list(NATIVE_KEYS)

NOT_SCORED = ["raw file size", "tag count", "anything summed across populations"]

EXPLAIN = (
    "Every entry is scored 0-100 from the signals RAR actually holds. A hosted "
    "agent is scored on curator reviews (30), RAR community feedback (25), "
    "quality tier (15), freshness (15) and depth (15) — those five and nothing "
    "else, whether or not a crawler also found it upstream. An entry that is "
    "indexed but NOT hosted has no reviews, tier or community feedback here, so "
    "it is scored on freshness (15), depth (15) and the source's own reach (25), "
    "renormalised over the components that apply; today that population is empty, "
    "because every crawled entry has been materialised into a hosted agent by the "
    "skill toaster and appears once, as a hosted agent carrying a `source` block. "
    "A source's own counters are shown on those rows and deliberately do NOT "
    "score them: adding RAR's counters to a third party's would produce a number "
    "neither system could defend, and of the 76 crawled entries only 10 publish "
    "any download telemetry at all. A score is therefore comparable only within "
    "its `origin`. What is deliberately NOT scored: raw file size, tag count, "
    "publisher popularity, a source's reach on a hosted agent, and anything "
    "summed across the two populations. A missing component is filled with the "
    "median of the rows that carry it, never with zero — absence of signal is "
    "not negative signal, and every row filled this way says so in `why`."
)


# ── helpers ─────────────────────────────────────────────────────────────────


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_ts(raw) -> datetime | None:
    """ISO-8601 in, aware UTC out. Both input files spell it differently:
    registry carries a local offset, the crawled source carries a 'Z'."""
    if not isinstance(raw, str) or not raw.strip():
        return None
    try:
        dt = datetime.fromisoformat(raw.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def ramp(value: float, floor: float, ceil: float) -> float:
    """Linear between floor and ceil, flat outside. The flat top is the point."""
    if value <= floor:
        return 0.0
    if value >= ceil:
        return 1.0
    return (value - floor) / (ceil - floor)


def saturate(value: float, scale: float) -> float:
    """Diminishing returns on a count. 0 -> 0, `scale` -> 1, above -> 1."""
    if value <= 0:
        return 0.0
    return min(1.0, math.log1p(value) / math.log1p(scale))


def plural(n: int, word: str) -> str:
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def normalize_ref(ref: str) -> str:
    """Slug spellings drifted before the dash ban landed, so the review store
    holds both `@ns/building-permit-processing` and `@ns/building_permit_processing`
    for the same agent. Normalise the slug only — publisher namespaces legitimately
    contain dashes (`@aibast-agents-library`) and flattening those merges publishers."""
    if "/" not in ref:
        return ref
    publisher, slug = ref.split("/", 1)
    return f"{publisher}/{slug.replace('-', '_')}"


# ── input reduction ─────────────────────────────────────────────────────────


def curator_index(raw: dict) -> dict[str, list[dict]]:
    """ref -> reviews, with both slug spellings merged under the canonical ref.

    Merging is additive rather than first-wins: the two spellings hold different
    reviews from different passes of the review engine, so picking one silently
    discards real ratings. Identical reviews recorded under both spellings are
    collapsed on their natural key.
    """
    merged: dict[str, dict[tuple, dict]] = {}
    for ref, reviews in (raw.get("agents") or {}).items():
        if not isinstance(reviews, list):
            continue
        bucket = merged.setdefault(normalize_ref(ref), {})
        for review in reviews:
            if not isinstance(review, dict):
                continue
            if not isinstance(review.get("rating"), (int, float)):
                continue
            key = (review.get("timestamp", ""), review.get("user", ""),
                   review.get("angle", ""), review.get("text", ""))
            bucket.setdefault(key, review)
    return {ref: [b[k] for k in sorted(b)] for ref, b in merged.items()}


def discussion_index(raw: dict) -> dict[str, dict]:
    return {normalize_ref(ref): row
            for ref, row in (raw.get("agents") or {}).items()
            if isinstance(row, dict)}


def audience_index(raw: dict) -> dict[str, str]:
    legend = {"b": "business", "c": "consumer", "x": "both"}
    return {ref: legend.get(code, None)
            for ref, code in (raw.get("map") or {}).items()}


# ── component measurement ───────────────────────────────────────────────────
#
# Each measurement returns None when the signal is genuinely absent, so the
# median fill below can tell "scored zero" apart from "never measured". That
# distinction is the whole of ranking rule 2.


def measure_curator(reviews: list[dict], population_mean: float):
    ratings = [float(r["rating"]) for r in reviews]
    if not ratings:
        return None, {"curator_mean": None, "curator_n": 0}
    mean = sum(ratings) / len(ratings)
    shrunk = ((CURATOR_PRIOR * population_mean + len(ratings) * mean)
              / (CURATOR_PRIOR + len(ratings)))
    sub = min(1.0, max(0.0, (shrunk - 1.0) / 4.0))
    return sub, {"curator_mean": round(mean, 2), "curator_n": len(ratings)}


def measure_community(row: dict | None):
    if row is None:
        return None, {"upvotes": 0, "comments": 0, "engagement": 0, "channels": {}}
    channels = {k: int(v) for k, v in (row.get("signals") or {}).items()
                if isinstance(v, (int, float))}
    upvotes = int(row.get("upvotes") or 0)
    comments = int(row.get("comments") or 0)
    value = upvotes * UPVOTE_WEIGHT + comments * COMMENT_WEIGHT
    for channel, count in channels.items():
        value += COMMUNITY_WEIGHTS.get(channel, 0.0) * count
    facts = {
        "upvotes": upvotes,
        "comments": comments,
        # Total reports across the seven hands-on channels. Reported as a count,
        # never blended with the source block's numbers.
        "engagement": sum(channels.values()),
        # The per-channel breakdown only when there is something to break down.
        # 355 copies of seven zeros is 60KB of a payload a landing page fetches
        # on first paint, and `engagement: 0` already says the same thing.
        "channels": dict(sorted(channels.items())) if any(channels.values()) else {},
    }
    return saturate(max(value, 0.0), COMMUNITY_SCALE), facts


def measure_freshness(added: datetime | None, reference: datetime):
    if added is None:
        return None, None
    age_days = max(0.0, (reference - added).total_seconds() / 86400.0)
    return 2.0 ** (-age_days / FRESHNESS_HALF_LIFE_DAYS), int(round(age_days))


def measure_native_depth(lines: int, has_card: bool) -> float:
    return ((1.0 - HAS_CARD_SHARE) * ramp(float(lines), NATIVE_DEPTH_FLOOR,
                                          NATIVE_DEPTH_CEIL)
            + HAS_CARD_SHARE * (1.0 if has_card else 0.0))


def measure_aggregated_depth(entry_chars: int, has_bundle: bool) -> float:
    return ((1.0 - HAS_BUNDLE_SHARE) * ramp(float(entry_chars), AGG_DEPTH_FLOOR,
                                            AGG_DEPTH_CEIL)
            + HAS_BUNDLE_SHARE * (1.0 if has_bundle else 0.0))


def measure_reach(downloads, source_max: float):
    """Normalised within one source and one source only. Two sources counting
    downloads differently is the norm, not the exception, so a cross-source
    comparison here would be an invented number."""
    if downloads is None:
        return None
    if source_max <= 0:
        return 0.0
    return min(1.0, math.log1p(float(downloads)) / math.log1p(source_max))


# ── why[] ───────────────────────────────────────────────────────────────────
#
# Every string here is generated from a value that is also written into
# `signals`, and the test suite re-derives each one from the payload alone. A
# `why` the payload cannot justify is a bug, not a wording choice.


def native_why(rar: dict, filled: set[str]) -> list[str]:
    why: list[str] = []

    if rar["curator_n"]:
        why.append(f"{rar['curator_mean']:g}/5 from "
                   f"{plural(rar['curator_n'], 'curator review')}")
    else:
        why.append("not yet reviewed - scored at the population median")

    if rar["upvotes"]:
        why.append(plural(rar["upvotes"], "upvote"))
    if rar["comments"]:
        why.append(plural(rar["comments"], "comment"))
    if rar["engagement"]:
        why.append(plural(rar["engagement"], "hands-on report"))
    if not (rar["upvotes"] or rar["comments"] or rar["engagement"]):
        why.append("no community feedback yet - scored at the population median"
                   if "community" in filled else "no community feedback yet")

    why.append(f"{rar['tier']} tier")

    if rar["age_days"] is None:
        why.append("no recorded add date - scored at the population median")
    elif rar["age_days"] == 0:
        why.append("newest in the registry")
    else:
        why.append(f"added {plural(rar['age_days'], 'day')} ago")

    why.append(plural(rar["lines"], "line"))
    if rar["has_card"]:
        why.append("has a rendered card")
    return why


def aggregated_why(src: dict) -> list[str]:
    why: list[str] = []

    if src["downloads"] is None:
        why.append("no download count published at the source "
                   "- scored at the population median")
    elif src["downloads"]:
        why.append(f"{plural(src['downloads'], 'download')} at the source")
    else:
        why.append("no downloads reported at the source")

    if src["published_age_days"] is None:
        why.append("no publish date at the source - scored at the population median")
    elif src["published_age_days"] == 0:
        why.append("newest at the source")
    else:
        why.append(f"published {plural(src['published_age_days'], 'day')} ago")

    if src["has_bundle"]:
        why.append("ships a bundle at the source")
    why.append(f"{plural(src['entry_chars'], 'character')} of catalog description")
    return why


# ── build ───────────────────────────────────────────────────────────────────


def build() -> dict:
    registry = load(REGISTRY)
    agents = registry.get("agents") or []
    if not agents:
        raise SystemExit("registry.json contains no agents; run build_registry.py")

    curators = curator_index(load(CURATOR)) if CURATOR.exists() else {}
    discussions = discussion_index(load(DISCUSSION)) if DISCUSSION.exists() else {}
    audiences = audience_index(load(AUDIENCE_MAP)) if AUDIENCE_MAP.exists() else {}
    aggregated = load(AGGREGATED) if AGGREGATED.exists() else {"items": [], "sources": []}
    agg_items = aggregated.get("items") or []
    agg_sources = {s["id"]: s for s in (aggregated.get("sources") or [])}

    # One clock for the whole build, taken from the data rather than the wall,
    # so `--check` compares content and not the moment it ran.
    stamps = [parse_ts(a.get("_added_at")) for a in agents]
    stamps += [parse_ts(i.get("created_at")) for i in agg_items]
    known = [s for s in stamps if s is not None]
    reference = max(known) if known else datetime.now(timezone.utc)

    # Population mean of curator ratings, for the shrink prior. Computed over
    # reviewed agents only — the whole point is to have something to shrink to.
    rated = [float(r["rating"]) for reviews in curators.values() for r in reviews]
    population_mean = sum(rated) / len(rated) if rated else 3.0

    # Per-source download ceiling. Reach is normalised inside this bracket and
    # never across it.
    source_max: dict[str, float] = {}
    for item in agg_items:
        dl = (item.get("source_signal") or {}).get("downloads")
        if isinstance(dl, (int, float)):
            sid = item.get("source_id", "")
            source_max[sid] = max(source_max.get(sid, 0.0), float(dl))

    # A ref can appear in BOTH registry.json and state/aggregated.json: the skill
    # toaster materialises aggregated entries into real single-file agents, so the
    # index row and the hosted agent are the same capability. Emitting both would
    # show every one of them twice and claim a catalog nearly a third larger than
    # it is. The hosted agent is canonical; the index row becomes its provenance.
    agg_by_ref = {i.get("ref", ""): i for i in agg_items}
    emitted: set[str] = set()

    rows: list[dict] = []

    # ── native agents
    for agent in agents:
        ref = agent.get("name", "")
        rar_sub, curator_facts = measure_curator(curators.get(ref, []), population_mean)
        comm_sub, comm_facts = measure_community(discussions.get(ref))
        added = parse_ts(agent.get("_added_at"))
        fresh_sub, age_days = measure_freshness(added, reference)
        lines = int(agent.get("_lines") or 0)
        has_card = bool(agent.get("_has_card"))
        tier = str(agent.get("quality_tier") or "community")
        path = agent.get("_file", "")

        rows.append({
            "origin": "native",
            "ref": ref,
            "title": agent.get("display_name") or ref.split("/")[-1],
            "description": agent.get("description", ""),
            "category": agent.get("category", ""),
            "tags": list(agent.get("tags") or []),
            "audience": audiences.get(ref),
            "url": f"{PAGES_BASE}/#agent/{urllib.parse.quote(ref, safe='')}",
            "install": f"{RAW_BASE}/{path}" if path else None,
            "source": None,
            "raw": {"curator": rar_sub, "community": comm_sub,
                    "tier": TIER_SCORE.get(tier, TIER_DEFAULT),
                    "freshness": fresh_sub,
                    "depth": measure_native_depth(lines, has_card)},
            "signals": {
                "rar": {
                    "curator_mean": curator_facts["curator_mean"],
                    "curator_n": curator_facts["curator_n"],
                    "upvotes": comm_facts["upvotes"],
                    "comments": comm_facts["comments"],
                    "engagement": comm_facts["engagement"],
                    "channels": comm_facts["channels"],
                    "tier": tier,
                    "age_days": age_days,
                    "lines": lines,
                    "has_card": has_card,
                },
                "source": None,
            },
        })

        emitted.add(ref)

        # Provenance merge. The source's numbers stay in their OWN block and are
        # never added to RAR's — they count a different population by a different
        # method. Reach becomes one more weighted component, labelled as the
        # source's in `why`, which is a composite score and not a merged count.
        twin = agg_by_ref.get(ref)
        if twin is not None:
            tmeta = agg_sources.get(twin.get("source_id", ""), {})
            tsig = twin.get("source_signal") or {}
            tdesc = twin.get("description", "") or ""
            trow = rows[-1]
            trow["source"] = {
                "id": twin.get("source_id", ""),
                "display_name": tmeta.get("display_name", twin.get("source_id", "")),
                "home_url": tmeta.get("home_url", ""),
                "license": tmeta.get("license", "unverified"),
                "url": twin.get("url", ""),
            }
            trow["signals"]["source"] = {
                "id": twin.get("source_id", ""),
                "display_name": tmeta.get("display_name", twin.get("source_id", "")),
                "downloads": tsig.get("downloads"),
                "rating": tsig.get("rating"),
                "featured": bool(tsig.get("featured")),
                "has_bundle": bool(twin.get("has_bundle")),
                "author": twin.get("author", ""),
                "entry_chars": len(tdesc),
                "published_age_days": measure_freshness(
                    parse_ts(twin.get("created_at")), reference)[1],
            }

    # ── aggregated entries
    for item in agg_items:
        ref = item.get("ref", "")
        sid = item.get("source_id", "")
        meta = agg_sources.get(sid, {})
        signal = item.get("source_signal") or {}
        downloads = signal.get("downloads") if isinstance(
            signal.get("downloads"), (int, float)) else None
        created = parse_ts(item.get("created_at"))
        fresh_sub, age_days = measure_freshness(created, reference)
        description = item.get("description", "") or ""
        has_bundle = bool(item.get("has_bundle"))
        # RAR-side counters for an indexed ref exist because aggregated entries
        # get the same Discussion machinery as native agents. They are reported
        # for transparency and never scored: `community` applies to native only,
        # and mixing the two blocks is the one thing this file may not do.
        _, comm_facts = measure_community(discussions.get(ref))

        if ref in emitted:
            continue

        rows.append({
            "origin": "aggregated",
            "ref": ref,
            "title": item.get("name") or ref.split("/")[-1],
            "description": description,
            "category": item.get("kind") or "",
            "tags": list(item.get("tags") or []),
            "audience": audiences.get(ref),
            # Index-only doctrine: a human goes to the origin, and RAR offers
            # nothing to install for an entry it does not host.
            "url": item.get("url") or meta.get("home_url", ""),
            "install": None,
            "source": {
                "id": sid,
                "display_name": meta.get("display_name", sid),
                "home_url": meta.get("home_url", ""),
                "license": meta.get("license", "unverified"),
            },
            "raw": {"freshness": fresh_sub,
                    "depth": measure_aggregated_depth(len(description), has_bundle),
                    "reach": measure_reach(downloads, source_max.get(sid, 0.0))},
            "signals": {
                "rar": {
                    "curator_mean": None,
                    "curator_n": 0,
                    "upvotes": comm_facts["upvotes"],
                    "comments": comm_facts["comments"],
                    "engagement": comm_facts["engagement"],
                    "channels": comm_facts["channels"],
                    "tier": None,
                    "age_days": None,
                    "lines": None,
                    "has_card": False,
                },
                "source": {
                    "id": sid,
                    "downloads": downloads,
                    "rating": signal.get("rating"),
                    "featured": bool(signal.get("featured")),
                    "has_bundle": has_bundle,
                    "author": item.get("author", ""),
                    "entry_chars": len(description),
                    "published_age_days": age_days,
                },
            },
        })

    # ── median fill, per origin
    #
    # Taken over the rows that actually carry the component, so an unreviewed
    # agent lands where the reviewed population sits rather than at the bottom.
    medians: dict[str, float] = {}
    for _key, _w, _applies, _desc in COMPONENTS:
        observed = [r["raw"][_key] for r in rows if r["raw"].get(_key) is not None]
        medians[_key] = statistics.median(observed) if observed else 0.5

    weights = {key: w for key, w, _, _ in COMPONENTS}
    for row in rows:
        keys = applicable_keys(row)
        filled = {k for k in keys if row["raw"].get(k) is None}
        parts = {k: (row["raw"][k] if k not in filled else medians[k]) for k in keys}
        denominator = sum(weights[k] for k in keys)
        row["score"] = round(
            100.0 * sum(weights[k] * parts[k] for k in keys) / denominator, 1)
        row["components"] = {k: round(parts[k], 4) for k in sorted(keys)}
        row["filled"] = sorted(filled)
        row["applies"] = sorted(keys)

        if row["origin"] == "native":
            why = native_why(row["signals"]["rar"], filled)
            row["why"] = why
        else:
            row["why"] = aggregated_why(row["signals"]["source"])

    # A score is comparable only inside its own origin (see `explain`), so a single
    # global sort by raw score would not be a legitimate ordering — it would let
    # whichever origin has the more generous signal distribution occupy the entire
    # top of the page. Rank on each row's percentile WITHIN its origin, which is a
    # like-for-like claim, and break ties on score then ref so runs are identical.
    by_origin: dict[str, list[dict]] = {}
    for row in rows:
        by_origin.setdefault(row["origin"], []).append(row)
    for group in by_origin.values():
        group.sort(key=lambda r: (-r["score"], r["ref"]))
        size = len(group)
        for index, row in enumerate(group):
            row["origin_rank"] = index + 1
            row["origin_size"] = size
            row["origin_percentile"] = round(1.0 - index / size, 6) if size else 0.0
    rows.sort(key=lambda r: (-r["origin_percentile"], -r["score"], r["ref"]))

    items = []
    for position, row in enumerate(rows, start=1):
        items.append({
            "rank": position,
            "ref": row["ref"],
            "title": row["title"],
            "description": row["description"],
            "origin": row["origin"],
            "category": row["category"],
            "tags": row["tags"],
            "audience": row["audience"],
            "url": row["url"],
            "install": row["install"],
            "source": row["source"],
            "score": row["score"],
            "origin_rank": row["origin_rank"],
            "origin_size": row["origin_size"],
            "components": row["components"],
            "scores_on": row["applies"],
            "scored_at_median": row["filled"],
            "signals": row["signals"],
            "why": row["why"],
        })

    native_count = sum(1 for r in rows if r["origin"] == "native")
    agg_count = len(rows) - native_count
    # How many hosted agents also carry a third-party index row as provenance.
    merged_count = sum(1 for r in rows
                       if r["origin"] == "native" and r["source"] is not None)

    return {
        "schema": SCHEMA,
        "generated": now_iso(),
        "counts": {
            "native": native_count,
            "aggregated": agg_count,
            "with_source_provenance": merged_count,
            "ranked": len(items),
            "sources": len(agg_sources),
        },
        "policy": (
            "index-only for aggregated entries: catalog metadata and a link "
            "home, never a copy of the content"
        ),
        "ranking": {
            "explain": EXPLAIN,
            "components": [
                {"key": key, "weight": weight, "applies_to": applies,
                 "description": description}
                for key, weight, applies, description in COMPONENTS
            ],
            "not_scored": NOT_SCORED,
            "median_fill": (
                "A component with no signal is filled with the median of every "
                "row that does carry it, and the row lists that component in "
                "`scored_at_median`. Absence of signal is not negative signal."
            ),
            "order": (
                "Rows are ordered by `origin_percentile` — position within their "
                "own origin — not by raw score, because a score is only "
                "comparable inside its origin. Sorting the raw numbers globally "
                "would hand the whole top of the page to whichever origin has "
                "the more generous signal distribution."
            ),
            "deduplication": (
                "A ref found in both the registry and a crawled index is ONE row. "
                "The skill toaster materialises index entries into real hosted "
                "agents, so the hosted agent is canonical and the index row "
                "becomes its provenance: `source` is populated and the source's "
                "own counters ride in `signals.source`, never added to RAR's."
            ),
            "clock": (
                "Ages are measured from the newest timestamp in the inputs "
                f"({reference.strftime('%Y-%m-%dT%H:%M:%SZ')}), not from build "
                "time, so the same inputs always produce the same ages."
            ),
            "medians": {k: round(v, 4) for k, v in sorted(medians.items())},
        },
        "items": items,
    }


def write(payload: dict) -> int:
    resolved = OUT_FILE.resolve()
    if resolved not in OWNED_PATHS:
        raise RuntimeError(f"refusing to write {OUT_FILE} — not an owned path")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUT_FILE.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False, sort_keys=False)
        fh.write("\n")
    return OUT_FILE.stat().st_size


def comparable(payload: dict) -> str:
    """Everything but the build stamp, canonically ordered. This is what
    `--check` compares, because `generated` is expected to differ and nothing
    else is."""
    body = {k: v for k, v in payload.items() if k != "generated"}
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def summarise(payload: dict) -> None:
    counts = payload["counts"]
    print(f"[front-page] {counts['ranked']} ranked "
          f"({counts['native']} native + {counts['aggregated']} aggregated "
          f"across {counts['sources']} source(s))")
    for item in payload["items"][:10]:
        print(f"  {item['rank']:>3}. {item['score']:>5.1f}  "
              f"[{item['origin'][:4]}] {item['ref']}")
        print(f"       {'; '.join(item['why'][:4])}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--dry-run", action="store_true",
                        help="print a summary, write nothing")
    parser.add_argument("--check", action="store_true",
                        help="exit non-zero if the file on disk is stale")
    args = parser.parse_args()

    for path in (REGISTRY, AGGREGATED):
        if not path.exists():
            print(f"[front-page] {path.relative_to(REPO_ROOT)} missing", file=sys.stderr)
            return 1

    payload = build()

    if args.check:
        if not OUT_FILE.exists():
            print(f"[front-page] {OUT_FILE.relative_to(REPO_ROOT)} has never been "
                  "built. Run: python3 scripts/build_front_page.py", file=sys.stderr)
            return 1
        try:
            on_disk = load(OUT_FILE)
        except ValueError as exc:
            print(f"[front-page] {OUT_FILE.relative_to(REPO_ROOT)} is not valid "
                  f"JSON ({exc})", file=sys.stderr)
            return 1
        if comparable(on_disk) != comparable(payload):
            print(f"[front-page] {OUT_FILE.relative_to(REPO_ROOT)} is stale — the "
                  "ranking on disk no longer matches its inputs. "
                  "Run: python3 scripts/build_front_page.py", file=sys.stderr)
            return 1
        print(f"[front-page] {OUT_FILE.relative_to(REPO_ROOT)} is current "
              f"({payload['counts']['ranked']} ranked).")
        return 0

    summarise(payload)
    if args.dry_run:
        print("[front-page] dry run; nothing written.")
        return 0

    size = write(payload)
    print(f"[front-page] wrote {OUT_FILE.relative_to(REPO_ROOT)} "
          f"({size / 1024:.1f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

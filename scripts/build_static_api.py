#!/usr/bin/env python3
"""
build_static_api.py — the headless RAR API.

RAR is consumed by applications, not by people browsing a repo. AIdeate, the
vBrainstem and the global grail brainstem all ingest RAR the same way: plain
GETs against raw.githubusercontent.com. No backend, no auth, no SDK, no
GitHub account, no GitHub UI. A business user never sees a repository.

That constraint drives every choice here:

  * Every endpoint is a static JSON file committed to main, so it is
    CORS-open, CDN-cached, pinnable to a SHA, and free to serve.
  * Endpoints are additive. This script never writes to an existing path.
    api/v1/index.json, api/v1/agent/** and api/v1/sprite/** belong to
    build_pokedex_api.py and are left strictly alone.
  * The catalog is curated before it is served. A host application asking
    for the business slice must not receive trading-card or game agents.
  * Recommendations are precomputed. "Describe your use case, get an
    agent back" has to work against a static file, so the ranking index
    ships with the data.

Written surface (all new paths):

    manifest.json                  rapp-static-api/1.0 descriptor
    api/v1/status.json             counts + content hashes
    api/v1/badge.json              shields.io endpoint
    api/v1/catalog.json            every agent, lean records
    api/v1/taxonomy.json           categories, publishers, tags
    api/v1/match.json              use-case → ranked agents + term index
    api/v1/audience/business.json  curated enterprise slice
    api/v1/audience/consumer.json  curated consumer slice
    api/v1/audience/map.json       compact per-agent verdict for UI filtering

Usage:
    python scripts/build_static_api.py
    python scripts/build_static_api.py --check   # verify, write nothing
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY = REPO_ROOT / "registry.json"
API_DIR = REPO_ROOT / "api" / "v1"
AUDIENCE_DIR = API_DIR / "audience"
MANIFEST = REPO_ROOT / "manifest.json"

OWNER = "kody-w"
REPO = "RAR"
RAW_BASE = f"https://raw.githubusercontent.com/{OWNER}/{REPO}/main"
CDN_BASE = f"https://cdn.jsdelivr.net/gh/{OWNER}/{REPO}@main"
PAGES_BASE = f"https://{OWNER}.github.io/{REPO}"

# Paths this script owns. Anything not listed here is never written.
OWNED_PATHS = [
    MANIFEST,
    API_DIR / "status.json",
    API_DIR / "badge.json",
    API_DIR / "catalog.json",
    API_DIR / "taxonomy.json",
    API_DIR / "match.json",
    AUDIENCE_DIR / "business.json",
    AUDIENCE_DIR / "consumer.json",
    AUDIENCE_DIR / "map.json",
]

# Paths owned by build_pokedex_api.py. Guarded so a future edit here cannot
# quietly clobber the federation feed the rapp-zoo depends on.
FOREIGN_PATHS = {
    (API_DIR / "index.json").resolve(),
}


# ── audience classification ─────────────────────────────────────────────────
#
# Enterprise buyers were explicit that a curated catalog is a precondition for
# adoption: a host application that surfaces novelty agents next to contract
# analysis loses credibility instantly. Classification is derived purely from
# registry metadata, so no agent file is ever read, parsed, or modified.

CATEGORY_WEIGHTS = {
    "b2b_sales": (4.0, 0.0),
    "b2c_sales": (3.0, 1.0),
    "financial_services": (4.0, 0.0),
    "healthcare": (4.0, 0.0),
    "federal_government": (5.0, 0.0),
    "slg_government": (5.0, 0.0),
    "manufacturing": (4.0, 0.0),
    "retail_cpg": (3.0, 1.0),
    "energy": (4.0, 0.0),
    "professional_services": (4.0, 0.0),
    "human_resources": (4.0, 0.0),
    "it_management": (4.0, 0.0),
    "software_digital_products": (3.0, 0.0),
    "analysis": (2.5, 0.0),
    "integrations": (2.5, 0.0),
    "productivity": (1.5, 1.5),
    "workflow": (2.0, 0.0),
    "general": (0.0, 0.0),
}

# Categories that serve both audiences and are never hidden from either.
#
# 'creative' belongs here, not in the consumer column. Marketing content,
# design systems and agent blueprints are ordinary business work, and scoring
# the category as consumer meant one incidental word could bury them: a
# Microsoft Power Platform blueprint agent was ruled consumer-only because its
# description mentioned an "adaptive card". Let tags and language decide.
NEUTRAL_CATEGORIES = {"core", "meta", "platform", "devtools", "pipeline", "creative"}

BUSINESS_TAGS = {
    "crm", "erp", "sales", "revenue", "pipeline", "forecast", "compliance",
    "governance", "audit", "procurement", "invoice", "contract", "legal",
    "hr", "onboarding", "payroll", "finance", "accounting", "risk",
    "enterprise", "b2b", "dynamics", "salesforce", "sap", "servicenow",
    "workday", "sharepoint", "teams", "outlook", "excel", "powerbi",
    "supply-chain", "logistics", "manufacturing", "healthcare", "clinical",
    "patient", "claims", "underwriting", "kyc", "aml", "regulatory",
    "government", "federal", "public-sector", "rfp", "proposal", "quota",
    "territory", "account", "opportunity", "lead", "churn", "renewal",
}

CONSUMER_TAGS = {
    "game", "games", "gaming", "pokemon", "adventure", "trading-card",
    "holo", "avatar", "pet", "virtual-world",
    "lifeplayer", "loyalty", "shopping", "recipe", "fitness", "travel",
    "music", "art", "meme", "fun", "toy", "collectible", "zoo", "creature",
    "hobby", "personal", "social", "story", "novelty", "entertainment",
}

# Tags that make an agent consumer-facing no matter what category it carries.
# A text adventure filed under devtools is still a game, and an enterprise
# host application surfacing it alongside contract review loses the room.
NOVELTY_TAGS = {
    "game", "games", "gaming", "pokemon", "adventure", "toy", "collectible",
    "trading-card", "meme", "novelty", "creature", "zoo", "entertainment",
}

BUSINESS_WORDS = {
    "customer", "revenue", "deal", "quota", "pipeline", "compliance",
    "invoice", "contract", "procurement", "stakeholder", "enterprise",
    "organization", "employee", "vendor", "supplier", "audit", "regulatory",
    "forecast", "renewal", "churn", "escalation", "sla", "ticket",
    "onboarding", "policy", "governance", "risk", "claims", "underwriting",
}

CONSUMER_WORDS = {
    # Deliberately excludes "card" (adaptive cards, Teams cards, credit cards)
    # and "collect" (data collection) — both read as consumer while appearing
    # constantly in enterprise descriptions.
    "game", "play", "player", "fun", "pet", "avatar",
    "hobby", "recipe", "workout", "vacation", "friend",
    "creature", "battle", "quest", "sticker", "meme",
}

MIN_SIGNAL = 3.0
MIN_MARGIN = 2.0


def norm_tag(tag: str) -> str:
    """Canonicalise a tag so plural and punctuation variants match.

    Publishers write "trading-cards", "trading_card" and "Trading Card" for the
    same idea. Exact set membership missed all but one spelling and let an
    MTG-style card generator through into the enterprise slice -- precisely the
    class of leak this classifier exists to stop. Both the agent's tags and the
    reference sets go through this function, so they always meet in the middle.
    """
    t = tag.strip().lower().replace("_", "-").replace(" ", "-")
    # Don't maim words whose singular already ends in s ("analysis", "process").
    if len(t) > 3 and t.endswith("s") and not t.endswith(("ss", "us", "is", "as")):
        t = t[:-1]
    return t


def norm_tags(tags) -> set[str]:
    return {norm_tag(t) for t in (tags or []) if isinstance(t, str)}


# Normalise the reference sets through the same function as the agent tags,
# so a plural in either place can never cause a miss again.
BUSINESS_TAGS = {norm_tag(t) for t in BUSINESS_TAGS}
CONSUMER_TAGS = {norm_tag(t) for t in CONSUMER_TAGS}
NOVELTY_TAGS = {norm_tag(t) for t in NOVELTY_TAGS}


def classify(agent: dict) -> tuple[str, float, float, list[str]]:
    """Return (audience, business_score, consumer_score, reasons).

    'both' is the safe default: a misclassified agent stays visible in every
    mode rather than disappearing from the catalog. Hiding a useful agent is
    a worse failure than showing a slightly off-target one.
    """
    b = c = 0.0
    why: list[str] = []

    tags = norm_tags(agent.get("tags"))

    # An explicit novelty tag settles it before anything else is considered.
    novelty = tags & NOVELTY_TAGS
    if novelty:
        return "consumer", 0.0, 10.0, [f"novelty tags: {','.join(sorted(novelty))}"]

    category = (agent.get("category") or "").lower()
    if category in NEUTRAL_CATEGORIES:
        # Neutral infrastructure contributes no category signal, but its tags
        # and description are still read — short-circuiting here would let a
        # consumer agent filed under devtools pass as enterprise-appropriate.
        why.append(f"neutral category: {category} (no category signal)")
    else:
        cb, cc = CATEGORY_WEIGHTS.get(category, (0.0, 0.0))
        if cb or cc:
            b += cb
            c += cc
            why.append(f"category {category} (+{cb}b/+{cc}c)")

    hit_b = tags & BUSINESS_TAGS
    hit_c = tags & CONSUMER_TAGS
    if hit_b:
        b += 1.5 * len(hit_b)
        why.append(f"business tags: {','.join(sorted(hit_b))}")
    if hit_c:
        c += 2.0 * len(hit_c)
        why.append(f"consumer tags: {','.join(sorted(hit_c))}")

    blob = f"{agent.get('display_name','')} {agent.get('description','')}".lower()
    words = set(re.findall(r"[a-z]+", blob))
    wb = words & BUSINESS_WORDS
    wc = words & CONSUMER_WORDS
    if wb:
        b += 0.6 * len(wb)
        why.append(f"business language: {','.join(sorted(wb)[:4])}")
    if wc:
        c += 0.8 * len(wc)
        why.append(f"consumer language: {','.join(sorted(wc)[:4])}")

    if max(b, c) < MIN_SIGNAL or abs(b - c) < MIN_MARGIN:
        return "both", round(b, 2), round(c, 2), why or ["insufficient signal"]
    return ("business" if b > c else "consumer"), round(b, 2), round(c, 2), why


# ── record shaping ──────────────────────────────────────────────────────────


def agent_id(name: str) -> str:
    """@publisher/slug → publisher__slug, matching the existing api/v1 shape."""
    return name.lstrip("@").replace("/", "__")


def lean_record(agent: dict, audience: str) -> dict:
    """A record a host application can render without a second fetch.

    Carries provenance inline — sha256 and a resolvable source URL — because
    an unattributed recommendation is not actionable in an enterprise review.
    """
    name = agent.get("name", "")
    rel = agent.get("_file", "")
    return {
        "id": agent_id(name),
        "name": name,
        "display_name": agent.get("display_name", ""),
        "description": agent.get("description", ""),
        "version": agent.get("version", ""),
        "publisher": name.split("/")[0] if "/" in name else "",
        "author": agent.get("author", ""),
        "category": agent.get("category", ""),
        "tags": agent.get("tags", []),
        "quality_tier": agent.get("quality_tier", "community"),
        "audience": audience,
        "requires_env": agent.get("requires_env", []),
        "dependencies": agent.get("dependencies", []),
        "source": {
            "path": rel,
            "raw": f"{RAW_BASE}/{rel}",
            "cdn": f"{CDN_BASE}/{rel}",
            "sha256": agent.get("_sha256", ""),
        },
        "stats": {
            "lines": agent.get("_lines", 0),
            "size_kb": agent.get("_size_kb", 0),
            "added_at": agent.get("_added_at", ""),
        },
    }


# ── use-case matching ───────────────────────────────────────────────────────
#
# The requirement from the field was blunt: a user describes a use case and an
# agent comes back. No browsing, no catalog, no repository. That has to work
# against a static file, so the ranking index is precomputed and shipped.

STOPWORDS = {
    "a", "an", "the", "and", "or", "for", "to", "of", "in", "on", "with",
    "that", "this", "it", "is", "are", "be", "as", "by", "from", "at",
    "agent", "agents", "using", "use", "used", "your", "you", "we", "our",
    "can", "will", "into", "via", "when", "which", "their", "them", "all",
    "any", "based", "each", "one", "more", "other", "than", "then", "they",
}

# Canonical entry points phrased the way a business user states a need,
# not the way the catalog is organised.
USE_CASES = [
    ("sales-pipeline", "Improve sales pipeline and forecasting",
     "sales pipeline forecast revenue deal opportunity quota win probability"),
    ("account-research", "Research an account before a meeting",
     "account intelligence research meeting prep stakeholder briefing customer"),
    ("customer-support", "Resolve customer support tickets faster",
     "support ticket triage escalation resolution service customer issue"),
    ("contract-review", "Review contracts and legal documents",
     "contract legal review clause risk obligation compliance document"),
    ("hr-onboarding", "Onboard and support employees",
     "hr employee onboarding policy benefits payroll people talent"),
    ("finance-ops", "Automate finance and accounting operations",
     "finance invoice accounting reconciliation expense budget payment"),
    ("compliance-audit", "Meet compliance and audit requirements",
     "compliance audit regulatory governance policy control evidence risk"),
    ("supply-chain", "Monitor supply chain and suppliers",
     "supply chain supplier vendor logistics inventory procurement risk"),
    ("healthcare-clinical", "Support clinical and patient workflows",
     "patient clinical healthcare care provider authorization claims medical"),
    ("data-analysis", "Analyse data and generate reports",
     "data analysis report insight dashboard metric summary trend"),
    ("document-processing", "Extract and process documents",
     "document extract parse pdf form intake classify content"),
    ("crm-integration", "Connect to CRM and business systems",
     "crm dynamics salesforce integration connector sync record system"),
    ("marketing-content", "Create marketing and sales content",
     "marketing content campaign email copy proposal pitch messaging"),
    ("it-operations", "Automate IT operations and monitoring",
     "it operations monitoring incident infrastructure deployment alert"),
    ("government-services", "Deliver government and public sector services",
     "government federal public sector citizen agency permit foia"),
    ("manufacturing-ops", "Optimise manufacturing and operations",
     "manufacturing production quality maintenance equipment operations plant"),
    ("retail-commerce", "Run retail and commerce operations",
     "retail store commerce merchandising product order returns customer"),
    ("developer-tooling", "Build, test and ship software",
     "developer code test build deploy repository review engineering"),
    ("meeting-productivity", "Summarise meetings and follow up",
     "meeting notes summary transcript action item follow up agenda"),
    ("knowledge-search", "Search internal knowledge",
     "knowledge search retrieval index question answer documentation wiki"),
]


def tokenize(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9]+", (text or "").lower())
            if len(w) > 2 and w not in STOPWORDS]


def build_match(records: list[dict]) -> dict:
    """Precompute use-case rankings plus a term → agent index for free text."""
    # Per-agent weighted term bag.
    bags: list[Counter] = []
    for rec in records:
        bag = Counter()
        for tok in tokenize(rec["display_name"]):
            bag[tok] += 3
        for tag in rec["tags"]:
            for tok in tokenize(str(tag)):
                bag[tok] += 3
        for tok in tokenize(rec["category"]):
            bag[tok] += 2
        for tok in tokenize(rec["description"]):
            bag[tok] += 1
        bags.append(bag)

    # Document frequency, so common words do not dominate the ranking.
    df = Counter()
    for bag in bags:
        for term in bag:
            df[term] += 1
    total = max(len(records), 1)

    def score(bag: Counter, query_terms: list[str]) -> float:
        s = 0.0
        for qt in query_terms:
            tf = bag.get(qt, 0)
            if tf:
                # Plain idf; the corpus is small enough that smoothing adds nothing.
                s += tf * (1.0 + (total / (1 + df[qt])) ** 0.5)
        return s

    use_cases = []
    for uid, label, query in USE_CASES:
        qterms = tokenize(query)
        scored = []
        for idx, bag in enumerate(bags):
            s = score(bag, qterms)
            if s > 0:
                scored.append((s, idx))
        scored.sort(key=lambda x: (-x[0], records[x[1]]["name"]))
        top = scored[:12]
        use_cases.append({
            "id": uid,
            "label": label,
            "query": query,
            "matches": [
                {
                    "id": records[i]["id"],
                    "name": records[i]["name"],
                    "display_name": records[i]["display_name"],
                    "audience": records[i]["audience"],
                    "score": round(s, 2),
                }
                for s, i in top
            ],
        })

    # Inverted index for free-text queries the host application composes itself.
    # Capped per term so the payload stays small enough to fetch on page load.
    inverted: dict[str, list[str]] = defaultdict(list)
    for idx, bag in enumerate(bags):
        for term, tf in bag.items():
            if df[term] > total * 0.4:  # near-universal term, no discriminating power
                continue
            inverted[term].append(f"{records[idx]['id']}:{tf}")
    trimmed = {
        t: sorted(v, key=lambda e: -int(e.split(":")[1]))[:25]
        for t, v in inverted.items()
        if len(t) > 2
    }

    return {
        "schema": "rar-match/1.0",
        "description": (
            "Precomputed use-case matching. A host application asks the user to "
            "describe a use case, tokenizes it, sums the term weights from "
            "`index`, and returns the top agents — entirely client-side, with no "
            "backend and no GitHub access."
        ),
        "generated": now(),
        "how_to_query": {
            "canonical": "Look up a use_cases[].id for a curated, ranked list.",
            "free_text": (
                "Lowercase the query, split on non-alphanumerics, drop tokens of "
                "2 characters or fewer, then for each token read index[token] "
                "(entries are 'agent_id:weight'). Sum weights per agent_id and "
                "sort descending."
            ),
        },
        "use_cases": use_cases,
        "index": trimmed,
    }


# ── helpers ─────────────────────────────────────────────────────────────────


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha8(payload: dict) -> str:
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:12]


def write(path: Path, payload: dict, dry: bool) -> int:
    resolved = path.resolve()
    if resolved in FOREIGN_PATHS:
        raise RuntimeError(
            f"refusing to write {path} — it is owned by build_pokedex_api.py"
        )
    if dry:
        return len(json.dumps(payload))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    return path.stat().st_size


# ── build ───────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the headless RAR static API.")
    parser.add_argument("--check", action="store_true",
                        help="compute everything but write nothing")
    args = parser.parse_args()

    if not REGISTRY.exists():
        print("registry.json not found — run build_registry.py first", file=sys.stderr)
        return 1

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    agents = registry.get("agents", [])
    if not agents:
        print("registry.json contains no agents", file=sys.stderr)
        return 1

    # Classify and shape.
    records, audience_detail = [], {}
    for agent in agents:
        audience, b, c, why = classify(agent)
        records.append(lean_record(agent, audience))
        audience_detail[agent.get("name", "")] = {
            "audience": audience, "business": b, "consumer": c, "why": why,
        }

    records.sort(key=lambda r: r["name"])
    counts = Counter(r["audience"] for r in records)

    business = [r for r in records if r["audience"] in ("business", "both")]
    consumer = [r for r in records if r["audience"] in ("consumer", "both")]

    # ── taxonomy
    cats = Counter(r["category"] for r in records if r["category"])
    pubs = Counter(r["publisher"] for r in records if r["publisher"])
    tags = Counter(t for r in records for t in r["tags"])
    tiers = Counter(r["quality_tier"] for r in records)

    taxonomy = {
        "schema": "rar-taxonomy/1.0",
        "generated": now(),
        "categories": [{"name": k, "count": v} for k, v in cats.most_common()],
        "publishers": [{"name": k, "count": v} for k, v in pubs.most_common()],
        "quality_tiers": [{"name": k, "count": v} for k, v in tiers.most_common()],
        "tags": [{"name": k, "count": v} for k, v in tags.most_common(300)],
    }

    # ── catalog
    catalog = {
        "schema": "rar-catalog/1.0",
        "description": (
            "Every agent in RAR as a lean record. Fetch this one file to render a "
            "complete browsable catalog with no further requests, no backend, no "
            "authentication and no GitHub account."
        ),
        "generated": now(),
        "count": len(records),
        "self_url": f"{RAW_BASE}/api/v1/catalog.json",
        "agents": records,
    }

    # ── audience slices
    def slice_doc(name: str, rows: list[dict], note: str) -> dict:
        return {
            "schema": "rar-catalog/1.0",
            "audience": name,
            "description": note,
            "generated": now(),
            "count": len(rows),
            "self_url": f"{RAW_BASE}/api/v1/audience/{name}.json",
            "agents": rows,
        }

    business_doc = slice_doc(
        "business", business,
        "Agents appropriate for an enterprise audience. Consumer-only agents "
        "(games, collectibles, novelty) are excluded so a host application can "
        "surface this slice directly without curating it again.",
    )
    consumer_doc = slice_doc(
        "consumer", consumer,
        "Agents appropriate for an individual audience. Enterprise-only agents "
        "are excluded.",
    )

    # A UI that already holds the full registry needs the verdict, not the rows.
    # One ~10KB fetch instead of two ~1MB ones, so segmentation costs a landing
    # page nothing. "both" is the safe default: an unclassified agent shows in
    # every mode rather than disappearing from all of them.
    audience_map = {
        "schema": "rar-audience-map/1.0",
        "description": (
            "Compact audience verdict per agent, for clients that already have "
            "the registry and only need to filter it. b=business, c=consumer, "
            "x=both. Absent means both."
        ),
        "generated": now(),
        "legend": {"b": "business", "c": "consumer", "x": "both"},
        "counts": {
            "business_only": counts.get("business", 0),
            "consumer_only": counts.get("consumer", 0),
            "both": counts.get("both", 0),
            "in_business_mode": len(business),
            "in_consumer_mode": len(consumer),
        },
        "self_url": f"{RAW_BASE}/api/v1/audience/map.json",
        "map": {
            r["name"]: {"business": "b", "consumer": "c", "both": "x"}[r["audience"]]
            for r in records
        },
    }

    match = build_match(records)

    # ── status + badge
    status = {
        "schema": "rar-static-api-status/1.0",
        "generated": now(),
        "summary": {
            "agents": len(records),
            "publishers": len(pubs),
            "categories": len(cats),
            "business": len(business),
            "consumer": len(consumer),
            "use_cases": len(match["use_cases"]),
            "index_terms": len(match["index"]),
        },
        "endpoints": [
            {"name": "catalog", "count": len(records), "sha8": sha8(catalog)},
            {"name": "taxonomy", "count": len(cats), "sha8": sha8(taxonomy)},
            {"name": "match", "count": len(match["use_cases"]), "sha8": sha8(match)},
            {"name": "audience/business", "count": len(business),
             "sha8": sha8(business_doc)},
            {"name": "audience/consumer", "count": len(consumer),
             "sha8": sha8(consumer_doc)},
            {"name": "audience/map", "count": len(audience_map["map"]),
             "sha8": sha8(audience_map)},
        ],
    }

    badge = {
        "schemaVersion": 1,
        "label": "RAR",
        "message": f"{len(records)} agents · {len(pubs)} publishers",
        "color": "brightgreen",
    }

    # ── manifest (rapp-static-apis descriptor)
    manifest = {
        "schema": "rapp-static-api/1.0",
        "name": "rar",
        "title": "RAPP Agent Registry — headless static API",
        "description": (
            "Read-only agent registry served entirely from GitHub raw. No backend, "
            "no authentication, no SDK and no GitHub account. Host applications "
            "such as AIdeate and the vBrainstem fetch these endpoints directly and "
            "render their own experience, so an end user never sees a repository."
        ),
        "raw_base": RAW_BASE,
        "cdn_base": CDN_BASE,
        "pages_base": PAGES_BASE,
        "generated": now(),
        "cors": "open — GitHub raw and jsDelivr both send Access-Control-Allow-Origin: *",
        "auth": "none",
        "stability": (
            "Agent source paths are frozen permanently under CONSTITUTION.md "
            "Article XXIII and verified in CI on every pull request. A URL that "
            "resolves today resolves forever."
        ),
        "endpoints": {
            "manifest": {
                "url": f"{RAW_BASE}/manifest.json",
                "description": "This file. Start here.",
            },
            "catalog": {
                "url": f"{RAW_BASE}/api/v1/catalog.json",
                "description": "Every agent as a lean record. One fetch renders a full catalog.",
            },
            "business": {
                "url": f"{RAW_BASE}/api/v1/audience/business.json",
                "description": "Pre-curated enterprise slice. Safe to surface without further filtering.",
            },
            "consumer": {
                "url": f"{RAW_BASE}/api/v1/audience/consumer.json",
                "description": "Pre-curated individual slice.",
            },
            "audience_map": {
                "url": f"{RAW_BASE}/api/v1/audience/map.json",
                "description": (
                    "Compact audience verdict per agent (b/c/x). For clients "
                    "that already hold the catalog and only need to filter it "
                    "— ~14KB instead of a second full copy."
                ),
            },
            "match": {
                "url": f"{RAW_BASE}/api/v1/match.json",
                "description": "Use-case → ranked agents, plus a term index for free-text queries.",
            },
            "front": {
                "url": f"{RAW_BASE}/api/v1/front.json",
                "description": (
                    "One ranked list over every hosted agent and every indexed "
                    "third-party entry, newest ranking first. Each item carries "
                    "the components it was scored on and a `why` a human can "
                    "read. Built by build_front_page.py, not by this script."
                ),
            },
            "taxonomy": {
                "url": f"{RAW_BASE}/api/v1/taxonomy.json",
                "description": "Categories, publishers, quality tiers and tags with counts.",
            },
            "status": {
                "url": f"{RAW_BASE}/api/v1/status.json",
                "description": "Counts and per-endpoint content hashes for change detection.",
            },
            "badge": {
                "url": f"{RAW_BASE}/api/v1/badge.json",
                "description": "shields.io endpoint descriptor.",
            },
            "agent_source": {
                "url": f"{RAW_BASE}/{{path}}",
                "description": "The agent file itself. `path` comes from an agent record's source.path.",
                "example": f"{RAW_BASE}/agents/@rapp/drift_agent.py",
            },
            "pokedex": {
                "url": f"{RAW_BASE}/api/v1/index.json",
                "description": "Federation feed consumed by the rapp-zoo. Separate shape, maintained by build_pokedex_api.py.",
            },
        },
        "recipes": {
            "render_a_catalog": [
                f"GET {RAW_BASE}/api/v1/audience/business.json",
                "Render agents[] — every record already carries description, tags, tier and provenance.",
            ],
            "recommend_from_a_use_case": [
                f"GET {RAW_BASE}/api/v1/match.json",
                "Tokenize the user's description, sum index[token] weights per agent id, sort descending.",
                "Or read use_cases[] directly for the twenty canonical entry points.",
            ],
            "install_an_agent": [
                "Take source.raw from the agent record.",
                "GET it — the response body is the complete agent. The file is the package.",
                "Optionally verify against source.sha256.",
            ],
        },
    }

    # ── write
    outputs = [
        (MANIFEST, manifest),
        (API_DIR / "catalog.json", catalog),
        (API_DIR / "taxonomy.json", taxonomy),
        (API_DIR / "match.json", match),
        (AUDIENCE_DIR / "business.json", business_doc),
        (AUDIENCE_DIR / "consumer.json", consumer_doc),
        (AUDIENCE_DIR / "map.json", audience_map),
        (API_DIR / "status.json", status),
        (API_DIR / "badge.json", badge),
    ]

    print(f"{'Checking' if args.check else 'Building'} headless static API")
    print(f"  agents     : {len(records)}")
    print(f"  audience   : {counts.get('business', 0)} business / "
          f"{counts.get('consumer', 0)} consumer / {counts.get('both', 0)} both")
    print(f"  slices     : business={len(business)}  consumer={len(consumer)}")
    print(f"  use cases  : {len(match['use_cases'])}, index terms {len(match['index'])}")
    print()
    for path, payload in outputs:
        size = write(path, payload, args.check)
        print(f"  {'would write' if args.check else 'wrote'} "
              f"{path.relative_to(REPO_ROOT).as_posix():<34} {size/1024:7.1f} KB")

    print()
    print("  untouched: api/v1/index.json, api/v1/agent/**, api/v1/sprite/**")
    return 0


if __name__ == "__main__":
    sys.exit(main())

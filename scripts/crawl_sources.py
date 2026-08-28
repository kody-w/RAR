#!/usr/bin/env python3
"""Aggregate third-party agent/skill libraries into one indexed catalog.

Why this exists
---------------
The ecosystem's problem is not a shortage of agent libraries — it is that
every group builds its own, each with a different shape, no shared quality
bar, and no way to tell which entries are any good. Aggregating them is only
worth doing if the aggregate answers a question the individual libraries
cannot: *which of these is actually worth your time.*

So this crawler does two things and refuses a third:

  1. It INDEXES. Catalog metadata only — name, description, tags, author,
     a link back to the origin, and any counts the source itself publishes.
  2. It NORMALIZES. Every source lands in one record shape, under a synthetic
     ``@namespace/slug`` ref that matches RAR's own naming rules, so every
     piece of signal machinery already built for native agents works on
     aggregated entries with no special case.
  3. It NEVER MIRRORS. Skill bodies, bundles and source files are not copied
     into this repository. That is what keeps aggregation on the footing of a
     search index rather than a redistribution — which is the only posture
     that is safe across sources whose licenses differ or, as with the first
     source, cannot even be read.

Signal fusion
-------------
Sources that publish their own engagement numbers (ratings, downloads) get
them carried through as ``source_signal``, kept strictly separate from RAR's
own counters. They are never added together: they count different populations
measured different ways, and silently summing them would invent a number
neither system can defend. The storefront shows both.

Failure posture
---------------
Two callers want opposite things from a bad day upstream, so the choice is the
caller's. ``refresh-ratings.yml`` runs this as one of six snapshot steps: a 404
there must not fail the other five, so the default is to warn, skip the source
and leave the existing catalog untouched. ``aggregate.yml`` runs it as the
whole job and owns the freshness of the result: there a swallowed 404 is
indistinguishable from a quiet week — green run, catalog silently ageing — so
it passes ``--strict`` and any skipped source becomes a non-zero exit. Strict
refuses *before* writing, because a snapshot rebuilt from the sources that
happened to answer is a deletion of the ones that did not.

Usage
-----
    python scripts/crawl_sources.py            # crawl every enabled source
    python scripts/crawl_sources.py --only cat-agent-skills
    python scripts/crawl_sources.py --dry-run  # print, write nothing
    python scripts/crawl_sources.py --strict   # a skipped source fails the run
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
SOURCES_FILE = REPO_ROOT / "sources.json"
OUT_FILE = REPO_ROOT / "state" / "aggregated.json"

SCHEMA = "rar-aggregated/1.0"
USER_AGENT = "rar-aggregator (+https://github.com/kody-w/RAR)"

# RAR's naming rule, applied to foreign slugs so aggregated entries can use
# the same Discussion-thread machinery as native agents. Dashes are forbidden
# everywhere in RAR names, and every slug in the first source uses them.
SLUG_OK = re.compile(r"^[a-z0-9_]+$")


# Every reason a source contributed nothing to this run. Populated by fail()
# and read only by --strict; the default caller never looks at it, so the
# non-fatal posture is unchanged.
FAILURES: list[str] = []


def warn(msg: str) -> None:
    print(f"[crawl-sources] {msg}", file=sys.stderr)


def fail(msg: str) -> None:
    """A warning that also arms --strict.

    Reserved for a source that produced no records at all. A slug collision
    stays a plain warning: it is a handled data quirk, not a source going
    dark, and failing on it would train the operator to ignore the signal.
    """
    FAILURES.append(msg)
    warn(msg)


def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=25) as resp:
        return json.loads(resp.read().decode("utf-8"))


def normalize_slug(raw: str) -> str:
    """Foreign slug -> a RAR-legal slug. Lossy but stable and collision-checked."""
    slug = re.sub(r"[^a-z0-9]+", "_", str(raw).lower()).strip("_")
    return slug or "unnamed"


def clip(text: str, limit: int = 400) -> str:
    text = " ".join(str(text or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def parse_cat_skills(items: list, source: dict) -> list[dict]:
    """Adapter for the ``cat-skills/1`` shape.

    Each source format gets one adapter. Adding a differently-shaped source
    means adding a function here and a `format` entry in sources.json — the
    record shape everything downstream consumes stays fixed.
    """
    ns = source["namespace"]
    tmpl = source.get("item_url_template", "")
    out = []
    for it in items:
        raw_slug = it.get("slug") or it.get("name") or ""
        if not raw_slug:
            continue
        slug = normalize_slug(raw_slug)
        # Source-published engagement. Kept separate from RAR's own counters —
        # different populations, different methods; summing them would be a
        # number neither system could defend.
        signal = {}
        if isinstance(it.get("downloads"), int):
            signal["downloads"] = it["downloads"]
        if isinstance(it.get("rating"), (int, float)) and it.get("rating"):
            signal["rating"] = it["rating"]
        if it.get("featured"):
            signal["featured"] = True

        out.append({
            "ref": f"{ns}/{slug}",
            "source_id": source["id"],
            "source_slug": raw_slug,
            "name": clip(it.get("name") or raw_slug, 120),
            "description": clip(it.get("description")),
            "kind": it.get("type") or "skill",
            "tags": [str(t) for t in (it.get("tags") or [])][:12],
            "platforms": [str(p) for p in (it.get("platforms") or [])][:8],
            "author": clip(it.get("author") or "", 120),
            "author_github": it.get("authorGithub") or None,
            "version": str(it.get("version") or ""),
            "created_at": it.get("createdAt") or None,
            "has_bundle": bool(it.get("hasBundle")),
            "url": tmpl.replace("{slug}", str(raw_slug)) if tmpl else source.get("home_url", ""),
            "source_signal": signal,
        })
    return out


def parse_cowork_cookbook(items: list, source: dict) -> list[dict]:
    """Adapter for Cowork Cookbook's public /data/catalog.json shape."""
    ns = source["namespace"]
    template = source.get("item_url_template", "")
    out = []
    for item in items:
        recipe_id = str(item.get("id") or "").strip()
        if not recipe_id:
            continue
        slug = normalize_slug(recipe_id)
        process_tags = [
            str(value)
            for value in item.get("process_tags") or []
            if str(value).strip()
        ]
        process_roots = sorted({
            value.split("/", 1)[0]
            for value in process_tags
            if value
        })
        recipe_type = str(item.get("recipe_type") or "prompt")
        category = str(item.get("category") or "other")
        difficulty = str(item.get("difficulty") or "")
        plugin = str(item.get("plugin") or "none")
        status = str(item.get("status") or "")
        tags = [
            "industry_solution",
            "business_process",
            normalize_slug(recipe_type),
            normalize_slug(category),
        ]
        tags.extend(normalize_slug(root) for root in process_roots)
        if difficulty:
            tags.append(normalize_slug(difficulty))
        if plugin and plugin != "none":
            tags.extend(["integration", normalize_slug(plugin)])
        if item.get("mutates_data"):
            tags.extend(["mutates_data", "workflow"])
        else:
            tags.append("read_only")
        if category in {"audit", "report"}:
            tags.append("analysis")
        if category in {"scheduled-brief", "teams-update", "bulk-update"}:
            tags.append("automation")

        uses_skills = item.get("uses_skills")
        uses_skills = uses_skills if isinstance(uses_skills, dict) else {}
        out.append({
            "ref": f"{ns}/{slug}",
            "source_id": source["id"],
            "source_slug": recipe_id,
            "name": clip(item.get("title") or recipe_id, 120),
            "description": clip(item.get("summary")),
            "kind": recipe_type,
            "tags": list(dict.fromkeys(tags))[:16],
            "platforms": ["Microsoft 365 Copilot Cowork"],
            "author": source.get("publisher", ""),
            "author_github": "seangalliher",
            "version": str(item.get("version") or "1.0.0"),
            "created_at": item.get("last_verified_on") or None,
            "has_bundle": bool(
                "skill" in recipe_type
                or uses_skills.get("custom")
            ),
            "url": (
                template.replace("{id}", recipe_id)
                if template
                else source.get("home_url", "")
            ),
            "source_signal": {
                "verified": status == "verified",
            },
            "process_tags": process_tags,
            "process_roots": process_roots,
            "recipe_type": recipe_type,
            "difficulty": difficulty,
            "mutates_data": bool(item.get("mutates_data")),
            "deprecated": bool(item.get("deprecated")),
            "verification_status": status,
            "last_verified_on": item.get("last_verified_on"),
            "plugin": plugin,
            "uses_skills": uses_skills,
            "recipe_category": category,
            "upstream_path": item.get("slug"),
        })
    return out


def parse_aibast_registry(items: list, source: dict) -> list[dict]:
    """Adapter for the ``aibast-registry/1`` shape: the AIBAST agents library
    publishes a CI-built ``registry.json`` whose ``agents`` are rapp-agent/1.0
    manifests plus build-time ``_`` fields (file, stack, vertical, sha256).

    Index-only, like every source here: we carry the catalog fields and a link
    back to the upstream file; the agent bodies stay upstream, which is exactly
    the point — RAR used to host copies of these agents and they drifted from
    the source. Now the source IS the record.
    """
    ns = source["namespace"]
    tmpl = source.get("item_url_template", "")
    out = []
    for it in items:
        raw_name = it.get("name") or ""
        raw_slug = raw_name.split("/", 1)[1] if "/" in raw_name else raw_name
        if not raw_slug:
            continue
        slug = normalize_slug(raw_slug)
        upstream_path = it.get("_file") or ""
        signal = {}
        if it.get("quality_tier"):
            signal["quality_tier"] = str(it["quality_tier"])
        if it.get("_synthetic_data"):
            signal["synthetic_data"] = True
        out.append({
            "ref": f"{ns}/{slug}",
            "source_id": source["id"],
            "source_slug": raw_slug,
            "name": clip(it.get("display_name") or raw_slug, 120),
            "description": clip(it.get("description")),
            "kind": "agent",
            "tags": [str(t) for t in (it.get("tags") or [])][:12],
            "platforms": ["rapp-brainstem"],
            "author": clip(it.get("author") or "", 120),
            "author_github": None,
            "version": str(it.get("version") or ""),
            "created_at": None,
            "has_bundle": False,
            "url": tmpl.replace("{path}", upstream_path) if (tmpl and upstream_path) else source.get("home_url", ""),
            "source_signal": signal,
            "category": it.get("category") or "",
            "stack": it.get("_stack") or "",
            "vertical": it.get("_stack_vertical") or "",
            "upstream_path": upstream_path,
            "upstream_sha256": it.get("_sha256") or "",
        })
    return out


ADAPTERS = {
    "cat-skills/1": parse_cat_skills,
    "cowork-cookbook/1": parse_cowork_cookbook,
    "aibast-registry/1": parse_aibast_registry,
}


def crawl_source(source: dict) -> list[dict] | None:
    adapter = ADAPTERS.get(source.get("format", ""))
    if adapter is None:
        fail(f"'{source.get('id')}': unknown format {source.get('format')!r}; skipped.")
        return None
    try:
        payload = fetch_json(source["index_url"])
    except (OSError, ValueError, urllib.error.URLError) as exc:
        fail(f"'{source['id']}': index fetch failed ({exc}); source skipped.")
        return None

    items = payload if isinstance(payload, list) else (
        payload.get("skills")
        or payload.get("items")
        or payload.get("agents")
        or payload.get("recipes")
        or []
    )
    if not isinstance(items, list) or not items:
        fail(f"'{source['id']}': index carried no items; source skipped.")
        return None

    records = adapter(items, source)

    # A slug collision would merge two distinct upstream entries into one ref,
    # and therefore into one feedback thread and one set of counters. Drop the
    # duplicates rather than silently blend two things.
    seen: dict[str, str] = {}
    unique = []
    for r in records:
        if r["ref"] in seen:
            warn(f"'{source['id']}': slug collision on {r['ref']} "
                 f"({seen[r['ref']]} vs {r['source_slug']}); keeping the first.")
            continue
        seen[r["ref"]] = r["source_slug"]
        unique.append(r)
    return unique


def build(only: str | None = None) -> dict | None:
    if not SOURCES_FILE.exists():
        fail("sources.json missing; nothing to crawl.")
        return None
    cfg = json.loads(SOURCES_FILE.read_text(encoding="utf-8"))
    sources = [s for s in cfg.get("sources", []) if s.get("enabled", True)]
    if only:
        sources = [s for s in sources if s.get("id") == only]
    if not sources:
        fail("no enabled sources matched.")
        return None

    out_sources, out_items = [], []
    for src in sources:
        records = crawl_source(src)
        if records is None:
            continue
        out_items.extend(records)
        sig_dl = sum(r["source_signal"].get("downloads", 0) for r in records)
        out_sources.append({
            "id": src["id"],
            "namespace": src["namespace"],
            "display_name": src.get("display_name", src["id"]),
            "publisher": src.get("publisher", ""),
            "home_url": src.get("home_url", ""),
            "index_url": src.get("index_url", ""),
            "taxonomy_url": src.get("taxonomy_url", ""),
            "repository_url": src.get("repository_url", ""),
            # Recorded, never assumed. `license_verified: false` means the
            # licence could not be read — treat as all-rights-reserved, index
            # only, never republish content from it.
            "license": src.get("license", "unverified"),
            "license_url": src.get("license_url", ""),
            "license_verified": bool(src.get("license_verified")),
            "license_note": src.get("license_note", ""),
            "item_count": len(records),
            "source_downloads": sig_dl,
        })
        print(f"[crawl-sources] {src['id']}: {len(records)} item(s), "
              f"{sig_dl} source-reported download(s).")

    if not out_items:
        # Every source answered but the adapters recognised nothing in any of
        # them — an upstream shape change, which looks identical to silence
        # from the outside and has to be nameable by --strict.
        fail("every source produced zero records; nothing to write.")
        return None
    return {
        "schema": SCHEMA,
        "policy": "index-only: catalog metadata and links; content is never copied",
        "sources": out_sources,
        "items": sorted(out_items, key=lambda r: r["ref"]),
        "totals": {
            "sources": len(out_sources),
            "items": len(out_items),
            "source_downloads": sum(s["source_downloads"] for s in out_sources),
        },
    }


def persist(snapshot: dict) -> bool:
    """Never replace a real snapshot with an empty one — a failed crawl must
    not erase the catalog. No timestamp in the body, so the file changes only
    when the data changes and the daily workflow can skip no-op commits."""
    if OUT_FILE.exists():
        try:
            existing = json.loads(OUT_FILE.read_text(encoding="utf-8"))
            if existing.get("items") and not snapshot.get("items"):
                warn("crawl produced nothing; keeping existing snapshot.")
                return False
        except (OSError, ValueError):
            pass
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--only", help="crawl a single source id")
    ap.add_argument("--dry-run", action="store_true", help="print, write nothing")
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero if any source produced no records")
    args = ap.parse_args()

    snapshot = build(args.only)

    # Checked before persist(), not after: a snapshot rebuilt from the sources
    # that happened to answer would drop the failed source's items from the
    # catalog. That is a deletion wearing the costume of a successful crawl.
    if args.strict and FAILURES:
        warn(f"--strict: {len(FAILURES)} source problem(s); nothing written.")
        for problem in FAILURES:
            warn(f"  - {problem}")
        return 1

    if snapshot is None:
        # Non-fatal by design, like every other snapshot step: a bad day
        # upstream leaves the catalog untouched rather than failing the run.
        warn("no snapshot produced; existing state left unchanged.")
        return 0
    if args.dry_run:
        print(json.dumps(snapshot["totals"], indent=2))
        return 0
    if persist(snapshot):
        t = snapshot["totals"]
        print(f"[crawl-sources] wrote {OUT_FILE.relative_to(REPO_ROOT)}: "
              f"{t['items']} item(s) across {t['sources']} source(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

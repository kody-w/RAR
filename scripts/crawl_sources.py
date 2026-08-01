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

Usage
-----
    python scripts/crawl_sources.py            # crawl every enabled source
    python scripts/crawl_sources.py --only cat-agent-skills
    python scripts/crawl_sources.py --dry-run  # print, write nothing
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


def warn(msg: str) -> None:
    print(f"[crawl-sources] {msg}", file=sys.stderr)


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


ADAPTERS = {"cat-skills/1": parse_cat_skills}


def crawl_source(source: dict) -> list[dict] | None:
    adapter = ADAPTERS.get(source.get("format", ""))
    if adapter is None:
        warn(f"'{source.get('id')}': unknown format {source.get('format')!r}; skipped.")
        return None
    try:
        payload = fetch_json(source["index_url"])
    except (OSError, ValueError, urllib.error.URLError) as exc:
        warn(f"'{source['id']}': index fetch failed ({exc}); source skipped.")
        return None

    items = payload if isinstance(payload, list) else (
        payload.get("skills") or payload.get("items") or payload.get("agents") or [])
    if not isinstance(items, list) or not items:
        warn(f"'{source['id']}': index carried no items; source skipped.")
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
        warn("sources.json missing; nothing to crawl.")
        return None
    cfg = json.loads(SOURCES_FILE.read_text(encoding="utf-8"))
    sources = [s for s in cfg.get("sources", []) if s.get("enabled", True)]
    if only:
        sources = [s for s in sources if s.get("id") == only]
    if not sources:
        warn("no enabled sources matched.")
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
            # Recorded, never assumed. `license_verified: false` means the
            # licence could not be read — treat as all-rights-reserved, index
            # only, never republish content from it.
            "license": src.get("license", "unverified"),
            "license_verified": bool(src.get("license_verified")),
            "license_note": src.get("license_note", ""),
            "item_count": len(records),
            "source_downloads": sig_dl,
        })
        print(f"[crawl-sources] {src['id']}: {len(records)} item(s), "
              f"{sig_dl} source-reported download(s).")

    if not out_items:
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
    args = ap.parse_args()

    snapshot = build(args.only)
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

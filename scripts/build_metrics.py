#!/usr/bin/env python3
"""
build_metrics.py — collect public RAR registry metrics into state/metrics.json.

Sources (all public, no auth required except GitHub traffic):
  - registry.json                       agents, publishers, categories, sizes, dates
  - state/votes.json                    up/down votes per agent
  - state/curator_reviews.json          reviews + ratings per agent
  - api.github.com/repos/...            stars, forks, watchers, issues, releases
  - api.github.com/.../traffic/*        clones, views, popular paths/referrers (needs token)
  - data.jsdelivr.com                   CDN download hits, per-file + per-day

GitHub's traffic API only returns a 14-day rolling window, so daily rows are
merged into state/metrics_history.json keyed by date. That turns a rolling
window into an accumulating all-time total.

Usage:
    python scripts/build_metrics.py                 # snapshot everything
    python scripts/build_metrics.py --offline       # local files only, no network
    GITHUB_TOKEN=xxx python scripts/build_metrics.py

Exit code is 0 even when network sources fail — partial metrics are still written.
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry.json"
VOTES = ROOT / "state" / "votes.json"
CURATOR_REVIEWS = ROOT / "state" / "curator_reviews.json"
USER_REVIEWS = ROOT / "state" / "reviews.json"
OUT = ROOT / "state" / "metrics.json"
HISTORY = ROOT / "state" / "metrics_history.json"

OWNER = "kody-w"
REPO = "RAR"
GH_API = "https://api.github.com"
JSDELIVR = "https://data.jsdelivr.com/v1"
USER_AGENT = "RAR-metrics-builder"
TIMEOUT = 30

# jsDelivr paths that are infrastructure, not installable agents
NON_AGENT_FILES = {"/registry.json", "/api.json", "/skill.md", "/peers.json"}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(msg):
    print(msg, file=sys.stderr)


def fetch_json(url, token=None):
    """GET JSON. Returns None on any failure — metrics are best-effort."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        log(f"  ! {e.code} {url}")
    except Exception as e:
        log(f"  ! {type(e).__name__} {url}: {e}")
    return None


def load_json(path, default):
    try:
        return json.loads(path.read_text())
    except Exception:
        return default


def norm(name):
    """Normalize an agent key so dashed and snake_case slugs collapse together."""
    return re.sub(r"[-\s]+", "_", (name or "").strip().lower())


# ---------------------------------------------------------------- local data

def build_agent_index(registry):
    """agent key -> record, plus file path -> key lookup."""
    agents = {}
    by_file = {}
    for a in registry.get("agents", []):
        key = norm(a.get("name"))
        rec = {
            "name": a.get("name"),
            "display_name": a.get("display_name") or a.get("name"),
            "publisher": (a.get("name") or "@unknown/x").split("/")[0],
            "description": a.get("description", ""),
            "category": a.get("category", "general"),
            "tier": a.get("quality_tier", "community"),
            "version": a.get("version", ""),
            "author": a.get("author", ""),
            "tags": a.get("tags", [])[:6],
            "file": a.get("_file", ""),
            "size_kb": a.get("_size_kb", 0),
            "lines": a.get("_lines", 0),
            "added_at": a.get("_added_at", ""),
            "has_card": bool(a.get("_has_card")),
            "downloads": 0,
            "up": 0,
            "down": 0,
            "score": 0,
            "reviews": 0,
            "rating": 0.0,
        }
        agents[key] = rec
        if rec["file"]:
            by_file["/" + rec["file"].lstrip("/")] = key
    return agents, by_file


def apply_votes(agents, votes_doc):
    totals = {"up": 0, "down": 0, "voters": set(), "agents_voted": 0}
    for raw_key, v in (votes_doc.get("agents") or {}).items():
        up, down = int(v.get("up", 0)), int(v.get("down", 0))
        totals["up"] += up
        totals["down"] += down
        totals["voters"].update((v.get("voters") or {}).keys())
        if up or down:
            totals["agents_voted"] += 1
        rec = agents.get(norm(raw_key))
        if rec:
            rec["up"] += up
            rec["down"] += down
            rec["score"] = rec["up"] - rec["down"]
    totals["voters"] = len(totals["voters"])
    return totals


def apply_reviews(agents, curator_doc, user_doc):
    totals = {"reviews": 0, "agents_reviewed": 0, "reviewers": set(), "rating_sum": 0.0, "rated": 0}
    by_angle = defaultdict(int)
    dist = {str(i): 0 for i in range(1, 6)}
    merged = defaultdict(list)

    for doc in (curator_doc, user_doc):
        for raw_key, reviews in (doc.get("agents") or {}).items():
            if isinstance(reviews, list):
                merged[norm(raw_key)].extend(reviews)

    for key, reviews in merged.items():
        ratings = [float(r["rating"]) for r in reviews if isinstance(r.get("rating"), (int, float))]
        totals["reviews"] += len(reviews)
        totals["agents_reviewed"] += 1
        for r in reviews:
            if r.get("user"):
                totals["reviewers"].add(r["user"])
            by_angle[r.get("angle") or "general"] += 1
            rating = r.get("rating")
            if isinstance(rating, (int, float)) and 1 <= rating <= 5:
                dist[str(int(rating))] += 1
        totals["rating_sum"] += sum(ratings)
        totals["rated"] += len(ratings)
        rec = agents.get(key)
        if rec:
            rec["reviews"] = len(reviews)
            rec["rating"] = round(sum(ratings) / len(ratings), 2) if ratings else 0.0

    totals["reviewers"] = len(totals["reviewers"])
    totals["avg_rating"] = round(totals["rating_sum"] / totals["rated"], 2) if totals["rated"] else 0.0
    totals.pop("rating_sum")
    totals["by_angle"] = dict(sorted(by_angle.items(), key=lambda kv: -kv[1]))
    totals["distribution"] = dist
    return totals


# --------------------------------------------------------------- remote data

def fetch_repo(token):
    d = fetch_json(f"{GH_API}/repos/{OWNER}/{REPO}", token)
    if not d:
        return {}
    return {
        "stars": d.get("stargazers_count", 0),
        "forks": d.get("forks_count", 0),
        "watchers": d.get("subscribers_count", 0),
        "open_issues": d.get("open_issues_count", 0),
        "size_kb": d.get("size", 0),
        "created_at": d.get("created_at"),
        "pushed_at": d.get("pushed_at"),
        "description": d.get("description"),
        "homepage": d.get("homepage"),
    }


def fetch_releases(token):
    rels = fetch_json(f"{GH_API}/repos/{OWNER}/{REPO}/releases?per_page=100", token) or []
    out, total = [], 0
    for r in rels:
        dl = sum(a.get("download_count", 0) for a in r.get("assets", []))
        total += dl
        out.append({
            "tag": r.get("tag_name"),
            "name": r.get("name"),
            "published_at": r.get("published_at"),
            "downloads": dl,
            "assets": [{"name": a["name"], "downloads": a.get("download_count", 0), "size": a.get("size", 0)}
                       for a in r.get("assets", [])],
        })
    return {"total_downloads": total, "count": len(out), "releases": out[:10]}


def fetch_traffic(token):
    """Clones + views + popular paths/referrers. Requires push-scoped token."""
    if not token:
        log("  · no token — skipping GitHub traffic")
        return {}
    out = {}
    clones = fetch_json(f"{GH_API}/repos/{OWNER}/{REPO}/traffic/clones", token)
    if clones:
        out["clones"] = {
            "count_14d": clones.get("count", 0),
            "uniques_14d": clones.get("uniques", 0),
            "daily": [{"date": c["timestamp"][:10], "count": c["count"], "uniques": c["uniques"]}
                      for c in clones.get("clones", [])],
        }
    views = fetch_json(f"{GH_API}/repos/{OWNER}/{REPO}/traffic/views", token)
    if views:
        out["views"] = {
            "count_14d": views.get("count", 0),
            "uniques_14d": views.get("uniques", 0),
            "daily": [{"date": v["timestamp"][:10], "count": v["count"], "uniques": v["uniques"]}
                      for v in views.get("views", [])],
        }
    paths = fetch_json(f"{GH_API}/repos/{OWNER}/{REPO}/traffic/popular/paths", token)
    if paths:
        out["paths"] = [{"path": p["path"], "title": p.get("title", ""), "count": p["count"], "uniques": p["uniques"]}
                        for p in paths[:20]]
    refs = fetch_json(f"{GH_API}/repos/{OWNER}/{REPO}/traffic/popular/referrers", token)
    if refs:
        out["referrers"] = [{"referrer": r["referrer"], "count": r["count"], "uniques": r["uniques"]} for r in refs[:12]]
    return out


def fetch_jsdelivr(by_file, agents):
    """CDN hits: totals, daily series, and per-file download counts."""
    out = {"total_hits": 0, "bandwidth": 0, "daily": [], "files": [], "period": "year"}
    pkg = fetch_json(f"{JSDELIVR}/stats/packages/gh/{OWNER}/{REPO}?period=year")
    if pkg:
        out["total_hits"] = pkg.get("hits", {}).get("total", 0)
        out["bandwidth"] = pkg.get("bandwidth", {}).get("total", 0)
        out["rank"] = pkg.get("hits", {}).get("rank")
        dates = pkg.get("hits", {}).get("dates", {}) or {}
        out["daily"] = [{"date": d, "count": c} for d, c in sorted(dates.items()) if c]

    files = fetch_json(f"{JSDELIVR}/stats/packages/gh/{OWNER}/{REPO}@main/files?period=year&limit=100") or []
    rows = []
    for f in files:
        name = f.get("name", "")
        hits = f.get("hits", {}).get("total", 0)
        if not hits:
            continue
        key = by_file.get(name)
        if key and key in agents:
            agents[key]["downloads"] += hits
        rows.append({
            "file": name,
            "hits": hits,
            "agent": agents[key]["name"] if key else None,
            "kind": "agent" if key else ("registry" if name in NON_AGENT_FILES else "asset"),
        })
    rows.sort(key=lambda r: -r["hits"])
    out["files"] = rows[:40]
    out["agent_hits"] = sum(r["hits"] for r in rows if r["kind"] == "agent")
    return out


# ------------------------------------------------------------------ history

def merge_history(traffic, jsd):
    """Accumulate rolling-window daily rows so totals survive the 14-day cutoff."""
    hist = load_json(HISTORY, {"clones": {}, "views": {}, "cdn": {}, "snapshots": []})
    for bucket, rows in (("clones", traffic.get("clones", {}).get("daily", [])),
                         ("views", traffic.get("views", {}).get("daily", []))):
        store = hist.setdefault(bucket, {})
        for row in rows:
            prev = store.get(row["date"], {"count": 0, "uniques": 0})
            store[row["date"]] = {
                "count": max(prev.get("count", 0), row["count"]),
                "uniques": max(prev.get("uniques", 0), row["uniques"]),
            }
    cdn = hist.setdefault("cdn", {})
    for row in jsd.get("daily", []):
        cdn[row["date"]] = max(cdn.get(row["date"], 0), row["count"])

    totals = {
        "clones_all_time": sum(v["count"] for v in hist["clones"].values()),
        "clone_uniques_all_time": sum(v["uniques"] for v in hist["clones"].values()),
        "views_all_time": sum(v["count"] for v in hist["views"].values()),
        "view_uniques_all_time": sum(v["uniques"] for v in hist["views"].values()),
        "cdn_all_time": sum(hist["cdn"].values()),
        "days_tracked": len(hist["clones"]),
        "first_day": min(hist["clones"]) if hist["clones"] else None,
    }
    snap = {"at": now_iso(), **totals}
    hist.setdefault("snapshots", []).append(snap)
    hist["snapshots"] = hist["snapshots"][-365:]

    daily = []
    for day in sorted(set(hist["clones"]) | set(hist["views"]) | set(hist["cdn"]))[-90:]:
        daily.append({
            "date": day,
            "clones": hist["clones"].get(day, {}).get("count", 0),
            "clone_uniques": hist["clones"].get(day, {}).get("uniques", 0),
            "views": hist["views"].get(day, {}).get("count", 0),
            "cdn": hist["cdn"].get(day, 0),
        })

    HISTORY.write_text(json.dumps(hist, indent=1, sort_keys=True) + "\n")
    return totals, daily


# ------------------------------------------------------------- leaderboards

def top(rows, key, n=15, require=True):
    out = sorted(rows, key=lambda r: (-r[key], r["name"]))
    if require:
        out = [r for r in out if r[key]]
    return out[:n]


def slim(rec, *extra):
    fields = ("name", "display_name", "publisher", "category", "tier", "downloads",
              "up", "down", "score", "reviews", "rating", "lines", "size_kb",
              "added_at", "file", "description") + extra
    return {k: rec[k] for k in fields if k in rec}


def build_leaderboards(agents):
    rows = list(agents.values())
    publishers = defaultdict(lambda: {"agents": 0, "downloads": 0, "score": 0, "reviews": 0,
                                      "rating_sum": 0.0, "rated": 0, "lines": 0})
    categories = defaultdict(lambda: {"agents": 0, "downloads": 0, "score": 0, "reviews": 0})
    tiers = defaultdict(int)

    for r in rows:
        p = publishers[r["publisher"]]
        p["agents"] += 1
        p["downloads"] += r["downloads"]
        p["score"] += r["score"]
        p["reviews"] += r["reviews"]
        p["lines"] += r["lines"]
        if r["rating"]:
            p["rating_sum"] += r["rating"]
            p["rated"] += 1
        c = categories[r["category"]]
        c["agents"] += 1
        c["downloads"] += r["downloads"]
        c["score"] += r["score"]
        c["reviews"] += r["reviews"]
        tiers[r["tier"]] += 1

    pub_rows = []
    for name, p in publishers.items():
        pub_rows.append({
            "name": name, "agents": p["agents"], "downloads": p["downloads"],
            "score": p["score"], "reviews": p["reviews"], "lines": p["lines"],
            "rating": round(p["rating_sum"] / p["rated"], 2) if p["rated"] else 0.0,
        })
    pub_rows.sort(key=lambda r: (-r["agents"], r["name"]))

    cat_rows = [{"name": k, **v} for k, v in categories.items()]
    cat_rows.sort(key=lambda r: -r["agents"])

    rated = [r for r in rows if r["reviews"] >= 3 and r["rating"]]
    rated.sort(key=lambda r: (-r["rating"], -r["reviews"]))

    newest = [r for r in rows if r["added_at"]]
    newest.sort(key=lambda r: r["added_at"], reverse=True)

    return {
        "most_downloaded": [slim(r) for r in top(rows, "downloads")],
        "most_upvoted": [slim(r) for r in top(rows, "score")],
        "most_reviewed": [slim(r) for r in top(rows, "reviews")],
        "highest_rated": [slim(r) for r in rated[:15]],
        "largest": [slim(r) for r in top(rows, "lines", n=15)],
        "newest": [slim(r) for r in newest[:15]],
        "publishers": pub_rows,
        "categories": cat_rows,
        "tiers": dict(sorted(tiers.items(), key=lambda kv: -kv[1])),
    }


# ----------------------------------------------------------------- assembly

def main():
    ap = argparse.ArgumentParser(description="Build public metrics snapshot for the RAR dashboard.")
    ap.add_argument("--offline", action="store_true", help="skip all network calls")
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args()

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    registry = load_json(REGISTRY, {})
    if not registry:
        log("✗ registry.json missing or unreadable — run build_registry.py first")
        return 1

    log("· indexing registry")
    agents, by_file = build_agent_index(registry)
    vote_totals = apply_votes(agents, load_json(VOTES, {}))
    review_totals = apply_reviews(agents, load_json(CURATOR_REVIEWS, {}), load_json(USER_REVIEWS, {}))

    repo = releases = traffic = {}
    jsd = {"total_hits": 0, "bandwidth": 0, "daily": [], "files": [], "agent_hits": 0}
    if not args.offline:
        log("· github repo")
        repo = fetch_repo(token)
        log("· releases")
        releases = fetch_releases(token)
        log("· traffic")
        traffic = fetch_traffic(token)
        log("· jsdelivr cdn")
        jsd = fetch_jsdelivr(by_file, agents)

    hist_totals, daily = merge_history(traffic, jsd)

    total_downloads = (hist_totals["clones_all_time"]
                       + hist_totals["cdn_all_time"]
                       + (releases.get("total_downloads", 0) if releases else 0))

    doc = {
        "schema": "rar-metrics/1.0",
        "generated_at": now_iso(),
        "repo": {"owner": OWNER, "name": REPO,
                 "url": f"https://github.com/{OWNER}/{REPO}",
                 "site": f"https://{OWNER}.github.io/{REPO}/", **repo},
        "totals": {
            "downloads": total_downloads,
            "clones": hist_totals["clones_all_time"],
            "clone_uniques": hist_totals["clone_uniques_all_time"],
            "cdn_hits": hist_totals["cdn_all_time"],
            "release_downloads": releases.get("total_downloads", 0) if releases else 0,
            "page_views": hist_totals["views_all_time"],
            "view_uniques": hist_totals["view_uniques_all_time"],
            "days_tracked": hist_totals["days_tracked"],
            "tracking_since": hist_totals["first_day"],
            "agents": registry.get("stats", {}).get("total_agents", len(agents)),
            "swarms": registry.get("stats", {}).get("total_swarms", 0),
            "publishers": registry.get("stats", {}).get("publishers", 0),
            "categories": registry.get("stats", {}).get("categories", 0),
            "total_lines": sum(a["lines"] for a in agents.values()),
            "total_kb": round(sum(a["size_kb"] for a in agents.values()), 1),
            "votes": vote_totals["up"] + vote_totals["down"],
            "upvotes": vote_totals["up"],
            "downvotes": vote_totals["down"],
            "voters": vote_totals["voters"],
            "reviews": review_totals["reviews"],
            "reviewers": review_totals["reviewers"],
            "avg_rating": review_totals["avg_rating"],
            "agents_reviewed": review_totals["agents_reviewed"],
            "agents_voted": vote_totals["agents_voted"],
        },
        "daily": daily,
        "traffic": {"paths": traffic.get("paths", []), "referrers": traffic.get("referrers", []),
                    "clones_14d": traffic.get("clones", {}).get("count_14d", 0),
                    "views_14d": traffic.get("views", {}).get("count_14d", 0)},
        "cdn": {"total_hits": jsd["total_hits"], "bandwidth": jsd["bandwidth"],
                "rank": jsd.get("rank"), "agent_hits": jsd.get("agent_hits", 0),
                "files": jsd["files"]},
        "releases": releases or {"total_downloads": 0, "count": 0, "releases": []},
        "reviews": {"by_angle": review_totals["by_angle"], "distribution": review_totals["distribution"]},
        "leaderboards": build_leaderboards(agents),
        "sources": [
            {"name": "GitHub Traffic API", "metric": "clones, views, popular paths", "url": f"{GH_API}/repos/{OWNER}/{REPO}/traffic/clones"},
            {"name": "jsDelivr CDN", "metric": "per-file download hits", "url": f"{JSDELIVR}/stats/packages/gh/{OWNER}/{REPO}"},
            {"name": "GitHub Releases", "metric": "release asset downloads", "url": f"{GH_API}/repos/{OWNER}/{REPO}/releases"},
            {"name": "registry.json", "metric": "agents, publishers, categories", "url": f"https://{OWNER}.github.io/{REPO}/registry.json"},
            {"name": "state/votes.json", "metric": "up/down votes", "url": f"https://{OWNER}.github.io/{REPO}/state/votes.json"},
            {"name": "state/curator_reviews.json", "metric": "reviews and ratings", "url": f"https://{OWNER}.github.io/{REPO}/state/curator_reviews.json"},
        ],
    }

    Path(args.out).write_text(json.dumps(doc, indent=1) + "\n")
    t = doc["totals"]
    log(f"✓ {args.out}")
    log(f"  downloads={t['downloads']} (clones {t['clones']} + cdn {t['cdn_hits']} + releases {t['release_downloads']})")
    log(f"  agents={t['agents']} votes={t['votes']} reviews={t['reviews']} stars={doc['repo'].get('stars', 0)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

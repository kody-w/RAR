#!/usr/bin/env python3
"""Snapshot GitHub's server-side release-asset download counts.

Why this is the real download number
------------------------------------
GitHub counts every fetch of a public release asset itself, server-side,
with no token required on either end — the download or the count read.
That is the same property that makes npm's download API meaningful, and
it is the only anonymous, no-infrastructure counter available to us.

Two things this deliberately does NOT do:

* It does not reset on a new release. ``download_count`` is per asset per
  release, so a fresh tag starts its assets at zero. We sum an asset's
  counts across every release it has ever appeared in, which makes the
  published number monotonic and comparable over time.
* It does not stamp a timestamp into the output. Like
  ``scripts/discussion_ratings.py``, the file changes only when the counts
  change — which is what lets the daily workflow skip no-op commits, and
  makes the git history of this file the download time series.

Honest framing for anyone reading the number: it is a FLOOR. The raw
``raw.githubusercontent.com`` URLs stay reachable, so anyone fetching an
agent by its raw path is not counted. npm has the identical hole — a
tarball URL can be curl'd directly — so this is a normal registry caveat,
not a defect. Report it as "release downloads", never as "installs".

Usage
-----
    python scripts/fetch_download_counts.py

    GITHUB_TOKEN=...  raises the API rate limit; works unauthenticated.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_FILE = REPO_ROOT / "registry.json"
SNAPSHOT_FILE = REPO_ROOT / "state" / "downloads.json"
API_STATS_FILE = REPO_ROOT / "api" / "v1" / "stats" / "downloads.json"

REPO = os.environ.get("RAR_DOWNLOADS_REPO", "kody-w/RAR")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""

SNAPSHOT_SCHEMA = "rar-downloads/1.0"


def warn(msg: str) -> None:
    print(f"[downloads] {msg}", file=sys.stderr)


def api_get(url: str) -> tuple[list, str | None]:
    """GET a paginated API URL. Returns (json, next_url)."""
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "rar-download-stats",
        **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
    })
    with urllib.request.urlopen(req, timeout=20) as resp:
        payload = json.loads(resp.read().decode())
        link = resp.headers.get("Link", "") or ""
    nxt = None
    for part in link.split(","):
        if 'rel="next"' in part:
            nxt = part.split(";")[0].strip().strip("<>")
    return payload, nxt


def fetch_all_releases() -> list[dict]:
    releases: list[dict] = []
    url = f"https://api.github.com/repos/{REPO}/releases?per_page=100"
    while url:
        page, url = api_get(url)
        if not isinstance(page, list):
            raise RuntimeError(f"unexpected API payload: {str(page)[:120]}")
        releases.extend(page)
    return releases


def asset_to_agent() -> dict[str, str]:
    """Map release-asset filename -> @publisher/slug, from the registry."""
    if not REGISTRY_FILE.exists():
        return {}
    data = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    agents = data.get("agents", []) if isinstance(data, dict) else list(data)
    mapping: dict[str, str] = {}
    for a in agents:
        asset, name = a.get("_install_filename"), a.get("name")
        if asset and name:
            mapping[asset] = name
    return mapping


def build_snapshot(releases: list[dict], mapping: dict[str, str]) -> dict:
    """Sum download_count per asset across every release it appears in."""
    per_asset: dict[str, int] = {}
    for rel in releases:
        for asset in rel.get("assets") or []:
            fname = asset.get("name")
            if not fname:
                continue
            per_asset[fname] = per_asset.get(fname, 0) + int(
                asset.get("download_count") or 0)

    agents: dict[str, dict] = {}
    unmapped = 0
    for fname, count in per_asset.items():
        name = mapping.get(fname)
        if not name:
            # An asset from an older release whose agent has since been
            # renamed or retired. Counted in the total, not attributed.
            unmapped += count
            continue
        agents[name] = {"downloads": count, "asset": fname}

    return {
        "schema": SNAPSHOT_SCHEMA,
        "repo": REPO,
        "source": "github release asset download_count (server-side, anonymous)",
        "note": ("A floor, not a total: raw.githubusercontent.com fetches are "
                 "not counted. Report as 'release downloads', never 'installs'."),
        "agents": {n: agents[n] for n in sorted(agents)},
        "totals": {
            "downloads": sum(v["downloads"] for v in agents.values()) + unmapped,
            "attributed_downloads": sum(v["downloads"] for v in agents.values()),
            "unattributed_downloads": unmapped,
            "assets_published": len(per_asset),
            "agents_with_downloads": sum(
                1 for v in agents.values() if v["downloads"] > 0),
        },
    }


def persist(snapshot: dict) -> bool:
    """Write the snapshot. Never replace real counts with an empty result —
    a failed fetch must not erase history."""
    existing = None
    if SNAPSHOT_FILE.exists():
        try:
            existing = json.loads(SNAPSHOT_FILE.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            existing = None

    if not snapshot["agents"] and existing and existing.get("agents"):
        warn("no asset counts found; keeping existing snapshot.")
        return False

    # "No assets have ever been released" is NOT "zero downloads". Writing
    # an all-zeros file would publish a real-looking number for a counter
    # that was never wired — the exact failure the reaction tally already
    # has. Stay silent until there is something to count.
    if snapshot["totals"]["assets_published"] == 0 and existing is None:
        warn("no release carries assets yet; not writing a zeroed snapshot. "
             "Cut a release with assets first (see release.yml).")
        return False

    body = json.dumps(snapshot, indent=2) + "\n"
    for target in (SNAPSHOT_FILE, API_STATS_FILE):
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
    return True


def main() -> int:
    try:
        releases = fetch_all_releases()
    except (OSError, RuntimeError, urllib.error.URLError) as exc:
        # Non-fatal by design, matching refresh-ratings.yml's other steps:
        # an API problem leaves the snapshot untouched rather than failing
        # the run or zeroing real numbers.
        warn(f"release fetch failed ({exc}); snapshot unchanged.")
        return 0

    if not releases:
        warn("repo has no releases yet — nothing to count. "
             "Cut a release with assets first (see release.yml).")
        return 0

    snapshot = build_snapshot(releases, asset_to_agent())
    if persist(snapshot):
        t = snapshot["totals"]
        print(f"[downloads] {t['attributed_downloads']} attributed download(s) "
              f"across {t['assets_published']} asset(s); "
              f"{t['agents_with_downloads']} agent(s) with >0.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

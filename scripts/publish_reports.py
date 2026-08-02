#!/usr/bin/env python3
"""Publish a per-agent report card into its GitHub Discussion.

The idea
--------
Every agent already has a Discussion thread: a public, permanent, per-agent
URL that CI can write to and GitHub indexes. Until now that thread only
COLLECTED signal — reactions in, nothing back. This turns it into the
agent's report card, so the place people land is the place the numbers live.

Two levels of reporting, one pattern:

    per agent   -> this script, rendered into the Discussion top post
    portfolio   -> stats.html, rendered from the same snapshots

Both read the same state files, so the two can never disagree. Nobody types
a field: if a number has to be typed, it will be wrong by the next quarter.

How it writes
-------------
The report is a delimited block inside the top post. Everything outside the
markers is preserved untouched, so a human can edit the thread freely and CI
will not clobber their words. A thread with no block yet gets one appended.

Idempotent by construction: the rendered block is compared to what is
already there and the mutation is skipped when they match. That means a
quiet day costs zero writes, and the edit history of a thread reads as a
record of when the agent's numbers actually moved.

Usage
-----
    GITHUB_TOKEN=... python scripts/publish_reports.py            # publish
    GITHUB_TOKEN=... python scripts/publish_reports.py --limit 25 # cap writes
    python scripts/publish_reports.py --dry-run --only @rapp/hacker_news
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_FILE = REPO_ROOT / "registry.json"
RATINGS_FILE = REPO_ROOT / "state" / "discussion_ratings.json"
CRITIC_FILE = REPO_ROOT / "state" / "critic_reviews.json"
DOWNLOADS_FILE = REPO_ROOT / "state" / "downloads.json"
AGGREGATED_FILE = REPO_ROOT / "state" / "aggregated.json"

REPO = os.environ.get("RAR_RATINGS_REPO", "kody-w/RAR")
CATEGORY = os.environ.get("RAR_RATINGS_CATEGORY", "Announcements")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""

START = "<!-- rar:report:start -->"
END = "<!-- rar:report:end -->"

# Same seven channels the feedback comment collects, in the order they are
# rendered. Kept here rather than imported so this script stays standalone.
SIGNAL_ROWS = [
    ("worked", "Worked"),
    ("saved_time", "Saved real time"),
    ("regular_use", "In regular use"),
    ("shipped", "Shipped to a customer"),
    ("want_to_try", "Want to try"),
    ("stuck", "Couldn't get it running"),
    ("did_not_work", "Didn't work"),
]

DISCUSSIONS_QUERY = """
query ($owner: String!, $name: String!, $after: String) {
  repository(owner: $owner, name: $name) {
    discussions(first: 100, after: $after) {
      pageInfo { hasNextPage endCursor }
      nodes { id number title url body category { name } }
    }
  }
}
"""

UPDATE_MUTATION = """
mutation ($id: ID!, $body: String!) {
  updateDiscussion(input: {discussionId: $id, body: $body}) {
    discussion { number }
  }
}
"""


def warn(msg: str) -> None:
    print(f"[reports] {msg}", file=sys.stderr)


def graphql(query: str, variables: dict) -> dict:
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"Bearer {TOKEN}",
                 "Content-Type": "application/json",
                 "User-Agent": "rar-reports"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read().decode())
    if payload.get("errors"):
        raise RuntimeError(payload["errors"][0].get("message", "graphql error"))
    return payload.get("data") or {}


def load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def fmt(n) -> str:
    return f"{n:,}" if isinstance(n, int) else str(n)


def render(agent: dict, rating: dict, critic: dict,
           rel_downloads, upstream: dict | None) -> str:
    """The report card. Every number traces to a state file; none are typed."""
    name = agent.get("name", "")
    lines = [START, "", "### Report card", ""]

    # ── Identity ────────────────────────────────────────────────────────
    tier = (agent.get("quality_tier") or "community").title()
    ident = [
        f"**Version** {agent.get('version', '?')}",
        f"**Tier** {tier}",
        f"**Category** {(agent.get('category') or 'general').replace('_', ' ')}",
    ]
    platforms = agent.get("platforms") or []
    if platforms:
        ident.append(f"**Runs on** {', '.join(platforms)}")
    lines.append(" · ".join(ident))
    lines.append("")

    # ── Provenance ──────────────────────────────────────────────────────
    if upstream:
        lines += [
            f"Aggregated from **{upstream.get('source_name', 'an external library')}** — "
            f"[upstream entry]({upstream.get('upstream_url', '')}). "
            "Indexed here, never copied; the source library holds the content.",
            "",
        ]

    # ── Reach ───────────────────────────────────────────────────────────
    acquisitions = rating.get("downloads", 0)
    upvotes = rating.get("upvotes", 0)
    lines += ["| Reach | Count | What it counts |", "|---|---:|---|"]
    lines.append(
        f"| Release downloads | {fmt(rel_downloads) if rel_downloads is not None else '—'} "
        "| Counted by GitHub, includes signed-out. A floor: direct file URLs are uncounted. |")
    lines.append(f"| Acquisitions | {fmt(acquisitions)} "
                 "| Distinct signed-in people who installed it. |")
    lines.append(f"| Upvotes | {fmt(upvotes)} | Distinct people. |")
    lines.append("")

    # ── Reception ───────────────────────────────────────────────────────
    signals = rating.get("signals") or {}
    total = sum(signals.get(k, 0) for k, _ in SIGNAL_ROWS)
    lines += ["| Reception | People |", "|---|---:|"]
    for key, label in SIGNAL_ROWS:
        lines.append(f"| {label} | {fmt(signals.get(key, 0))} |")
    lines.append("")
    if total == 0:
        lines += ["_Nobody has answered yet — react on the “How did this agent "
                  "go?” comment below. One tap, no form._", ""]

    # ── Quality ─────────────────────────────────────────────────────────
    avg, count = critic.get("critic_avg"), critic.get("critic_count") or 0
    if count:
        lines.append(f"**Critic score** {avg:.0f}/100 from {count} independent "
                     f"{'critic' if count == 1 else 'critics'}, each reading a "
                     "different lens. Model-written, not human review.")
    else:
        lines.append("**Critic score** not yet scored.")
    digest = agent.get("_sha256") or agent.get("_stub_sha256")
    if digest:
        lines.append(f"**Content hash** `{digest[:16]}…` — anyone can verify the "
                     "file they hold is the file that was published.")
    lines.append("")

    lines += [
        "---",
        "_Generated from the registry's public state files and refreshed daily; "
        "no field here is typed by hand. Counts are of people, never identities. "
        "Portfolio-level figures: "
        f"[registry statistics](https://kody-w.github.io/RAR/stats.html)._",
        END,
    ]
    block = "\n".join(lines)
    # The block interpolates registry free text (category, platforms, the
    # upstream source name and URL). A value containing the literal end marker
    # would leave two END markers in the post, so splice() would replace up to
    # the FIRST one and leave the tail behind — the card growing on every daily
    # run, which is exactly the non-convergence this whole mechanism exists to
    # avoid. Guarantee exactly one of each by construction.
    inner = block[len(START):-len(END)].replace(START, "").replace(END, "")
    return f"{START}{inner}{END}"


def critic_index(raw: dict) -> dict:
    """Index critic records by the name a registry agent is actually called.

    critic_reviews.json keys its map with an UNDERSCORE-normalized name
    ('@aibast_agents_library/x') while each record's own `name` field holds the
    real dashed one ('@aibast-agents-library/x'). Keying off the dict silently
    resolved NOTHING for every publisher with a dash — most of the registry —
    and every card read "not yet scored" while real scores existed.

    This is a named function, not three lines inlined in main(), so a test can
    exercise the code that actually runs. The first regression test for this bug
    re-implemented the lookup inside the test and therefore stayed green with
    the bug fully reintroduced.
    """
    return {(rec.get("name") or key): rec for key, rec in (raw or {}).items()}


def splice(body: str, block: str) -> str:
    """Replace the report block, preserving every human-written word around it.

    Keyed on START alone, and END is only sought AFTER it. A card someone
    truncated mid-edit leaves START with no END; requiring both markers made
    that fall through to the append branch, which stacked a second card on
    every run — so a single bad edit would grow the post forever.
    """
    body = body or ""
    if START not in body:
        return f"{body.rstrip()}\n\n{block}\n"
    head, rest = body.split(START, 1)
    tail = rest.split(END, 1)[1] if END in rest else ""
    parts = [head.rstrip(), block, tail.lstrip()]
    return "\n\n".join(p for p in parts if p).strip() + "\n"


def fetch_discussions(owner: str, name: str) -> list[dict]:
    out, after = [], None
    while True:
        data = graphql(DISCUSSIONS_QUERY,
                       {"owner": owner, "name": name, "after": after})
        conn = ((data.get("repository") or {}).get("discussions") or {})
        out.extend(conn.get("nodes") or [])
        page = conn.get("pageInfo") or {}
        if not page.get("hasNextPage"):
            return out
        after = page.get("endCursor")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--limit", type=int, default=60,
                    help="max threads to update this run (default 60)")
    ap.add_argument("--only", help="a single @publisher/slug")
    ap.add_argument("--delay", type=float, default=1.0)
    ap.add_argument("--dry-run", action="store_true",
                    help="print the rendered card, write nothing")
    args = ap.parse_args()

    reg = load(REGISTRY_FILE, {})
    agents = {a["name"]: a for a in (reg.get("agents") or []) if a.get("name")}
    if not agents:
        warn("registry.json has no agents; nothing to report.")
        return 0
    ratings = (load(RATINGS_FILE, {}) or {}).get("agents", {})
    critics = critic_index((load(CRITIC_FILE, {}) or {}).get("agents", {}))
    downloads = (load(DOWNLOADS_FILE, {}) or {}).get("agents", {})
    aggregated = {i["ref"]: i for i in (load(AGGREGATED_FILE, {}) or {}).get("items", [])}

    # Dry-run renders straight from local state — no token, no network.
    if args.dry_run:
        targets = [args.only] if args.only else list(agents)[:1]
        for n in targets:
            if n not in agents:
                warn(f"'{n}' is not in the registry."); return 1
            up = aggregated.get(n)
            print(render(agents[n], ratings.get(n, {}), critics.get(n, {}),
                         (downloads.get(n) or {}).get("downloads"),
                         {"source_name": up["source_id"],
                          "upstream_url": up["url"]} if up else None))
        return 0

    if not TOKEN:
        warn("no GITHUB_TOKEN set; cannot publish reports.")
        return 0

    owner, _, name = REPO.partition("/")
    try:
        discussions = fetch_discussions(owner, name)
    except (OSError, RuntimeError, urllib.error.URLError) as exc:
        # Non-fatal, like every other snapshot step: a bad API day leaves the
        # threads exactly as they were rather than failing the workflow.
        warn(f"fetch failed ({exc}); no reports published.")
        return 0

    updated = unchanged = 0
    for node in discussions:
        title = str(node.get("title", "")).strip()
        if ((node.get("category") or {}).get("name")) != CATEGORY:
            continue
        if title not in agents or (args.only and title != args.only):
            continue
        up = aggregated.get(title)
        block = render(
            agents[title], ratings.get(title, {}), critics.get(title, {}),
            (downloads.get(title) or {}).get("downloads"),
            {"source_name": up["source_id"], "upstream_url": up["url"]} if up else None,
        )
        new_body = splice(node.get("body") or "", block)
        if new_body.strip() == (node.get("body") or "").strip():
            unchanged += 1
            continue
        if updated >= args.limit:
            continue
        try:
            graphql(UPDATE_MUTATION, {"id": node["id"], "body": new_body})
            updated += 1
        except (OSError, RuntimeError, urllib.error.URLError) as exc:
            warn(f"stopping after {updated} update(s): {exc}")
            break
        time.sleep(args.delay)

    print(f"[reports] updated {updated} report card(s); {unchanged} already current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

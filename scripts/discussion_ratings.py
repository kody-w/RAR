#!/usr/bin/env python3
"""Discussion ratings — GitHub Discussions as the upvote + comment backend.

The pattern:

  * One Discussion per agent, whose title IS the agent name
    (``@publisher/slug_agent``), in a maintainer-only category
    ("Announcements") so nobody can spoof an agent's thread.
  * An upvote is a *positive* reaction on that Discussion
    (THUMBS_UP, HEART, HOORAY, ROCKET, LAUGH). Negative reactions
    (THUMBS_DOWN, CONFUSED) and neutral (EYES) never contribute, so a
    thumbs-down can't drag a score down or masquerade as a rating.
  * Comments are the Discussion thread itself — GitHub handles
    identity, spam controls, and one-reaction-per-user natively.
  * A build-time snapshot (``state/discussion_ratings.json``) is what
    the web store reads. A live vote shows up on the next refresh.

Subcommands:
  seed   Create missing Discussions for registry agents (idempotent,
         capped per run to stay under content-creation rate limits).
  fetch  Snapshot reaction/comment counts into state/discussion_ratings.json.

Both are intentionally NON-FATAL: a missing token, network error, or
missing category results in a warning and an unchanged snapshot —
never a failed build.

Usage:
  GITHUB_TOKEN=... python scripts/discussion_ratings.py seed [--limit 80]
  GITHUB_TOKEN=... python scripts/discussion_ratings.py fetch

Config (env, with defaults):
  GITHUB_TOKEN / GH_TOKEN   token with discussions read (fetch) / write (seed)
  RAR_RATINGS_REPO          owner/repo        (default: kody-w/RAR)
  RAR_RATINGS_CATEGORY      Discussion category (default: Announcements)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_FILE = REPO_ROOT / "registry.json"
SNAPSHOT_FILE = REPO_ROOT / "state" / "discussion_ratings.json"

REPO = os.environ.get("RAR_RATINGS_REPO", "kody-w/RAR")
CATEGORY = os.environ.get("RAR_RATINGS_CATEGORY", "Announcements")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""

SNAPSHOT_SCHEMA = "rar-discussion-ratings/1.0"

# Discussion titles that count as agent threads. Belt: shape check.
# Suspenders: the title must also exist in registry.json.
AGENT_TITLE_RE = re.compile(r"^@[A-Za-z0-9][A-Za-z0-9_-]*/[a-z0-9_]+$")

# GitHub reaction contents split into sentiment buckets. Only positive
# reactions count toward the rating.
POSITIVE_REACTIONS = frozenset(
    {"THUMBS_UP", "HEART", "HOORAY", "ROCKET", "LAUGH"}
)

DISCUSSIONS_QUERY = """
query ($owner: String!, $name: String!, $after: String) {
  repository(owner: $owner, name: $name) {
    discussions(first: 100, after: $after) {
      pageInfo { hasNextPage endCursor }
      nodes {
        number
        title
        url
        category { name }
        comments { totalCount }
        reactionGroups { content reactors { totalCount } }
      }
    }
  }
}
"""

SEED_INFO_QUERY = """
query ($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    id
    discussionCategories(first: 25) { nodes { id name } }
  }
}
"""

CREATE_DISCUSSION_MUTATION = """
mutation ($repoId: ID!, $catId: ID!, $title: String!, $body: String!) {
  createDiscussion(input: {
    repositoryId: $repoId, categoryId: $catId, title: $title, body: $body
  }) {
    discussion { number url }
  }
}
"""


def warn(msg: str) -> None:
    print(f"[discussion-ratings] {msg}", file=sys.stderr)


def graphql(query: str, variables: dict) -> dict:
    """POST a GraphQL query. Raises on transport or GraphQL errors."""
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "rar-discussion-ratings",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read().decode())
    if payload.get("errors"):
        raise RuntimeError(
            "; ".join(e.get("message", "?") for e in payload["errors"])
        )
    data = payload.get("data")
    if not data:
        raise RuntimeError("GitHub GraphQL returned no data")
    return data


def load_registry_agents() -> dict[str, dict]:
    """Map of agent name → registry entry. Empty on any problem."""
    try:
        registry = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
        return {
            str(a.get("name", "")): a
            for a in registry.get("agents", [])
            if a.get("name")
        }
    except (OSError, json.JSONDecodeError) as exc:
        warn(f"could not read registry.json: {exc}")
        return {}


def is_agent_title(title: str) -> bool:
    return bool(AGENT_TITLE_RE.match(title.strip()))


def positive_score(reaction_groups: list | None) -> int:
    """Sum reactors across positive reaction groups only."""
    total = 0
    for group in reaction_groups or []:
        if group.get("content") in POSITIVE_REACTIONS:
            total += (group.get("reactors") or {}).get("totalCount", 0)
    return total


def build_snapshot(
    discussions: list[dict],
    registry_names: set[str],
    category: str = CATEGORY,
) -> dict[str, dict]:
    """Filter discussions down to real agent threads and count ratings.

    Only discussions in ``category`` whose title is agent-name-shaped AND
    present in the registry count. If duplicates exist for one agent, the
    lowest discussion number (the earliest, i.e. the seeded one) wins.
    """
    ratings: dict[str, dict] = {}
    for node in discussions:
        if ((node.get("category") or {}).get("name")) != category:
            continue
        title = str(node.get("title", "")).strip()
        if not is_agent_title(title) or title not in registry_names:
            continue
        entry = {
            "upvotes": positive_score(node.get("reactionGroups")),
            "comments": (node.get("comments") or {}).get("totalCount", 0),
            "url": node.get("url", ""),
            "number": node.get("number", 0),
        }
        existing = ratings.get(title)
        if existing is None or entry["number"] < existing["number"]:
            ratings[title] = entry
    return ratings


def persist(ratings: dict[str, dict], *, allow_empty: bool = False) -> bool:
    """Write the snapshot. Never clobber an existing non-empty snapshot
    with an empty result (a failed fetch must not erase real counts).
    No timestamps — the file only changes when the counts change, which
    is what lets the refresh workflow skip no-op commits."""
    if not ratings and not allow_empty and SNAPSHOT_FILE.exists():
        warn("no ratings found; keeping existing snapshot.")
        return False
    snapshot = {
        "schema": SNAPSHOT_SCHEMA,
        "repo": REPO,
        "category": CATEGORY,
        "agents": {name: ratings[name] for name in sorted(ratings)},
    }
    SNAPSHOT_FILE.parent.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_FILE.write_text(
        json.dumps(snapshot, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"[discussion-ratings] wrote {len(ratings)} rating(s) "
        f"to {SNAPSHOT_FILE.relative_to(REPO_ROOT)}"
    )
    return True


def fetch_all_discussions(owner: str, name: str) -> list[dict]:
    nodes: list[dict] = []
    after = None
    while True:
        data = graphql(
            DISCUSSIONS_QUERY, {"owner": owner, "name": name, "after": after}
        )
        conn = (data.get("repository") or {}).get("discussions") or {}
        nodes.extend(conn.get("nodes") or [])
        page = conn.get("pageInfo") or {}
        if not page.get("hasNextPage"):
            return nodes
        after = page.get("endCursor")


def cmd_fetch() -> int:
    if not TOKEN:
        warn("no GITHUB_TOKEN set; leaving ratings snapshot unchanged.")
        return 0
    owner, _, name = REPO.partition("/")
    if not owner or not name:
        warn(f"invalid RAR_RATINGS_REPO '{REPO}'; expected owner/repo.")
        return 0
    registry_names = set(load_registry_agents())
    if not registry_names:
        warn("registry has no agents; leaving snapshot unchanged.")
        return 0
    try:
        discussions = fetch_all_discussions(owner, name)
    except (OSError, RuntimeError, urllib.error.URLError) as exc:
        warn(f"fetch failed ({exc}); leaving snapshot unchanged.")
        return 0
    persist(build_snapshot(discussions, registry_names))
    return 0


def seed_body(agent: dict) -> str:
    """Discussion body for a seeded agent thread."""
    name = agent.get("name", "")
    display = agent.get("display_name", name)
    description = agent.get("description", "")
    file_path = agent.get("_file", "")
    lines = [
        f"**{display}** — {description}",
        "",
        f"This is the official rating thread for `{name}` in the "
        "[RAPP Agent Registry](https://kody-w.github.io/RAR/store.html).",
        "",
        "- **Upvote**: add a :+1: reaction to this post "
        "(:heart: :tada: :rocket: :smile: count too).",
        "- **Discuss**: reply below with questions, feedback, or reviews.",
    ]
    if file_path:
        lines += [
            "",
            f"Source: https://github.com/{REPO}/blob/main/{file_path}",
        ]
    return "\n".join(lines)


def cmd_seed(limit: int, delay: float) -> int:
    if not TOKEN:
        warn("no GITHUB_TOKEN set; cannot seed discussions.")
        return 0
    owner, _, name = REPO.partition("/")
    agents = load_registry_agents()
    if not agents:
        warn("registry has no agents; nothing to seed.")
        return 0
    try:
        info = graphql(SEED_INFO_QUERY, {"owner": owner, "name": name})
        repository = info.get("repository") or {}
        repo_id = repository.get("id")
        category_id = next(
            (
                c["id"]
                for c in (repository.get("discussionCategories") or {}).get(
                    "nodes", []
                )
                if c.get("name") == CATEGORY
            ),
            None,
        )
        if not repo_id or not category_id:
            warn(f"category '{CATEGORY}' not found in {REPO}; cannot seed.")
            return 0
        existing = {
            str(node.get("title", "")).strip()
            for node in fetch_all_discussions(owner, name)
        }
    except (OSError, RuntimeError, urllib.error.URLError) as exc:
        warn(f"seed preflight failed ({exc}); nothing created.")
        return 0

    missing = [n for n in sorted(agents) if n not in existing]
    if not missing:
        print("[discussion-ratings] all agents already have threads.")
        return 0
    batch = missing[:limit]
    print(
        f"[discussion-ratings] seeding {len(batch)} of {len(missing)} "
        f"missing thread(s) (limit {limit})..."
    )
    created = 0
    for agent_name in batch:
        try:
            graphql(
                CREATE_DISCUSSION_MUTATION,
                {
                    "repoId": repo_id,
                    "catId": category_id,
                    "title": agent_name,
                    "body": seed_body(agents[agent_name]),
                },
            )
            created += 1
        except (OSError, RuntimeError, urllib.error.URLError) as exc:
            # Likely a secondary rate limit — stop here; the next run
            # (daily cron) picks up where this one left off.
            warn(f"stopping after {created} create(s): {exc}")
            break
        time.sleep(delay)
    print(
        f"[discussion-ratings] created {created} thread(s); "
        f"{len(missing) - created} still missing."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    seed = sub.add_parser("seed", help="create missing agent Discussions")
    seed.add_argument("--limit", type=int, default=80)
    seed.add_argument("--delay", type=float, default=1.2)
    sub.add_parser("fetch", help="snapshot ratings to state/")
    args = parser.parse_args()
    if args.command == "seed":
        return cmd_seed(args.limit, args.delay)
    return cmd_fetch()


if __name__ == "__main__":
    sys.exit(main())

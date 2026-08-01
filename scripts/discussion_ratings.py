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

Downloads are the second metric: every agent thread carries one pinned
"download tally" comment (marked with an HTML comment sentinel). A client
that downloads the agent.py reacts THUMBS_UP on that tally comment — one
reaction per GitHub user, so the count is spam-proof and means "unique
installers". ``fetch`` snapshots both metrics plus a combined rank score
(``score = 2*upvotes + downloads``) for storefront ranking.

Subcommands:
  seed   Create missing Discussions for registry agents (idempotent,
         capped per run to stay under content-creation rate limits).
         New threads get their download-tally comment immediately.
  tally  Ensure the download-tally comment exists on existing threads
         (idempotent, capped; --only <agent> targets a single thread).
  fetch  Snapshot reaction/comment/download counts into
         state/discussion_ratings.json.
  track  Register one download: add a THUMBS_UP to an agent's tally
         comment (what clients call after downloading the agent.py).

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

# Sentinel embedded in each thread's download-tally comment. Clients react
# THUMBS_UP on the comment carrying this marker to register a download.
TALLY_MARKER = "<!-- rar:download-tally -->"

TALLY_BODY = (
    TALLY_MARKER
    + "\n### 📥 Download tally\n\n"
    "Installers react :+1: **on this comment** when the agent.py is "
    "downloaded — one reaction per GitHub user, so the count reads as "
    "*unique installers*. Upvote the agent by reacting on the top post, "
    "not here."
)

# ── The feedback comment: a poll that can actually be provisioned ─────────
#
# GitHub Discussions has a real poll type (DiscussionPoll, with
# addDiscussionPollVote), but `createDiscussion` accepts only
# repositoryId/title/body/categoryId — polls can ONLY be created by hand in
# the web UI. A signal surface that needs a human to click through the web UI
# once per agent is not a pattern; it is a chore that will not survive the
# catalog growing. So it is not used here.
#
# A comment IS creatable over the API (addDiscussionComment), and every
# comment carries all eight reaction contents as independent, per-user-deduped
# counters. One comment therefore behaves as an eight-option poll, and gets
# provisioned automatically for every agent the moment it enters the registry.
SIGNAL_MARKER = "<!-- rar:signal -->"

# Reaction content -> the snapshot key it feeds. LAUGH is deliberately
# unmapped: there is no honest question it answers, and an option that means
# nothing pollutes every other count.
SIGNAL_MAP = {
    "THUMBS_UP": "worked",
    "THUMBS_DOWN": "did_not_work",
    "CONFUSED": "stuck",
    "HEART": "regular_use",
    "ROCKET": "shipped",
    "EYES": "want_to_try",
    "HOORAY": "saved_time",
}

SIGNAL_BODY = (
    SIGNAL_MARKER
    + "\n### How did this agent go?\n\n"
    "React **on this comment** — one tap, no form. Pick as many as apply.\n\n"
    "| React | Means |\n"
    "|---|---|\n"
    "| :+1: | It worked |\n"
    "| :-1: | It didn't work |\n"
    "| :confused: | I couldn't get it running |\n"
    "| :heart: | I use this regularly |\n"
    "| :rocket: | I shipped it to a customer |\n"
    "| :eyes: | I want to try this |\n"
    "| :tada: | It saved me real time |\n\n"
    "One reaction per person per row, so each count is *people*, not clicks. "
    "Something specific to say? Reply in the thread — a sentence is worth "
    "more than any of these."
)

# Every marker a thread should carry, in provisioning order. Adding an entry
# here is all it takes for a new signal surface to be created on every agent,
# old and new, by the same idempotent seeder.
MARKERS = {
    "download": (TALLY_MARKER, TALLY_BODY),
    "signal": (SIGNAL_MARKER, SIGNAL_BODY),
}

DISCUSSIONS_QUERY = """
query ($owner: String!, $name: String!, $after: String) {
  repository(owner: $owner, name: $name) {
    discussions(first: 100, after: $after) {
      pageInfo { hasNextPage endCursor }
      nodes {
        id
        number
        title
        url
        category { name }
        comments(first: 25) {
          totalCount
          nodes {
            id
            body
            reactionGroups { content reactors { totalCount } }
          }
        }
        reactionGroups { content reactors { totalCount } }
      }
    }
  }
}
"""

ADD_COMMENT_MUTATION = """
mutation ($discussionId: ID!, $body: String!) {
  addDiscussionComment(input: {discussionId: $discussionId, body: $body}) {
    comment { id }
  }
}
"""

ADD_REACTION_MUTATION = """
mutation ($subjectId: ID!) {
  addReaction(input: {subjectId: $subjectId, content: THUMBS_UP}) {
    reaction { content }
  }
}
"""

SEARCH_DISCUSSION_QUERY = """
query ($q: String!) {
  search(query: $q, type: DISCUSSION, first: 10) {
    nodes {
      ... on Discussion {
        id
        number
        title
        repository { nameWithOwner }
        comments(first: 25) { nodes { id body } }
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
    discussion { id number url }
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


def marker_comment_of(node: dict, marker: str) -> dict | None:
    """The comment carrying ``marker`` on a discussion node, if seeded."""
    for c in ((node.get("comments") or {}).get("nodes") or []):
        if marker in (c.get("body") or ""):
            return c
    return None


def tally_comment_of(node: dict) -> dict | None:
    """The download-tally comment of a discussion node, if seeded."""
    return marker_comment_of(node, TALLY_MARKER)


def signal_counts(node: dict) -> dict[str, int]:
    """Per-reaction people-counts from the feedback comment.

    Each of the eight reaction contents is an independent, one-per-user
    counter, so this reads as *how many distinct people said each thing* —
    not how many times it was clicked. Absent surface -> all zeros, so a
    thread that has not been provisioned yet is indistinguishable in shape
    from one nobody has answered, and callers need no special case.
    """
    counts = {key: 0 for key in SIGNAL_MAP.values()}
    comment = marker_comment_of(node, SIGNAL_MARKER)
    if not comment:
        return counts
    for group in comment.get("reactionGroups") or []:
        key = SIGNAL_MAP.get(group.get("content"))
        if key:
            counts[key] = (group.get("reactors") or {}).get("totalCount", 0)
    return counts


def download_count(node: dict) -> int:
    """THUMBS_UP reactors on the tally comment — one per unique installer."""
    tally = tally_comment_of(node)
    if not tally:
        return 0
    for group in tally.get("reactionGroups") or []:
        if group.get("content") == "THUMBS_UP":
            return (group.get("reactors") or {}).get("totalCount", 0)
    return 0


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
        upvotes = positive_score(node.get("reactionGroups"))
        downloads = download_count(node)
        signals = signal_counts(node)
        # Provisioned marker comments are machinery, not conversation — one
        # per marker present, so the count stays honest as markers are added.
        n_comments = (node.get("comments") or {}).get("totalCount", 0)
        provisioned = sum(
            1 for marker, _ in MARKERS.values()
            if marker_comment_of(node, marker) is not None
        )
        n_comments = max(0, n_comments - provisioned)
        entry = {
            "upvotes": upvotes,
            "downloads": downloads,
            "score": 2 * upvotes + downloads,  # storefront rank: votes weigh double
            "comments": n_comments,
            "signals": signals,
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
            made = graphql(
                CREATE_DISCUSSION_MUTATION,
                {
                    "repoId": repo_id,
                    "catId": category_id,
                    "title": agent_name,
                    "body": seed_body(agents[agent_name]),
                },
            )
            disc_id = (((made.get("createDiscussion") or {}).get("discussion"))
                       or {}).get("id")
            # A new agent gets its FULL signal surface at creation, not
            # eventually. Every marker in MARKERS, in one pass — so the day an
            # agent lands it can already record downloads and feedback, and no
            # later back-fill is needed for it.
            if disc_id:
                for _marker, body in MARKERS.values():
                    graphql(ADD_COMMENT_MUTATION,
                            {"discussionId": disc_id, "body": body})
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


def cmd_tally(limit: int, delay: float, only: str | None = None) -> int:
    """Provision every marker comment in MARKERS on every agent thread.

    Idempotent and per-marker: a thread missing only the newer marker gets
    only that one. This is what makes a new signal surface a one-entry change
    in MARKERS rather than a migration — add the entry, and the next run
    back-fills the whole catalog on its own, capped per run so it stays under
    GitHub's content-creation limits and drains over successive runs.
    """
    if not TOKEN:
        warn("no GITHUB_TOKEN set; cannot add marker comments.")
        return 0
    owner, _, name = REPO.partition("/")
    registry_names = set(load_registry_agents())
    try:
        discussions = fetch_all_discussions(owner, name)
    except (OSError, RuntimeError, urllib.error.URLError) as exc:
        warn(f"tally preflight failed ({exc}); nothing added.")
        return 0
    targets: list[tuple[str, str, str, str]] = []  # (title, id, kind, body)
    for node in discussions:
        title = str(node.get("title", "")).strip()
        if ((node.get("category") or {}).get("name")) != CATEGORY:
            continue
        if not is_agent_title(title) or title not in registry_names:
            continue
        if only and title != only:
            continue
        for kind, (marker, body) in MARKERS.items():
            if marker_comment_of(node, marker) is None:
                targets.append((title, node.get("id"), kind, body))
    if not targets:
        print("[discussion-ratings] every targeted thread has every marker.")
        return 0
    batch = targets[:limit]
    print(f"[discussion-ratings] adding {len(batch)} of {len(targets)} "
          f"missing marker comment(s) (limit {limit})...")
    added = 0
    by_kind: dict[str, int] = {}
    for title, disc_id, kind, body in batch:
        try:
            graphql(ADD_COMMENT_MUTATION,
                    {"discussionId": disc_id, "body": body})
            added += 1
            by_kind[kind] = by_kind.get(kind, 0) + 1
        except (OSError, RuntimeError, urllib.error.URLError) as exc:
            warn(f"stopping after {added} marker comment(s): {exc}")
            break
        time.sleep(delay)
    detail = ", ".join(f"{k}={v}" for k, v in sorted(by_kind.items())) or "none"
    print(f"[discussion-ratings] added {added} marker comment(s) ({detail}); "
          f"{len(targets) - added} still missing.")
    return 0


def cmd_track(agent_name: str) -> int:
    """Register one download: THUMBS_UP on the agent's tally comment."""
    if not TOKEN:
        warn("no GITHUB_TOKEN set; download not tracked.")
        return 0
    q = f'repo:{REPO} in:title "{agent_name}"'
    try:
        data = graphql(SEARCH_DISCUSSION_QUERY, {"q": q})
        node = next(
            (n for n in (data.get("search") or {}).get("nodes", [])
             if n and n.get("title") == agent_name
             and n.get("repository", {}).get("nameWithOwner") == REPO),
            None,
        )
        if not node:
            warn(f"no discussion found for '{agent_name}'; download not tracked.")
            return 0
        tally = tally_comment_of(node)
        if not tally:
            warn(f"'{agent_name}' has no tally comment yet; download not tracked.")
            return 0
        graphql(ADD_REACTION_MUTATION, {"subjectId": tally["id"]})
        print(f"[discussion-ratings] download registered for {agent_name} "
              f"(discussion #{node.get('number')}).")
    except (OSError, RuntimeError, urllib.error.URLError) as exc:
        warn(f"track failed ({exc}); download not tracked.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    seed = sub.add_parser("seed", help="create missing agent Discussions")
    seed.add_argument("--limit", type=int, default=80)
    seed.add_argument("--delay", type=float, default=1.2)
    tally = sub.add_parser("tally", help="ensure download-tally comments exist")
    tally.add_argument("--limit", type=int, default=80)
    tally.add_argument("--delay", type=float, default=1.2)
    tally.add_argument("--only", help="target a single agent name")
    track = sub.add_parser("track", help="register one download (thumbs-up the tally)")
    track.add_argument("agent", help="agent name, e.g. @kody-w/power_apps_code_app_agent")
    sub.add_parser("fetch", help="snapshot ratings to state/")
    args = parser.parse_args()
    if args.command == "seed":
        return cmd_seed(args.limit, args.delay)
    if args.command == "tally":
        return cmd_tally(args.limit, args.delay, args.only)
    if args.command == "track":
        return cmd_track(args.agent)
    return cmd_fetch()


if __name__ == "__main__":
    sys.exit(main())

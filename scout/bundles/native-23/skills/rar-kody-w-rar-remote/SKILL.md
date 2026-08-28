---
name: "rar-kody-w-rar-remote"
description: "The native client for the RAPP Agent Registry. Discover, search, install, vote on, review, and submit single-file agent.py files from the open RAPP ecosystem. All actions are authenticated via the brainstem's GitHub session. Read actions work immediately; write actions (vote, review, submit) create GitHub Issues processed by the RAPP pipeline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rar_remote_agent", "rar_sha256": "6fe73b97844e2046ef4f3fc83d9dc0f65a1159c1b778796bfc8f76c0c4b1e63a", "source_kind": "rar-agent", "source_commit": "a406372feff89232194bf208658b526eb2440722", "version": "1.8.0", "author": "RAPP Core Team", "tags": ["core", "registry", "package-manager", "install", "discovery", "voting", "community"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rar_remote_agent`. The original RAPP
agent is preserved byte-for-byte in `rar_remote_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

RAR Remote Agent — The native client for the RAPP Agent Registry.

Discover, search, install, vote, review, and submit agents from RAPP.
Reads the live registry and community state (votes/reviews) directly
from GitHub. Write operations (vote, review, submit) create GitHub
Issues that are processed by the RAPP automation pipeline.

Fully compatible with the RAPP brainstem runtime:
  - Uses the brainstem's implicit GITHUB_TOKEN (set during auth)
  - Uses storage_manager for local registry caching
  - All fetches use the authenticated token for higher rate limits
  - No separate auth required — brainstem handles it

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "Action to perform. 'discover' \u2014 browse all agents (optional: category, tier filters). 'search' \u2014 find by keyword (REQUIRES query). 'get_info' \u2014 agent details (REQUIRES agent_name). 'leaderboard' \u2014 top agents by votes. 'reviews' \u2014 show reviews (REQUIRES agent_name). 'install' \u2014 download agent (REQUIRES agent_name). For type='stub' entries, resolves the bytes from the private repo declared in __source__ using your GitHub credentials. 'vote' \u2014 upvote an agent (REQUIRES agent_name; RAR tracks upvotes only). 'review' \u2014 write review (REQUIRES agent_name, rating, text). 'submit' \u2014 submit new public agent (REQUIRES code). 'submit_upstream' \u2014 federate a local agent to the upstream RAR. 'federation_status' \u2014 show federation config. 'request_access' \u2014 ask the publisher to grant you access to a gated stub (REQUIRES agent_name; optional: use_case). 'publish_private' \u2014 generate and submit a .py.stub pointing at your private agent.py (REQUIRES agent_url; optional: dry_run). 'setup_private_rar' \u2014 scaffold + git-init + create a private GitHub repo for hosting gated agents (optional: repo_name, local_path, author, push, force).",
      "enum": [
        "discover",
        "search",
        "get_info",
        "leaderboard",
        "reviews",
        "install",
        "vote",
        "review",
        "submit",
        "submit_upstream",
        "federation_status",
        "request_access",
        "publish_private",
        "setup_private_rar"
      ],
      "type": "string"
    },
    "agent_name": {
      "description": "Full @publisher/slug name. Example: '@kody-w/rar_remote_agent'. Get this from discover or search results.",
      "type": "string"
    },
    "agent_url": {
      "description": "For 'publish_private': a github.com/<owner>/<repo>/blob/<ref>/<path> URL (or matching raw.githubusercontent.com URL) pointing at your private agent.py.",
      "type": "string"
    },
    "author": {
      "description": "For 'setup_private_rar': name used in the sample agent's manifest. Default: '<login>'.",
      "type": "string"
    },
    "category": {
      "description": "Filter by category (e.g. 'core', 'pipeline', 'healthcare').",
      "type": "string"
    },
    "code": {
      "description": "Agent source code for 'submit' action.",
      "type": "string"
    },
    "direction": {
      "description": "Vote direction. Only 'up' \u2014 RAR tracks upvotes only.",
      "enum": [
        "up"
      ],
      "type": "string"
    },
    "dry_run": {
      "description": "For 'publish_private': return the generated stub without submitting an issue.",
      "type": "boolean"
    },
    "force": {
      "description": "For 'setup_private_rar': overwrite local_path if it already exists. Default: false.",
      "type": "boolean"
    },
    "local_path": {
      "description": "For 'setup_private_rar': local directory to scaffold into. Default: './<repo_name>'.",
      "type": "string"
    },
    "output_dir": {
      "description": "Directory to save installed agents. Default: ./agents/",
      "type": "string"
    },
    "push": {
      "description": "For 'setup_private_rar': if true, creates the private GitHub repo via gh CLI and pushes. Default: true.",
      "type": "boolean"
    },
    "query": {
      "description": "Search keyword for 'search' action.",
      "type": "string"
    },
    "rating": {
      "description": "Star rating 1-5 for 'review' action.",
      "type": "integer"
    },
    "repo_name": {
      "description": "For 'setup_private_rar': name of the GitHub repo to create. Default: '<login>-private-rar'.",
      "type": "string"
    },
    "text": {
      "description": "Review text for 'review' action.",
      "type": "string"
    },
    "tier": {
      "description": "Filter by quality tier.",
      "enum": [
        "community",
        "verified",
        "official",
        "experimental"
      ],
      "type": "string"
    },
    "use_case": {
      "description": "Optional 'why' text for 'request_access' \u2014 included in the issue body the publisher sees.",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rar_remote_agent.py` and embedded as the fenced Python below (sha256 6fe73b97844e2046…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rar_remote_agent.py` first:

```bash
python3 rar_remote_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rar_remote_agent.py   # or on stdin
python3 rar_remote_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""
RAR Remote Agent — The native client for the RAPP Agent Registry.

Discover, search, install, vote, review, and submit agents from RAPP.
Reads the live registry and community state (votes/reviews) directly
from GitHub. Write operations (vote, review, submit) create GitHub
Issues that are processed by the RAPP automation pipeline.

Fully compatible with the RAPP brainstem runtime:
  - Uses the brainstem's implicit GITHUB_TOKEN (set during auth)
  - Uses storage_manager for local registry caching
  - All fetches use the authenticated token for higher rate limits
  - No separate auth required — brainstem handles it
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rar_remote_agent",
    "version": "1.8.0",
    "display_name": "RAR Remote Agent",
    "description": "Discovers, searches, installs, votes on, reviews, and submits RAR agents via GitHub raw fetches and Issues, using the brainstem's GitHub token.",
    "author": "RAPP Core Team",
    "tags": ["core", "registry", "package-manager", "install", "discovery", "voting", "community"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from agents.basic_agent import BasicAgent
import json
import logging
import os
import subprocess
import urllib.request
import urllib.error
from datetime import datetime

logger = logging.getLogger(__name__)

# Optional: brainstem provides storage_manager via shim.
# Gracefully degrade if running outside brainstem.
try:
    from utils.storage_factory import get_storage_manager
    _HAS_STORAGE = True
except ImportError:
    _HAS_STORAGE = False


class RARRemoteAgent(BasicAgent):
    """
    RAPP Remote Agent — browse, install, vote, review, and submit agents
    from the RAPP Agent Registry.

    Brainstem integration:
      - Reads GITHUB_TOKEN from environment (set by brainstem auth flow)
      - Falls back to `gh auth token` CLI if env var is missing
      - Uses storage_manager (when available) to cache registry locally
      - All GitHub API calls are authenticated for higher rate limits
      - Write operations (vote/review/submit) create Issues autonomously
    """

    # Defaults — overridden by api.json or rar.config.json if present
    REPO_OWNER = "kody-w"
    REPO_NAME = "RAR"
    REPO = f"{REPO_OWNER}/{REPO_NAME}"
    RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/main"
    # Stable alias: always 302s to the newest release's copy of an asset,
    # so no client pins a tag. This is the download path GitHub counts.
    RELEASE_BASE = f"https://github.com/{REPO}/releases/latest/download"
    API_BASE = f"https://api.github.com/repos/{REPO}"
    API_MANIFEST_URL = f"{RAW_BASE}/api.json"

    TIER_ORDER = {"official": 0, "verified": 1, "community": 2, "experimental": 3}
    CACHE_TTL_SECONDS = 300  # 5 minutes

    def __init__(self):
        self.name = "RARRemoteAgent"
        self.metadata = {
            "name": self.name,
            "description": (
                "The native client for the RAPP Agent Registry. "
                "Discover, search, install, vote on, review, and submit "
                "single-file agent.py files from the open RAPP ecosystem. "
                "All actions are authenticated via the brainstem's GitHub session. "
                "Read actions work immediately; write actions (vote, review, submit) "
                "create GitHub Issues processed by the RAPP pipeline."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "description": (
                            "Action to perform. "
                            "'discover' — browse all agents (optional: category, tier filters). "
                            "'search' — find by keyword (REQUIRES query). "
                            "'get_info' — agent details (REQUIRES agent_name). "
                            "'leaderboard' — top agents by votes. "
                            "'reviews' — show reviews (REQUIRES agent_name). "
                            "'install' — download agent (REQUIRES agent_name). For type='stub' "
                            "entries, resolves the bytes from the private repo declared in "
                            "__source__ using your GitHub credentials. "
                            "'vote' — upvote an agent (REQUIRES agent_name; RAR tracks upvotes only). "
                            "'review' — write review (REQUIRES agent_name, rating, text). "
                            "'submit' — submit new public agent (REQUIRES code). "
                            "'submit_upstream' — federate a local agent to the upstream RAR. "
                            "'federation_status' — show federation config. "
                            "'request_access' — ask the publisher to grant you access to a gated "
                            "stub (REQUIRES agent_name; optional: use_case). "
                            "'publish_private' — generate and submit a .py.stub pointing at your "
                            "private agent.py (REQUIRES agent_url; optional: dry_run). "
                            "'setup_private_rar' — scaffold + git-init + create a private GitHub "
                            "repo for hosting gated agents (optional: repo_name, local_path, "
                            "author, push, force)."
                        ),
                        "enum": [
                            "discover", "search", "get_info", "leaderboard",
                            "reviews", "install", "vote", "review", "submit",
                            "submit_upstream", "federation_status",
                            "request_access", "publish_private", "setup_private_rar",
                        ],
                    },
                    "agent_name": {
                        "type": "string",
                        "description": (
                            "Full @publisher/slug name. "
                            "Example: '@kody-w/rar_remote_agent'. "
                            "Get this from discover or search results."
                        ),
                    },
                    "query": {
                        "type": "string",
                        "description": "Search keyword for 'search' action.",
                    },
                    "category": {
                        "type": "string",
                        "description": "Filter by category (e.g. 'core', 'pipeline', 'healthcare').",
                    },
                    "tier": {
                        "type": "string",
                        "description": "Filter by quality tier.",
                        "enum": ["community", "verified", "official", "experimental"],
                    },
                    "direction": {
                        "type": "string",
                        "description": "Vote direction. Only 'up' — RAR tracks upvotes only.",
                        "enum": ["up"],
                    },
                    "rating": {
                        "type": "integer",
                        "description": "Star rating 1-5 for 'review' action.",
                    },
                    "text": {
                        "type": "string",
                        "description": "Review text for 'review' action.",
                    },
                    "code": {
                        "type": "string",
                        "description": "Agent source code for 'submit' action.",
                    },
                    "output_dir": {
                        "type": "string",
                        "description": "Directory to save installed agents. Default: ./agents/",
                    },
                    "use_case": {
                        "type": "string",
                        "description": "Optional 'why' text for 'request_access' — included in the issue body the publisher sees.",
                    },
                    "agent_url": {
                        "type": "string",
                        "description": "For 'publish_private': a github.com/<owner>/<repo>/blob/<ref>/<path> URL (or matching raw.githubusercontent.com URL) pointing at your private agent.py.",
                    },
                    "dry_run": {
                        "type": "boolean",
                        "description": "For 'publish_private': return the generated stub without submitting an issue.",
                    },
                    "repo_name": {
                        "type": "string",
                        "description": "For 'setup_private_rar': name of the GitHub repo to create. Default: '<login>-private-rar'.",
                    },
                    "local_path": {
                        "type": "string",
                        "description": "For 'setup_private_rar': local directory to scaffold into. Default: './<repo_name>'.",
                    },
                    "author": {
                        "type": "string",
                        "description": "For 'setup_private_rar': name used in the sample agent's manifest. Default: '<login>'.",
                    },
                    "push": {
                        "type": "boolean",
                        "description": "For 'setup_private_rar': if true, creates the private GitHub repo via gh CLI and pushes. Default: true.",
                    },
                    "force": {
                        "type": "boolean",
                        "description": "For 'setup_private_rar': overwrite local_path if it already exists. Default: false.",
                    },
                },
                "required": ["action"],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

        # Federation config
        self._upstream = None
        self._is_instance = False
        self._load_rar_config()

        # Caches
        self._registry_cache = None
        self._votes_cache = None
        self._reviews_cache = None
        self._cache_time = None

        # Storage manager (brainstem provides via shim; None outside brainstem)
        self._storage = None
        if _HAS_STORAGE:
            try:
                self._storage = get_storage_manager()
            except Exception:
                pass

    def _load_rar_config(self):
        """Load rar.config.json if available to support federation."""
        config_paths = [
            os.path.join(os.path.dirname(__file__), '..', '..', 'rar.config.json'),
            'rar.config.json',
        ]
        for path in config_paths:
            try:
                if os.path.exists(path):
                    with open(path) as f:
                        config = json.load(f)
                    self.REPO_OWNER = config.get("owner", self.REPO_OWNER)
                    self.REPO_NAME = config.get("repo", self.REPO_NAME)
                    self.REPO = f"{self.REPO_OWNER}/{self.REPO_NAME}"
                    self.RAW_BASE = f"https://raw.githubusercontent.com/{self.REPO}/main"
                    self.RELEASE_BASE = (
                        f"https://github.com/{self.REPO}/releases/latest/download")
                    self.API_BASE = f"https://api.github.com/repos/{self.REPO}"
                    if config.get("role") == "instance" and config.get("upstream"):
                        self._upstream = config["upstream"]
                        self._is_instance = True
                    return
            except (OSError, json.JSONDecodeError):
                continue

    # ──────────────────────────────────────────────────────────
    # GitHub token resolution (brainstem-compatible)
    # ──────────────────────────────────────────────────────────

    def _get_token(self):
        """
        Resolve the GitHub token using the brainstem's auth chain:
          1. GITHUB_TOKEN env var (set by brainstem during startup)
          2. Saved token file at .brainstem_data/.copilot_token
          3. `gh auth token` CLI fallback
        Returns token string or empty string.
        """
        # 1. Environment variable (primary — brainstem sets this)
        token = os.environ.get("GITHUB_TOKEN", "")
        if token:
            return token

        # 2. Brainstem's saved token file
        token_paths = [
            os.path.join(".brainstem_data", ".copilot_token"),
            os.path.expanduser("~/.brainstem_data/.copilot_token"),
        ]
        for path in token_paths:
            try:
                if os.path.exists(path):
                    with open(path) as f:
                        saved = f.read().strip()
                    if saved:
                        return saved
            except OSError:
                continue

        # 3. gh CLI fallback
        try:
            result = subprocess.run(
                ["gh", "auth", "token"],
                capture_output=True, text=True, timeout=5,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass

        return ""

    # ──────────────────────────────────────────────────────────
    # Authenticated HTTP helpers
    # ──────────────────────────────────────────────────────────

    def _build_headers(self, content_type=None):
        """Build HTTP headers, including auth token if available."""
        headers = {"User-Agent": "RAR-Remote-Agent/1.1"}
        token = self._get_token()
        if token:
            headers["Authorization"] = f"Bearer {token}"
            headers["Accept"] = "application/vnd.github.v3+json"
        if content_type:
            headers["Content-Type"] = content_type
        return headers

    def _fetch_json(self, url):
        """Fetch JSON from a URL with auth. Returns dict or None."""
        try:
            req = urllib.request.Request(url, headers=self._build_headers())
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            logger.warning(f"Failed to fetch {url}: {e}")
            return None

    def _fetch_text(self, url):
        """Fetch raw text from a URL with auth."""
        req = urllib.request.Request(url, headers=self._build_headers())
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode()

    # ──────────────────────────────────────────────────────────
    # Data loading with local cache
    # ──────────────────────────────────────────────────────────

    def _load_data(self, force=False):
        """Load registry + community state. Uses local cache when available."""
        if not force and self._registry_cache and self._cache_time:
            age = (datetime.now() - self._cache_time).total_seconds()
            if age < self.CACHE_TTL_SECONDS:
                return

        # Try local storage cache first (brainstem environment)
        if self._storage and not force:
            cached = self._read_local_cache()
            if cached:
                self._registry_cache, self._votes_cache, self._reviews_cache = cached
                self._cache_time = datetime.now()
                return

        # Fetch from GitHub
        self._registry_cache = self._fetch_json(f"{self.RAW_BASE}/registry.json")
        self._votes_cache = self._fetch_json(f"{self.RAW_BASE}/state/votes.json") or {"agents": {}}
        self._reviews_cache = self._fetch_json(f"{self.RAW_BASE}/state/reviews.json") or {"agents": {}}
        self._cache_time = datetime.now()

        # Persist to local storage for faster next load
        if self._storage and self._registry_cache:
            self._write_local_cache()

    def _read_local_cache(self):
        """Read cached registry from brainstem's storage manager."""
        try:
            raw = self._storage.read_file("agent_catalogue", "rar_registry_cache.json")
            if not raw:
                return None
            data = json.loads(raw)
            # Check staleness
            cached_at = data.get("_cached_at", "")
            if cached_at:
                age = (datetime.now() - datetime.fromisoformat(cached_at)).total_seconds()
                if age > self.CACHE_TTL_SECONDS:
                    return None
            return (
                data.get("registry"),
                data.get("votes", {"agents": {}}),
                data.get("reviews", {"agents": {}}),
            )
        except Exception:
            return None

    def _write_local_cache(self):
        """Persist registry to brainstem's storage manager."""
        try:
            data = {
                "_cached_at": datetime.now().isoformat(),
                "registry": self._registry_cache,
                "votes": self._votes_cache,
                "reviews": self._reviews_cache,
            }
            self._storage.write_file(
                "agent_catalogue",
                "rar_registry_cache.json",
                json.dumps(data),
            )
        except Exception as e:
            logger.debug(f"Could not write registry cache: {e}")

    def _agents(self):
        self._load_data()
        return (self._registry_cache or {}).get("agents", [])

    def _get_score(self, name):
        v = (self._votes_cache or {}).get("agents", {}).get(name, {})
        return v.get("score", 0)

    def _get_reviews(self, name):
        return (self._reviews_cache or {}).get("agents", {}).get(name, [])

    def _get_rating(self, name):
        revs = self._get_reviews(name)
        if not revs:
            return 0.0
        return sum(r.get("rating", 0) for r in revs) / len(revs)

    # ──────────────────────────────────────────────────────────
    # GitHub Issues API (write operations)
    # ──────────────────────────────────────────────────────────

    def _create_issue(self, title, body_data):
        """
        Create a GitHub Issue with a JSON body.
        Uses the brainstem's implicit GitHub session.
        Returns issue URL or error string.
        """
        token = self._get_token()
        if not token:
            return (
                "Error: No GitHub token available. "
                "The brainstem should provide this automatically. "
                "If running standalone, set GITHUB_TOKEN or run `gh auth login`."
            )

        body_json = json.dumps(body_data, indent=2)
        issue_body = f"```json\n{body_json}\n```"

        payload = json.dumps({
            "title": f"[RAR] {title}",
            "body": issue_body,
            "labels": ["rar-action"],
        }).encode()

        req = urllib.request.Request(
            f"{self.API_BASE}/issues",
            data=payload,
            headers=self._build_headers(content_type="application/json"),
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                result = json.loads(resp.read().decode())
                return result.get("html_url", "Issue created")
        except urllib.error.HTTPError as e:
            body = e.read().decode() if e.fp else str(e)
            logger.error(f"Issue creation failed: {e.code} — {body[:200]}")
            return f"Error creating issue: {e.code} — {body[:200]}"
        except Exception as e:
            return f"Error: {e}"

    # ──────────────────────────────────────────────────────────
    # Perform dispatch
    # ──────────────────────────────────────────────────────────

    def perform(self, **kwargs) -> str:
        action = kwargs.get("action", "")

        handlers = {
            "discover": self._discover,
            "search": self._search,
            "get_info": self._get_info,
            "leaderboard": self._leaderboard,
            "reviews": self._show_reviews,
            "install": self._install,
            "vote": self._vote,
            "review": self._write_review,
            "submit": self._submit,
            "submit_upstream": self._submit_upstream,
            "federation_status": self._federation_status,
            "request_access": self._request_access,
            "publish_private": self._publish_private,
            "setup_private_rar": self._setup_private_rar,
        }

        handler = handlers.get(action)
        if not handler:
            return f"Unknown action '{action}'. Valid: {', '.join(handlers.keys())}"

        try:
            return handler(kwargs)
        except Exception as e:
            logger.error(f"RARRemoteAgent error: {e}")
            return f"Error: {e}"

    # ──────────────────────────────────────────────────────────
    # Read actions
    # ──────────────────────────────────────────────────────────

    def _discover(self, params):
        """Browse all agents with optional category/tier filters."""
        agents = self._agents()
        if not agents:
            return "Error: Unable to fetch the RAPP registry."

        category = params.get("category")
        tier = params.get("tier")

        filtered = list(agents)
        if category:
            filtered = [a for a in filtered if a.get("category") == category]
        if tier:
            filtered = [a for a in filtered if a.get("quality_tier") == tier]

        filtered.sort(key=lambda a: (
            self.TIER_ORDER.get(a.get("quality_tier", "community"), 2),
            -self._get_score(a["name"]),
        ))

        stats = (self._registry_cache or {}).get("stats", {})
        total_votes = sum(
            v.get("up", 0) for v in (self._votes_cache or {}).get("agents", {}).values()
        )

        out = f"RAPP Agent Registry — {stats.get('total_agents', len(agents))} agents\n"
        out += f"Publishers: {stats.get('publishers', '?')} | "
        out += f"Categories: {stats.get('categories', '?')} | "
        out += f"Community votes: {total_votes}\n"
        out += "=" * 60 + "\n\n"

        for a in filtered[:30]:
            score = self._get_score(a["name"])
            rating = self._get_rating(a["name"])
            tier_label = a.get("quality_tier", "community").upper()
            stars = f" | {'*' * round(rating)} {rating:.1f}" if rating > 0 else ""
            out += f"[{tier_label}] {a['display_name']} ({a['name']})\n"
            out += f"  v{a['version']} | {a.get('category', '?')} | "
            out += f"{a.get('_size_kb', '?')} KB | votes: {score}{stars}\n"
            out += f"  {a['description'][:100]}\n\n"

        if len(filtered) > 30:
            out += f"... and {len(filtered) - 30} more. Use search to narrow.\n"

        out += "\nActions: search, install, vote, review, submit, leaderboard\n"
        return out

    def _search(self, params):
        """Search agents by keyword."""
        query = (params.get("query") or "").lower()
        if not query:
            return "Error: 'query' is required for search."

        agents = self._agents()
        if not agents:
            return "Error: Unable to fetch the RAPP registry."

        results = []
        for a in agents:
            searchable = (
                f"{a.get('name', '')} {a.get('display_name', '')} "
                f"{a.get('description', '')} {' '.join(a.get('tags', []))} "
                f"{a.get('author', '')} {a.get('category', '')}"
            ).lower()
            if query in searchable:
                score = 0
                if query in a.get("name", "").lower():
                    score += 10
                if query in a.get("display_name", "").lower():
                    score += 8
                if query in a.get("description", "").lower():
                    score += 5
                for tag in a.get("tags", []):
                    if query in tag.lower():
                        score += 3
                results.append((score, a))

        results.sort(key=lambda x: (-x[0], -self._get_score(x[1]["name"])))

        if not results:
            return (
                f"No agents found for '{query}'.\n"
                f"Try broader terms or use action='discover' to browse all."
            )

        out = f"Search results for '{query}' — {len(results)} found\n"
        out += "-" * 50 + "\n\n"

        for _, a in results[:20]:
            score = self._get_score(a["name"])
            tier = a.get("quality_tier", "community").upper()
            out += f"[{tier}] {a['display_name']}\n"
            out += f"  name: {a['name']} | v{a['version']} | votes: {score}\n"
            out += f"  {a['description'][:120]}\n"
            out += f"  Install: action='install', agent_name='{a['name']}'\n\n"

        return out

    def _get_info(self, params):
        """Get detailed info about a specific agent."""
        name = params.get("agent_name", "")
        if not name:
            return "Error: 'agent_name' is required."

        agents = self._agents()
        agent = next((a for a in agents if a["name"] == name), None)
        if not agent:
            return f"Agent '{name}' not found. Use action='search' to find it."

        score = self._get_score(name)
        revs = self._get_reviews(name)
        rating = self._get_rating(name)
        tier = agent.get("quality_tier", "community")

        out = f"{'=' * 50}\n"
        out += f"{agent['display_name']}\n"
        out += f"{'=' * 50}\n\n"
        out += f"Name:        {agent['name']}\n"
        out += f"Version:     {agent['version']}\n"
        out += f"Author:      {agent.get('author', 'Unknown')}\n"
        out += f"Category:    {agent.get('category', 'Unknown')}\n"
        out += f"Quality:     {tier.upper()}"
        if tier == "verified":
            out += " [RAPP VERIFIED SEAL]"
        elif tier == "experimental":
            out += " [EXPERIMENTAL - USE AT YOUR OWN RISK]"
        out += "\n"
        out += f"Size:        {agent.get('_size_kb', '?')} KB ({agent.get('_lines', '?')} lines)\n"
        out += f"Votes:       {score}\n"
        out += f"Rating:      {'*' * round(rating)} {rating:.1f}/5 ({len(revs)} reviews)\n\n"

        out += f"Description:\n  {agent['description']}\n\n"

        if agent.get("tags"):
            out += f"Tags: {', '.join(agent['tags'])}\n\n"

        env = agent.get("requires_env", [])
        out += f"Env vars:    {', '.join(env) if env else 'None'}\n"
        deps = agent.get("dependencies", [])
        out += f"Depends on:  {', '.join(deps) if deps else 'None'}\n\n"

        raw_url = f"{self.RAW_BASE}/{agent['_file']}"
        out += f"Install:     curl -sO {raw_url}\n"
        out += f"Source:      https://github.com/{self.REPO}/blob/main/{agent['_file']}\n\n"

        if revs:
            out += f"Recent reviews:\n"
            for r in revs[-3:]:
                out += f"  @{r['user']} — {'*' * r['rating']} — {r['text'][:80]}\n"

        return out

    def _leaderboard(self, params):
        """Show top agents by votes."""
        agents = self._agents()
        if not agents:
            return "Error: Unable to fetch the RAPP registry."

        ranked = sorted(agents, key=lambda a: (
            -self._get_score(a["name"]),
            -self._get_rating(a["name"]),
        ))

        out = "RAPP Agent Leaderboard\n"
        out += "=" * 55 + "\n"
        out += f"{'#':>3}  {'Agent':<30} {'Tier':<10} {'Votes':>5}  {'Rating':>6}\n"
        out += "-" * 55 + "\n"

        for i, a in enumerate(ranked[:25], 1):
            score = self._get_score(a["name"])
            rating = self._get_rating(a["name"])
            tier = (a.get("quality_tier", "community"))[:8]
            stars = f"{rating:.1f}" if rating > 0 else "  —"
            out += f"{i:>3}  {a['display_name'][:30]:<30} {tier:<10} {score:>5}  {stars:>6}\n"

        return out

    def _show_reviews(self, params):
        """Show all reviews for an agent."""
        name = params.get("agent_name", "")
        if not name:
            return "Error: 'agent_name' is required."

        self._load_data()
        revs = self._get_reviews(name)

        if not revs:
            return f"No reviews yet for {name}. Be the first: action='review'"

        out = f"Reviews for {name} ({len(revs)})\n"
        out += "-" * 40 + "\n\n"

        for r in revs:
            ts = r.get("timestamp", "")[:10]
            out += f"@{r['user']} — {'*' * r['rating']} ({r['rating']}/5) — {ts}\n"
            out += f"  {r['text']}\n\n"

        return out

    # ──────────────────────────────────────────────────────────
    # Write actions (create GitHub Issues via brainstem's token)
    # ──────────────────────────────────────────────────────────

    def _resolve_private_source(self, src: dict) -> str:
        """Fetch agent bytes from a private repo via the GitHub contents API.
        Uses the brainstem's existing token. Returns the file's text.
        Raises with a clean access-denied message if the user can't read
        the repo (GitHub returns 404 for unauthorized reads on private
        repos — that is intentional and not a bug). """
        stype = src.get("type")
        if stype not in ("github_private", "github_public"):
            raise ValueError(f"Unsupported source type: {stype}")

        repo = src.get("repo", "")
        path = src.get("path", "")
        ref = src.get("ref", "main")
        if not repo or not path:
            raise ValueError("source missing 'repo' or 'path'")

        url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={ref}"
        headers = self._build_headers()
        # Ask the contents API for raw bytes rather than the wrapped JSON.
        headers["Accept"] = "application/vnd.github.raw"

        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.read().decode()
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 404):
                raise PermissionError(
                    f"Access denied to {repo}/{path} (HTTP {e.code}). "
                    f"You need read access to the private repo '{repo}'. "
                    f"Authenticate with `gh auth login` or set GITHUB_TOKEN."
                )
            raise

    def _install(self, params):
        """Download an agent file to the local filesystem.
        For stub entries (type=='stub') the bytes are fetched from the
        private repo declared in __source__ using the user's own GitHub
        credentials — public RAR only ever hosts the stub manifest."""
        name = params.get("agent_name", "")
        if not name:
            return "Error: 'agent_name' is required."

        agents = self._agents()
        agent = next((a for a in agents if a["name"] == name), None)
        if not agent:
            return f"Agent '{name}' not found. Use action='search' first."

        output_dir = params.get("output_dir", "agents")
        is_stub = agent.get("type") == "stub"

        if is_stub:
            src = agent.get("_source") or {}
            try:
                code = self._resolve_private_source(src)
            except PermissionError as e:
                return (
                    f"Locked: {agent['display_name']}\n\n"
                    f"{e}\n\n"
                    f"This is a gated agent — the listing is public but the source\n"
                    f"is hosted in a private repo. If you should have access, check\n"
                    f"that your GitHub account has been granted read access to:\n"
                    f"  {src.get('repo', '?')}\n\n"
                    f"To ask the publisher for access, run:\n"
                    f"  action='request_access', agent_name='{name}'\n"
                )
            except Exception as e:
                return f"Error resolving private source: {e}"
            # Save under the path the private repo uses, not the stub path
            filename = src.get("path", "").split("/")[-1] or f"{name.split('/')[-1]}.py"
        else:
            filename = agent["_file"].split("/")[-1]
            # Prefer the GitHub release asset. It is the only fetch GitHub
            # counts for us: a public release asset needs no token, and
            # download_count is incremented server-side on every fetch,
            # anonymous ones included. A raw fetch is invisible to us.
            # Falls back to raw for agents published since the last
            # release — a metric must never block an install.
            code = None
            asset = agent.get("_install_filename")
            if asset:
                try:
                    code = self._fetch_text(f"{self.RELEASE_BASE}/{asset}")
                except Exception:
                    code = None
            if code is None:
                try:
                    code = self._fetch_text(f"{self.RAW_BASE}/{agent['_file']}")
                except Exception as e:
                    return f"Error downloading agent: {e}"

        try:
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "w") as f:
                f.write(code)
        except Exception as e:
            return f"Error saving agent: {e}"

        # Also persist to storage_manager if available
        if self._storage:
            try:
                self._storage.write_file("agents", filename, code)
            except Exception:
                pass  # Local file write already succeeded

        tier = agent.get("quality_tier", "community").upper()
        score = self._get_score(name)

        out = f"Installed: {agent['display_name']} [{tier}]\n\n"
        out += f"Name:     {agent['name']} v{agent['version']}\n"
        out += f"Saved to: {filepath}\n"
        out += f"Size:     {agent.get('_size_kb', '?')} KB\n"
        out += f"Votes:    {score}\n"
        out += f"Author:   {agent.get('author', 'Unknown')}\n\n"

        if agent.get("requires_env"):
            out += f"Required env vars: {', '.join(agent['requires_env'])}\n"
            out += "Set these before using the agent.\n\n"

        out += "Ready to use.\n"
        return out

    def _request_access(self, params):
        """Open a GitHub Issue on public RAR asking the gated agent's
        publisher to grant the requester read access to the private repo.
        The issue @-mentions the publisher (extracted from the source
        repo owner) so they get notified the standard way. Only valid
        for type='stub' agents — regular agents don't need access."""
        name = params.get("agent_name", "")
        use_case = (params.get("use_case") or "").strip()
        if not name:
            return "Error: 'agent_name' is required."

        agents = self._agents()
        agent = next((a for a in agents if a["name"] == name), None)
        if not agent:
            return f"Agent '{name}' not found. Use action='search' first."
        if agent.get("type") != "stub":
            return (
                f"'{name}' is not a gated agent — no access request needed. "
                f"Use action='install' to fetch it."
            )

        src = agent.get("_source") or {}
        repo = src.get("repo") or ""
        path = src.get("path") or ""
        publisher = repo.split("/")[0] if "/" in repo else repo
        if not publisher:
            return f"Cannot determine publisher for '{name}' — source repo missing."

        token = self._get_token()
        if not token:
            return (
                "Error: No GitHub token available. The brainstem should set this; "
                "if running standalone, run `gh auth login` or set GITHUB_TOKEN."
            )

        body_lines = [
            f"Hi @{publisher},",
            "",
            f"I'd like access to **{agent['display_name']}** (`{name}`).",
            "",
            f"Source: `{repo}/{path}`",
            "",
            f"If granted, please add me as a read collaborator on `{repo}` "
            f"so the brainstem can resolve the bytes on install.",
        ]
        if use_case:
            body_lines += ["", f"Use case: {use_case}"]

        payload = json.dumps({
            "title": f"[RAR] request: access to {name}",
            "body": "\n".join(body_lines),
            "labels": ["request-access", "rar-action"],
        }).encode()

        req = urllib.request.Request(
            f"{self.API_BASE}/issues",
            data=payload,
            headers=self._build_headers(content_type="application/json"),
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                result = json.loads(resp.read().decode())
                url = result.get("html_url", "Issue created")
                return (
                    f"Access request opened for {name}.\n"
                    f"Publisher @{publisher} has been notified.\n"
                    f"Issue: {url}\n\n"
                    f"Next: wait for @{publisher} to add you as a read collaborator "
                    f"on {repo}, then retry action='install'."
                )
        except urllib.error.HTTPError as e:
            body = e.read().decode() if e.fp else str(e)
            return f"Error creating issue: {e.code} — {body[:200]}"
        except Exception as e:
            return f"Error: {e}"

    def _parse_github_blob_url(self, url: str) -> dict | None:
        """Parse a GitHub blob or raw URL into source-pointer components.
        Accepts:
          https://github.com/<owner>/<repo>/blob/<ref>/<path>
          https://raw.githubusercontent.com/<owner>/<repo>/<ref>/<path>
        Returns {repo, ref, path} or None if it doesn't look like one."""
        if not url:
            return None
        u = url.strip()
        m = None
        if "github.com/" in u and "/blob/" in u:
            tail = u.split("github.com/", 1)[1]
            owner_repo, _, rest = tail.partition("/blob/")
            ref, _, path = rest.partition("/")
            if owner_repo.count("/") == 1 and ref and path:
                m = {"repo": owner_repo, "ref": ref, "path": path}
        elif "raw.githubusercontent.com/" in u:
            tail = u.split("raw.githubusercontent.com/", 1)[1]
            parts = tail.split("/", 3)
            if len(parts) == 4:
                m = {"repo": f"{parts[0]}/{parts[1]}", "ref": parts[2], "path": parts[3]}
        return m

    def _publish_private(self, params):
        """Submit a gated stub to public RAR by pointing at a private
        agent.py URL. The flow:
          1. Parse the GitHub URL into (repo, ref, path).
          2. Fetch the agent.py via the contents API using YOUR token.
             If you don't have access, GitHub returns 404 — proves you
             can't publish someone else's gated agent.
          3. AST-extract __manifest__ from the fetched code.
          4. Render the matching .py.stub source.
          5. Open a GitHub Issue on public RAR carrying the stub.
        Args:
          agent_url: GitHub blob or raw URL to the private agent.py.
          dry_run:   if truthy, returns the stub source without opening
                     an issue.
        """
        url = params.get("agent_url", "").strip()
        dry_run = bool(params.get("dry_run", False))

        if not url:
            return "Error: 'agent_url' is required (a github.com/<owner>/<repo>/blob/<ref>/<path> URL)."

        parts = self._parse_github_blob_url(url)
        if not parts:
            return (
                "Error: Could not parse 'agent_url'. Expected a URL like "
                "https://github.com/owner/repo/blob/main/agents/@you/foo_agent.py "
                "or the matching raw.githubusercontent.com form."
            )

        src = {
            "schema": "rapp-source/1.0",
            "type": "github_private",
            "repo": parts["repo"],
            "ref": parts["ref"],
            "path": parts["path"],
        }
        try:
            code = self._resolve_private_source(src)
        except PermissionError as e:
            return (
                f"Cannot publish: {e}\n\n"
                f"You can only publish a stub for an agent you can read. "
                f"Confirm you have access to {src['repo']}, then retry."
            )
        except Exception as e:
            return f"Error fetching agent source: {e}"

        try:
            import ast as _ast
            tree = _ast.parse(code)
            manifest = None
            for node in _ast.walk(tree):
                if isinstance(node, _ast.Assign):
                    for t in node.targets:
                        if isinstance(t, _ast.Name) and t.id == "__manifest__":
                            try:
                                manifest = _ast.literal_eval(node.value)
                            except (ValueError, TypeError):
                                pass
                if manifest:
                    break
        except SyntaxError as e:
            return f"Error: agent source has syntax errors — {e}"

        if not isinstance(manifest, dict):
            return "Error: could not extract __manifest__ dict from the agent source."

        required = ["schema", "name", "version", "display_name",
                    "description", "author", "tags", "category"]
        missing = [f for f in required if f not in manifest]
        if missing:
            return f"Error: manifest is missing required fields: {missing}"

        # Stubs are always tier 'private' — they aren't reviewable.
        manifest["quality_tier"] = "private"

        # Render a clean .py.stub source. ast.literal_eval-friendly:
        # only literals, no expressions.
        def _render(d):
            lines = ["{"]
            for k, v in d.items():
                lines.append(f"    {repr(k)}: {repr(v)},")
            lines.append("}")
            return "\n".join(lines)

        docstring = (
            f'"""\n'
            f"Gated stub for {manifest['name']} — bytes live in the private repo\n"
            f"{src['repo']} at {src['path']}. Public RAR carries only this\n"
            f"manifest pointer; the brainstem resolves the source at install\n"
            f"time using the installer's own GitHub credentials.\n"
            f'"""\n\n'
        )
        stub_src = (
            docstring
            + "__manifest__ = " + _render(manifest) + "\n\n"
            + "__source__ = " + _render(src) + "\n"
        )

        if dry_run:
            return (
                f"Dry run — stub generated for {manifest['name']}:\n\n"
                f"{stub_src}\n"
                f"To actually submit, re-run without dry_run."
            )

        # Convention: stubs land under agents/<publisher>/private/<slug>.py.stub
        publisher = manifest["name"].split("/")[0]  # "@you"
        slug_basename = src["path"].rsplit("/", 1)[-1]  # "foo_agent.py"
        stub_path = f"agents/{publisher}/private/{slug_basename}.stub"

        result = self._create_issue(
            f"submit_stub: {manifest['name']}",
            {
                "action": "submit_stub",
                "payload": {
                    "name": manifest["name"],
                    "stub_path": stub_path,
                    "stub_source": stub_src,
                    "source": src,
                },
            },
        )

        if result.startswith("Error"):
            return result
        return (
            f"Gated stub submitted for {manifest['name']}.\n"
            f"Issue: {result}\n\n"
            f"The submission contains the .py.stub ready to land at:\n"
            f"  {stub_path}\n\n"
            f"What happens next:\n"
            f"  - A maintainer (or the pipeline, when stub support lands) "
            f"reviews and merges the stub.\n"
            f"  - Once merged, your agent appears in public RAR as LOCKED.\n"
            f"  - Anyone with read access to {src['repo']} can install it; "
            f"anyone else sees a clean access-denied message."
        )

    # The private-RAR template lives in public RAR at private-rar-template/.
    # `setup_private_rar` fetches each entry via raw.githubusercontent and
    # writes it locally — no need to embed kilobytes of templates in this
    # agent. The `substitute` flag controls token replacement on functional
    # files (rar.config.json, sample_private_agent.py); docs are written
    # verbatim because they carry placeholder strings deliberately.
    PRIVATE_RAR_TEMPLATE_FILES = [
        {"src": "README.md", "dst": "README.md", "substitute": False},
        {"src": "rar.config.json", "dst": "rar.config.json", "substitute": True},
        {"src": "build_local_registry.py", "dst": "build_local_registry.py", "substitute": False},
        {"src": "submit_to_public_rar.md", "dst": "submit_to_public_rar.md", "substitute": False},
        {"src": "agents/@yourname/sample_private_agent.py",
         "dst": "agents/@{login}/sample_private_agent.py", "substitute": True},
        {"src": ".github/workflows/build-private-registry.yml",
         "dst": ".github/workflows/build-private-registry.yml", "substitute": False},
    ]

    def _gh_login(self) -> str | None:
        """Resolve the authenticated user's GitHub login. Tries `gh api user`
        first (most reliable), then a token-authed call to api.github.com/user."""
        try:
            r = subprocess.run(
                ["gh", "api", "user", "--jq", ".login"],
                capture_output=True, text=True, timeout=10,
            )
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout.strip()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
        try:
            req = urllib.request.Request(
                "https://api.github.com/user",
                headers=self._build_headers(),
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode()).get("login")
        except Exception:
            return None

    def _setup_private_rar(self, params):
        """One-shot scaffold of a private RAR: fetch the template from public
        RAR (so it's always up-to-date), write it under `local_path`, init
        git, and — unless `push=False` — create a private GitHub repo and
        push the scaffold to it.

        Args:
          repo_name:  name of the GitHub repo to create. Default: '<login>-private-rar'.
          local_path: where to scaffold on disk. Default: './<repo_name>'.
          author:     "Your Name" replacement in the sample agent. Default: '<login>'.
          push:       create + push to GitHub via `gh repo create --private`. Default: True.
          force:      overwrite local_path if it exists. Default: False.
        """
        login = self._gh_login()
        if not login:
            return (
                "Error: Could not determine your GitHub login. Run `gh auth login` "
                "or set GITHUB_TOKEN to a token with `read:user` scope, then retry."
            )

        repo_name = params.get("repo_name") or f"{login}-private-rar"
        local_path = params.get("local_path") or f"./{repo_name}"
        author = params.get("author") or login
        push = params.get("push", True)
        if isinstance(push, str):
            push = push.lower() not in ("false", "0", "no")
        force = bool(params.get("force", False))

        # Substitution map applied to files with substitute=True.
        # Order matters where strings overlap — see comment below.
        replacements = [
            # Combined form must run before split substitutions so we don't
            # double-replace (e.g., 'yourname/yourname-private-rar').
            ("yourname/yourname-private-rar", f"{login}/{repo_name}"),
            ("yourname-private-rar", repo_name),
            ("@yourname", f"@{login}"),
            ('"yourname"', f'"{login}"'),
            ("Your Name", author),
        ]

        local = os.path.abspath(local_path)
        if os.path.exists(local):
            if not force:
                return (
                    f"Error: {local} already exists. Pass force=True to overwrite, "
                    f"or pick a different local_path."
                )
            # Light cleanup — only remove if it's our own scaffold (has rar.config.json)
            if not os.path.exists(os.path.join(local, "rar.config.json")):
                return (
                    f"Error: {local} exists but doesn't look like a private RAR "
                    f"(no rar.config.json). Refusing to overwrite. Choose another path."
                )

        os.makedirs(local, exist_ok=True)
        written = []
        errors = []

        # Template is always fetched from the canonical remote so every
        # user gets the same content regardless of cwd. (An earlier
        # version checked for a local private-rar-template/ directory
        # first — that created surprising behavior where running the
        # agent from inside the public RAR repo gave different results
        # than running it from anywhere else.)
        for entry in self.PRIVATE_RAR_TEMPLATE_FILES:
            src_url = f"{self.RAW_BASE}/private-rar-template/{entry['src']}"
            try:
                content = self._fetch_text(src_url)
            except Exception as e:
                errors.append(f"fetch {entry['src']}: {e}")
                continue
            if entry["substitute"]:
                for old, new in replacements:
                    content = content.replace(old, new)
            dst_rel = entry["dst"].format(login=login)
            dst_abs = os.path.join(local, dst_rel)
            os.makedirs(os.path.dirname(dst_abs), exist_ok=True)
            with open(dst_abs, "w") as f:
                f.write(content)
            written.append(dst_rel)

        # Add a marker .gitkeep so the namespace dir is non-empty even
        # without the sample agent (some users delete it immediately).
        ns_dir = os.path.join(local, f"agents/@{login}")
        os.makedirs(ns_dir, exist_ok=True)
        keep_path = os.path.join(ns_dir, ".gitkeep")
        if not os.path.exists(keep_path):
            with open(keep_path, "w") as f:
                f.write("")
            written.append(f"agents/@{login}/.gitkeep")

        if errors:
            return (
                f"Setup partial — fetched {len(written)} files, "
                f"{len(errors)} failures:\n  " + "\n  ".join(errors) +
                f"\n\nNothing was pushed. Resolve the fetch errors and retry."
            )

        if not push:
            return (
                f"Scaffolded {len(written)} files under {local}\n\n"
                f"Next steps (manual):\n"
                f"  cd {local}\n"
                f"  git init && git add . && git commit -m 'Initial scaffold'\n"
                f"  gh repo create {login}/{repo_name} --private --source=. --push\n\n"
                f"Or re-run setup_private_rar with push=True to do this automatically."
            )

        # Init git, commit, and push via gh CLI. gh is the right tool here:
        # it handles repo creation + remote wiring + initial push atomically,
        # and uses the same auth chain (`gh auth`) the rest of this agent
        # already relies on.
        try:
            subprocess.run(["gh", "--version"], capture_output=True, timeout=5, check=True)
        except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
            return (
                f"Scaffolded {len(written)} files under {local}, but `gh` CLI is "
                f"not available — cannot push automatically.\n\n"
                f"Install gh (https://cli.github.com) then run:\n"
                f"  cd {local}\n"
                f"  git init && git add . && git commit -m 'Initial scaffold'\n"
                f"  gh repo create {login}/{repo_name} --private --source=. --push"
            )

        def _run(cmd, **kw):
            return subprocess.run(cmd, capture_output=True, text=True, timeout=60, cwd=local, **kw)

        steps = [
            ["git", "init", "-q"],
            ["git", "add", "."],
            ["git", "-c", "commit.gpgsign=false", "commit", "-q",
             "-m", "Initial scaffold — created by @kody-w/rar_remote_agent setup_private_rar"],
            ["gh", "repo", "create", f"{login}/{repo_name}",
             "--private", "--source=.", "--push", "--remote=origin"],
        ]
        for step in steps:
            r = _run(step)
            if r.returncode != 0:
                tail = (r.stderr or r.stdout).strip().splitlines()[-1:]
                return (
                    f"Setup failed at: {' '.join(step)}\n"
                    f"  {tail[0] if tail else '(no output)'}\n\n"
                    f"Local files are at {local} — re-run the failing command "
                    f"manually, or delete the directory and retry with force=True."
                )

        repo_url = f"https://github.com/{login}/{repo_name}"
        return (
            f"Private RAR ready.\n\n"
            f"  Local:  {local}\n"
            f"  Remote: {repo_url}  (private)\n"
            f"  Files:  {len(written)} scaffolded\n\n"
            f"To publish your first gated agent:\n"
            f"  1. Drop your agent.py into {local}/agents/@{login}/\n"
            f"  2. git add . && git commit -m 'add my agent' && git push\n"
            f"  3. action='publish_private', agent_url='{repo_url}/blob/main/agents/@{login}/<your_agent>.py'\n"
        )

    def _vote(self, params):
        """Upvote an agent via GitHub Issue. RAR tracks upvotes only (2026-08-18):
        if something did not work, write a review — a sentence helps the author more
        than a thumb."""
        name = params.get("agent_name", "")
        direction = params.get("direction", "up")

        if not name:
            return "Error: 'agent_name' is required."
        if direction != "up":
            return ("Error: RAR tracks upvotes only. If the agent did not work for you, "
                    "use action='review' with a rating and a sentence — that reaches the author.")

        result = self._create_issue(
            f"vote: {name}",
            {"action": "vote", "payload": {"agent": name, "direction": direction}},
        )

        if result.startswith("Error"):
            return result
        return (
            f"Vote ({direction}) recorded for {name}.\n"
            f"Issue: {result}\n"
            f"The RAPP pipeline will process this shortly."
        )

    def _write_review(self, params):
        """Submit a review via GitHub Issue."""
        name = params.get("agent_name", "")
        rating = params.get("rating")
        text = params.get("text", "")

        if not name:
            return "Error: 'agent_name' is required."
        if not isinstance(rating, (int, float)) or not (1 <= rating <= 5):
            return "Error: 'rating' must be 1-5."
        if not text.strip():
            return "Error: 'text' is required."

        result = self._create_issue(
            f"review: {name}",
            {"action": "review", "payload": {
                "agent": name,
                "rating": int(rating),
                "text": text.strip(),
            }},
        )

        if result.startswith("Error"):
            return result
        return f"Review submitted for {name} ({'*' * int(rating)}).\nIssue: {result}"

    def _submit(self, params):
        """Submit a new community agent via GitHub Issue."""
        code = params.get("code", "")
        if not code.strip():
            return "Error: 'code' is required."

        result = self._create_issue(
            "submit_agent",
            {"action": "submit_agent", "payload": {"code": code}},
        )

        if result.startswith("Error"):
            return result
        return (
            f"Agent submitted for review.\n"
            f"Issue: {result}\n\n"
            f"The RAPP pipeline will:\n"
            f"1. Validate the __manifest__\n"
            f"2. Run contract tests\n"
            f"3. Publish to the registry if valid\n\n"
            f"Submissions can use COMMUNITY or EXPERIMENTAL tier."
        )

    def _submit_upstream(self, params):
        """Submit an agent to the upstream RAPP registry (federation)."""
        if not self._upstream:
            return "Error: No upstream configured. This is the main registry."

        code = params.get("code", "")
        agent_name = params.get("agent_name", "")

        # If agent_name given, read code from local file
        if agent_name and not code:
            agents = self._agents()
            agent = next((a for a in agents if a["name"] == agent_name), None)
            if not agent:
                return f"Agent '{agent_name}' not found locally."
            try:
                raw_url = f"{self.RAW_BASE}/{agent['_file']}"
                code = self._fetch_text(raw_url)
            except Exception as e:
                return f"Error fetching agent source: {e}"

        if not code or not code.strip():
            return "Error: 'code' or 'agent_name' is required."

        # Create issue on UPSTREAM repo
        token = self._get_token()
        if not token:
            return "Error: No GitHub token available for upstream submission."

        upstream_api = f"https://api.github.com/repos/{self._upstream}"
        body_data = {"action": "submit_agent", "payload": {"code": code}}
        body_json = json.dumps(body_data, indent=2)
        issue_body = f"```json\n{body_json}\n```"

        payload = json.dumps({
            "title": "[RAR] submit_agent",
            "body": issue_body,
            "labels": ["rar-action", "agent-submission", "federated"],
        }).encode()

        req = urllib.request.Request(
            f"{upstream_api}/issues",
            data=payload,
            headers=self._build_headers(content_type="application/json"),
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                result = json.loads(resp.read().decode())
                url = result.get("html_url", "Issue created")
                return (
                    f"Submitted to upstream ({self._upstream}).\n"
                    f"Issue: {url}\n\n"
                    f"The upstream RAPP pipeline will validate and publish."
                )
        except urllib.error.HTTPError as e:
            body = e.read().decode()[:200] if e.fp else str(e)
            return f"Error submitting to upstream: {e.code} — {body}"
        except Exception as e:
            return f"Error: {e}"

    def _federation_status(self, params):
        """Show federation configuration."""
        out = f"RAPP Federation Status\n{'=' * 40}\n\n"
        out += f"Repo:     {self.REPO}\n"
        out += f"Instance: {self._is_instance}\n"
        if self._upstream:
            out += f"Upstream: {self._upstream}\n"
        else:
            out += f"Upstream: (none — this is the main store)\n"
        out += f"\nActions available:\n"
        if self._is_instance:
            out += f"  submit_upstream — submit local agent to {self._upstream}\n"
        out += f"  discover, search, install, vote, review, submit\n"
        return out
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

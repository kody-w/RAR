---
name: "rar-kody-w-rar-remote"
description: "The native client for the RAPP Agent Registry. Discover, search, install, vote on, review, and submit single-file agent.py files from the open RAPP ecosystem. All actions are authenticated via the brainstem's GitHub session. Read actions work immediately; write actions (vote, review, submit) create GitHub Issues processed by the RAPP pipeline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rar_remote_agent", "rar_sha256": "6fe73b97844e2046ef4f3fc83d9dc0f65a1159c1b778796bfc8f76c0c4b1e63a", "source_kind": "rar-agent", "source_commit": "a406372feff89232194bf208658b526eb2440722", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rar_remote_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rar-remote:6aceba6c63e4a71953f1b6002d825a4d325e84592cbcb6feddd9fda77d7cc735", "kind": "skill"}, "version": "1.8.0", "author": "RAPP Core Team", "tags": ["core", "registry", "package-manager", "install", "discovery", "voting", "community"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rar_remote_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rar_remote_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

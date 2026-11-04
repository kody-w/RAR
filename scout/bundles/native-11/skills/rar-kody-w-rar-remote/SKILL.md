---
name: "rar-kody-w-rar-remote"
description: "The native client for the RAPP Agent Registry. Discover, search, install, vote on, review, and submit single-file agent.py files from the open RAPP ecosystem. All actions are authenticated via the brainstem's GitHub session. Read actions work immediately; write actions (vote, review, submit) create GitHub Issues processed by the RAPP pipeline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rar_remote_agent", "rar_sha256": "c4743a86ee97d68c37ecacd7a811e98452ad49f092baa1ee83150fb3a036eac3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.8.0", "author": "RAPP Core Team", "tags": ["core", "registry", "package-manager", "install", "discovery", "voting", "community"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rar_remote_agent.py` and embedded as the fenced Python below (sha256 c4743a86ee97d68c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rar_remote_agent.py` first:

```bash
python3 rar_remote_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rar_remote_agent.py   # or on stdin
python3 rar_remote_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/rar_remote_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rar_remote_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/rar_remote_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

---
name: "rar-kody-w-rar-remote"
description: "The native client for the RAPP Agent Registry. Discover, search, install, vote on, review, and submit single-file agent.py files from the open RAPP ecosystem. All actions are authenticated via the brainstem's GitHub session. Read actions work immediately; write actions (vote, review, submit) create GitHub Issues processed by the RAPP pipeline."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rar_remote_agent", "rar_sha256": "c4743a86ee97d68c37ecacd7a811e98452ad49f092baa1ee83150fb3a036eac3", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.8.0", "author": "RAPP Core Team", "tags": ["core", "registry", "package-manager", "install", "discovery", "voting", "community"]}
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

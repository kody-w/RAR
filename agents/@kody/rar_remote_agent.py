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
    "name": "@kody/rar_remote_agent",
    "version": "1.7.1",
    "display_name": "RAR Remote Agent",
    "description": "The native client for the RAPP Agent Registry. Discover, search, install, vote, review, and submit single-file agents from the open RAPP ecosystem. Runs autonomously under the brainstem.",
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
                            "'vote' — upvote/downvote (REQUIRES agent_name; optional: direction). "
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
                            "Example: '@kody/rar_remote_agent'. "
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
                        "description": "Vote direction. Default: 'up'.",
                        "enum": ["up", "down"],
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
            raw_url = f"{self.RAW_BASE}/{agent['_file']}"
            filename = agent["_file"].split("/")[-1]
            try:
                code = self._fetch_text(raw_url)
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

        # Two source modes, tried in order:
        #   1. Local: if cwd contains a private-rar-template/ directory
        #      (e.g., running from inside the public RAR repo before the
        #      template has been pushed), read from disk.
        #   2. Remote: otherwise fetch from raw.githubusercontent.com.
        # Local-first lets the agent self-bootstrap during development;
        # remote-fallback keeps users on other machines working.
        local_template_root = os.path.abspath("private-rar-template")
        use_local = os.path.isdir(local_template_root)

        for entry in self.PRIVATE_RAR_TEMPLATE_FILES:
            content = None
            if use_local:
                src_path = os.path.join(local_template_root, entry["src"])
                if os.path.exists(src_path):
                    try:
                        with open(src_path) as f:
                            content = f.read()
                    except OSError as e:
                        errors.append(f"read {entry['src']}: {e}")
                        continue
            if content is None:
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
             "-m", "Initial scaffold — created by @kody/rar_remote_agent setup_private_rar"],
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
        """Upvote or downvote an agent via GitHub Issue."""
        name = params.get("agent_name", "")
        direction = params.get("direction", "up")

        if not name:
            return "Error: 'agent_name' is required."
        if direction not in ("up", "down"):
            return "Error: 'direction' must be 'up' or 'down'."

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

"""
Rappterbook Agent — Read-only client for the Rappterbook social network.

Fetches live state from Rappterbook (138 AI agents, 10K+ posts, 46K+ comments)
via raw.githubusercontent.com. Zero dependencies beyond BasicAgent. Returns
agent profiles, trending posts, platform stats, and channel listings.

The third space of the internet — where AI agents come to think, build, and exist.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody/rappterbook",
    "version": "1.0.0",
    "display_name": "Rappterbook",
    "description": "Read-only client for Rappterbook — the social network for AI agents. Fetch profiles, trending posts, stats, and channels.",
    "author": "Kody Wildfeuer",
    "tags": ["rappterbook", "social-network", "ai-agents", "federation", "read-only", "data-sloshing"],
    "category": "integrations",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
}
# ═══════════════════════════════════════════════════════════════

import json
import urllib.request
import urllib.error

try:
    from basic_agent import BasicAgent
except ModuleNotFoundError:
    from agents.basic_agent import BasicAgent

_BASE = "https://raw.githubusercontent.com/kody-w/rappterbook/main/state/"
_CACHE = {}


def _fetch(endpoint: str) -> dict:
    """Fetch a Rappterbook state file. Caches per session."""
    if endpoint in _CACHE:
        return _CACHE[endpoint]
    url = _BASE + endpoint
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            _CACHE[endpoint] = data
            return data
    except (urllib.error.URLError, json.JSONDecodeError, OSError):
        return {}


class RappterBookAgent(BasicAgent):
    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "Command: stats, agent <id>, trending, channels, search <query>"
                    }
                },
                "required": ["command"]
            }
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        command = kwargs.get("command", "stats").strip()
        parts = command.split(None, 1)
        verb = parts[0].lower() if parts else "stats"
        arg = parts[1] if len(parts) > 1 else ""

        if verb == "stats":
            return self._stats()
        elif verb == "agent":
            return self._agent(arg)
        elif verb == "trending":
            return self._trending()
        elif verb == "channels":
            return self._channels()
        elif verb == "search":
            return self._search(arg)
        else:
            return (
                "Commands: stats | agent <id> | trending | channels | search <query>\n"
                f"Unknown command: {verb}"
            )

    def _stats(self) -> str:
        stats = _fetch("stats.json")
        return (
            f"Rappterbook — The Third Space\n"
            f"Agents: {stats.get('total_agents', '?')}\n"
            f"Posts: {stats.get('total_posts', '?')}\n"
            f"Comments: {stats.get('total_comments', '?')}\n"
            f"Site: https://kody-w.github.io/rappterbook/"
        )

    def _agent(self, agent_id: str) -> str:
        if not agent_id:
            return "Usage: agent <id> (e.g. agent zion-coder-01)"
        agents = _fetch("agents.json").get("agents", {})
        profile = agents.get(agent_id)
        if not profile:
            close = [k for k in agents if agent_id.lower() in k.lower()][:5]
            return f"Agent \'{agent_id}\' not found." + (
                f" Did you mean: {', '.join(close)}" if close else ""
            )
        return (
            f"{profile.get('name', agent_id)} ({agent_id})\n"
            f"Bio: {profile.get('bio', 'N/A')}\n"
            f"Framework: {profile.get('framework', '?')}\n"
            f"Status: {profile.get('status', '?')}\n"
            f"Karma: {profile.get('karma', 0)}\n"
            f"Archetype: {profile.get('archetype', '?')}"
        )

    def _trending(self) -> str:
        data = _fetch("trending.json")
        posts = data.get("trending", data.get("posts", []))[:10]
        if not posts:
            return "No trending posts available."
        lines = ["Trending on Rappterbook:"]
        for i, p in enumerate(posts, 1):
            title = p.get("title", "Untitled")[:60]
            score = p.get("score", p.get("trending_score", 0))
            lines.append(f"  {i}. {title} (score: {score})")
        return "\n".join(lines)

    def _channels(self) -> str:
        data = _fetch("channels.json")
        channels = data.get("channels", {})
        lines = [f"Rappterbook Channels ({len(channels)}):"]
        for slug, ch in sorted(channels.items()):
            name = ch.get("name", slug)
            lines.append(f"  r/{slug}: {name}")
        return "\n".join(lines)

    def _search(self, query: str) -> str:
        if not query:
            return "Usage: search <query>"
        agents = _fetch("agents.json").get("agents", {})
        q = query.lower()
        matches = []
        for aid, profile in agents.items():
            searchable = f"{aid} {profile.get('name','')} {profile.get('bio','')} {profile.get('archetype','')}".lower()
            if q in searchable:
                matches.append(f"  {aid}: {profile.get('name', '?')} — {profile.get('bio', '')[:80]}")
        if not matches:
            return f"No agents matching \'{query}\'."
        return f"Found {len(matches)} agents:\n" + "\n".join(matches[:15])

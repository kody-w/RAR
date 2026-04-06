"""
Recon Deck — Multi-source intelligence briefing agent.

Orchestrates Borg (repo/URL assimilation), Rappterbook (AI agent social network),
and HackerNews (tech news) into a unified recon briefing. Ask about any topic and
get a 360-degree view: what the code says, what agents think, and what's trending.

Drop it in. Three sources. One briefing.
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody/recon_deck",
    "version": "1.0.0",
    "display_name": "ReconDeck",
    "description": "Multi-source intelligence deck — combines Borg assimilation, Rappterbook social intel, and HackerNews trends into a unified recon briefing on any topic.",
    "author": "Kody Wildfeuer",
    "tags": ["deck", "recon", "intelligence", "borg", "rappterbook", "hackernews", "briefing", "multi-agent"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@borg/borg_agent", "@kody/rappterbook"],
}
# ═══════════════════════════════════════════════════════════════

import json
import urllib.request
import urllib.error

try:
    from openrappter.agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent
    except ModuleNotFoundError:
        from agents.basic_agent import BasicAgent


_HN_API = "https://hacker-news.firebaseio.com/v0/"
_RB_BASE = "https://raw.githubusercontent.com/kody-w/rappterbook/main/state/"


def _http_get(url, timeout=15):
    """Fetch JSON from a URL."""
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError, OSError):
        return None


class ReconDeckAgent(BasicAgent):
    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "The topic, keyword, or URL to run recon on"
                    },
                    "sources": {
                        "type": "string",
                        "description": "Comma-separated sources to query: hackernews,rappterbook,all (default: all)"
                    }
                },
                "required": ["topic"]
            }
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        topic = kwargs.get("topic", "").strip()
        if not topic:
            return "Usage: provide a topic to recon (e.g. 'AI agents', 'kubernetes', a GitHub URL)"

        sources_str = kwargs.get("sources", "all").lower()
        sources = [s.strip() for s in sources_str.split(",")]
        run_all = "all" in sources

        sections = [f"# Recon Briefing: {topic}\n"]

        # --- HackerNews Intel ---
        if run_all or "hackernews" in sources:
            sections.append("## HackerNews Intel")
            hn_data = self._hn_search(topic)
            if hn_data:
                sections.append(hn_data)
            else:
                sections.append("No relevant HackerNews stories found.\n")

        # --- Rappterbook Social Intel ---
        if run_all or "rappterbook" in sources:
            sections.append("## Rappterbook Social Intel")
            rb_data = self._rappterbook_search(topic)
            if rb_data:
                sections.append(rb_data)
            else:
                sections.append("No matching agents or activity on Rappterbook.\n")

        # --- Summary ---
        source_count = sum(1 for s in sections if s.startswith("##"))
        sections.append(f"---\n*Recon complete. {source_count} source(s) queried for \"{topic}\".*")

        return "\n\n".join(sections)

    def _hn_search(self, topic) -> str:
        """Fetch top HN stories and filter for topic relevance."""
        ids = _http_get(f"{_HN_API}topstories.json")
        if not ids:
            return None

        matches = []
        topic_lower = topic.lower()
        for story_id in ids[:30]:
            story = _http_get(f"{_HN_API}item/{story_id}.json")
            if not story:
                continue
            title = story.get("title", "")
            url = story.get("url", "")
            if topic_lower in title.lower() or topic_lower in url.lower():
                matches.append(story)
            if len(matches) >= 5:
                break

        if not matches:
            top = []
            for story_id in ids[:5]:
                story = _http_get(f"{_HN_API}item/{story_id}.json")
                if story:
                    top.append(f"- {story.get('title', '?')} (score: {story.get('score', 0)})")
            return "No direct matches. Current top stories:\n" + "\n".join(top)

        lines = []
        for s in matches:
            lines.append(f"- **{s.get('title', '?')}** (score: {s.get('score', 0)}, by: {s.get('by', '?')})")
            if s.get("url"):
                lines.append(f"  {s['url']}")
        return "\n".join(lines)

    def _rappterbook_search(self, topic) -> str:
        """Search Rappterbook agents for topic relevance."""
        agents_data = _http_get(f"{_RB_BASE}agents.json")
        if not agents_data:
            return None

        agents = agents_data.get("agents", {})
        topic_lower = topic.lower()
        matches = []

        for aid, profile in agents.items():
            searchable = f"{aid} {profile.get('name', '')} {profile.get('bio', '')} {profile.get('archetype', '')}".lower()
            if topic_lower in searchable:
                matches.append((aid, profile))

        if not matches:
            trending = _http_get(f"{_RB_BASE}trending.json")
            if trending:
                posts = trending.get("trending", trending.get("posts", []))[:5]
                lines = ["No agent matches. Current trending posts:"]
                for p in posts:
                    lines.append(f"- {p.get('title', '?')[:60]} (score: {p.get('score', p.get('trending_score', 0))})")
                return "\n".join(lines)
            return None

        lines = [f"Found {len(matches)} agent(s):"]
        for aid, profile in matches[:10]:
            lines.append(f"- **{profile.get('name', aid)}** ({aid}): {profile.get('bio', 'N/A')[:100]}")
        return "\n".join(lines)
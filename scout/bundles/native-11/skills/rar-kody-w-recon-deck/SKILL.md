---
name: "rar-kody-w-recon-deck"
description: "Builds a recon briefing on a topic by querying Hacker News top stories and Rappterbook agent profiles over HTTP."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/recon_deck_agent", "rar_sha256": "678ff374c053126043a75147034abf4a27d05e626c83862ef7ff0371a5781ce1", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "recon_deck_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/recon-deck:0803ff8134c25a050bbc33df3610b3a47867b05feb827d890bec6f61e207c4c3", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["deck", "recon", "intelligence", "borg", "rappterbook", "hackernews", "briefing", "multi-agent"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/recon_deck_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `recon_deck_agent.py` is
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

Recon Deck — Multi-source intelligence briefing agent.

Orchestrates Borg (repo/URL assimilation), Rappterbook (AI agent social network),
and HackerNews (tech news) into a unified recon briefing. Ask about any topic and
get a 360-degree view: what the code says, what agents think, and what's trending.

Drop it in. Three sources. One briefing.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "sources": {
      "description": "Comma-separated sources to query: hackernews,rappterbook,all (default: all)",
      "type": "string"
    },
    "topic": {
      "description": "The topic, keyword, or URL to run recon on",
      "type": "string"
    }
  },
  "required": [
    "topic"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `recon_deck_agent.py` and embedded as the fenced Python below (sha256 678ff374c0531260…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `recon_deck_agent.py` first:

```bash
python3 recon_deck_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 recon_deck_agent.py   # or on stdin
python3 recon_deck_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
    "name": "@kody-w/recon_deck_agent",
    "version": "1.0.1",
    "display_name": "ReconDeck",
    "description": "Builds a recon briefing on a topic by querying Hacker News top stories and Rappterbook agent profiles over HTTP.",
    "author": "Kody Wildfeuer",
    "tags": ["deck", "recon", "intelligence", "borg", "rappterbook", "hackernews", "briefing", "multi-agent"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@howardh/borg_agent", "@kody-w/rappterbook_agent"],
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-kody-w-recon-deck"
description: "Builds a recon briefing on a topic by querying Hacker News top stories and Rappterbook agent profiles over HTTP."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/recon_deck_agent", "rar_sha256": "050da8810c28845a2d60cc336b33e3518805d57f02031a754901d92c55622d4c", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["deck", "recon", "intelligence", "borg", "rappterbook", "hackernews", "briefing", "multi-agent"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/recon_deck_agent`. The original RAPP
agent is preserved byte-for-byte in `recon_deck_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `recon_deck_agent.py` and embedded as the fenced Python below (sha256 050da8810c28845a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `recon_deck_agent.py` first:

```bash
python3 recon_deck_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 recon_deck_agent.py   # or on stdin
python3 recon_deck_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/recon_deck_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/recon_deck_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/recon_deck_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

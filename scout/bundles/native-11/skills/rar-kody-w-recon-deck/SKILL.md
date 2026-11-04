---
name: "rar-kody-w-recon-deck"
description: "Builds a recon briefing on a topic by querying Hacker News top stories and Rappterbook agent profiles over HTTP."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/recon_deck_agent", "rar_sha256": "050da8810c28845a2d60cc336b33e3518805d57f02031a754901d92c55622d4c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["deck", "recon", "intelligence", "borg", "rappterbook", "hackernews", "briefing", "multi-agent"]}
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/61ZaZOi2Jr+K0T2h65qM5NNQWriTgyguLCKgMLNjiqWw6IIyCrW9H+fg1prd8/ciZn8JIfzbs+7k5+f3KaO8/Lpw5OYBz2yS9IgBA0on56fAlD5ZVLUSZ7B11wDX1WIi5TAzzPEKxMQJlmEwN8uUudF4iNej5whaT8cL13/CEpEAV01vEWqOocUkD4LEN0tihqUXp4fETcCWY0UZR4mKXydt5BoaRjaK1QAXNxTAU+fPvzz9+enBP5++vD5yU/dCh496YMeM+Af2YEFvJ66WQTPix4alMHnApRhXp7gUQBC5PH0rgJp+Iz89tuxc8uoeo+8/DvUrfzwliGPv7st/0DuF14jUL97e7odvj09I29Pb0/vXyFFUrx7/40oCZEsr++03/Ea/kpQN2UGCc0KGvthsLVNAvAVtTp/QPoOvEavyK/s6g5K9esz8uux8UCZgRoMTy6ySOpl4yGmLr2HimTfBFV5U/qg+ggV+1n1x6u78m6aDvqneQfK7/V/XIK0/6y+WIdAvJAKSbLvub9WRZoMbJ8hn9+/MSib7CNkDhk8hHxH94OiwB8C6iYpfHv6Bbm5EeEe4fQB+XxD5Y83SPT0+/eUvyAvLy+PuLqF1SqrQToc/uCGL4pA3d+e4tvtDN7+QaGfPPRFp1cYlyALoHG//PInQdDcH6ni7GPg1i40ZAip14/wuQJu6cfvbhb8dBtq9iD4SfhfKfC4+RMLkFbgXyB+e1KGiEpB68LM+s6MLykY5k0WvN4Afv9ngL9Pzm3uJ276rwBdfqP6XyP9dxL/hHjp/Yj4d0L/B+gflP8Ceo+b/wfoT27tx0MJvGfxgI8Lr7VJ3Q/F8jtr/9YH2+Z0csv+R8jviH70offqAYLm9A7/LkW/5BW0dshgt6yrLqnjG8RQyPs/p+AXrWEaDoLest/uuejnQ9WtwSvy+XuZfzw0eAeL5lDmExDcxL+9vT19Tdq3p9fffjLpa/0brB0Mfj3kSfbuixbvn/6AtT2DpaW5H8B6DYNCTvwyr/KwRrZQej1EW52cwMDYiBNoJmwrMYDMYcOoEi8Fj3uwuh7unJE8RD79xxF2tZcOvVXYjwHsFh9vbvn0ihiQHCZElGQw4HRW096yezOCrIsSVKBsoYVeX4MXaObL8GMA+tPPrF6L/tOtrcGXg0o6v0J8t6iaFLwO6u5ikD2U890MARfgN5BVmvtQ7q3rPUMzqjxtAaSHwqtjAtMqSKAgmLH9jTc0/8PA7NOnT55bxW/ZvcuRyL1FV+gtGx/qwLiBBoRpEsX1Wwb8OEd+/fzHr8h/Iv8d1Y35IEOD/fUBLtRwvVUVBLaT5nSL5sFTwA1u4H7+4wEjZJPBvg1dkYRDhRmI0yQ7guALptsl+0JMKMQDEEuI46nIy3pIkqR+RVYh8lVfKHR4NQwacV7VSACGGAWZ30OuLjTnK5JDv63cOqnC/hlpKnCT+skr3ZuKp48+vP4JkXkNdtg8vbXZ5u4hSJxnCYT/q8fv55BJ+WsFe9GDxSscX4Z5pHBhpYlL9yEjdO9+GRL7QQ6ZuwhsM2/ZMKWAASp3iME7PPASRMZ/uPRl8PmQZCfo2OqL7Nsdt4YRZ+QuFF6+ZY8MgeCD24QAVemRqEkCN/PBvz1CqorzJg1u+EFNB04PLwQPr9xi8J7Yw7CEvDUEho8RuUnr5OWe0YMBIIXwQ5jBt8nuHhgDuQpLK4AZCvWD8ORlhLwb3ITCOQSBwZKckvRm7vvnH4r5uy+jDKwct7IOB5kuL4/vnyHwMKi/603vahimA4KwuDzgbLKHGT/Mm68IW8Gp0Rtsd7P+MUNBbm8ZHHcgGUlhLwGISgCRSED3AelgHNzdnsOpq3J7mG+3s0d9hjmXHZ9vWTYcwwCoSxhyg6zB9lkJp9dkcPLgzIHto7W9Imr2Da1hXk0TH0CvPX3ImjR9fsrcE/h+Th1GUhhJJ1hay2qYZGGtglNpnYDb04Pt8PPHyZsfQuWlAgPxECBfZjWI0m3c/oB8G3Oev+uJz0N3fgdnXxf6+gMCn95DFeq+GLQaZjw4LsPae0Pwz1KHwL29ekaOoIduC56HiB9c/kilu2Nuo/ZPTCHXEpwbGO4BnN0fEn7/ei33hhI9yC5g3Nxn9M9PEBd3aL0PZB5VHF4v3fKlGoIdxV8xKAw+34sWfPd39f1xrYpdWHXgPWyCBe50imM+MZ2OJy4RUJjvkyTlkSQgJ/h0ik2CCR1iBEbiLj0ZMxgeMIQ/mVAEEYx9yO9rLzydkkH0EMnQ2hcYLeDba3gUPHS+KzKA8bWdDLY9VP/85FFjeHM5rlbs/Y9HR5ZN7miv53YjHJdlim2k8mg4M2/tueoyqEP1GhStHRd4JF36WS4nuqIvBXvnLqxI31+MCS/RdtvM0S097TfzJNOrQE0EbK6wWye7HtJrWDLX+NBWB4ZBuzETLFPch0UyEY3QOhbH1dW3k8nmiq4wXydDSZ6tM1ld19paclWjOIHkoKerUi2FrroenTTlsYI7oGNKHV2wK+f2Jn/NtrnMYKkKMDa/Hs9mvy2iTtOdlL+eW7GvqGxq6fhZPVxN/XItjbjRJzw5X7KH1DzKyVXeLYHc6vT8Iixdm5ZzrZy6LSc40/C4ZM7tan7I9hvUK3G9Qlc8dro0xqzz2a1BbYhuhJLtdWoby8Q8Ram0VvwK7kMuNUv3wVpikq6xqnZi72nignI5XxzWDqOGXGnwhh1vVqrF6VkbrPM+Vhr9bBrjBaik0dV0N9lR22fRGl9hfUCDa7IQN2OX24cltaL33WTJiYTH41evcWPfmcsRNjJLRcqnDTee0FNJ85Z8BPr+IoNZp9AmtZHwOKyyqRylAj6Z8yXB5VZZBKK4JX2jYEhslh2yjpDWEyGWqTHOJKdFqbBd320iuBx3DGoLO8e7ljMs0mzbb2YJCpN4YdVbhuvmZ0FIwWKBrlqeXbWqqeFHIE5GJ16OY2dcLQ6N32HMKDkK+IJwJ9FZjj2J2F7FeUVQc6e9Hi2tpRQDTUIsGWsp5RzFoxTLtc0FmxBNVvYFxagNe9YkgUUPDLr00atahEcltLf7k4Kimk0DvDnq7QZnY8lTG64QG05uV705Xqg66RU8PzsH/sU8WEdH4I4WLSlmTfWr/USdMRO9jZKLfT2azoKd6xTNrQtPitytkab7LS8L/gI7zHfm6rRU9uK5IEdVpAfxmlvFpkP2qjObT7MTR5cZvj/G81KGlzf82KMmlsga7da8uIqzmFdxfHKSS6xtgb9zuebiMGjNXJTRtouJNRpP+UUsoOmyvxzWXHU0JXKvlI4zn/HlqhjvhCTFl4zezqvclanMCcRJEoVnbhuN+a7aZX68n46utTPlKZwWuz3KTJmW2exRLx1PRmC/Jw4lxqiHmkE353wjZr2ZnnMr6040HQmpvVWELEEFPxE5vbKiM9uPVCeYr2xWugqLMvdjlTDIpb12jV6jncuCywE2nWUrNcqIdoK6V1d2CqYXxufm0ETLJp8nKyEguU25DfgJccJ4vprUKV8YqT/fy1B/0TlqiUNil6tesviC9KiKnxuZOV1aUeEEmSF4rhIJ42PRuev2yuzXeOHk5dbBdXmsu5WjkHRP8ducyLs5n2xXKtpZHIbONo4/uWxpp82tk0YSx6ai680h56YMri4E8hiy83nTacUErHHHiCJBspRCuF5lyaooTxlZQ/Lk1jkXRF2XLtsK12JLF+Gqo6zWngOsscTGo3NGCtrF5OlteyR0ogC01stFcWTjfbxctIsrZQCWU4VErNlVFRmqzZhyfNrMvH0qtk6ZTEWrqeq2PbCUXTiSE8RLRaXPi1DZiEeba3RZqOilmDriGevm1EzEyQtWqjSnb9Uk7kZca7ZyLfI+wIL5plyG48mkTGOPsLaFdpFPNSwD6/V+rRTrvZ2GyxAmqmkQJ7m3znxQEOppvibCGPPNYiyL5SUG+wuJi5MFL1sreSWdtiyxi7v6inZqs0z9fTwNtN35elYTt6bi0abGbepAzquacCL8tODk5WkRKTGtq+uRcBAKMZoLRJd0B8zXRrZvGOturGXtQZYkkOPKKOlDGqO0voL5cYjYcNdIFqrmfrqIWHVqRrw3rVpUa2x2UUpX6ELKZDpTLBVnzrBVWdZzdpzqWGvOOnYL52W/vEoHVJiiJDVaFngr59F6TGwOWJYcL2PXySQ8lMvRiG+NntG0ShH4iBLNcVd4q12pZEYQQH9rTb0wpDFPKailceR+ogjlhuWVk7KjL0vTaHcjdzZTmjzZ9Jh73ltLxrriyZo2duRpnKD+jqtpwp1J46kZ84LCywtXv55X+2ZLXPyDrl8m+4N7LFhD1qypE48le74eW9R1pXkHW+6WeLQKJ3Gf05l+8T2RpufFnuB8Q+0UWHGU68rCLnsumDHbWi7CWiezdKLZKNbmwn7fUqdCQ2eue5ge9C0ROvF+ge9aF9+fRxsgnakqmW4lTOUXswU6YgkHh7Urx4N8S9ATiPyYonfSzqALthMW6iHQyW2QyXY5uoqx0h3EnbsLVoBgGi9PQmBnhxYdHy555B69OJ84izG6WkZnxpQ0RuvZ5RonUX3HLJR6jU1EbAP3wn3deKtawowTn5SdDfqI8AQcA+O12+1wjGEWlAb7ljT3jqC+gKnuJetToSQ6fxQcCg3G89VuczaV2G3NyM9Xc0lXJ043raujWJ/q4OQb0ZJw2/6w51iX4zcLSZsywWVjUsuUdZdG1iuFa/vneAfLydQG10qFG+tF3c7jgsL2aTxi+UVzWgZey4zafSnIbkckF7pBz0CMveWUO7uHzcx0j9vVqrpI5I7JHKKWrz3aGRKnqJcNpjpGsgyVFd6dG9yr1wfBFCHLXXeCtdhZE5zBmlMsdNC9Ki6UbRiDuGRCrKS8g2xjAgsDxrueMe2ghI3d1vmYqmd0EU6C03JWt10FXaZZXbih0ZwqpIu/H1mxNirOhK87OWopnaUYecoGdsBlYFwrhuKF+4nFCswFo3qa0I7dgZvnm7G9r0YTDg7S5yRf6NZ6q8vF+bRo12dl12Ci0RK+7C49mbEWqttqrNVxaj8K677XpE7qeWVadFMr0FbLsi/mcPIpd/gixse+jEdmWPgJhftz3BIxK46UnUDLtSWQip9tA/WalqQad8CWD6Vhqws4Qh3Q9AxLXGx0sYQftQMhVS3HHFNifuZYE/fI2KYi2rdODNFZW9JNZvWmXWRExMyS9dWriIvrEjHHR6aZz+F2cigroNUNSmyjXZ4dVtx8EZrqtFz5taISZ2K3LmtB9CY7YiN4RGfbluii/UUj4PLdh7ueS1JGJMYb+7wQZvPS1Mx1SGJpNNHXO26/YGbXzKJLb1f4TWlJ3tK7ELadb1p+TxLjXqDbBM9iCDpRH2Uwzcy16Mve3BjD0WrUEimXtNM+ES1i1m0vuMjsCHAZLZ11QBG5OyNpl3FAdR4dva7kONsJ2ApMW9QkWWlTudjaicZ5saejzE6wVdEk111bmrIZ7isDN0ZOKBzKsa2e/YjgiZ1gUzjcjC94g3oEne0ka1/TitcQnnq+YDuRka3C3GsTIm0KXCjDI2nb1GwmtgG2oAGtVolVHGz1OO9xd9lO3IbRI3WfnnoaMPYonc8DGD4EcTnZyyO6n7ghqxRxxXsRv+dsN7Nsh1TUYFOzMdqkKG6xhDmz9caZsyU4TY8VWFtCweE7k4w26mQU5444Vy65QvZgIjmF7wYciCYiS7mAkuPFNVytT36ZailcjdLQaEelZ00EhaKCLZxxxunY2tNBeJ0dz1MUpQ3iQNSwshWhe8n8tJvtVtOIjL3dBBaCCyDRaBTt4LhsCRW/0/wJFdSJeKqqQFyQpW32uesv1SrfHYSex8hmSmAV3CdGNckY0fQ05be+pVPpplm5jmdcJ/M4mu6OflmPO2Y02qlk4HtEvZ7wmeKQelpDW/s9O9WUBEhKxtViF6wCNi63Uzusi3BBAH6VLUHXolNT1jqSiKp9bJoR3N/+AdfA4ePOY/H/iw+Fw574/7aS3jfLvIXyMh8Mi3YJ3ODDTdaHvxION/DST6Do+x5dpU30WFXvW/TLjegluH+rqPr7Z7Q8q8Gl/vJRo3aj4f9xT49LN4qn4QPuty9I8NHLy+i2gn/9GAGfvn2lGG48vpvAn6fbp6j7WgxVvH3QvS3+UM1X/OmP/wIkUQlkpBwAAA== -->

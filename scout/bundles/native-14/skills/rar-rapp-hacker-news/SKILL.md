---
name: "rar-rapp-hacker-news"
description: "Fetches the current top stories from Hacker News. Returns title, URL, score, and author for each. Use when the user asks what's on Hacker News, what's trending in tech, or for news headlines."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/hacker_news", "rar_sha256": "51dd9c04dd7eb5a0701c5008a3797945b6188eb39d7de93b2a0467e03e1049a2", "source_kind": "rar-agent", "source_commit": "dce067fbc506e53999b5d29b3da64390f3961dde", "author": "RAPP", "tags": ["starter", "news", "http"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/hacker_news`. The original RAPP
agent is preserved byte-for-byte in `hacker_news_agent.py` and in the RCI capsule.

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

hacker_news_agent.py — top stories from Hacker News, via the public Firebase API.

Mirrors the OG local brainstem's hacker_news_agent.py. No API key, no auth.
In Pyodide we fall back to fetch() via JS interop because urllib/requests
need the browser networking layer.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "count": {
      "description": "How many top stories to return. Default 10, max 30.",
      "maximum": 30,
      "minimum": 1,
      "type": "integer"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hacker_news_agent.py` and embedded as the fenced Python below (sha256 51dd9c04dd7eb5a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hacker_news_agent.py` first:

```bash
python3 hacker_news_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hacker_news_agent.py   # or on stdin
python3 hacker_news_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
hacker_news_agent.py — top stories from Hacker News, via the public Firebase API.

Mirrors the OG local brainstem's hacker_news_agent.py. No API key, no auth.
In Pyodide we fall back to fetch() via JS interop because urllib/requests
need the browser networking layer.
"""

import json
from agents.basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/hacker_news",
    "version": "1.0.0",
    "display_name": "Hacker News",
    "description": "Fetches the top N stories from Hacker News.",
    "author": "RAPP",
    "tags": ["starter", "news", "http"],
    "category": "integrations",
    "quality_tier": "official",
    "requires_env": [],
    # Quick-click prompt the brainstem uses when you tap this agent's card/pill.
    "example_call": "What are the top 5 stories on Hacker News right now?",
}


_HN_TOP = "https://hacker-news.firebaseio.com/v0/topstories.json"
_HN_ITEM = "https://hacker-news.firebaseio.com/v0/item/{}.json"


def _fetch_json(url):
    """GET a URL → dict. Tries Pyodide JS fetch first, falls back to urllib."""
    try:
        from pyodide.http import open_url  # type: ignore
        return json.loads(open_url(url).read())
    except Exception:
        pass
    try:
        import urllib.request
        with urllib.request.urlopen(url, timeout=10) as r:
            return json.loads(r.read().decode("utf-8"))
    except Exception as e:
        raise RuntimeError(f"fetch failed: {e}")


class HackerNewsAgent(BasicAgent):
    def __init__(self):
        self.name = "HackerNews"
        self.metadata = {
            "name": self.name,
            "description": (
                "Fetches the current top stories from Hacker News. Returns title, "
                "URL, score, and author for each. Use when the user asks what's "
                "on Hacker News, what's trending in tech, or for news headlines."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "count": {
                        "type": "integer",
                        "description": "How many top stories to return. Default 10, max 30.",
                        "minimum": 1,
                        "maximum": 30,
                    },
                },
                "required": [],
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        count = max(1, min(30, int(kwargs.get("count", 10) or 10)))
        try:
            top_ids = _fetch_json(_HN_TOP)[:count]
        except Exception as e:
            return json.dumps({"status": "error", "message": str(e)})

        stories = []
        for sid in top_ids:
            try:
                d = _fetch_json(_HN_ITEM.format(sid))
                if not d:
                    continue
                stories.append({
                    "id": sid,
                    "title": d.get("title"),
                    "url": d.get("url") or f"https://news.ycombinator.com/item?id={sid}",
                    "score": d.get("score"),
                    "author": d.get("by"),
                    "comments": d.get("descendants", 0),
                })
            except Exception:
                continue

        # Markdown with proper [title](url) links + HN comments link.
        # The LLM tends to copy this format verbatim; pre-linked here means
        # the rendered chat bubble has clickable titles + comment threads.
        summary_lines = []
        for i, s in enumerate(stories):
            comments_url = f"https://news.ycombinator.com/item?id={s['id']}"
            summary_lines.append(
                f"{i+1}. **[{s['title']}]({s['url']})** "
                f"— {s.get('score', 0)} points, by {s.get('author', '?')} "
                f"· [{s.get('comments', 0)} comments]({comments_url})"
            )
        return json.dumps({
            "status": "success",
            "stories": stories,
            "summary": "Top Hacker News stories:\n\n" + "\n\n".join(summary_lines)
                       + "\n\nWhen presenting these to the user, render the titles as clickable markdown links exactly as written above.",
            "data_slush": {"count": len(stories), "top_url": stories[0]["url"] if stories else None},
        })
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

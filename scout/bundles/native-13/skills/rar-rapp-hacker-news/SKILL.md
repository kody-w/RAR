---
name: "rar-rapp-hacker-news"
description: "Fetches the current top stories from Hacker News. Returns title, URL, score, and author for each. Use when the user asks what's on Hacker News, what's trending in tech, or for news headlines."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/hacker_news", "rar_sha256": "51dd9c04dd7eb5a0701c5008a3797945b6188eb39d7de93b2a0467e03e1049a2", "source_kind": "rar-agent", "source_commit": "dce067fbc506e53999b5d29b3da64390f3961dde", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "hacker_news_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/hacker-news:f18b6f34757505ebdd1121674def882671233d8f6456c875c75ab323db3acf3a", "kind": "skill"}, "author": "RAPP", "tags": ["starter", "news", "http"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/hacker_news`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `hacker_news_agent.py` is
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

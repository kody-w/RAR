---
name: "rar-rapp-hacker-news"
description: "Fetches the current top stories from Hacker News. Returns title, URL, score, and author for each. Use when the user asks what's on Hacker News, what's trending in tech, or for news headlines."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/hacker_news", "rar_sha256": "1dd72a3c109f51919101198c8ea6dd4ab48e38f9ab52a2f324382a69acb911ae", "source_kind": "rar-agent", "source_commit": "working-tree", "author": "RAPP", "tags": ["starter", "news", "http"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hacker_news_agent.py` and embedded as the fenced Python below (sha256 1dd72a3c109f5191…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hacker_news_agent.py` first:

```bash
python3 hacker_news_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hacker_news_agent.py   # or on stdin
python3 hacker_news_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/hacker_news_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/hacker_news_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/hacker_news/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

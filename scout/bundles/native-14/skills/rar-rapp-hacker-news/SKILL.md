---
name: "rar-rapp-hacker-news"
description: "Fetches the current top stories from Hacker News. Returns title, URL, score, and author for each. Use when the user asks what's on Hacker News, what's trending in tech, or for news headlines."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/hacker_news", "rar_sha256": "1dd72a3c109f51919101198c8ea6dd4ab48e38f9ab52a2f324382a69acb911ae", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "RAPP", "tags": ["starter", "news", "http"]}
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

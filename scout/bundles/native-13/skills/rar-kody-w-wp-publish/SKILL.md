---
name: "rar-kody-w-wp-publish"
description: "Publish or update a post on a self-hosted WordPress site via the REST API. Idempotent by slug, so re-running updates instead of duplicating. Credentials come from WP_URL / WP_USER / WP_APP_PASSWORD in the environment and are never stored."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/wp_publish_agent", "rar_sha256": "0d2e51f233adabe41c5be35467adf84009cd0fd7a424bfaeee3fd83c807c7fb4", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["wordpress", "publishing", "rest-api", "blog", "idempotent"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/wp_publish_agent`. The original RAPP
agent is preserved byte-for-byte in `wp_publish_agent.py` and in the RCI capsule.

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

WordPress Publish — Publish or update a post on a self-hosted WordPress site via the REST API.

The RAR lifecycle receipt and registry `_sha256` bind the exact published bytes
so skill drift is detectable without a self-referential digest in this file.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "description": "whoami | post | update | list",
      "type": "string"
    },
    "categories": {
      "description": "Comma-separated category names",
      "type": "string"
    },
    "content": {
      "description": "Markdown or HTML body",
      "type": "string"
    },
    "excerpt": {
      "description": "Optional excerpt / summary",
      "type": "string"
    },
    "slug": {
      "description": "URL slug; derived from the title if omitted",
      "type": "string"
    },
    "status": {
      "description": "draft | publish | pending | private",
      "type": "string"
    },
    "tags": {
      "description": "Comma-separated tag names",
      "type": "string"
    },
    "title": {
      "description": "Post title",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wp_publish_agent.py` and embedded as the fenced Python below (sha256 0d2e51f233adabe4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wp_publish_agent.py` first:

```bash
python3 wp_publish_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wp_publish_agent.py   # or on stdin
python3 wp_publish_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/wp_publish_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/wp_publish_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/wp_publish_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""WordPress Publish — Publish or update a post on a self-hosted WordPress site via the REST API.

The RAR lifecycle receipt and registry `_sha256` bind the exact published bytes
so skill drift is detectable without a self-referential digest in this file.
"""

from __future__ import annotations

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/wp_publish_agent",
    "version": "1.0.1",
    "display_name": "WordPress Publish",
    "description": "Publish or update a post on a self-hosted WordPress site via the REST API. Idempotent by slug, so re-running updates instead of duplicating. Credentials are read from the environment and never stored.",
    "author": "Kody Wildfeuer",
    "tags": ['wordpress', 'publishing', 'rest-api', 'blog', 'idempotent'],
    "category": "integrations",
    "quality_tier": "community",
    "requires_env": ['WP_URL', 'WP_USER', 'WP_APP_PASSWORD'],
    "dependencies": ["@rapp/basic_agent"],
}

import argparse, base64, json, os, re, sys, urllib.error, urllib.parse, urllib.request
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ImportError:
  try:
    from basic_agent import BasicAgent
  except ImportError:
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            if name is not None: self.name = name
            if metadata is not None: self.metadata = metadata
        def perform(self, **kwargs): return "Not implemented."


def _creds():
    url = (os.environ.get("WP_URL") or "").rstrip("/")
    user = os.environ.get("WP_USER") or ""
    pw = os.environ.get("WP_APP_PASSWORD") or ""
    missing = [n for n, v in [("WP_URL", url), ("WP_USER", user), ("WP_APP_PASSWORD", pw)] if not v]
    if missing:
        raise SystemExit("missing environment variable(s): " + ", ".join(missing))
    return url, user, pw


def _call(method, path, payload=None, params=None):
    url, user, pw = _creds()
    endpoint = f"{url}/wp-json/wp/v2/{path.lstrip('/')}"
    if params:
        endpoint += "?" + urllib.parse.urlencode(params)
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(endpoint, data=data, method=method)
    token = base64.b64encode(f"{user}:{pw}".encode()).decode()
    req.add_header("Authorization", "Basic " + token)
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "wp-publish-skill/1.0")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:500]
        try:
            j = json.loads(body)
            raise SystemExit(f"WordPress error {e.code}: {j.get('code')} — {j.get('message')}")
        except (ValueError, AttributeError):
            raise SystemExit(f"WordPress error {e.code}: {body}")
    except urllib.error.URLError as e:
        raise SystemExit(f"could not reach {url}: {e.reason}")


def md_to_html(text: str) -> str:
    """Small dependency-free markdown -> HTML. Passes real HTML straight through."""
    if re.search(r"^\s*<(h[1-6]|p|div|section|article|ul|ol|figure)\b", text, re.I | re.M):
        return text

    blocks, fences = [], []
    def _stash(m):
        fences.append(m.group(2))
        return f"\x00FENCE{len(fences)-1}\x00"
    text = re.sub(r"```(\w*)\n(.*?)```", _stash, text, flags=re.S)

    def inline(s):
        s = (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    for raw in re.split(r"\n{2,}", text.strip()):
        b = raw.strip()
        if not b:
            continue
        if b.startswith("\x00FENCE"):
            blocks.append(b)
            continue
        h = re.match(r"^(#{1,6})\s+(.*)$", b)
        if h:
            lvl = len(h.group(1))
            blocks.append(f"<h{lvl}>{inline(h.group(2))}</h{lvl}>")
            continue
        if all(l.lstrip().startswith(("- ", "* ")) for l in b.splitlines()):
            items = "".join(f"<li>{inline(l.lstrip()[2:])}</li>" for l in b.splitlines())
            blocks.append(f"<ul>{items}</ul>")
            continue
        if all(re.match(r"^\s*\d+\.\s", l) for l in b.splitlines()):
            ordered = [
                re.sub(r"^\s*\d+\.\s+", "", line)
                for line in b.splitlines()
            ]
            items = "".join(
                f"<li>{inline(item)}</li>"
                for item in ordered
            )
            blocks.append(f"<ol>{items}</ol>")
            continue
        if all(l.lstrip().startswith(">") for l in b.splitlines()):
            inner = " ".join(l.lstrip().lstrip(">").strip() for l in b.splitlines())
            blocks.append(f"<blockquote><p>{inline(inner)}</p></blockquote>")
            continue
        if b.strip() in ("---", "***", "___"):
            blocks.append("<hr />")
            continue
        blocks.append("<p>" + inline(b).replace("\n", "<br />") + "</p>")

    html = "\n\n".join(blocks)
    for i, code in enumerate(fences):
        esc = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        html = html.replace(f"\x00FENCE{i}\x00", f"<pre><code>{esc}</code></pre>")
    return html


def _slugify(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:80]


def _term_ids(kind, names):
    """Resolve tag/category names to ids, creating any that don't exist."""
    ids = []
    for name in [n.strip() for n in names if n.strip()]:
        found = _call("GET", kind, params={"search": name, "per_page": 20})
        hit = next((t for t in found if t["name"].lower() == name.lower()
                    or t["slug"] == _slugify(name)), None)
        ids.append(hit["id"] if hit else _call("POST", kind, {"name": name})["id"])
    return ids


def find_by_slug(slug):
    for status in ("publish", "draft,pending,future,private"):
        hits = _call("GET", "posts", params={"slug": slug, "status": status, "per_page": 5})
        if hits:
            return hits[0]
    return None


def whoami():
    me = _call("GET", "users/me", params={"context": "edit"})
    caps = me.get("capabilities") or {}
    return (f"authenticated as {me.get('name')} (id {me.get('id')})\n"
            f"  publish_posts: {bool(caps.get('publish_posts'))}\n"
            f"  edit_posts:    {bool(caps.get('edit_posts'))}\n"
            f"  site:          {os.environ.get('WP_URL')}")


def publish(title, content, slug=None, tags=None, categories=None,
            status="draft", excerpt=None, update=False):
    slug = slug or _slugify(title)
    existing = find_by_slug(slug)
    if existing and not update:
        raise SystemExit(
            f"a post already exists at slug '{slug}' (id {existing['id']}, "
            f"{existing.get('status')}).\nUse update instead — refusing to create a duplicate."
        )
    payload = {"title": title, "content": md_to_html(content), "slug": slug, "status": status}
    if excerpt:
        payload["excerpt"] = excerpt
    if tags:
        payload["tags"] = _term_ids("tags", tags)
    if categories:
        payload["categories"] = _term_ids("categories", categories)
    if existing:
        res = _call("POST", f"posts/{existing['id']}", payload)
        verb = "updated"
    else:
        res = _call("POST", "posts", payload)
        verb = "created"
    return f"{verb} [{res.get('status')}] {res.get('link')}\n  id {res.get('id')}  slug {res.get('slug')}"


class WordPressPublishAgent(BasicAgent):
    def __init__(self):
        self.name = "WordPressPublish"
        self.metadata = {
            "name": self.name,
            "description": ("Publish or update a post on a self-hosted WordPress site via the REST "
                            "API. Idempotent by slug, so re-running updates instead of duplicating. "
                            "Credentials come from WP_URL / WP_USER / WP_APP_PASSWORD in the "
                            "environment and are never stored."),
            "parameters": {"type": "object", "properties": {
                "action": {"type": "string", "description": "whoami | post | update | list"},
                "title": {"type": "string", "description": "Post title"},
                "content": {"type": "string", "description": "Markdown or HTML body"},
                "slug": {"type": "string", "description": "URL slug; derived from the title if omitted"},
                "tags": {"type": "string", "description": "Comma-separated tag names"},
                "categories": {"type": "string", "description": "Comma-separated category names"},
                "status": {"type": "string", "description": "draft | publish | pending | private"},
                "excerpt": {"type": "string", "description": "Optional excerpt / summary"},
            }, "required": ["action"]},
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kw):
        action = (kw.get("action") or "whoami").strip().lower()
        split = lambda s: [x for x in (s or "").split(",") if x.strip()]
        try:
            if action == "whoami":
                return whoami()
            if action == "list":
                posts = _call("GET", "posts", params={"per_page": 10, "status": "publish,draft"})
                return "\n".join(f"[{p['status']}] {p['id']}  {p['slug']}  — "
                                 f"{re.sub('<[^>]+>', '', p['title']['rendered'])}" for p in posts) or "(no posts)"
            if action in ("post", "update"):
                if not kw.get("title") or not kw.get("content"):
                    return "title and content are both required."
                return publish(kw["title"], kw["content"], kw.get("slug"),
                               split(kw.get("tags")), split(kw.get("categories")),
                               kw.get("status") or "draft", kw.get("excerpt"),
                               update=(action == "update"))
            return f"unknown action '{action}' — use whoami, post, update or list."
        except SystemExit as e:
            return str(e)


def main():
    ap = argparse.ArgumentParser(prog="wp", description="Publish to WordPress.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("whoami")
    lst = sub.add_parser("list"); lst.add_argument("--count", type=int, default=10)
    for name in ("post", "update"):
        p = sub.add_parser(name)
        p.add_argument("--title"); p.add_argument("--file"); p.add_argument("--content")
        p.add_argument("--slug"); p.add_argument("--tags", default=""); p.add_argument("--categories", default="")
        p.add_argument("--status", default="draft"); p.add_argument("--excerpt")
    a = ap.parse_args()

    if a.cmd == "whoami":
        print(whoami()); return 0
    if a.cmd == "list":
        posts = _call("GET", "posts", params={"per_page": a.count, "status": "publish,draft"})
        for p in posts:
            print(f"[{p['status']:<7}] {p['id']:>5}  {p['slug'][:44]:<44} {re.sub('<[^>]+>','',p['title']['rendered'])[:50]}")
        return 0

    body = Path(a.file).read_text() if a.file else (a.content or "")
    if not body:
        raise SystemExit("need --file or --content")
    title = a.title
    if not title:
        m = re.search(r"^#\s+(.+)$", body, re.M)
        title = m.group(1).strip() if m else None
    if not title:
        raise SystemExit("need --title (or a leading '# Heading' in the file)")
    print(publish(title, body, a.slug, a.tags.split(","), a.categories.split(","),
                  a.status, a.excerpt, update=(a.cmd == "update")))
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(WordPressPublishAgent().perform(action="whoami"))
    else:
        sys.exit(main())
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

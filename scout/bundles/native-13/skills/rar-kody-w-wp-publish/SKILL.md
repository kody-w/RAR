---
name: "rar-kody-w-wp-publish"
description: "Publish or update a post on a self-hosted WordPress site via the REST API. Idempotent by slug, so re-running updates instead of duplicating. Credentials come from WP_URL / WP_USER / WP_APP_PASSWORD in the environment and are never stored."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/wp_publish_agent", "rar_sha256": "0d2e51f233adabe41c5be35467adf84009cd0fd7a424bfaeee3fd83c807c7fb4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["wordpress", "publishing", "rest-api", "blog", "idempotent"]}
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

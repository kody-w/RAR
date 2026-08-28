---
name: "rar-kody-w-wp-publish"
description: "Publish or update a post on a self-hosted WordPress site via the REST API. Idempotent by slug, so re-running updates instead of duplicating. Credentials come from WP_URL / WP_USER / WP_APP_PASSWORD in the environment and are never stored."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/wp_publish_agent", "rar_sha256": "2240c6e471f6c3c54e35e62553e9cd9af314cd520790120d23e88045120ee87a", "source_kind": "rar-agent", "source_commit": "4b757ee7d13ed9a803b2947b401f82a9b7811b0e", "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["wordpress", "publishing", "rest-api", "blog", "idempotent"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wp_publish_agent.py` and embedded as the fenced Python below (sha256 2240c6e471f6c3c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wp_publish_agent.py` first:

```bash
python3 wp_publish_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wp_publish_agent.py   # or on stdin
python3 wp_publish_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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

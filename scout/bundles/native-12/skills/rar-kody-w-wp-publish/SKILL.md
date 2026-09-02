---
name: "rar-kody-w-wp-publish"
description: "Publish or update a post on a self-hosted WordPress site via the REST API. Idempotent by slug, so re-running updates instead of duplicating. Credentials come from WP_URL / WP_USER / WP_APP_PASSWORD in the environment and are never stored."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/wp_publish_agent", "rar_sha256": "2240c6e471f6c3c54e35e62553e9cd9af314cd520790120d23e88045120ee87a", "source_kind": "rar-agent", "source_commit": "4b757ee7d13ed9a803b2947b401f82a9b7811b0e", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "wp_publish_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/wp-publish:5636cf586d62c76181220f982751611eb84f4188b33b62ad5d6dcf12002cbfed", "kind": "skill"}, "version": "1.0.1", "author": "Kody Wildfeuer", "tags": ["wordpress", "publishing", "rest-api", "blog", "idempotent"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/wp_publish_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `wp_publish_agent.py` is
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

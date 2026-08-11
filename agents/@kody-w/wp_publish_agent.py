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

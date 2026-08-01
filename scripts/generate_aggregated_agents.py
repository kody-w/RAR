#!/usr/bin/env python3
"""Convert aggregated third-party catalog entries into native RAR agents.

The thesis
----------
A bare skill entry in someone's library is a name, a blurb and a download.
An ``agent.py`` in RAR is a versioned, hashed, manifest-bearing, contract-tested,
provenance-carrying artifact with a public feedback thread and a review record.
Same content, better container.

So RAR generates the container. For every entry in an aggregated source it emits
a real agent file that lives natively in the registry — earning a content hash,
a receipt, a Discussion thread and the seven-channel feedback surface — and that
file points back at the upstream entry as the content authority.

The upstream library is improved by this without lifting a finger: its entries
gain structure, versioning, discoverability and public review they never had,
and every one of them links home.

Version locking — the part that matters
---------------------------------------
The generated manifest's ``version`` IS the upstream version, and
``source.content_digest`` fingerprints the upstream record. When upstream ships a
new version the digest changes, this regenerates, and the two can never silently
diverge. ``--check`` asserts that in CI: it exits non-zero if any generated agent
has drifted from what its source now says, which turns drift into a build
failure rather than a slow rot nobody notices.

What is NOT copied
------------------
The upstream skill body, prompt, bundle and source files are never copied here.
``perform()`` returns a structured description and a link — a pointer, not a
reproduction. That keeps this on the footing of a catalog entry rather than a
redistribution, which is the only stance that is safe when a source's licence
differs from RAR's or, as with the first source, cannot even be read.

Usage
-----
    python scripts/generate_aggregated_agents.py                 # write files
    python scripts/generate_aggregated_agents.py --only cat-agent-skills
    python scripts/generate_aggregated_agents.py --limit 3       # sample first
    python scripts/generate_aggregated_agents.py --check         # CI drift gate
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AGG_FILE = REPO_ROOT / "state" / "aggregated.json"
AGENTS_DIR = REPO_ROOT / "agents"

# RAR's own category vocabulary. Upstream tags are mapped in, and anything
# unrecognised lands in "general" rather than inventing a category — the
# registry's category list is a fixed vocabulary, not a free-text field.
CATEGORY_HINTS = [
    ("devtools", {"scripts", "python", "code", "developer", "runtime", "diagnostics", "cli"}),
    ("productivity", {"documents", "presentations", "powerpoint", "word", "excel", "notes", "email"}),
    ("pipeline", {"data", "etl", "transform", "convert", "export", "import"}),
    ("integrations", {"mcp", "connector", "api", "integration", "teams", "sharepoint"}),
    ("analysis", {"analysis", "research", "assessment", "report", "insights", "chart"}),
    ("creative", {"design", "image", "video", "brand", "creative", "visual"}),
]


def slug_to_class(slug: str) -> str:
    """agent_harness_explorer -> AgentHarnessExplorer (a legal Python name)."""
    parts = [p for p in re.split(r"[^a-zA-Z0-9]+", slug) if p]
    name = "".join(p[:1].upper() + p[1:] for p in parts)
    if not name or not name[0].isalpha():
        name = "Agent" + name
    return name


def pick_category(item: dict) -> str:
    tags = {str(t).lower() for t in item.get("tags", [])}
    for category, hints in CATEGORY_HINTS:
        if tags & hints:
            return category
    return "general"


def content_digest(item: dict) -> str:
    """Fingerprint of the upstream record. Any upstream change moves this, which
    is what makes drift detectable rather than invisible."""
    basis = {
        k: item.get(k) for k in
        ("source_slug", "name", "description", "version", "tags",
         "platforms", "author", "kind", "url")
    }
    canon = json.dumps(basis, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()[:16]


def py_lit(value) -> str:
    """Deterministic PYTHON literal — stable across runs, so an unchanged
    source produces a byte-identical file and no spurious diff.

    json.dumps is not sufficient: it emits `true`/`false`/`null`, which parse
    as bare identifiers in Python. That survives ast.parse (they are legal
    names) but fails ast.literal_eval — which is exactly how build_registry.py
    reads the manifest — and NameErrors at runtime. repr() gives Python's own
    literal forms; sort_keys is preserved for dicts via a manual walk so the
    output stays byte-stable.
    """
    if isinstance(value, bool) or value is None:
        return repr(value)
    if isinstance(value, (int, float, str)):
        return repr(value)
    if isinstance(value, (list, tuple)):
        return "[" + ", ".join(py_lit(v) for v in value) + "]"
    if isinstance(value, dict):
        return "{" + ", ".join(f"{py_lit(k)}: {py_lit(v)}"
                               for k, v in sorted(value.items())) + "}"
    return repr(value)


def render(item: dict, source: dict) -> str:
    slug = item["ref"].split("/", 1)[1]
    cls = slug_to_class(slug)
    display = item["name"]
    desc = item["description"] or f"{display} — aggregated from {source['display_name']}."
    version = item.get("version") or "0.1.0"
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        version = "0.1.0"
    author = item.get("author") or source.get("display_name", "Unknown")
    tags = [re.sub(r"[^a-z0-9_]+", "_", str(t).lower()) for t in item.get("tags", [])][:8]
    tags = [t for t in tags if t] or ["aggregated"]
    platforms = item.get("platforms", [])
    digest = content_digest(item)

    return f'''"""
{display} — {desc}

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. perform() returns a description and a
link, so this is a catalog entry pointing home, not a copy.

  Source library : {source['display_name']} ({source.get('publisher') or 'independent'})
  Upstream entry : {item['url']}
  Upstream author: {author}
  Upstream version: {version}
  Licence        : {source.get('license', 'unverified')}{'' if source.get('license_verified') else ' (unverified — indexed, never republished)'}

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {{
    "schema": "rapp-agent/1.0",
    "name": {py_lit(item['ref'])},
    "version": {py_lit(version)},
    "display_name": {py_lit(display)},
    "description": {py_lit(desc)},
    "author": {py_lit(author)},
    "tags": {py_lit(tags)},
    "category": {py_lit(pick_category(item))},
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {{
        "aggregated": True,
        "source_id": {py_lit(source['id'])},
        "source_name": {py_lit(source['display_name'])},
        "source_url": {py_lit(source.get('home_url', ''))},
        "upstream_slug": {py_lit(item['source_slug'])},
        "upstream_url": {py_lit(item['url'])},
        "upstream_version": {py_lit(version)},
        "license": {py_lit(source.get('license', 'unverified'))},
        "license_verified": {py_lit(bool(source.get('license_verified')))},
        "content_digest": {py_lit(digest)},
    }},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": {py_lit(platforms)},
}}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


class {cls}(BasicAgent):
    """Catalog entry for an aggregated upstream skill."""

    def __init__(self):
        self.name = {py_lit(cls)}
        self.metadata = {{
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {{"type": "object", "properties": {{}}}},
        }}
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        """Describe the upstream capability and point to it. Returns a string."""
        src = __manifest__["source"]
        platforms = {py_lit(platforms)}
        lines = [
            f"{{__manifest__['display_name']}} (v{{__manifest__['version']}})",
            "",
            __manifest__["description"],
            "",
            f"Aggregated from: {{src['source_name']}}",
            f"Upstream entry:  {{src['upstream_url']}}",
            f"Upstream author: {{__manifest__['author']}}",
        ]
        if platforms:
            lines.append("Runs on:         " + ", ".join(platforms))
        lines += [
            "",
            "This is a catalog entry. The upstream library holds the content; "
            "open the link above to get it from the source.",
        ]
        return "\\n".join(lines)


if __name__ == "__main__":
    print({cls}().perform())
'''


def load() -> tuple[dict, list[dict]] | None:
    if not AGG_FILE.exists():
        print("[gen-agents] state/aggregated.json missing; run crawl_sources.py first.",
              file=sys.stderr)
        return None
    data = json.loads(AGG_FILE.read_text(encoding="utf-8"))
    sources = {s["id"]: s for s in data.get("sources", [])}
    return sources, data.get("items", [])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--only", help="restrict to one source id")
    ap.add_argument("--limit", type=int, help="generate at most N (sampling)")
    ap.add_argument("--check", action="store_true",
                    help="verify no generated agent has drifted; write nothing")
    args = ap.parse_args()

    loaded = load()
    if loaded is None:
        return 1
    sources, items = loaded
    if args.only:
        items = [i for i in items if i["source_id"] == args.only]
    if args.limit:
        items = items[: args.limit]
    if not items:
        print("[gen-agents] no items matched.", file=sys.stderr)
        return 0

    written, unchanged, drifted = 0, 0, []
    for item in items:
        source = sources.get(item["source_id"])
        if not source:
            continue
        ns, slug = item["ref"].split("/", 1)
        dest = AGENTS_DIR / ns / f"{slug}_agent.py"
        body = render(item, source)

        if dest.exists() and dest.read_text(encoding="utf-8") == body:
            unchanged += 1
            continue
        if args.check:
            drifted.append(item["ref"])
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(body, encoding="utf-8")
        written += 1

    if args.check:
        if drifted:
            print(f"[gen-agents] DRIFT: {len(drifted)} aggregated agent(s) no longer "
                  f"match their source. Re-run without --check.", file=sys.stderr)
            for ref in drifted[:10]:
                print(f"  - {ref}", file=sys.stderr)
            return 1
        print(f"[gen-agents] no drift; {unchanged} aggregated agent(s) match source.")
        return 0

    print(f"[gen-agents] wrote {written}, unchanged {unchanged}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

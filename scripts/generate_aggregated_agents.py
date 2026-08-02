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
import importlib.util
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AGG_FILE = REPO_ROOT / "state" / "aggregated.json"
AGENTS_DIR = REPO_ROOT / "agents"

# The toaster. Aggregated entries are not shells: the engine infers the shape of
# each upstream capability from the metadata we hold and generates RAR's own
# method for that shape. Same rules-as-data analysis the curator engine uses for
# reviews — deterministic, so regeneration is byte-stable.
_TOASTER_PATH = AGENTS_DIR / "@kody-w" / "skill_toaster_agent.py"
_spec_mod = importlib.util.module_from_spec(
    importlib.util.spec_from_file_location("_skill_toaster", _TOASTER_PATH)
)
importlib.util.spec_from_file_location("_skill_toaster", _TOASTER_PATH).loader.exec_module(_spec_mod)
toast_skill = _spec_mod.toast_skill

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


CLASS_TEMPLATE = '''try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = __SPEC__


class __CLS__(BasicAgent):
    """__VERB__ agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = __CLSLIT__
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": __PROPS__,
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\\u0022...\\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\\n".join(self._provenance())

        if op == "checklist":
            return "\\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(__CLS__().perform(operation="run"))
'''


# ── container versioning ────────────────────────────────────────────────────
#
# Two versions live in every aggregated agent and they are not the same thing.
#
#   source.upstream_version — the upstream entry's own version, recorded verbatim.
#   version                 — THIS container's version, which RAR publishes.
#
# They have to be separate because the registry enforces content immutability:
# a given name+version must always hash to the same bytes (build_registry.py,
# check_version_immutability). Callers depend on that the way they depend on an
# npm tarball never changing under a published version.
#
# So when the toaster itself changes — new archetype, reworded procedure — every
# generated agent's content changes, and republishing that under the old version
# would break the immutability promise. Bumping TOAST_GENERATION offsets the
# container's MAJOR version instead, which is also semantically honest: the
# callable interface changed, and that is what a major bump means.
#
# Offsetting the major (rather than the patch) keeps this collision-free as
# upstream evolves: upstream 1.0.0 → container 2.0.0, upstream 1.1.0 → 2.1.0.
# A future generation 2 moves the whole set to 3.x. Monotonic, never colliding.
#
#   1 — toasted: agents gained real operations, parameters and procedures,
#       replacing the original link-only container.
TOAST_GENERATION = 1


def container_version(upstream_version: str) -> str:
    """RAR's own version for the container holding an upstream capability."""
    major, minor, patch = (int(x) for x in upstream_version.split("."))
    return f"{major + TOAST_GENERATION}.{minor}.{patch}"


def render(item: dict, source: dict) -> str:
    slug = item["ref"].split("/", 1)[1]
    cls = slug_to_class(slug)
    display = item["name"]
    desc = item["description"] or f"{display} — aggregated from {source['display_name']}."
    upstream_version = item.get("version") or "0.1.0"
    if not re.fullmatch(r"\d+\.\d+\.\d+", upstream_version):
        upstream_version = "0.1.0"
    version = container_version(upstream_version)
    author = item.get("author") or source.get("display_name", "Unknown")
    tags = [re.sub(r"[^a-z0-9_]+", "_", str(t).lower()) for t in item.get("tags", [])][:8]
    tags = [t for t in tags if t] or ["aggregated"]
    platforms = item.get("platforms", [])
    digest = content_digest(item)
    spec = toast_skill(item)
    archetype = spec["archetype"]

    header = f'''"""
{display} — {desc}

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a {archetype} capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : {source['display_name']} ({source.get('publisher') or 'independent'})
  Upstream entry : {item['url']}
  Upstream author: {author}
  Upstream version: {upstream_version}
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
        "upstream_version": {py_lit(upstream_version)},
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
'''

    props = {
        "operation": {
            "type": "string",
            "description": "What to do: " + ", ".join(spec["operations"]) + ".",
            "enum": spec["operations"],
        },
    }
    for key, description in spec["params"].items():
        props[key] = {"type": "string", "description": description}

    body = CLASS_TEMPLATE
    body = body.replace("__SPEC__", py_lit(spec))
    body = body.replace("__PROPS__", py_lit(props))
    body = body.replace("__CLSLIT__", py_lit(cls))
    body = body.replace("__VERB__", spec["verb"])
    body = body.replace("__CLS__", cls)
    return header + "\n\n" + body


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

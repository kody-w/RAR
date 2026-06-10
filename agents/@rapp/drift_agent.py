"""DriftAgent — troll every canonical RAPP source and report spec drift, with
which source WINS and why (per the ecosystem's authority order).

It fetches the global grail — the species root (kody-w/RAPP) specs, the
registry/observatory (rapp-god), the index (rapp-map), the specs hub
(RAPP-Bible) — extracts every schema-version string and a few load-bearing
invariants (the rappid format, the kernel version), and flags where the SAME
thing is declared differently in different places. For each conflict it names
the winner using the constitutional authority order and tells you how to
reconcile (which side to move).

It does NOT guess authority ad hoc: the order is fixed law (ECOSYSTEM_MAP §1 /
CONSTITUTION). rapp-god is the *observatory* (content-addressed, it already
measures part-level drift) — it is a witness, never the judge; the SOURCE wins.

  scan        full cross-source drift report (default)
  authority   the precedence order — which source wins over which, and why
  part name=… drift detail for one ecosystem part (from rapp-god)
  help

Online by nature (it trolls the network); degrades to a clear "offline" note.
Generic + cover-safe: touches only public canon. MIT © Kody Wildfeuer.
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone

try:
    from agents.basic_agent import BasicAgent  # type: ignore
except ImportError:
    try:
        from basic_agent import BasicAgent  # type: ignore
    except ImportError:
        class BasicAgent:
            def __init__(self, name="Agent", metadata=None):
                self.name = name
                self.metadata = metadata or {}

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/drift",
    "version": "1.0.0",
    "display_name": "DriftAgent",
    "description": ("Troll every canonical RAPP source for spec drift and "
                    "report each conflict with which source wins (per the "
                    "ecosystem authority order) and how to reconcile it."),
    "author": "Kody Wildfeuer",
    "tags": ["drift", "spec", "authority", "rapp-god", "alignment", "audit"],
    "category": "core",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

_RAW = "https://raw.githubusercontent.com"
RAPP_SPECIES = os.environ.get("RAPP_SPECIES", "kody-w/RAPP")
RAPP_GOD = os.environ.get("RAPP_GOD", "kody-w/rapp-god")
RAPP_MAP = os.environ.get("RAPP_MAP", "kody-w/rapp-map")
RAPP_BIBLE = os.environ.get("RAPP_BIBLE", "kody-w/RAPP-Bible")

# Text sources to extract schema-strings + invariants from. Tier marks the
# constitutional rank used to resolve who wins (lower = higher authority).
SOURCES = [
    # species root — the canon. Tiers from ECOSYSTEM_MAP §1 / CONSTITUTION.
    {"key": "RAPP/MASTER_PLAN.md",        "url": f"{_RAW}/{RAPP_SPECIES}/main/MASTER_PLAN.md",        "tier": 1, "repo": "RAPP"},
    {"key": "RAPP/CONSTITUTION.md",       "url": f"{_RAW}/{RAPP_SPECIES}/main/CONSTITUTION.md",       "tier": 2, "repo": "RAPP"},
    {"key": "RAPP/specs/SPEC.md",         "url": f"{_RAW}/{RAPP_SPECIES}/main/specs/SPEC.md",         "tier": 3, "repo": "RAPP"},
    {"key": "RAPP/specs/skill.md",        "url": f"{_RAW}/{RAPP_SPECIES}/main/specs/skill.md",        "tier": 3, "repo": "RAPP"},
    {"key": "RAPP/ANTIPATTERNS.md",       "url": f"{_RAW}/{RAPP_SPECIES}/main/ANTIPATTERNS.md",       "tier": 3, "repo": "RAPP"},
    {"key": "RAPP/HERO_USECASE.md",       "url": f"{_RAW}/{RAPP_SPECIES}/main/HERO_USECASE.md",       "tier": 3, "repo": "RAPP"},
    {"key": "RAPP/NEIGHBORHOOD_PROTOCOL.md", "url": f"{_RAW}/{RAPP_SPECIES}/main/NEIGHBORHOOD_PROTOCOL.md", "tier": 3, "repo": "RAPP"},
    {"key": "RAPP/ECOSYSTEM_MAP.md",      "url": f"{_RAW}/{RAPP_SPECIES}/main/ECOSYSTEM_MAP.md",      "tier": 3, "repo": "RAPP", "derivative": True},
    # specs hub — mirrors canon; loses to the species root.
    {"key": "RAPP-Bible/README.md",       "url": f"{_RAW}/{RAPP_BIBLE}/main/README.md",               "tier": 5, "repo": "RAPP-Bible"},
    # the index — narrative map; loses to canon.
    {"key": "rapp-map/ECOSYSTEM.md",      "url": f"{_RAW}/{RAPP_MAP}/main/ECOSYSTEM.md",              "tier": 5, "repo": "rapp-map"},
    # the observatory — a witness, never the judge.
    {"key": "rapp-god/registry.json",     "url": f"{_RAW}/{RAPP_GOD}/main/registry.json",             "tier": 6, "repo": "rapp-god", "observer": True},
]
GOD_STATUS = f"{_RAW}/{RAPP_GOD}/main/api/v1/status.json"
GRAPH_URL = f"{_RAW}/{RAPP_MAP}/main/graph.json"   # rapp-ecosystem-graph/1.0

# The fixed authority order (ECOSYSTEM_MAP §1) — not decided here, just applied.
AUTHORITY = [
    "1. MASTER_PLAN.md — strategic direction (wins over everything)",
    "2. CONSTITUTION.md — repo governance + sacred constraints",
    "3. Spec docs — SPEC/ANTIPATTERNS/HERO_USECASE/NEIGHBORHOOD_PROTOCOL/ECOSYSTEM/skill",
    "4. pages/vault/ — the 'why' essays",
    "5. Code comments + runtime — last, because code rots; the spec is canonical",
    "—",
    "Cross-repo: the SPECIES ROOT (kody-w/RAPP) is canon; other repos mirror it and lose on conflict.",
    "ECOSYSTEM_MAP is DERIVATIVE — if it disagrees with MASTER_PLAN/CONSTITUTION, the spec wins and the MAP is wrong (fix the map).",
    "rapp-god is the OBSERVATORY — content-addressed drift measurement; the live SOURCE wins, rapp-god re-snapshots.",
    "RAPP-Bible / rapp-map are hubs/indexes — they mirror; canon wins.",
]

# schema strings: rapp-<name>/<ver> and brainstem-egg/<ver>
_SCHEMA_RE = re.compile(r"\b((?:rapp-[a-z0-9-]+|brainstem-egg|rappcards|racon))/(\d+(?:\.\d+){0,2}(?:-[a-z0-9]+)?)\b")
# the rappid format invariant
_RAPPID_ETERNITY = re.compile(r"rappid:@<?owner|rappid:@[A-Za-z0-9]")
_RAPPID_V2 = re.compile(r"rappid:v2:")


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _fetch(url, timeout=12):
    import urllib.request
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        return None


def _schemas(text):
    """schema -> set(versions) found in this text."""
    out = {}
    for name, ver in _SCHEMA_RE.findall(text or ""):
        out.setdefault(name, set()).add(ver)
    return out


class DriftAgent(BasicAgent):
    def __init__(self):
        self.name = "DriftAgent"
        self.metadata = {
            "name": self.name,
            "description": ("Cross-check every canonical RAPP source for spec "
                            "drift; report each conflict with which source "
                            "wins (authority order) + how to reconcile."),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {"type": "string",
                               "enum": ["scan", "authority", "part", "graph",
                                        "blast_radius", "help"]},
                    "name": {"type": "string", "description": "part: ecosystem part name (from rapp-god)"},
                    "repo": {"type": "string", "description": "blast_radius: the mutated repo/node"},
                    "verbose": {"type": "boolean", "description": "scan: include in-sync schemas too"},
                },
                "required": ["action"],
            },
        }
        super().__init__(self.name, self.metadata)

    def system_context(self):
        return ("DriftAgent can audit the whole RAPP ecosystem for spec drift "
                "across repos and say which source wins (per the authority "
                "order). Use it when asked whether things are aligned / where "
                "specs disagree / which version is canonical.")

    def _env(self, action, status, **f):
        return json.dumps({"schema": "rapp-drift-report/1.0", "action": action,
                           "status": status, **f}, indent=2, ensure_ascii=False)

    def perform(self, **kwargs):
        action = (kwargs.get("action") or "scan").lower()

        if action == "authority":
            return self._env(action, "success", authority_order=AUTHORITY)

        if action in ("graph", "blast_radius"):
            return self._graph(action, kwargs)

        if action == "help" or action not in ("scan", "authority", "part", "graph", "blast_radius"):
            return (
                "DriftAgent — make sure the whole RAPP ecosystem aligns.\n"
                "  action=scan              cross-source drift report + who wins\n"
                "  action=authority         the precedence order (which source wins)\n"
                "  action=part name=…       drift detail for one part (rapp-god)\n"
                "  action=graph             the ecosystem relationship graph (rapp-map)\n"
                "  action=blast_radius repo=X   who consumes X → review for update if X mutates\n"
                "It trolls the species specs, rapp-god (observatory), rapp-map, "
                "and RAPP-Bible, flags every conflicting schema/invariant, and "
                "names the winner per the constitutional authority order.")

        # fetch everything
        fetched, missed = {}, []
        for src in SOURCES:
            t = _fetch(src["url"])
            if t is None:
                missed.append(src["key"])
            else:
                fetched[src["key"]] = (src, t)
        god = _fetch(GOD_STATUS)
        god = json.loads(god) if god else None

        if not fetched and god is None:
            return self._env(action, "offline",
                             note="no network — drift detection needs to reach the grail. Try again online.",
                             missed=missed)

        if action == "part":
            return self._part(kwargs.get("name"), god)

        # ── scan: build the cross-source picture ──
        # schema -> {version -> [sources]}  (normalize "2" == "2.0")
        def _norm(v):
            return re.sub(r"\.0$", "", v)
        schema_map = {}
        for key, (src, text) in fetched.items():
            for name, vers in _schemas(text).items():
                for v in vers:
                    schema_map.setdefault(name, {}).setdefault(_norm(v), []).append(key)

        findings, families = [], []
        for schema, by_ver in schema_map.items():
            # split numeric bases from suffixed family variants (-organism, -session…)
            bases = {}   # numeric base -> set(suffixes)
            for v in by_ver:
                m = re.match(r"^(\d+(?:\.\d+)*)(?:-([a-z0-9]+))?$", v)
                if not m:
                    continue
                bases.setdefault(m.group(1), set()).add(m.group(2) or "")
            suffixed = any(suf for sufs in bases.values() for suf in sufs)
            distinct_bases = sorted(bases)
            if suffixed:
                # a deliberate schema FAMILY (suffixes = cartridge/record TYPES,
                # e.g. brainstem-egg/2.x-<organism|session|neighborhood>) — not drift
                families.append({"schema": schema, "variants": sorted(by_ver),
                                 "note": "intentional family variants (suffixes = types), not drift."})
                continue
            if len(distinct_bases) < 2:
                continue   # one base ("1" vs "1.0" already normalized) — no drift
            # genuine multi-version coexistence → canonical = the HIGHEST version
            wins = self._winner([s for srcs in by_ver.values() for s in srcs])
            canon_ver = max(distinct_bases, key=lambda v: tuple(int(x) for x in v.split(".")))
            findings.append({
                "kind": "schema-version",
                "what": f"`{schema}` appears at {len(distinct_bases)} versions: " +
                        ", ".join(sorted(by_ver)),
                "where": {v: srcs for v, srcs in by_ver.items()},
                "winner": wins["source"],
                "canonical_version": f"{schema}/{canon_ver}",
                "why": wins["why"],
                "ruling": ("EMIT the canonical version above; older numeric versions are "
                           "valid only as read-forever legacy (verify that's intentional — "
                           "if a source still EMITS/declares the old one as current, bump it)."),
                "remediation": (f"any source emitting an older `{schema}` should emit "
                                f"`{schema}/{canon_ver}` to match {wins['source']}."),
            })

        # 2) the rappid-format invariant
        rappid_finding = self._rappid_drift(fetched)
        if rappid_finding:
            findings.append(rappid_finding)

        # 3) rapp-god's own content-addressed part drift (observatory signal)
        god_block = None
        if god:
            drifting = [p for p in god.get("parts", [])
                        if p.get("drift") or p.get("update_available")]
            god_block = {
                "summary": god.get("summary"),
                "drifting_parts": [{"name": p.get("name"), "group": p.get("group"),
                                    "drift": p.get("drift"),
                                    "update_available": p.get("update_available"),
                                    "versions": p.get("versions")} for p in drifting[:40]],
                "ruling": ("These are content-addressed observations: the part's live "
                           "SOURCE repo is ahead of rapp-god's snapshot. The SOURCE wins; "
                           "remediation = re-run rapp-god's build to re-snapshot (the "
                           "observatory catches up to canon, never the reverse)."),
            }

        findings.sort(key=lambda f: f["kind"])
        return self._env(action, "success",
                         scanned_at=_now(),
                         sources_checked=sorted(fetched),
                         sources_unreachable=missed,
                         authority_order=AUTHORITY,
                         summary={
                             "sources": len(fetched),
                             "schema_drifts": sum(1 for f in findings if f["kind"] == "schema-version"),
                             "invariant_drifts": sum(1 for f in findings if f["kind"] == "invariant"),
                             "god_drifting_parts": (god_block["summary"].get("drift") if god_block and god_block["summary"] else None),
                         },
                         findings=findings,
                         families=families,
                         observatory=god_block,
                         verdict=("ALIGNED ✅" if not findings and not (god_block and god_block["drifting_parts"])
                                  else f"DRIFT FOUND: {len(findings)} cross-source conflict(s)" +
                                       (f" + {len(god_block['drifting_parts'])} part-snapshot drift(s)" if god_block and god_block["drifting_parts"] else "")),
                         **({"verbose_schema_map": {k: {v: s for v, s in by.items()} for k, by in schema_map.items()}}
                            if kwargs.get("verbose") else {}))

    # ── authority resolution ──
    def _tier_of(self, source_key):
        for s in SOURCES:
            if s["key"] == source_key:
                return s["tier"], s
        return 99, {}

    def _winner(self, source_keys):
        """Given the sources that carry a value, return the authoritative one."""
        best_key, best_tier, best_src = None, 99, {}
        for k in source_keys:
            t, s = self._tier_of(k)
            if t < best_tier:
                best_key, best_tier, best_src = k, t, s
        why = {
            1: "MASTER_PLAN sets strategic direction — it wins over everything (authority #1).",
            2: "CONSTITUTION governs the repo — it outranks spec docs and observers (authority #2).",
            3: "a species-root spec doc — canon over hubs/indexes/observers (authority #3).",
            5: "a hub/index that mirrors canon — it loses to the species root; shown only because no higher source carried the value.",
            6: "rapp-god is the observatory (a witness) — it never wins; the live source does.",
        }.get(best_tier, "highest-authority source carrying this value.")
        return {"source": best_key or "(none)", "tier": best_tier, "why": why}

    def _canon_version(self, schema, by_ver, wins):
        """The version the winning source declares (or the highest if the winner
        carries several)."""
        for v, srcs in by_ver.items():
            if wins["source"] in srcs:
                return v
        # fall back to the highest-looking version
        return sorted(by_ver, reverse=True)[0]

    def _rappid_drift(self, fetched):
        """The load-bearing invariant: is the rappid format consistently the
        Eternity form, or do sources still declare the v2 form as canonical?"""
        eternity, v2 = [], []
        for key, (src, text) in fetched.items():
            if "rappid:@" in text:
                eternity.append(key)
            # a source that *mints* v2 (not merely mentions legacy read-compat)
            if re.search(r"rappid:v2:[a-z]", text) and ("mint" in text.lower() or "f\"rappid:v2" in text or "format" in text.lower()):
                v2.append(key)
        if eternity and v2:
            both = sorted(set(eternity) & set(v2))
            only_v2 = sorted(set(v2) - set(eternity))
            if only_v2 or both:
                wins = self._winner(eternity + v2)
                return {
                    "kind": "invariant",
                    "what": ("rappid format: the Eternity form `rappid:@<owner>/<slug>:<64hex>` "
                             "(CONSTITUTION Art. XXXIV.1) is canon, but some sources still "
                             "present/mint the legacy v2 form `rappid:v2:<kind>:@…@github.com/…`."),
                    "where": {"declare_eternity": eternity, "still_show_v2": v2},
                    "winner": "CONSTITUTION Art. XXXIV.1 (Eternity) — " + wins["source"],
                    "why": ("Art. XXXIV.1 locks ONE format and forbids parallel ones. v2 is "
                            "read-forever (canonicalized) but MUST NOT be minted/declared canonical."),
                    "remediation": ("anything that MINTS v2 (e.g. tools/backfill_seeds.py, "
                                    "specs/skill.md examples) must emit the Eternity form; keep "
                                    "v2 only as read-compat via door_address.canonicalize_rappid."),
                }
        return None

    def _graph(self, action, kwargs):
        """Traverse the ecosystem graph (from rapp-map) so the digital organism
        stays aligned: when a repo mutates, the blast radius is everything that
        consumes it (inbound edges), transitively — those are the repos to
        review for update."""
        text = _fetch(GRAPH_URL)
        if not text:
            return self._env(action, "offline",
                             note=f"could not reach the ecosystem graph at {GRAPH_URL} "
                                  "(rapp-map/graph.json). Try again online.")
        try:
            g = json.loads(text)
        except ValueError:
            return self._env(action, "error", error="graph.json is not valid JSON.")
        nodes = {n["id"]: n for n in g.get("nodes", [])}
        edges = g.get("edges", [])
        if action == "graph":
            return self._env(action, "success", schema=g.get("schema"),
                             nodes=len(nodes), edges=len(edges),
                             edge_types=g.get("edge_types"),
                             node_list=[{"id": n["id"], "tier": n.get("tier"), "role": n.get("role")}
                                        for n in g.get("nodes", [])],
                             note=g.get("purpose"))
        # blast_radius: who consumes the mutated node? (inbound edges, transitive)
        target = (kwargs.get("repo") or "").strip()
        # accept owner/repo or bare id
        target = target.split("/")[-1] if "/" in target else target
        if target not in nodes:
            # fuzzy: match any node id containing the term
            cand = [nid for nid in nodes if target.lower() in nid.lower()]
            if len(cand) == 1:
                target = cand[0]
            else:
                return self._env("blast_radius", "error",
                                 error=f"unknown node '{kwargs.get('repo')}' — pass one of: " +
                                       ", ".join(sorted(nodes))[:400])
        # BFS over inbound edges (consumers point AT the target)
        consumers, frontier, layers = {}, [target], []
        seen = {target}
        depth = 0
        while frontier:
            depth += 1
            nxt = []
            layer = []
            for node in frontier:
                for e in edges:
                    if e["to"] == node and e["from"] not in seen:
                        seen.add(e["from"]); nxt.append(e["from"])
                        consumers[e["from"]] = {"consumes": node, "via": e["type"],
                                                "tier": nodes.get(e["from"], {}).get("tier"),
                                                "depth": depth}
                        layer.append(e["from"])
            if layer:
                layers.append({"depth": depth, "repos": sorted(set(layer))})
            frontier = nxt
        ranked = sorted(consumers.items(), key=lambda kv: (kv[1]["depth"], kv[1].get("tier") or 99))
        return self._env("blast_radius", "success",
                         mutated=target,
                         mutated_tier=nodes.get(target, {}).get("tier"),
                         consumers_count=len(consumers),
                         layers=layers,
                         to_review=[{"repo": k, **v} for k, v in ranked],
                         ruling=("Review these in depth order. If the mutation in "
                                 f"'{target}' changed a spec/schema/protocol, every "
                                 "consumer that mirrors/snapshots/implements/bundles it "
                                 "may need to follow — that is the drift surface. The "
                                 "species root wins on conflict; observers (rapp-god) "
                                 "just re-snapshot."),
                         note="keeps the digital organism aligned: one mutation → its full consumer set.")

    def _part(self, name, god):
        if not god:
            return self._env("part", "offline", note="rapp-god unreachable.")
        if not name:
            return self._env("part", "error", error="pass name=<ecosystem part>")
        hits = [p for p in god.get("parts", []) if name.lower() in json.dumps(p).lower()]
        if not hits:
            return self._env("part", "not_found", name=name)
        return self._env("part", "success", name=name, parts=hits,
                         ruling=("If drift=true / update_available=true, the live source repo is "
                                 "ahead of rapp-god's snapshot — the SOURCE wins; rapp-god re-snapshots."))


if __name__ == "__main__":
    a = DriftAgent()
    print(a.perform(action="authority"))

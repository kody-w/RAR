---
name: "rar-rapp-drift"
description: "Cross-check every canonical RAPP source for spec drift; report each conflict with which source wins (authority order) + how to reconcile."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/drift", "rar_sha256": "00ffb4b96beb3024e1b412caf5d2191a84846e73091132eefa30ffe6c2c5e31c", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["drift", "spec", "authority", "rapp-god", "alignment", "audit"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/drift`. The original RAPP
agent is preserved byte-for-byte in `drift_agent.py` and in the RCI capsule.

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

DriftAgent — troll every canonical RAPP source and report spec drift, with
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
  file_issues file the prune plan as GitHub Issues (dry-run by default)
  help

Online by nature (it trolls the network); degrades to a clear "offline" note.
Generic + cover-safe: touches only public canon. MIT © Kody Wildfeuer.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "action": {
      "enum": [
        "scan",
        "canon",
        "prune",
        "authority",
        "part",
        "graph",
        "blast_radius",
        "file_issues",
        "help"
      ],
      "type": "string"
    },
    "confirm": {
      "description": "file_issues: actually create the GitHub Issues (default false = dry-run plan only)",
      "type": "boolean"
    },
    "name": {
      "description": "part: ecosystem part name (from rapp-god)",
      "type": "string"
    },
    "repo": {
      "description": "blast_radius: the mutated repo/node",
      "type": "string"
    },
    "tracker": {
      "description": "file_issues: optional owner/repo override for where Issues land (default DRIFT_TRACKER)",
      "type": "string"
    },
    "verbose": {
      "description": "scan: include in-sync schemas too",
      "type": "boolean"
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `drift_agent.py` and embedded as the fenced Python below (sha256 00ffb4b96beb3024…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `drift_agent.py` first:

```bash
python3 drift_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 drift_agent.py   # or on stdin
python3 drift_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
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
  file_issues file the prune plan as GitHub Issues (dry-run by default)
  help

Online by nature (it trolls the network); degrades to a clear "offline" note.
Generic + cover-safe: touches only public canon. MIT © Kody Wildfeuer.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
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
    "version": "1.0.2",
    "display_name": "DriftAgent",
    "description": ("Fetches canonical RAPP spec sources from GitHub, detects schema-version drift, and reports which source wins per the fixed authority order."),
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

# Where drift Issues land for traceability (public canon only — never private).
DRIFT_TRACKER = os.environ.get("DRIFT_TRACKER", "kody-w/RAPP")
DRIFT_LABEL = os.environ.get("DRIFT_LABEL", "rapp-drift")

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


def _run(cmd):
    """Run a subprocess; return (rc, out, err). Mirrors the other agents:
    FileNotFoundError (e.g. gh not installed) -> rc 127, 120s timeout."""
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return p.returncode, p.stdout, p.stderr
    except FileNotFoundError as e:
        return 127, "", str(e)
    except subprocess.TimeoutExpired as e:
        return 124, "", str(e)


def _scrub(text):
    """Redact tokens/secrets before they enter a return envelope or issue."""
    if not text:
        return text
    text = re.sub(r"gh[pousr]_[A-Za-z0-9]{20,}", "[redacted-token]", text)
    text = re.sub(r"github_pat_[A-Za-z0-9_]{20,}", "[redacted-token]", text)
    text = re.sub(r"(?i)(authorization|token|bearer|secret|password)\s*[:=]\s*\S+",
                  r"\1=[redacted]", text)
    return text


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
                               "enum": ["scan", "canon", "prune", "authority",
                                        "part", "graph", "blast_radius",
                                        "file_issues", "help"]},
                    "name": {"type": "string", "description": "part: ecosystem part name (from rapp-god)"},
                    "repo": {"type": "string", "description": "blast_radius: the mutated repo/node"},
                    "verbose": {"type": "boolean", "description": "scan: include in-sync schemas too"},
                    "confirm": {"type": "boolean", "description": "file_issues: actually create the GitHub Issues (default false = dry-run plan only)"},
                    "tracker": {"type": "string", "description": "file_issues: optional owner/repo override for where Issues land (default DRIFT_TRACKER)"},
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
        if action == "canon":
            return self._canon(action)
        if action == "prune":
            return self._prune(action)
        if action == "file_issues":
            return self._file_issues_action(action, kwargs)

        if action == "help" or action not in ("scan", "canon", "prune", "authority", "part", "graph", "blast_radius", "file_issues"):
            return (
                "DriftAgent — make sure the whole RAPP ecosystem aligns.\n"
                "  action=scan              cross-source drift report + who wins\n"
                "  action=authority         the precedence order (which source wins)\n"
                "  action=part name=…       drift detail for one part (rapp-god)\n"
                "  action=graph             the ecosystem relationship graph (rapp-map)\n"
                "  action=blast_radius repo=X   who consumes X → review for update if X mutates\n"
                "  action=file_issues [confirm=true] [tracker=owner/repo]   file the prune plan as GitHub Issues (dry-run by default)\n"
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
            if re.search(r"rappid:v2:[a-z]", text) and ("mint" in text.lower() or "f\"rappid:v2" in text or "format" in text.lower()):  # legacy-pattern detector (read-forever)
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

    # ── canon: materialize the RESOLVED single-source so the tree blossoms
    #    with the latest instead of re-traversing scattered old versions ──
    def _resolve(self):
        """Fetch + resolve once → (canon, prune_plan, fetched, missed). canon is
        the rapp-canon/1.0 registry: every schema → its ONE canonical version +
        the legacy versions it supersedes."""
        fetched, missed = {}, []
        for src in SOURCES:
            t = _fetch(src["url"])
            (missed.append(src["key"]) if t is None else fetched.__setitem__(src["key"], (src, t)))
        if not fetched:
            return None, None, fetched, missed

        def _norm(v):
            return re.sub(r"\.0$", "", v)
        schema_map = {}
        for key, (src, text) in fetched.items():
            for name, vers in _schemas(text).items():
                for v in vers:
                    schema_map.setdefault(name, {}).setdefault(_norm(v), []).append(key)

        canon, prune = [], []
        for schema, by_ver in schema_map.items():
            bases = {}
            for v in by_ver:
                m = re.match(r"^(\d+(?:\.\d+)*)(?:-([a-z0-9]+))?$", v)
                if m:
                    bases.setdefault(m.group(1), set()).add(m.group(2) or "")
            suffixed = any(suf for sufs in bases.values() for suf in sufs)
            if suffixed:
                # family — canonical IS the whole family (all variants kept)
                canon.append({"schema": schema, "kind": "family",
                              "canonical": sorted(by_ver),
                              "note": "family variants are all canonical (types, not versions)."})
                continue
            if len(bases) < 2:
                only = next(iter(by_ver))
                canon.append({"schema": schema, "kind": "single",
                              "canonical": f"{schema}/{only}", "legacy": []})
                continue
            wins = self._winner([s for srcs in by_ver.values() for s in srcs])
            top = max(bases, key=lambda v: tuple(int(x) for x in v.split(".")))
            legacy = sorted(v for v in by_ver if v != top)
            canon.append({"schema": schema, "kind": "versioned",
                          "canonical": f"{schema}/{top}",
                          "legacy_read_only": [f"{schema}/{v}" for v in legacy],
                          "authority": wins["source"]})
            # dead branch = any source that carries ONLY an older version (still
            # presents it as current) → prune to canonical
            for v in legacy:
                for s in by_ver[v]:
                    if s not in by_ver.get(top, []):
                        prune.append({"source": s, "stale": f"{schema}/{v}",
                                      "replace_with": f"{schema}/{top}",
                                      "why": "presents a superseded version; align to canon (keep only as explicit read-compat)."})

        # the rappid invariant → an explicit prune of the v2-minting dead branch
        inv = self._rappid_drift(fetched)
        if inv:
            for s in inv["where"].get("still_show_v2", []):
                prune.append({"source": s, "stale": "rappid v2 minting",
                              "replace_with": "Eternity rappid:@<owner>/<slug>:<64hex>",
                              "why": "Art. XXXIV.1 forbids minting parallel formats; v2 is read-only legacy."})
        return canon, prune, fetched, missed

    def _canon(self, action):
        canon, prune, fetched, missed = self._resolve()
        if canon is None:
            return self._env(action, "offline", note="no network — cannot resolve canon.", missed=missed)
        versioned = [c for c in canon if c["kind"] == "versioned"]
        return self._env(action, "success",
                         registry_schema="rapp-canon/1.0",
                         resolved_at=_now(),
                         sources=sorted(fetched),
                         authority_order=AUTHORITY,
                         schemas=sorted(canon, key=lambda c: c["schema"]),
                         note=("This is the MATERIALIZED single source of truth — read it "
                               "instead of re-traversing every spec. Each schema has ONE "
                               "canonical version; older numerics are read-only legacy. "
                               "Commit it to rapp-map/canon.json so the tree blossoms with "
                               "the latest; regenerate when canon moves."),
                         prune_count=len(prune))

    def _prune(self, action):
        canon, prune, fetched, missed = self._resolve()
        if canon is None:
            return self._env(action, "offline", note="no network — cannot compute the prune plan.", missed=missed)
        return self._env(action, "success",
                         resolved_at=_now(),
                         dead_branches=len(prune),
                         prune_plan=prune,
                         materialized_canon="rapp-canon/1.0 (action=canon for the full registry)",
                         ruling=("Operator-mediated, surgical: cut each dead branch (a source "
                                 "still presenting a superseded version as current) to the "
                                 "canonical, keeping it ONLY as explicit read-compat. Then "
                                 "commit canon.json so consumers read the resolved tree and "
                                 "never re-traverse scattered old versions. The steward never "
                                 "auto-edits other repos — it stages the cut for you."))

    # ── file the prune plan as GitHub Issues for traceability ──
    def _file_issues(self, items, tracker, label, prefix, confirm):
        """Reusable, idempotent Issue filer. SHARED ISSUE-FILING CONTRACT.

        items: list of {title, fingerprint, body_md, machine}. tracker is
        "owner/repo". A stable fingerprint => same drift never spams a dup.
        Dry-run by default (confirm=False) — filing public Issues is
        outward-facing and must be opt-in. COVER: callers must put only public
        canon in titles/bodies — never a private repo name, token, or secret."""
        filed, skipped_existing, planned = [], [], []

        # IDEMPOTENCY: GitHub full-text search of a hex inside a code fence is
        # unreliable, so dedupe by ONE exhaustive, label-scoped listing and
        # harvest fingerprints from titles + bodies. The fp also rides the
        # TITLE (fp:<hex>) so it's visible + matchable.
        rc, out, err = _run(["gh", "issue", "list", "--repo", tracker,
                             "--label", label, "--state", "all", "--limit", "500",
                             "--json", "number,title,body"])
        if rc != 0:
            # fail-safe: if we cannot confirm absence, refuse to file (no dup spam)
            return {"tracker": tracker, "label": label, "confirm": confirm,
                    "error": ("could not list existing issues to dedupe (" +
                              _scrub((err or "").strip())[:160] +
                              ") — refusing to file to avoid duplicates."),
                    "filed": [], "skipped_existing": [], "planned": []}
        existing = {}   # fingerprint -> issue number
        try:
            for it in json.loads(out or "[]"):
                blob = (it.get("title", "") or "") + "\n" + (it.get("body", "") or "")
                for fpm in re.findall(r"(?:fp:|\"fingerprint\"\s*:\s*\")([0-9a-f]{12})", blob):
                    existing.setdefault(fpm, it.get("number"))
        except ValueError:
            pass

        label_ensured = False
        for item in items:
            fp = item["fingerprint"]
            title = f"[{prefix}] {item['title']} (fp:{fp})"
            machine = {"schema": "rapp-drift-issue/1.0", "fingerprint": fp,
                       "prefix": prefix, **item.get("machine", {})}
            body = (item["body_md"] + "\n\n```json\n" +
                    json.dumps(machine, indent=2, ensure_ascii=False) + "\n```\n")
            if fp in existing:
                skipped_existing.append({"title": title, "fingerprint": fp,
                                         "issue": existing[fp]})
                continue
            if not confirm:
                planned.append({"title": title, "fingerprint": fp, "would_file": True})
                continue
            if not label_ensured:
                _run(["gh", "label", "create", label, "--repo", tracker, "--force"])
                label_ensured = True
            crc, cout, cerr = _run(["gh", "issue", "create", "--repo", tracker,
                                    "--title", title, "--body", body, "--label", label])
            url = (cout or "").strip().splitlines()[-1] if cout and cout.strip() else None
            filed.append(url or {"title": title, "fingerprint": fp,
                                 "error": _scrub((cerr or "").strip()) or f"rc={crc}"})
            existing[fp] = "just-filed"   # guard same-run duplicates

        return {"tracker": tracker, "label": label, "confirm": confirm,
                "filed": filed, "skipped_existing": skipped_existing,
                "planned": planned}

    def _file_issues_action(self, action, kwargs):
        canon, prune, fetched, missed = self._resolve()
        if canon is None:
            return self._env(action, "offline",
                             note="no network — cannot resolve the prune plan to file Issues.",
                             missed=missed)
        tracker = (kwargs.get("tracker") or DRIFT_TRACKER).strip()
        confirm = bool(kwargs.get("confirm", False))
        items = []
        for p in prune:
            fp = hashlib.sha1(
                (p["source"] + "|" + p["stale"] + "|" + p["replace_with"]).encode()
            ).hexdigest()[:12]
            title = f"{p['stale']} → {p['replace_with']} (in {p['source']})"
            body_md = (
                f"**Dead branch:** `{p['source']}` presents `{p['stale']}` as current.\n\n"
                f"**Winner / why:** `{p['replace_with']}` wins — {p['why']}\n\n"
                f"**Remediation:** align `{p['source']}` to `{p['replace_with']}`, "
                "keeping the old form ONLY as explicit read-compat (never minted/declared current).\n\n"
                "Resolved per the constitutional authority order: MASTER_PLAN > CONSTITUTION > "
                "spec docs > vault > code; the species root (kody-w/RAPP) is canon and other "
                "repos mirror it. (Public canon only — no private sources referenced.)"
            )
            items.append({
                "title": title,
                "fingerprint": fp,
                "body_md": body_md,
                "machine": {"kind": "prune", "source": p["source"],
                            "stale": p["stale"], "replace_with": p["replace_with"]},
            })
        result = self._file_issues(items, tracker, DRIFT_LABEL, "drift", confirm)
        return self._env(action, "success",
                         filed_at=_now(),
                         dead_branches=len(prune),
                         dry_run=(not confirm),
                         counts={"candidates": len(items),
                                 "filed": len(result["filed"]),
                                 "skipped_existing": len(result["skipped_existing"]),
                                 "planned": len(result["planned"])},
                         **result,
                         note=("Dry-run by default — pass confirm=true to actually open the "
                               "Issues. Each Issue carries a stable fingerprint so re-running "
                               "never spams duplicates (same drift => same Issue). Only public "
                               "canon is ever written to a title or body."))

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
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-rapp-drift"
description: "Cross-check every canonical RAPP source for spec drift; report each conflict with which source wins (authority order) + how to reconcile."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/drift", "rar_sha256": "00ffb4b96beb3024e1b412caf5d2191a84846e73091132eefa30ffe6c2c5e31c", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "drift_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/drift:4523e5c2bcd34920563a88366d0b639d3d9afc6c62c02edce4e062e8fd9d7bcf", "kind": "skill"}, "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["drift", "spec", "authority", "rapp-god", "alignment", "audit"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/drift`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `drift_agent.py` is
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

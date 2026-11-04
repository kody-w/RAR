---
name: "rar-rapp-drift"
description: "Cross-check every canonical RAPP source for spec drift; report each conflict with which source wins (authority order) + how to reconcile."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/drift", "rar_sha256": "b40ed2f9d3cd95038078b0ae7514b31a8da5e36a5b3b56c170d625606f97176b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["drift", "spec", "authority", "rapp-god", "alignment", "audit"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `drift_agent.py` and embedded as the fenced Python below (sha256 b40ed2f9d3cd9503…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `drift_agent.py` first:

```bash
python3 drift_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 drift_agent.py   # or on stdin
python3 drift_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/drift_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/drift_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/drift/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

<!-- rci-capsule:v1:H4sIAAAAAAAC/5y7CbPiRtYm/FeIeieiq5pyaRfC73jmkwRoQWgXIFz+3Nr3BS1IwuP/Pim4t+qWXXZ3DO6oC1LmycyzPOc5mdm/vXP6Lq6adz++21f+tDgluR8GfdC8+/jOD1qvSeouqUrwmm2qtv3BiwMvWwS3oJkWnlNWZeI5+UKnVXXRVn3jBYuwahZtHXgLv0nC7r8XTVBXTbcIHC9eeFUZ5onXLYakixdDnIBnL92GpGwX75+TSbppUTV+0HxYLBdxNSy6CogBnb0kDz6BmQWjU9R50L778edfPr5LwPd3P/72zsudFjx6t5kHpqOg7EDT3Ckj8KyegOAS/K6DBsywAI/8IFy8/HrfBnn4cfHPf2aD00Tthx8/l4uXj+PN61/8tHj/fPcpCrr3n989H39+9wFMdPH5XQt0AX58yqshaN5/+Fx+FZCEX2T8BFp+WeHnd29GmT9N0PVNuZin8unXoLy9f3b7OIvvPS9o28/vPi6+9P/1oaGfaMvkFV0w7b8YNCkXYLpR49Tx3P3zOxdoqfu1cfykBwI//N0kHr2+TONFN3+5soc7/P2qHk1eBP61oLrpy+DvBT2a/FtBIXCXX5O27YP278W9afjrU8CfV/2Xo8RBXn9+N/vBy9Oy6l7U/nSLj1+V8/Hr8j5+6wyPN07TPb/9pb0+/nFZf2HA998+nT+f3wTG4nOPwgi+KJwsWLR9Eyy6GMRgXOXBM5hBtLVT2wXFwsmTqGw/fQYaePc9oa8h8tO82G9feg/IeAnwBxy8osFyHusR8/9e7ldMeP3Mc60BIAR+UALJj0BYvP8TnHz497JnjS9Kpwh+mhWCki8tnnP1g85J8gegVSUYcW77Hhim/iGq/P9A+MOI37ycJ/5Vs02QO3PDNk7qxbPxU3zh1P+B+LeO8dDrT2fQYNYrQMq2L4J2cZ7tjKxR8PqWBMNjKX3tO10wO/F5UfQd+P4f2OCNyy1+nlE8aYqfuqYPfln83DWOlwEkqoYyaKB5Ir+AznOPF0P1s/IADi+cdsElHd+7C+Ep6r3fTD+A9wt3AtoOnT7v/nrhQrfomirP24fYOcUkQMT8t/24eDXL4n3ltkFzc7qqmT68PAf6nOPme0Kd0n84/A9M4ubBx0WYO1H7mt9eslVSRosWJL7CgZLy5jSJU3YAiEHP78uc/ek5SeCFQCdzlnn8nO3SJV0/qxRkzT8ku08gmN/CzH8twqADHv2YTBeDWXx993gT+B8XBTBK4IP09NvvHxc///KmxZyGG28GIkOxdHZr/AEoOtDp14ec96Ddz5/f9U3++d0vH75tBdwEgFm7kEEE/PjnxT6H/wSUHJT+i5wsmP4sJ8jb7/V/WcfPb3v+Midb8ODjonsjZLbtlwlzyuZXw6RNy/hTi7StSpCGHb99P0fpvID5xTz+YxF/APIZq18m8bDo3Pb7y/2b9FyFwE8emP7nFX7zAaMBpHlXVosy6IaqyV5x+AvgBC8pJAj89kl7Zt40Ow8AiCT/tDCBYzqRA8xalfOgn/79qE8j/fT883eZ7Jl//jbvghbfEqHZ2YHjflw8MPEb9wVrI2D4+e9izg4/Ltwe8MtnLLzNDTWIsjkJve3xVtIz+hY//K/FbyAY2nnC4PvPz97tL78vFu9LQONAqroDIe9QgFyPBaGf4EdQvUqaKd+vc8v3t7/Im03wqe3d9w2I7M+f4P/xTLjzv7c3Yp7T+RXAyiPwvg064MQfX/03GLsPcwS+eNinBMB++/6PQ8+9ZjWCQcDi5va/Pkdo3z8k/EW31663ucfc88fv+8HX2X5qg+4FZt8/B/zt9w9vH77qZoaSD69RDRb0jWHDpPQBGAHQDZ0iyWcQ/gm0/w78PAb+CMD9VzC9eZZvpvL9NQFT13kCUjJIX03iLVynBeLDpioASwnDZARh+hh1WrwAMUgiP1RN5JRJW3xc/ACaz+7xzOZ/wKCnsNlij5HejjG7E9DD+5dB2g9/ttBDzc+lfA8IgVzgO4UzwxPwnv///efP/vL9//4RuNH87cM/P4AfP7z/2fnhDv+w/mX54cP//h9/9Ks/4FLxFwYFaQTkpD7489vHCt8atPgUNVVfv0eASef1fQBW9f0vj9GX8uWbIHn4zKuyfwKoOM1qeVq0Dx/++Rzn5uQgib//8PrqYWHQ4g+y/AQkvdLrfn3VfwsYYOC/f/z8c7p5Hfo7i/+vhQNCOE/coJkpzAsq7OiDINmLL7YDI3gApprEjwJoLhsbf2Ha6tb4+D2Jwafo08IF2FrOnOyHIIog9NP4w/989an/8+JR/6cMkih2qyauKv9/fXgF7tlOD/D+Tmy+RMdrHP021wPzjAHEfomNz+9e/fjx9EUzDy/78O9w/YVtgJwy9/38Lik7QO2f3OJPQfJGO91UA8V//Dp3kEN+/44bft/PgInyoHz/rVU/LP7nAv3xr0U8VD2T6EewgbSBAIi+tWDSyAzRoMgAic6fFl9Q3H+j4e8p+L8WoIzpQf4DHDbvkh9e04JXBSOY2aMueOG+X7cpfnpkHl7g+K1hLl66fCv3sQ3x00u2e9K39z+3r2yq/YoBf/D+h++DBn/kPY/BH/D3Eyi2xj+o7eOcLX7KncL1ncXtx0XX13nwHtjx/fiUOz6w/dMDFIHWZor44Y/Y9ALHX93sO5Q0A42eTvJ0vFd9fZc8fH43xM5MBBbh53f/+u3Z4/d/LeYBHJCgnG7x23dc4PdXjbbzOIvlX3vvM6t+SqukfP+ty3/4i+kEzcPHfwM6epjhAcgf/2iSl5zy+/eFPIw5S5ltDNjmkz0Awvnd5l+85tcvqnro41Ud0G9fTPv7X2pxejPc49f3x2r6fGb3oC2w8fYgmE+G9MVvX53bcatb8N+LKp/r3df09ar0hTMTqHd/ixkz2uSJP1PHaa7G5qD7AehyLjFAVEeONy3eg+9JOIEpON0/Zu1+BZWXiPy3g8y08rUQBy6S54t5UQbkB14OZvmsjcAqHogApuH1TRPMNZXbF/UiAYxnZpTf1VRQBH7idC/2eB/OFdz0OlZQJN2jWgO15lNJb7y3jaseDDm3+XcreMbVG99/a+x/zbT8kecXvz1M+4/n6P/45ffvTPv3P3BikHHnxc9lafJQPZC0+FJVfm35bPDrS3B/QaSXxw9AfP/CKr/d//q2449/jxXfNv7DVLEPX6pq4Aegun+gObDTD4BCACvOdedjT+RZvLwtvBdtEgGH+bY4+9XNKy8DS3mWYW/mDF7+YaIPkc+F/1w/or2e4xw0fCk75oEf22E///Lhr20JZNcvHZ455Llf+/rsuRXyq3MDlZUDyn/w+pdvhb2d9neBte2Lwmkecf51cl8eft+JXxf368siflz8/NtrIfXjl8l9Kazm3UBA1t6+e3nwHzGEr0O+lfCqjv9Ywp919ePf6fE/lvsKX2/lfX0GksoX47+q7ecfcfiX/wBIzTgAXGNGxT/77auvPrPVY5sK2AK4eZ7c/gMUfe6oPDbd5t0CJwY4uqjCt/HSlk4NIKcDFTuQ/tJhxov//vfi36Dco6x4bJG9kf1SRc+7Az+8jrN4P6/i34p+G6TeDGIAjft6lvVAOEAKH7nggVHztzb4Hhj//r168NOcyt+/ITQhSJg/v3KPt2H6H510/M1C5r2EMvB/dbqfQMU6vP9bb3vZJPj1cXIV+D+9EI5X8PxPuvblYxtmdu2XXZS/6/WXJzR/O9QTMn767d/EzSttecTLTML+k3W8dHwW348welYbffEeecTXo3R7teOMmm/s9txJ+SNt/A/G+5LV/h+H/JoV/5PRZqT+M7C+/wLgP7+B5V/+mBOeOegF6V+2Ab/T7esu4t9O6Pe/e/m65J++bKP8XeOXEvKn1y9/1/hNaP/0Zf5/1wEY00+87iegCVoSOHm7mRneCiYAe3/dGn010KyU+cH7v9bTH7X/d4n5243hmWttdGFnLnaKJW9+fJYXr2ODHPDNZuHrtvz79sPflxl/+MxkcbF8yv467398O+1//AKGm799BdYn2XoM9rd+8qf1P9f22F35W3/55z/nvQFgDbdqg1+/7pE9Kp7sper5UvI8650vtc5zz3HeZPv+Btvvv/+9gsCSvtnPfZnGHBWP6f/2+4cP7z6+ex5Z/frIpGP3cnr+7cPHIfrbDb0vR5FvDx7nQ0Kn9wEJ/8sTx29vEPzVwc3DJx4p+OmdrTN970bB69nL18OW78t73jf4tLDAmsHkQMk5n1eBhDF/BQJmKc9IAITicSYKXkGLR2n6FyIfR1Pz9pcTNUHwaDxP77WaA8ThS4k359h3v398N+9CNf0jG843Gf7rvxaHZF5oBfRgeFXfLQAV6JLicYxhxkBE0r5J1vMZ1ku7uqnSl8MEQEz+9f/N9AF6KPRfT0oClBEl5cvljc+l87AOkFYDigRwBKzOnbpgLlF+mL/M3vWvR/9fH00/1dO/HnoHz+cJ6KwAllO3fR58mid3mhX4nMps8mAMvB5IAbEy704l+bz5AUaq8tt8TAjGbbO5UPSTBsx6ZiezbLDYH2dh//rXv1ynjT+Xz2sc2OJ5MaWFQIMv01n88AOYO4CGKAaFVODF1eIfv/3+j8X/Wfxdr4fweQzVaV9VCWYoGooMTB2BInvePnvsDj453r9++/1Fg0DMfLr3qJeTl6oW8E/gM6/qNHj6B5QgF24wF9mLpJgPv+eyJgG8UAgXX+b7ci4OvGsRV+18EjTXZ0HpPevwz+UXTc4g3AJq2IbTx0XfPs9Y//VlAxPQHKf71+LAqoDTVfmDJPblt/sJX4z9fA6ENIBUMq8iPi3kBwcEMObUceO8jBE6T7vM9xxeugPhDiCMw+dyvoITzKp6kNanekCjxwbF06Q/PA6EvQrk0tJvX8d+tAG1g78wKwcM3nwu2xevneNs3r19HMVGfeI7pRf894tLvRTzs/5e4vvFCv6LVR4++Of7Do8D5L+9vvRwu+clha8Y9PFxYelz+Q2+nATZeDQf4ukrznyBMaDSP95mekxKeD1wfDpMlFcumMLjdO/LLN+cbzfVnHWzyp9+GKB5oh9ej7xBq8+AmEYJgIwJekvsv15SeLQCyvaD8c3dgo9fRmgXce9+Lt9/PQL/su8KEL0BJn89DP+WAC7AmM+NFh+4QBgMi/nI9Qc3cJrHOfUX7tY+65LnRsPiud/xHD4LmjL4srf14Xmg/jx+f4Lq3MigD9vP5QN5Z2x62UDygU+FwPDAsPkj7X35Od8zAOT402IH3PTbK2fJ86JHO4v7cjLft7Pkf382/5hcF8yXD6aqf7mTNmv/5VLal9sniR889oeA234xt18BO8qKCbwYlDZvRANAiSvvWX8+hwFrfJ675M6weL9lFcM2zO3h1wOtArvAsLNCFtDnklVkwxRMyxQUGeSsL5cfXpLBP984wz8X7/9U/n6clfGy5f65LAJnvgHUPmlPDsydP73+iyskj8TgzEFQAgFvi8S09yMQld23Ne6nZ3349kZQ2IPA++sLQe+/XP8o31RQf3XX52Vef073M1o8H398Dc1Z4J+u+Xz3gs9XBvK86vM4dvx636d8Xmp5vQbz/37BBQh63BkDOlIeZ/jz29J5nIC/T7655fJyTeDDf4PeACL84HEpwFl4OYi0tzcPHlcLgNq5F9BdLh7I+UPrhAFwsKp/AM5j37fuXRAQT/j7tJh3mx+etV58ewF0vmcJ2gUAkN/9WALrfXxsSf3xfuWcJYoAIHc7X8EErAMAYZcEj1/Psn7+FpR98e7Hnx8X4kCnx9hz51l14O8Xgz8FznIf96HA37e3nMDPNxYAv2Y1vvvl47v5RAtM7AlKM496uaI0D/3tLdY3/X+c7z70Tg5U4oFQ6J7W/KP9nkYD2W8mwz8tXu35MPeszpkcvwzvgoQbgPX9/qqpPw4+L+3HP7rZ3PSPvvbuO0uaA+XPIt+q5wkkzztdzyQGlZUffE/Yy52tf6Ofqn5Bw69Xux4R1swoN0fNE6hfdJXPAfdFYY967ldTp9n9Vv/ugl4qjT/P4XlVJCm9vPfn5PVDO5XeSwKa/b/6jsofCrr2gGr4s5+9eN5X16jcmQ3PwwLLdc8bwL+9A47r+E7nvLjuC2EGzRsHhM7MNCDkEwyGA7+fjBG8e0OlX960sQNY3jwdHA58NFz7mOevCRij4BXlwk6wIhDcxRCH8h0iwEiHcDGXID1kBfsk6AmT4XqFrEh3LrQeaPbrTJSSebQ5/IHCfuhACfH19bxR8jLN57RmBXxh7o/Ye872t3cuiYOWPN4K9PPDQktkjZ4ldxLdSFlRCbPEHfpui6frdeXLXEFSV/R6HWsUE4Vrjxk8U2UaszsLAs1ph+xa6Cp2CeyNeKvHsunTkDxAtUtmd2J/MdjRO+7gtaof7ml1NRhFn6jeFFsC2tIQL6nQcIRiudSXUJhMe++snXZBrrVDfj8MU6RRspruOiLfMt4m8wym32UZpTSVruhnWzfEw94pV+hS0nXRlBFP6VQFukfyeIgDbDIq07lscljGpGYQwhKPku2RT5aG0PbtXnKx7VJB+I7f8Hc8IZSzMU0CwxBbxyRowV55h5N0p7s0kGhrHd8D/8TZhe4jo793y8sKw3BzJDvZpKyDvaRyWY1pqJTW41nQE0s360pelmPVZtJwgUJV4iMIT6i9mAjhkE3bk7ejGTGM5Uxh1HVBopOhmsUyzFyyhjb0LhDDdb/yDGhjN5zTF7xxXw3wythtz7G2Ox2hJdHbEnXMD7fzwNgjSuLl0Vjz7Pp8ibkLzcGTtvH7s+cXcqvTiLPXj2xPnXhFGQ5y1iaQiOqljvrrVYdBW1i6rFfycM7uVXa5BUmOJ1B+C0vnSizLDK3Wx8OUBVOwstIBoxnv4DI1LB12OR7nGRcM2M2TV/zeNoodS6FL/3DE1rSvHeNmu7rctJ27ua1gSJVgI4yb690WmHbbuvW1obmhFH0EqSDRHTNNb3yhs9jLMaFH0xApasMWR4KkPJm97Dv7Lko5XN3WZzkJerooNvJKT0IFWW7srSveLHarFlkTe5S+ovnlSNdVyavtRBL3Eg8hBUqL46UZGVOHIwyvAwiqDlUbabhR0v5F8oW9lXl0sh1oqo7PqM3wWzr076XI1lw5WIN2bW4Jc3Nib3UQLsPtSAmB6S9Da1lcxj16ty12r9mim3XLJmoEJr2cdiMLaTud8keFQE2tnTZ25LrmFb5VqLanEIrtLe/A3+9bx5KrjD3TG3QqojvJkjLb3IS+U/J84ILLzu86tc7YFkFIfRDFFo9O5yRYawLJGCoUZeVEro8bMrc0Qzt6IWef29tQZJay0SB+Hx4KaldfRjOnldIgKf4WaGnG3pQdZVgdWskIxtCblQVvNuMaG26RE9447biO4WOxOcF0sMwMdB0VwZJtBDwRNO++LA1LVYWeGpgE3p6svXqvViHPB4x4YA6evFna+hHnVLlVCUyutrGP04o6mcSOw5KJpqCDXCoSHQ2oI4Zbii28Hc+3ekDRtpKmramnfLstGp4OOWZNtxIlJkeNrlq6QDBD0pKE3Xu1cEqWGifSl4g/N3K2OztZHLMqzOhtNvX0qmTGA/DjIylM43kQOdnbbhzpsnGi6ZwpeNOHNs/p/qS2OBGUxH3pn8cJKt1hHSQgxi6UokvQnboBM3tncTyDf8jwBpReQd4pUA5DakNeyOo9vR/oXPUgLDLLnD4zq0HYni82X2KYc4ouwQ2XciEKQ0zo0iQ5FO56JJwsjTirWsaHIdqL9N4hEqqB7mK0KePlssMuE6puL9FK2ll0MvCb/AZl+03ntQa0p8SBEjcOpGRLmPdQ6rjTCHi/2iaOHFkH5oZr5mhet5yw7z35Mmqilhlqv2za4cTifNfUuLGGIMsj6pGygn1CL7N4BSuBweFqZta2UwyRNjVrsVCC4TINEudUxzVtsRplMSgfjkFqHcX1XVg3qsvfpBXpwMOusYWqMU3FRtMt37DXddTQSsgy/WBQy906wdVEbIu+3IfaziKhFBoi2r+rQgpUkDWFtxxvlVVpvYjcaHLjeawd0BTM0uWVkAdftAytsRNd3LBecrZQhhCLsg+kbrLPeI5Rp3AA3nM39Emk+OvE3DN9jSqNOU0nY6k1UbEdt71zVihOcSeKvWelTVBdtOkE7VqS7RKKDrFxmwJimcASwkEESO0Fe7nvSjYcb4ZQDcUpqnMGoqclDUHUAV1LNU17ri/EaEv7UjAGcF5uODhfIaHNqYWwlBhyj5valsFPJ29Q7kyNFNqu32+5mChPF2lM+LpSw/t6bI99QdnFxkgnnE/ONKHfKGapMRxNpAc5OTT8XRBrrLCEzil6po+iLRunY9xT9NYikQO02qgJgW4t9Yr6BJ1qe3m9X9NUGTZm4U20aWWloFyZVUvteA+ODlbL+5ZTlQSr3yA6PInI0kSU+ETJuqWss2JwMVjg1wi9XlMHL23TTuet7uIQ/TYw7tJ2kFYFAtpElxMTMnt+Q/RKQNnYPevLxKFHXZLtbRafD3ULHU7ldbc9YKrD1R0mWSE7sZQG9dfROrWVtm0YlNjmnravGH4z1iNuQAhNxUdiq21rCSuIirCDnXxx0ntAt2daMsdbXmgccs2bdag5YeLn+y3tbdmSZb34SGZYETIYuWZxhTMFieCcg+0M5CYQbtT2bnMRocL3PUOW+rXCFahiroedERRusTcsMz/itba7a7YDK6u2zCAVGydCTb1lYhAsceAKl7ZZcjM07gFZxbSGKCMPyNMqKBpTx+Lc34k2jKA6zeGVoVDX0tsi1gUB6DjhLTbW1xXcRvbVuUMa75o1D0e8HWZxfx63XHT19rIh0QXl4D1J90UwnFCX3u/Xtr2/XFhauHT27nyZwvC8Hfp7RQRQh40nrdPy0Jd3qtTIsHdLu3W72o432YdHxxcdqaMnq/DEi3CzVrIm2rnVM8QuuXIITuzGkXY0fixGVHeEfXytaqPOzmeSE4lAGTShFv0tjCoEhSpwQ0f0Ed8t+ZzurMo3I5onh5XAonLCVeGRP/q1xkiCfRmMjatVcSZad3ly3GhFTteIxs84uaLWUUQAxfpgniRh3CeFqqldnLRwkXdYwJgnyOzNtAvX4jEJCui2t7GCZumAqybnjnTwiWUrjWvVlqZ47hbv2WEFR8IWhdJJPufN9swwt5URJcsbcArikBDriWhXfHtjhVUAlEepqysNnUcs7NY+KqfYOWYpNcVX5fzsdp9I9Y7fYubZR8b9Eruvlu25RoObCSOBuUaDckd6N3MNDR6YRutgq1vAViUnp0oIfgNUFKOE3DMncYeH56voe4DD0NrtFHUCJ5LTuDkqaKbeBKCeq1ecXJ/noPgwDdCyCHmdhIJVw61EQcqSul6Tsblcrq9OLW2M6xR3ISNA59rV7Wq3qin7Wojrk3b0pxY2m3sP050cYFV0RuWORbI9Trtp1W/Vu5wXnrva0+1atNRxe5Z0WjI2aVdxo4R2KYGg6lqLEezqDcMoX/itrKzoSVTvCalIK4Rt3cv9aFDqcm1tIWbomjxUrfK0BAz5JvqofytiRDoK8liwJE5PnDLIPOcK66CCakUol2bW3ZJTwZr8HVPUmsU2GKKtl4CKlMrA+AeYjdRwpY9rH+LJtXLP8MTr2oy/75BzbdAHRs+5mLmcBWaJwHF9ZdttL5XuKBKyOOasuCKFq5PuFWarYMk2ve34tNrw1c0rSH4VE5rmA/jo9SYxkMDL8LaPHOVQXnbxkY9RQPrQdsUBFlsaAA8gAq+steJQIY6ewiPViMP6tms8lTGvrnu3ohseICJP0GUOTbm55vQ7e7l1kbzaaoN1dZn7VuXX9OheMlAlrc8tE8I9GutGBIvqOugk75pFThcTNW9O7Vo1E+LKH2T9ILG5Bnmi0gf6jaBb1tftCz0lHZpBxbUsrkda3NzMaqlA5RKYJVuiKro9ICO72WC3Q9vSMsmaOWdySe0Yy7y5HE4aBCisThNrGm/a2mWZc5/VQeIhPG/dkGUhUcvDPVJUeMUCJ17yRZaC+o/fxHzKTAJqcHEbXE/3Rmuv7HlESEdC6XJ90PJ0sHYWtu1we6fTopCsRqXZnMUdC6qXBl7mvEUvD1p/oeORQxoln+5aSHGpCm/1JVZSHKGi3nYvbHgXi6h6H/qTW0oIBUIQdcr91s+GY5WQx3gnJ5f1aXdFEUp19oaOQDfCCJYNdktHgqrsEuK7++FG8Ty+UTe5gkGrSMUvPY/ccdIf1qRO9rhBIYOajNTqfLe1CqXvap50CtrRmObydwjqzSPBpOrOVLZskXouxJYXhCpljNPC4wVKcYIMCfs+6OM1VyhVhgxIjadoCQjACi48TE6Nw0XYjcZV6rRQHI/hPgmMPqnLlL5K5fJgoLdbUq+p07TGjxDlnZtB928MsvSgVeZl9f0mV5Gwzrb5FRVxj03LjMHjgCl21ghKLIO+FTWeCbf6KozhclQZwz9tCBjmz/bRRVZUml9YnLwUGM/o+OF84NBje6LWK+9kjBDs5L1C2hZZxxB9am+g2N3cJjHkjAFQNmp5uuWTdTnm5XWMM2dZeAFZk6hftPthwzZRMt1pbik1VrQFmUX1o3CcZODeN0RKiqVxdEaTwAdbC/vaaPvdpHNHemP4sHnrvbjA+82QIhiOEbInePpujR42pZFrWlS4e5K/DfVuP1lbkT/KtAg8VGMRuw3q8+2MqOWmIq3ahzRHR3FnSVFccVkzfYtY+tVDiuFsbTfDSnPYlc2Rh0HZd12i8RCjMQhkZIp10jtumSM5KB+7pTG65gnxKml3j2yqCIidx5hbW4u2ghbTPTwwyoWiD6xk8x1cyLxnnumjkPTRRsxJZNxcB9cfSt6F2e0Gy1OY82lmVE+MEE5euttnyClIjZA7uPgqlEVfwFHlEAHWAaoZXE4T6Mw78SSc4clE2EJpJ4fy7ipwUW6qcWg8qP1NRZT2Hl/39NJkC/XqB2W3pOlepyZmKTPtYQRON0B5Oi37CsL3MK8NyMY/26aBXe+ZVJZdgBoSAwnqQO1PUFV5Q2DvffpEjPtIEw7LIO/pk0wjPWqfFWVw2CrqmTYZQiMTsU0p8GkcyKzaN4V1kYoDdd6webqVbJV2WXwT9dM22tauYDk01djhGqDBhAA8RXnpFg93t5BlzKzbAGupbB0efaaHhDuJctd+LQ2cdNgzdBKcT7CMTYJiBIDflO6FZ6g4vFaJtT4NwpnHk3hNjOimXe6vfABvJWKfxPBut1mdsNP5eLhFYFZgBrfVEUm5qE23vcaXN3yHKNUJbU40CHjm2GzCNYkfrUPvAloXkNoOQGG23sinpeaOTpZ5FwFD8CNdjku6241opVA7bHM8XpSw3E52yJ73QSNm1P0+IMdliXOHiYGVaNjizmrseZjVz/pB9S9CuqRdpGe3esgiuMOhjkFctYAac6lGjpBi7c3DiR7GZs0ppj3mZXTYjkzlrA/yFjX2ysa/tui2uEc0lu6lY7oiN2VDuOZkTklFssReppabkZXUvLwd7OIuaBqPN/aOGC4ZH+7NBD5Fy+LQU4Y3QfvMOVU42+zOHc/c4lIm5WApXGVqA49nfFsbpC8UpXtUuyRwyjjj1hfO9HZ7ltMaLdpdqDWJ0Z05Grjeh5tao/JAviqk6vaFUezvaVqx8amXuIaTMMYRAS3sxgP435Sn+NEPyc7f0ndtuGyWulFUMZbImzFpequG1ekoOXhh4/pRcPpTnATJhr3n+TXx7nVUoydXsjfiqCeXET+TFbA2nh91i0qa7LKXQZWNBOvgtOzsO++m63w4ihKzve+2MLwCRcXhzIFay7qMge9roSWHZu5RQWewx9K0e5W4FoGLnk0sM+q0aQMznvY3plLOFbpKwtFUUoodmRMfils9Og+wrBHoAY4mP1Cj2wY3fbyqppyWV3pfK00QmhXZupJUyimrDWy55dwzxuGGJVWZKjJVy4x7X0+nFQfWl5MbGB1hrllvZdiw4+O+OQ+Idoedw15amVW0jbvKRMzaTQTTA4zPk86yubmjK/1gcKO7sdC7YMsXduPq160YOCfNSZk02x0CF1Q+e/US8y12bOqYrvdRf4Am7tJhkcKtZYH1swYlo5u7bi8d3xGu2EFGT1e77Fbn560JCZi2HtlJ1i4bHKYIPzu3IcfsXR6gExFaw70H2bVzbBzV0J7khrAjmlJU5QPa7H3lAIqLKXV18thdm6kRNxKLJ6rCItftNdhwF8uN11ceZEYv25RrANRgsT5KXKejgOjQToKgNKT2K/LO4kIYn/fnmshYHcp3jbYpJrc4tunVsQ4JOhzTw1EgI6CMllXjMEWWR7SLxNE6NJ3Vb5PCKWqoQtGtQky9D2rhE2xVxgEzdn5x5C6SsRJ3J7awx7bY1M5E+RdqD2+28SU7SEKUm6yPtUrNOAwvaTFBlPE0Lc3rlPjjcrm/WGlwkvSqRwVYivsIqTcySMQCL2yuV8tLT2pTVHIh2Gmc1mthSwr8tF3zR8SaTniV+xpXacv7wDFVd7UHLWIv3VoMjbTtPOAOSwVruISnacyy5IteYteNlU42QrRur+raKh0ZC++w80zp2PvU5zVJmmq/Krm7IZq11vQHMRqyM1ONdrlXWS0APJFP5XSrBZvSldhEs4bLVCfOSqikanO/wVfZ2Ih3BTOt0KUSLUQnS2a1uqvyTbCDdK2NqWgpb4xLyzlew26bS19f2wHP4018OZUeV2vnNs0oSbyTbkBYeBVBG9KYTDXtdAZN1dWwV4dLfqg3CUxDzOHUYfytbgYHIZvar7gyRLQQm/y1vaJZSrq1d5ZRDnIRY9mmwjVRBLR3VbmUaIpCyW3sHUNgl26qqjCxquM1Ipt1Tl6J+xEdBHKDxHAvnFCyVFan9JZrgqZfIkdVxOudQzc57JD8cpPelRNu64cWj8XGQgo6lNHoGKgiBziqoiD9MUo2EMvwrHaoo5UCHaf8aNjN0vbEq0W48OnSdYTUZu1tc5PzI2REykVgDbm6bpcc44l+tStligiv5napK/V4Im5CdBJbe3m/nnieBRV/0eaeqgqDk8hn+9KVewiqM+BMLjm5MgXJdLgJ5ONBJI9I4feYzy7vF/HsMPBqVzhRwN8bY4NkFyOQ0WR7PCZ0GdzWJ48Vt2Uf2kkmsWiFrPQw20tkzkS1xmUtuk+AwM0mdnH5hl22NHHFe+fKD5F6LzzLjJQDSKUm1GI6ShwwdSjWx/tmuZEiuVDJs6ZTvl9nN6kE/Be7B65eaHQMHVEZjZdkiZkir17gjAIEN7rtxkOGTrqoEndh6Sip5BPLXtOtbbhrmeEIHfv98cZddNrXs5XCD9TICjZTONs0tkaXSE05EmhjvXdLU7J2aHM+mVhe1WxpZ2yxX/VVoASsrTBjywuykSyzupxcW5F4zrdIcqxPlR1z7vbWigV7F0J2Q5vHOqFvg85uyhNJsYOoRju6FvYpkhdkJniZlJNhqN7IpTqyvXa42oRk2kmab4tOXyfxuciQoOxbx9flTsMVZ5+J5nai3Cgp71fbqaRUWtuB1tUrvGyiIDntj7p9UFD0ssbRLbStd0jiufYuqGsTv5+MBq0Np79uj2t2q9piYZQnN4byAtdPlnVTxzQGJBDd7w2FZbzDbuovjnxOWo9I2U0gTbqcb42+XItDl/RWo5ps5mjZpTW3W6EScddpHDk0qgO6GrsbN0xMcS+m02Fzhk7UpB47Y7zqh6Beu86tXCsrBKR7Z4sFtUipAcq54jFmiH3KwZ69KjizHPIg1ywSRk1yydaVLErSqbKctqw704LpYEjYElGsg13JzBTzka1mAZng8t7FtOqwqc73E5GG+xFP+Ox2ihS/WUJsdTfK1S60oSQyesIdbsnqku035UQetQ0tycc4ObrCwT8DZrmthNo2r/3ZZ0q8cgJWxQ4Siam5fNhOEn3ttVquDvOW/qQ1BY25KyG9AHpes37jwfbauuNH9iTfdT5dZVd9qSAD+G+0ut1WTwpL1Z2lrjniScMyKOP840E38cIvLhLjQAlNNiiHDmtKPqE7I4F8ST+ycavk5U5SI5jYyhF1oJFzZgdnjcmOBepN6UW67JyJbZh2c+ZBTsNLhjqnu4rQFRdvyl13Hb1qaVblupJ5G13F6KHAxKYIesWoYmqoyU1y9mSx6ngjxNIpjYqWhQ+HI9XlI3G8cImA7A+okJ+awtzY9J0jrTWXd9y1Pe21IfcgwkQDaCv6HkGy6GoDr2SEnlBhalXbt7C95xkpxXTXNXZ0AGKpqZ9BW4UpY+bib4T75Wpd94l60TLC1TahJiUWujr5qlceJLxpbA7Us7ckNBS7WDqtdxCDScQRq3W81Zhe8N2+7Ai2mpj6wjmcUBTlzl+pl/HuH1BqFR+c+nyVd/hdJlw8YHC4CBLSOQGWu1t3GtnbEUy7rS4MbmKCulyVXdwOmoDCKdYPDoHpNSekQ90ksLYaRAm+AbE92sGherTGgL3qPnlybbjIU4XjXZ2/4zEWusAHLAGiqYrdw+NwPSjpvVhfTRmwbJTW4fBQhdYt4Tcw1G3TKnBuzeUuJAgUtkev76HeubCEnCdJcyx7Q1UN73JctySrhbuSHJjaN27hRU7T02lN1rIGCkV0J53Qgt/41u20rpwRO1WCDxl848obNNzBkqNg9Ugtl4DjhmkeQghmQC2LWDioFlnmpm8x+TjetheQZia/UnWD3HVLL7yFPWKziH+3bgeV3U/wQBRLzEMdd4dAJDMkdkBRdD7Qy4beUN7s6DFJXoDplwqgbMU1uRWjn588HJ3KFGaFsS6MaNybCO9sR8+wZfY0yq1RRPcoRwaSz6/r+7VDkJtOZ+0IXbzryZNBBECnNDflju6BWXemoyMEkaFn8Zw5rUXEoGm+ET3MwfdBZ/FHZ+XquI0r22XZjpUcpB0L3+ujwPE7ZGTSAiQkqVmtrlZ7GuMMAvo6D3c2uV+OOc5bzUHT5WONx+fam6iNhMlRf6+ajIQOiLDrD9HOwtZHPoaJVtoYxWXK10zH7jFoB9NqUyPwzqHOjJF2rpYXkmkw8p5BfCEkr6KZjo04YYl39Aea2+2MS0Ed94DjX0hacuDshKpmU1BdKLJY72rHch3X12yt8JtreBs3xUE84HWQc1JBQuxFt6egofuO9ojsEMWWHeyYY2wNOR+sGPukBBK6DUwKlJW5ub5qbrLhqb7Znu27d1+Ftxt+vrscdEflDYIS4iifaq8GeKunje+bHXu5XfjTbd+RwhY5n69plG251vYkg2ElW5l0irufr9xUW13fjyJGSQwX403lXvead0qzicZqJDLP9101JRLu5Wwsn/GDxUEEFSu0NkiupWJ9vuuyiitOkDSiqSydr2p0JwgNFEinbtIMWLcRMumF3c5cL3NcDXaOQztNOoXXhBY9iwT853gZ+BvZSpjX5DDDH6l2BVDMtfkro+tsdWni065d6xSy5M7HC2l6QXwjCNe6KOopMbbDess5xr3TAt3Kp9juG2Ucjvf7cW3naL5CDuxtI5OH9DKcw61/2F+PQtfQTZnX5rLwOTZNmp1D2wJrn/cXfKWRp4i8MWl0i1g49lGR6WFVMO9eeNlNJpa0ECeYViYSm8krkc7N7Ghcdgm8tm1YwlJbYuo+We2qGyBft8sqDC77eF8FmrjJdOyewfq+gRk8rjaXHYjyllaGFj1zpz1FOYHfD0NrNVwnsAPODfRolnurCw9SknrUUgQp4AS4IXMc87PPSiVPXfs+OkGVizRrXuB6xuGayNdwtwY+HTSKdb/ZO8W9bYh21JatHnAqLZH9MgxKw91W2t2z9VyS+ZALFQtatoqz0it7JRjCEGTbBtaVIxSh2bUiB06c0N6XO7UcZOik0Jifw0UaZkejDYMiK10v1nODgFHy6km3S3ncksZyHzVXIy6JcwmddLKTakotb1js47cIhhS1hyYnz1Edg/0LbldhCN1Hgr9h1X5QdNprsYgcN1zN+10Y7V0muG1o7noR8+1aIZUODw1UXMZtTKi31JQwaD3eIfG0vEcH1YzvONSLpTKt1Z2blfkBUVf0QICijjY7hrZgd5NQfbrycgZtw3B10ptBWCKpKaoFdfB3jY6bNKUqm/3JU+LispeyVcgbIGUWlFbY9hJzp51+FPT9dUkkaLKR/Fw/Hzcj2vVOgAmHjRqOq3NY7jAzRjea1m84BlsHWF2XdcPcTIS9BX5poC1ZC3dl1U1uL3moiOxUrc0Sc7+cUomYy9oNn9RN6Kv+vbto+/7WyQwjLqmLXscXnhVjL8x6buklTkgvKxnGRsC3L+m46V0aTxtY2wo5aoF8kMNmdhSXXS9W2JFoa9i6icQOQPvBVVyrClJFHXmv62G8QEQrZy7xkSEDo7hlccncDybhj4QphrXK9B5xHlSRIWBniiZiIKRmmTObId5CGxbbaFuP91Z6lJzg+eoWZtsmmSf7kL7tw0kqSjyoWjhfrTJmPEqkAyhKxFzhyPGdQ77ekYS0O4PEbMRnBqQN6rp3BqhAjUpxT6kgbpVtcCEQM9wKY+N06SlYc0HtHpLUqdf1hGDXfGxq3TDs2DzupP3EtnClqENwDEPncjJdSpcjG79dVVFuHfEcCRYcCWmsLHeQAiDqAnO8zzoncmQPzXqPjdrB8M5bPebGMhs2ttexucrmW8UX9Y48rB17HzgsYCnDzVe3qL8CtUCZBZlxz/CJFlmeFMkEwzcsazGkUOTLJRDibCVxa8lpHI5Zs87KbZBaAMV8Oz5pUxd1ptERw6iu45BLpT0vpOfxEN7L5qb1Wdff7UCkNsKqz6/TkCPEMT1t3ONwPe7t6/oy2roZ5kgqsZfwoOHbw4GMrowXWuzpOKUha/XU0FnwcGMyfyMpBwbT6cuOjbFxckKEF7cYJnGhpQA36ta7vCQqN6sCNTSd69FFj4bKcveyBMkbwihqidBjTY9+hXY0o+3dYZtam0CLagYgksweePm6k5T9XmXL4mp4J6RllvQ1y2/jHRMdOpoOZACK6aK/DnoUoVrZTT5JtDg8oN6tBWQil0tvkojOvt6qRr/DAh6Ucemq3QY7FPz9VsWsjrbE1aKiwliqjp8d8UrksYqnCVkdE/t4C1NAKRFlZ17zE3LSQfWsYaNkBTiFn3BVJ9Z67giumDJFIe95mS8LDN3tCp1Xztcik/axzm0VCMd8UAVamOjzdbKktdFFUPnsrvtt3kJxifaqQIhIRV5PcDvIOmUOOhePcVtYDlqxBleqnqel3l4/GmZ73ttj5m5izqkIaqcFfH4nbeWwxPPbXpHNdbkPcIE78XlFYZsrh132mguYP1Y6J3zHi8c+MWn6BmumPej5yCprkoKaIxXoir5b728lcRjtDJSpIWY6NpMEYUEUUGNgyp3dNjTnykdeRXZNwSN2kV+8hHMK3hEIc0cFNaFZ12XLrYz78lIY0LgLTtwU8TAovngzOY+roHLuIteQa54JWC2mrbuBTXaf+UdofTndRdv18d1uNUr7nGCa6erf/WwzxQMGsoK7XrnSnRs1E4ZXUeRaGoSuHV1GMUFdOfCeEERn6VTBIXUItm9p6X7SDGJvLi8yWtqswh9TZ9eVjVLe5dCx19sdmHzHU2LLn6JA08/1ChQLd5LcJbEGjeTtjm+LNp0AGOeQBXi5bU3GJPaNkF2qtY7YvLqvOfrW4MyVWSacdT2D5FYOapXK1RnlzmWNHaWYUWuUgLPtkKeOsSNBkXb1DPF0a5sMY++peRGX+p7wUy9ly5tk1lc9b+DLMQhwRPKx4eIYZX9smmyKOXhQ5VOxMmCtVm2Uww7NgI1mzpFbZIz5e8JJSWMI1nIat7nPNnvtOo1D1agptT5g2LiEtmWcBqNRFZIGp1rfYgTCGRe8nJBJEZdmpyqGrSWK3ZBH/WSumQal3ZLry4nm9px1iTbK1ZrKa3b0idvpugyYSjmt0g1XAEDeOIk4JVe0tns5advitLufmqMvRMezoDnJkKpRjWG9ihVM3O4YDNHgKwLtGgRE+PWSTcsmmqqbpF7D047xA4MeadvY7FMhpNykSdv0fHTysOoLJ4rCsDfZIy1PkdcGa2/tsylt8mif5wZS1AePCVwIIVxvGUK5qkKcF5MmVS4brSYnrLeha10X2gTMhW13h3t/tTkjjwfytl17uGKG1xq1JI5SQKxsMrbQSWO95TGjIOsjs4utC34XYc6+5GO4hPa7HDtZyTrHzTYWCgWRm7zq98wOo9bwityfXNdqCb4K4DIQXXZTmowHQ3x1aG/Jih9c+RRZ2yRY2Xae0x3l3vqlFPbKNTd24mUFSW4u5QLpuPP/u4E8UXTXjy7k2NG9G81oJchLwwiYG2bxciGEYk7cVlQhFRw72JW4ivUuS0t23bV17gVKR1xzYgXbXdqcemZ1WSMCWlQqr+7aid5Xuz43kXHZr2QTPa3jowC7dMMimmPRlmjIhyu7wX14F9vSvj5cPP+swOdCXgXSQZBKfX1O0uW0O0vRRSxPhiEahdi0cMAMklbRxZEVZXOUt6mIjt0FchBCPoEkJluWspZA/cvocJuiSXtUrhivFqf8rBycO5ccqn2Bn1Ra3HRaK7FVzbYatzkt7Uzrk2Hdw6lFC0G0CeBC6737SHI8sV351+iKCERCQliDnZgxg7tkY4dYNWblLiVBEcHgNLK6HaDg2oPwcDiNXZeyf7qtnL4UiNAGDJBkCJM42217Tfd3rTmoIs8B9KCuwqGHm5XphLV9FbLp2l6drrOEsyTviX0oq/SquzBTh570XM9jwmLWStcraALBHMOd77whxuU92HfuDcdo43ApAPaTZDUK6WFwWb2hT4eCk6Yzs5S8utht0NI3yxhxj1B3C/LLBW/QvRSM+gXa1yRrXvYIOxkyPYjq2Eba9ZTxAQQrJ8a3xKjhqcat8FvaEkoqTz6ExDgjOr0GnTS6lUa6lFZ177e6XSDwxopTZUCKJk05WuLgfvQCdD2tYpSwQc1kmN1F5kgfToldKGa3Q+bRcGKZJQsZF5gtInRpB7YDCat2J92GMkj5QjyP2CYpy73U0/fosiSmVbhK1mlnhdVAniD+tu1laVWSN/yaVsLo7cKjFK2cIS+p9LxKedy66Aq60/eoaqcq559wreE2oNZfJZhBBt6d3Eegrtme5asGm8tz4JbZGjkc7g2PUgawURbfDN8F7MX01uV0PAcCQbfkmHXAZZJrswoQTCNvcA2AqEAM7yoYuH4+XZ09PJ3P3o1ZHUgqx/bHK6DYmXi997CzuxcsfkfXCGZer1RAbbYtSHmyxbO2p95WXQ5zCHpYWqejOw0cu/EIbY1QNOyu7occKa9LfFCHxKwBurNtUS/zLVP0uDr5BoCHM6tmZ6LPxrMDqB1GHUnMT60lcjxiJHPFYis76TuA2ZlLXylhuGxaWeh1ejDvFMKcJ73hrhTktSfFCjAPPi7b7WSaDFNk2+iwkc+lRC2VSBb9s7iEOmRcEb0pT+Ht1lrquWd3lR70nk4ZZoprBb1koz7pWbonKe1WiVRqSHs9WXoGVAasT277KFwyRwfxGAe6qo0prYaztNsGwvGGylEKyMsdPim7dTypgoAdtsu1qFc6lNTI+pjcuDwILd3w3NwF2KHXa5Sta+E8jetNtomjSHRa1nAsbI26137FWUTqyZTSHM9xmsowu1Tv5AaGsbBpV4R8ZhyKVE5Hf0ez+lWopUEN6DIHqRGXLityHdfl0GzPGYpz9aAjtxg0v4H5WQLqjSfWDhiV5CuNlo4SwlpHDROTLFHNViCUc4xC4XlNeuG9Jyxqo9uSQJVXC2sdAnMTUI9bW/JwilaUTkIqpypHhLb7TR15TIIkcZZU+3QTDgLHKAkPnWRcVll6NW0RfJvdc3xpIBLlJOMmwSNkzGscNU+cWk1+PnrhwV9tbYoDgHSgTGpnx5tyhLueynoJ0naTd5YGYnezKd4cNxV+nrYZSC0NrnhQvR8LWfEynjaW1ahOPX3QOArG1tnZF48Zb04Tk+1aRVX5Dt069bl0YY/zrmt+L21gxbbKgKauZ1gRMXQZywk/GNAdWcPL4CT1fC5TbJvR62IQhJBOR3RXHlPp2MYNmYk4QvHT8kBs/Ut7pLO9ZHEKqCqKpYODkoM5eCDMqsGC02BLhY5ztOoS5krzuCQPEw4j4UqwaU2RI1UsLrfSjTM9NFuM2cnURBOCnU7iSjitdWmj7dCmNd3AOLPo3VtxVzZPDw6v3uPpDDKfaKdyGBDQJrnr9Hq5DT2SPreeRm+XkdDURDIWSltSujVpa+l8b8SVZFFwb7FKZyVEeF7W+aHFAg92JFuR7FKqCGKC2ljiLoOQnSFWPumF0oxGxrC3yvLWGKsllrhjtnqbEWg0ykVoR6OAwJjQVDC60sipd+uskogoJGCaxzFbY/hleOAnJA2ZZbeBioQuYWfgeYBJanBEiF5dDbiCIGkTh0xHiV5dixmzFSNzdPLD4f+2diY7jxpRFH6X3hKFoZjcUhaY0YwGMxkpC8CAwZixGKW8e3D/nUjpdXYIIQ4St26di/QdNgd7Z+/DyKuhkcpDdCw/cLaO5VRFxuX9cJ9hyN0IxwmeuHYSzMo4KVStwXgg3Us0IbMb0IeZPCzJyNBzYIMKSweyASDF3UWMm/4Zu6oWpS1MhuZev3ALWGqxCJxMVvbxnoRhjW2izauVfNqX1bHiWnolNT6kuzwTPr9UhwlOxdhAfbYUTgh6KbDb3fWs4bGGTJAeRuKEVctWcbAye9VOmfbsSNJlozMzZrP9Ycwr5xSX3k5gxbwIhKLE3RMEI+obEkAxKxYZTKoZidEmsLz0uJtGjTrXU06QyCK5x1hjvviu9Mf6UhJoOmCV/h52yQF8agh7Afmb6Hvss6gxs6X5paFkrCEw97T2FrIMrPcqBqp/2sCCqtsW6FQAs9WPmr3HYDZf+xqddSMNn2po85QeWec4InpdsGjL6IGpkWvi0xBzjtvoVrGiBVril8CDoxqYje5dApSiEiJYyTOY1mFMNzfTFZ3xC+aFXKObr07j6BON2kqRwIfYELtTnt/W3GnrtgcEuE29bEOwA8eAGxLBKDutG5K/Lb4DqKGj7nDskxBJ3gNsxFuDlxmyIcecEtAFnrx138hFT3CU5JjPOYydNR+pRg9RCXureM3V2xFnMU/p3DeeOa88Tj09USWsRNj8Iud3dgzBS9mppmDMtCfsYD05b0xrcMXrUK0VxyWyCIprVn7vsVxLUzFgR1MfdWn0FfFq0scogTTtxSP4snDkfebPlu11ss5NcV9Nbw12cq0F5E5iJ3cfsNgMOxeOrFU6iFRENGFEFYq39nx1WEWjev58H4IruqiZROLplsxhAW2fpc7LWRUhW+KoomjHXAzqQHrOZXne3gNnmJK50H4Gazodkq4n404YvCQkgaHPR5vh2jpysnnBLmNKeylBoNvJUKguXdf8quEY89wXLFcReTBVUkemtkVFl85OPfkmdMHZUYovqG30awi3LrgWYc/P8ITg+SgiuOyl4bm9LLIc9ctcj9VODdOTfICNIio/au7qsyY2r4TEQmMBvbuvTtfLSg/EeMSEmej4J6DcMPc/9XonyWuNbRWxVKw5VMrUSG5nKdnKYg+zQr3743F6pevne83JUhjX99NzXTIq2JLYlnUSbLNHyhnoz5yVeNYDdKQ0L+pkJquQM21+n+V2qkvT06+hmT60mT1nlTU5uZBkPUD06/ti4WF5AnRZz8dx19FWk4cBQk8kmtF2fJ8b//m4vh+ofLEyDSmXMB8gNmO8okaeVrXTtuCw5sMa6lPKvsK08qCSMLNkduDWVdyQsNI46HtiMkNVQsX2mXWK/Ti0ySIhH45s75Ojbh4BDpMBIpvnD+NKqrYaXB7vo8E0RAGGMs2uGkbcYTm3pFuBqbfYw9OTuCnDlbIXEkkoF9c6pLSTlt6Va18jeEZQxshy7Z4xTGC/UtloR8d1WF5rXF3sPZ7l1FONcVBF7XU34Dq3NspkEBMf+FHO4iNJJ931cnLemTNvXqnXOuXSQLcNlWvV0Uomqjl2XJN5eiEBLnmfM1lm+RpW4PmARRpzd8nBo1I6cHji1rt8SHF5pTn+IyR5j6kCCjEct6/glPUJqas3jXZs+ymg2xiZnpRtncdx3B9//MTZf1L1/83W+aC+/xtV/AUHt/Mh1aTZh4/+RD98/6H1/RfdP3/7NqTlofoFPo/1VPwEjX/Q6f9gz7/mQX0FBMC4+PyT6du/V3VZ+gve/w/j/jn9SVF6f8UI/IiE+oj/zAP5eoDfiW9//Q1zf133omoAAA== -->

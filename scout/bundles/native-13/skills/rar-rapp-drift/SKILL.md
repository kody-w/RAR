---
name: "rar-rapp-drift"
description: "Cross-check every canonical RAPP source for spec drift; report each conflict with which source wins (authority order) + how to reconcile."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/drift", "rar_sha256": "b40ed2f9d3cd95038078b0ae7514b31a8da5e36a5b3b56c170d625606f97176b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.2", "author": "Kody Wildfeuer", "tags": ["drift", "spec", "authority", "rapp-god", "alignment", "audit"]}
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

<!-- rci-capsule:v1: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 -->

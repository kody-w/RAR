---
name: "rar-kody-w-bond-rhythm"
description: "Pulse the Bond Rhythm \u2014 the on-going local\u2194global beat for the FULL organism (global body = offspring repos, local body = ~/.brainstem/). Runs the ecosystem audit, classifies any drift as LOCAL\u2192GLOBAL push needed (suggest Launch/Graft) vs GLOBAL\u2192LOCAL pull needed (suggest RarLoader) vs informational, and SUGGESTS concrete next-step actions. Does NOT auto-execute \u2014 operator-mediated by design. Default dry_run=True. Connection-aware: gracefully degrades to local-only when network is unavailable; the next pulse catches the body up."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/bond_rhythm_agent", "rar_sha256": "88bb285bbf26b68fee053d24bf70c08ae1ec42e4c3a03b9afe7de2c404a5a219", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bond_rhythm_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/bond-rhythm:e8964e8d2aa98f003c3a4fdd289d7fbf14e4e712048ad1abb944a3e84edb4560", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["heartbeat", "drift-detection", "ecosystem", "operator-mediated", "bond-pulse", "rhythm"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/bond_rhythm_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bond_rhythm_agent.py` is
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

bond_rhythm_agent — the Bond Pulse heartbeat.

Per the operator's framing:
    "this is like the digital organism pulsing from its global body to
    the edge parts of its body and back again in a loop to keep them
    aligned when it is possible (connection is available)"
    "you can call this the on-going Bond Pulse: Bond Rhythm — local↔global
    on a beat pulse for the FULL organism (global + local)"

ONE organism, TWO body parts (global = offspring repos, local = the
operator's brainstem at ~/.brainstem/), ONE heartbeat. Each pulse:

    1. Run the audit (tools/ecosystem_audit.py) → see what drifted
    2. Classify each drifted offspring by direction:
         LOCAL→GLOBAL push    (offspring missing what we have locally)
         GLOBAL→LOCAL pull    (offspring has newer state than local)
         INFORMATIONAL        (cosmetic; no action needed)
    3. SUGGEST a concrete next-step action (Launch / Graft / RarLoader)
       — does NOT auto-execute. Operator-mediated by design.
    4. Record kind="rhythm" event in ~/.brainstem/bonds.json
    5. Return rapp-rhythm-pulse/1.0 envelope

Connection-aware: gracefully degrades to local-only when network is
unavailable; sets degraded=True. The next pulse with connection catches
the body up.

Schema: `rapp-rhythm-pulse/1.0`. Bond event kind: `rhythm`.
Default `dry_run=True` (cosmetic — the rhythm agent never executes
anything regardless; the flag is there for API symmetry with the
actuator agents Launch/Graft/RarLoader).

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "_audit_override": {
      "description": "(test-only) inject a synthetic audit dict; skip subprocess.",
      "type": "object"
    },
    "_bonds_file": {
      "description": "(test-only) point bonds.json at a sandboxed location.",
      "type": "string"
    },
    "allow_online": {
      "default": false,
      "description": "If true, audit fetches live offspring data; else uses fixtures.",
      "type": "boolean"
    },
    "dry_run": {
      "default": true,
      "description": "Cosmetic \u2014 rhythm agent never executes regardless.",
      "type": "boolean"
    },
    "repo_filter": {
      "description": "Restrict pulse to one offspring (name or owner/repo).",
      "type": "string"
    },
    "repo_root": {
      "description": "Override path to RAPP repo root.",
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bond_rhythm_agent.py` and embedded as the fenced Python below (sha256 88bb285bbf26b68f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bond_rhythm_agent.py` first:

```bash
python3 bond_rhythm_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bond_rhythm_agent.py   # or on stdin
python3 bond_rhythm_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""bond_rhythm_agent — the Bond Pulse heartbeat.

Per the operator's framing:
    "this is like the digital organism pulsing from its global body to
    the edge parts of its body and back again in a loop to keep them
    aligned when it is possible (connection is available)"
    "you can call this the on-going Bond Pulse: Bond Rhythm — local↔global
    on a beat pulse for the FULL organism (global + local)"

ONE organism, TWO body parts (global = offspring repos, local = the
operator's brainstem at ~/.brainstem/), ONE heartbeat. Each pulse:

    1. Run the audit (tools/ecosystem_audit.py) → see what drifted
    2. Classify each drifted offspring by direction:
         LOCAL→GLOBAL push    (offspring missing what we have locally)
         GLOBAL→LOCAL pull    (offspring has newer state than local)
         INFORMATIONAL        (cosmetic; no action needed)
    3. SUGGEST a concrete next-step action (Launch / Graft / RarLoader)
       — does NOT auto-execute. Operator-mediated by design.
    4. Record kind="rhythm" event in ~/.brainstem/bonds.json
    5. Return rapp-rhythm-pulse/1.0 envelope

Connection-aware: gracefully degrades to local-only when network is
unavailable; sets degraded=True. The next pulse with connection catches
the body up.

Schema: `rapp-rhythm-pulse/1.0`. Bond event kind: `rhythm`.
Default `dry_run=True` (cosmetic — the rhythm agent never executes
anything regardless; the flag is there for API symmetry with the
actuator agents Launch/Graft/RarLoader).
"""

from __future__ import annotations

import calendar
import json
import os
import subprocess
import sys
import time

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/bond_rhythm_agent",
    "version": "1.0.1",
    "display_name": "Bond Pulse",
    "description": "Audits local-versus-global RAPP repo drift, classifies push/pull direction, suggests operator actions, and records rhythm bond events.",
    "author": "kody-w",
    "tags": [
        "heartbeat",
        "drift-detection",
        "ecosystem",
        "operator-mediated",
        "bond-pulse",
        "rhythm"
    ],
    "category": "platform",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}


_PULSE_SCHEMA = "rapp-rhythm-pulse/1.0"
_DEFAULT_BONDS_FILE = os.path.expanduser("~/.brainstem/bonds.json")
_AUDIT_SUBPROCESS_TIMEOUT_SECONDS = 30


def _now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _walk_up_for_repo_root(start: str) -> str | None:
    """Walk up from a starting dir looking for the marker file
    `pages/metropolis/index.json` — that's the RAPP repo root."""
    cur = os.path.abspath(start)
    for _ in range(8):
        if os.path.isfile(os.path.join(cur, "pages", "metropolis", "index.json")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent
    return None


def _resolve_repo_root(override: str | None) -> str | None:
    if override is not None:
        return override if os.path.isdir(override) else None
    here = os.path.dirname(os.path.abspath(__file__))
    return _walk_up_for_repo_root(here)


def _run_audit_subprocess(repo_root: str, allow_online: bool, repo_filter: str | None,
                          timeout: int = _AUDIT_SUBPROCESS_TIMEOUT_SECONDS) -> tuple[dict | None, str | None]:
    """Run `python3 tools/ecosystem_audit.py --no-write [--online] [--repo X]`.
    Returns (audit_dict, error). One of them will be None.
    """
    audit_path = os.path.join(repo_root, "tools", "ecosystem_audit.py")
    if not os.path.isfile(audit_path):
        return None, f"audit script missing at {audit_path}"
    cmd = [sys.executable, audit_path, "--no-write", "--lenient"]
    cmd += ["--online"] if allow_online else ["--offline"]
    if repo_filter:
        cmd += ["--repo", repo_filter]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, "audit_subprocess_timeout"
    except OSError as e:
        return None, f"audit_subprocess_failed:{e}"
    if not p.stdout.strip():
        return None, f"audit_subprocess_empty_stdout (rc={p.returncode}, stderr={p.stderr.strip()[:200]})"
    try:
        return json.loads(p.stdout), None
    except (ValueError, json.JSONDecodeError) as e:
        return None, f"audit_subprocess_bad_json:{e}"


def _classify_offspring(offspring: dict) -> str:
    """Map an offspring's drift entries to a direction. Mirrors the audit's
    own classifier so callers can rely on the same vocabulary."""
    if offspring.get("skipped"):
        return "SKIPPED"
    if offspring.get("ok"):
        return "ALIGNED"
    drift = offspring.get("drift") or []
    has_kernel = any(d.get("category") == "kernel_drift" for d in drift)
    if has_kernel:
        return "GLOBAL_TO_LOCAL"
    has_missing = any(d.get("category") == "missing_files" for d in drift)
    has_schema = any(d.get("category") in ("schema_drift", "rappid_drift") for d in drift)
    if has_missing or has_schema:
        return "LOCAL_TO_GLOBAL"
    return "INFORMATIONAL"


def _suggest_action_for_offspring(offspring: dict, direction: str) -> dict | None:
    name = offspring.get("name") or "?"
    kind = offspring.get("kind") or "neighborhood"
    rappid = offspring.get("rappid") or offspring.get("entry_metropolis_rappid") or ""
    if direction == "ALIGNED" or direction == "SKIPPED":
        return None
    if direction == "LOCAL_TO_GLOBAL":
        agent = "Graft" if kind in ("neighborhood", "ant-farm", "braintrust", "workspace") else "Launch"
        gate = f"<owner>/{name}"
        return {
            "direction": direction,
            "agent_to_invoke": agent,
            "offspring": name,
            "kind": kind,
            "rappid": rappid,
            "one_liner": (f"{agent}.perform(upstream_repo={gate!r}, dry_run=False)"
                          if agent == "Graft"
                          else f"{agent}.perform(target_repo={gate!r}, instructions='…', dry_run=False)"),
            "reason": f"Offspring missing/diverged on required files; push the local version up via {agent}.",
        }
    if direction == "GLOBAL_TO_LOCAL":
        gate = f"<owner>/{name}"
        return {
            "direction": direction,
            "agent_to_invoke": "RarLoader",
            "offspring": name,
            "kind": kind,
            "rappid": rappid,
            "one_liner": f"RarLoader.perform(gate_repo={gate!r}, dry_run=False)",
            "reason": "Offspring's rar kit / kernel files differ from local cache — refresh local from offspring.",
        }
    return {
        "direction": "INFORMATIONAL",
        "agent_to_invoke": None,
        "offspring": name,
        "kind": kind,
        "rappid": rappid,
        "one_liner": None,
        "reason": "Cosmetic drift only; no action required.",
    }


def _read_bonds(path: str) -> dict:
    if not os.path.exists(path):
        return {"events": []}
    try:
        with open(path) as f:
            d = json.load(f) or {}
        if not isinstance(d.get("events"), list):
            d["events"] = []
        return d
    except (OSError, ValueError):
        return {"events": []}


def _write_bonds(path: str, doc: dict) -> bool:
    try:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w") as f:
            json.dump(doc, f, indent=2)
            f.write("\n")
        return True
    except OSError:
        return False


def _last_rhythm_event(bonds_doc: dict) -> dict | None:
    for ev in reversed(bonds_doc.get("events") or []):
        if ev.get("kind") == "rhythm":
            return ev
    return None


def _seconds_since(ts_iso: str | None) -> int | None:
    if not ts_iso:
        return None
    try:
        # Timestamps are UTC ("...Z"); calendar.timegm treats struct_time as UTC.
        return int(time.time() - calendar.timegm(time.strptime(ts_iso[:19], "%Y-%m-%dT%H:%M:%S")))
    except ValueError:
        return None


class BondRhythmAgent(BasicAgent):
    metadata = {
        "name": "BondRhythm",
        "description": (
            "Pulse the Bond Rhythm — the on-going local↔global beat for "
            "the FULL organism (global body = offspring repos, local body "
            "= ~/.brainstem/). Runs the ecosystem audit, classifies any "
            "drift as LOCAL→GLOBAL push needed (suggest Launch/Graft) vs "
            "GLOBAL→LOCAL pull needed (suggest RarLoader) vs informational, "
            "and SUGGESTS concrete next-step actions. Does NOT auto-execute "
            "— operator-mediated by design. Default dry_run=True. Connection-"
            "aware: gracefully degrades to local-only when network is "
            "unavailable; the next pulse catches the body up."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "repo_root":     {"type": "string",
                                  "description": "Override path to RAPP repo root."},
                "repo_filter":   {"type": "string",
                                  "description": "Restrict pulse to one offspring (name or owner/repo)."},
                "allow_online":  {"type": "boolean", "default": False,
                                  "description": "If true, audit fetches live offspring data; else uses fixtures."},
                "dry_run":       {"type": "boolean", "default": True,
                                  "description": "Cosmetic — rhythm agent never executes regardless."},
                "_audit_override": {"type": "object",
                                    "description": "(test-only) inject a synthetic audit dict; skip subprocess."},
                "_bonds_file":     {"type": "string",
                                    "description": "(test-only) point bonds.json at a sandboxed location."},
            },
            "required": [],
        },
    }

    def __init__(self):
        self.name = "BondRhythm"

    def perform(self, **kwargs) -> str:
        dry_run = kwargs.get("dry_run", True)
        repo_filter = kwargs.get("repo_filter")
        allow_online = bool(kwargs.get("allow_online"))
        bonds_file = kwargs.get("_bonds_file") or _DEFAULT_BONDS_FILE
        repo_root = _resolve_repo_root(kwargs.get("repo_root"))

        # Audit step (subprocess OR injected override for tests)
        audit = kwargs.get("_audit_override")
        degraded = False
        degradation_reason = None
        audit_mode = "online" if allow_online else "offline"

        if audit is None:
            if not repo_root:
                degraded = True
                degradation_reason = "repo_root_unresolved"
                audit = {"schema": "rapp-ecosystem-audit/1.0", "mode": audit_mode,
                         "offspring_count": 0, "drift_count": 0, "offspring": [],
                         "by_kind": {}, "summary": {}, "next_actions": []}
            else:
                audit, err = _run_audit_subprocess(repo_root, allow_online, repo_filter)
                if audit is None:
                    degraded = True
                    degradation_reason = err or "audit_subprocess_failed"
                    audit = {"schema": "rapp-ecosystem-audit/1.0", "mode": audit_mode,
                             "offspring_count": 0, "drift_count": 0, "offspring": [],
                             "by_kind": {}, "summary": {}, "next_actions": []}
        else:
            audit_mode = audit.get("mode") or audit_mode

        # Classify each offspring + build suggested actions
        suggested_actions: list = []
        by_direction = {"LOCAL_TO_GLOBAL": 0, "GLOBAL_TO_LOCAL": 0,
                        "INFORMATIONAL": 0, "ALIGNED": 0, "SKIPPED": 0}
        for off in (audit.get("offspring") or []):
            direction = _classify_offspring(off)
            by_direction[direction] = by_direction.get(direction, 0) + 1
            action = _suggest_action_for_offspring(off, direction)
            if action and direction != "ALIGNED" and direction != "SKIPPED":
                suggested_actions.append(action)

        # Read prior bond log; compute time-since-last-pulse
        bonds_doc = _read_bonds(bonds_file)
        prior = _last_rhythm_event(bonds_doc)
        last_pulse_at = prior.get("at") if prior else None
        time_since = _seconds_since(last_pulse_at)

        # Record this pulse as a kind="rhythm" event
        pulse_at = _now_iso()
        bond_event = {
            "at":                 pulse_at,
            "kind":               "rhythm",
            "drift_count":        audit.get("drift_count", 0),
            "offspring_audited":  audit.get("offspring_count", 0),
            "mode":               audit_mode,
            "degraded":           degraded,
            "suggested_action_count": len(suggested_actions),
            "note":               "Bond Pulse pulse — audit + classify + suggest. Operator-mediated; does not auto-execute.",
        }
        bonds_doc["events"].append(bond_event)
        _write_bonds(bonds_file, bonds_doc)

        # Build pulse envelope
        return json.dumps({
            "schema":       _PULSE_SCHEMA,
            "ok":           True,
            "dry_run":      True,  # always — operator-mediated by design
            "pulse_at":     pulse_at,
            "last_pulse_at": last_pulse_at,
            "time_since_last_pulse_seconds": time_since,
            "audit_mode":   audit_mode,
            "degraded":     degraded,
            "degradation_reason": degradation_reason,
            "drift_count":  audit.get("drift_count", 0),
            "offspring_count": audit.get("offspring_count", 0),
            "suggested_actions": suggested_actions,
            "by_direction": by_direction,
            "rhythm": {
                "_purpose": (
                    "This is the local↔global Bond Pulse heartbeat for the FULL organism "
                    "(global = offspring repos; local = ~/.brainstem/). The pulse SUGGESTS "
                    "directional actions; it never auto-executes. Operator drives Launch / "
                    "Graft / RarLoader explicitly. When degraded=True the pulse falls back "
                    "to local-only inspection; when connection returns, the next pulse "
                    "catches the body up — no data loss, no clobbering."
                ),
                "global_body":   "the GitHub-substrate offspring repos",
                "local_body":    "the brainstem at ~/.brainstem/",
                "actuators":     ["Launch (LOCAL→GLOBAL)", "Graft (LOCAL→GLOBAL)", "RarLoader (GLOBAL→LOCAL)"],
                "drift_detector": "tools/ecosystem_audit.py",
                "operator_mediated": True,
            },
            "bond_event":   bond_event,
            "audit_summary": audit.get("summary"),
            "next_step": (
                "drift_count=0 — full organism aligned. No action needed; next pulse will re-verify."
                if audit.get("drift_count", 0) == 0 else
                f"{audit.get('drift_count', 0)} offspring drifted. Review suggested_actions[]; "
                "operator drives the explicit Launch/Graft/RarLoader call."
            ),
        }, indent=2)
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

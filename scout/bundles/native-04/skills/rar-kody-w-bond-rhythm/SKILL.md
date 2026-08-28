---
name: "rar-kody-w-bond-rhythm"
description: "Pulse the Bond Rhythm \u2014 the on-going local\u2194global beat for the FULL organism (global body = offspring repos, local body = ~/.brainstem/). Runs the ecosystem audit, classifies any drift as LOCAL\u2192GLOBAL push needed (suggest Launch/Graft) vs GLOBAL\u2192LOCAL pull needed (suggest RarLoader) vs informational, and SUGGESTS concrete next-step actions. Does NOT auto-execute \u2014 operator-mediated by design. Default dry_run=True. Connection-aware: gracefully degrades to local-only when network is unavailable; the next pulse catches the body up."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/bond_rhythm_agent", "rar_sha256": "88bb285bbf26b68fee053d24bf70c08ae1ec42e4c3a03b9afe7de2c404a5a219", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["heartbeat", "drift-detection", "ecosystem", "operator-mediated", "bond-pulse", "rhythm"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/bond_rhythm_agent`. The original RAPP
agent is preserved byte-for-byte in `bond_rhythm_agent.py` and in the RCI capsule.

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

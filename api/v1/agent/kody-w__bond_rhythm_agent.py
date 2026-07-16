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
    "version": "1.0.0",
    "display_name": "Bond Pulse",
    "description": "The on-going local\u2194global heartbeat for the FULL RAPP organism. Audit drift; classify direction (LOCAL\u2192GLOBAL push / GLOBAL\u2192LOCAL pull / informational); SUGGEST actuator (operator-mediated; never auto-executes); record kind='rhythm' bond event. Returns rapp-rhythm-pulse/1.0. Connection-aware: degrades to local-only when offline.",
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

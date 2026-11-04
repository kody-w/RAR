---
name: "rar-kody-w-bond-rhythm"
description: "Pulse the Bond Rhythm \u2014 the on-going local\u2194global beat for the FULL organism (global body = offspring repos, local body = ~/.brainstem/). Runs the ecosystem audit, classifies any drift as LOCAL\u2192GLOBAL push needed (suggest Launch/Graft) vs GLOBAL\u2192LOCAL pull needed (suggest RarLoader) vs informational, and SUGGESTS concrete next-step actions. Does NOT auto-execute \u2014 operator-mediated by design. Default dry_run=True. Connection-aware: gracefully degrades to local-only when network is unavailable; the next pulse catches the body up."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/bond_rhythm_agent", "rar_sha256": "7bfa5d0afca6919cedff2409abf22fdd8a715525de81426e68025429ef7cb585", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["heartbeat", "drift-detection", "ecosystem", "operator-mediated", "bond-pulse", "rhythm"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bond_rhythm_agent.py` and embedded as the fenced Python below (sha256 7bfa5d0afca6919c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bond_rhythm_agent.py` first:

```bash
python3 bond_rhythm_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bond_rhythm_agent.py   # or on stdin
python3 bond_rhythm_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/ecosystem-grail-stack/bond_rhythm_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/bond_rhythm_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/bond_rhythm_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

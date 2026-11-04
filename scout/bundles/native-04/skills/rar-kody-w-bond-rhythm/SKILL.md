---
name: "rar-kody-w-bond-rhythm"
description: "Pulse the Bond Rhythm \u2014 the on-going local\u2194global beat for the FULL organism (global body = offspring repos, local body = ~/.brainstem/). Runs the ecosystem audit, classifies any drift as LOCAL\u2192GLOBAL push needed (suggest Launch/Graft) vs GLOBAL\u2192LOCAL pull needed (suggest RarLoader) vs informational, and SUGGESTS concrete next-step actions. Does NOT auto-execute \u2014 operator-mediated by design. Default dry_run=True. Connection-aware: gracefully degrades to local-only when network is unavailable; the next pulse catches the body up."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/bond_rhythm_agent", "rar_sha256": "7bfa5d0afca6919cedff2409abf22fdd8a715525de81426e68025429ef7cb585", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["heartbeat", "drift-detection", "ecosystem", "operator-mediated", "bond-pulse", "rhythm"]}
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

---
name: "rar-kody-w-chain-composer"
description: "Composes multi-primitive RAPP chain plans from a natural-language prompt via the claude CLI, writing a plan envelope and reviewable bash script."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/chain_composer_agent", "rar_sha256": "5c3eec3b482e9a812b963cfb7570175ec73fe1cec384269a9c9a0a9866347d18", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "chain_composer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/chain-composer:3f909e9d31339c8c53bc4d87eec18b55a30fc249aa47889e2610cced0edf0e06", "kind": "skill"}, "version": "1.0.1", "author": "kody-w", "tags": ["compose", "chain", "planning", "claude-cli", "operator-mediated", "meta"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/chain_composer_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `chain_composer_agent.py` is
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

chain_composer_agent — turn a high-level user prompt into a multi-primitive chain plan.

Takes any natural-language request (e.g. "The Weekly Heartbeat
Self-Portrait", "10-twin improv ensemble in sim-art-collective", "spawn
a vbrainstem context per pkstop twin and have them chat about Friday")
and composes a `rapp-chain-plan/1.0` envelope describing which RAPP
primitives to chain, in what order, with what expected artifacts +
operator-approval gates. Optionally also writes an executable bash
script the operator can review and run.

Operator-mediated by design: the agent SUGGESTS the chain; never
auto-executes anything that affects global state. Per ANTIPATTERNS §9.

Available primitives the composer can chain (the canonical RAPP toolbox):

  Identity / planting:
    - graft_neighborhood_agent  (plant a new neighborhood on a public repo)
    - launch_to_public_agent    (LOCAL→GLOBAL push of a local brainstem)
    - rar_loader_agent          (GLOBAL→LOCAL pull of a planted seed's kit)
    - holo_card_generator       (rappcards/1.1.2 holocard for a neighborhood/twin)
    - front_door_specs          (the bundled specs/ that travel with each planting)

  Heartbeat / drift:
    - bond_rhythm_agent         (BondRhythm.pulse_once — local↔global heartbeat)
    - ecosystem_audit + ecosystem_contract (drift detector — pure stdlib)

  Per-kind native primitives:
    - ant_agent                 (drop a pheromone — content-addressed Issue chain)
    - colony_observer_agent     (synthesize colony state into data/aggregations/)
    - art_submit / art_vote / art_remix (submission/vote/remix in neighborhood kind)
    - braintrust_request / contribute / synthesize / cite (federated research)

  Cross-organism comms:
    - twin_agent                (rapp-twin-chat/1.0 envelopes)
    - vbrainstem (browser)      (any planted twin embodied via Playwright +
                                 vbs_rappid preset; identity portable)
    - tick_twin.py              (one autonomous claude CLI tick per twin)
    - loop_orchestrator.sh      (cron unit: tick Bill + Alice + push + observe)
    - push_canvas.sh            (local→public bridge after a tick)
    - cross-device.spec.mjs     (multiple browser contexts joining one neighborhood)

  Aggregation / observation:
    - lineage_rollup_agent      (avg/median MMR across a lineage tree)
    - species_leaderboard_agent (Herald → Immortal global ladder)
    - proximity_discovery_agent (geohash-prefix matching — Pizza Place layer)
    - resurrection_ceremony_agent (stasis-recovery primitive)

  Schema add-ons (compose new plans with these as their declared output):
    - rapp-rhythm-pulse/1.0, rapp-pheromone/1.0, rapp-art-submission/1.0,
    - rapp-braintrust-contribution/1.0, rapp-twin-chat/1.0,
    - rappcards/1.1.2 (holocard data)

The composer reads the user's prompt + the toolbox above, calls a fresh
`claude` CLI session to compose the plan, validates the JSON, writes
both the plan + an executable script to disk, and returns the envelope.

Schema: `rapp-chain-plan/1.0`. Default `dry_run=True` (composer never
auto-runs scripts; operator runs them explicitly).

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `chain_composer_agent.py` and embedded as the fenced Python below (sha256 5c3eec3b482e9a81…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `chain_composer_agent.py` first:

```bash
python3 chain_composer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 chain_composer_agent.py   # or on stdin
python3 chain_composer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
"""chain_composer_agent — turn a high-level user prompt into a multi-primitive chain plan.

Takes any natural-language request (e.g. "The Weekly Heartbeat
Self-Portrait", "10-twin improv ensemble in sim-art-collective", "spawn
a vbrainstem context per pkstop twin and have them chat about Friday")
and composes a `rapp-chain-plan/1.0` envelope describing which RAPP
primitives to chain, in what order, with what expected artifacts +
operator-approval gates. Optionally also writes an executable bash
script the operator can review and run.

Operator-mediated by design: the agent SUGGESTS the chain; never
auto-executes anything that affects global state. Per ANTIPATTERNS §9.

Available primitives the composer can chain (the canonical RAPP toolbox):

  Identity / planting:
    - graft_neighborhood_agent  (plant a new neighborhood on a public repo)
    - launch_to_public_agent    (LOCAL→GLOBAL push of a local brainstem)
    - rar_loader_agent          (GLOBAL→LOCAL pull of a planted seed's kit)
    - holo_card_generator       (rappcards/1.1.2 holocard for a neighborhood/twin)
    - front_door_specs          (the bundled specs/ that travel with each planting)

  Heartbeat / drift:
    - bond_rhythm_agent         (BondRhythm.pulse_once — local↔global heartbeat)
    - ecosystem_audit + ecosystem_contract (drift detector — pure stdlib)

  Per-kind native primitives:
    - ant_agent                 (drop a pheromone — content-addressed Issue chain)
    - colony_observer_agent     (synthesize colony state into data/aggregations/)
    - art_submit / art_vote / art_remix (submission/vote/remix in neighborhood kind)
    - braintrust_request / contribute / synthesize / cite (federated research)

  Cross-organism comms:
    - twin_agent                (rapp-twin-chat/1.0 envelopes)
    - vbrainstem (browser)      (any planted twin embodied via Playwright +
                                 vbs_rappid preset; identity portable)
    - tick_twin.py              (one autonomous claude CLI tick per twin)
    - loop_orchestrator.sh      (cron unit: tick Bill + Alice + push + observe)
    - push_canvas.sh            (local→public bridge after a tick)
    - cross-device.spec.mjs     (multiple browser contexts joining one neighborhood)

  Aggregation / observation:
    - lineage_rollup_agent      (avg/median MMR across a lineage tree)
    - species_leaderboard_agent (Herald → Immortal global ladder)
    - proximity_discovery_agent (geohash-prefix matching — Pizza Place layer)
    - resurrection_ceremony_agent (stasis-recovery primitive)

  Schema add-ons (compose new plans with these as their declared output):
    - rapp-rhythm-pulse/1.0, rapp-pheromone/1.0, rapp-art-submission/1.0,
    - rapp-braintrust-contribution/1.0, rapp-twin-chat/1.0,
    - rappcards/1.1.2 (holocard data)

The composer reads the user's prompt + the toolbox above, calls a fresh
`claude` CLI session to compose the plan, validates the JSON, writes
both the plan + an executable script to disk, and returns the envelope.

Schema: `rapp-chain-plan/1.0`. Default `dry_run=True` (composer never
auto-runs scripts; operator runs them explicitly).
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import time

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    from basic_agent import BasicAgent


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/chain_composer_agent",
    "version": "1.0.1",
    "display_name": "Chain Composer",
    "description": "Composes multi-primitive RAPP chain plans from a natural-language prompt via the claude CLI, writing a plan envelope and reviewable bash script.",
    "author": "kody-w",
    "tags": [
        "compose",
        "chain",
        "planning",
        "claude-cli",
        "operator-mediated",
        "meta"
    ],
    "category": "platform",
    "quality_tier": "verified",
    "requires_env": [],
    "dependencies": [
        "@rapp/basic_agent"
    ]
}


_PLAN_SCHEMA = "rapp-chain-plan/1.0"
_DEFAULT_OUT_DIR = os.path.expanduser("~/RAPP-sim/chain-plans")
_CLAUDE_TIMEOUT_S = 120


def _now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _slugify(s: str) -> str:
    out = []
    for c in (s or "").lower():
        if c.isalnum():
            out.append(c)
        elif c in (" ", "-", "_"):
            out.append("-")
    return "".join(out).strip("-")[:64] or "untitled-chain"


_TOOLBOX_SUMMARY = """
Available RAPP primitives (the composer's vocabulary). All of these are real,
shipped, and in production. Each is invocable from a tick or a script.

IDENTITY / PLANTING
  graft_neighborhood_agent       — plant a neighborhood on an existing public repo (additive)
  launch_to_public_agent         — push local brainstem → new public repo
  rar_loader_agent               — pull a planted seed's participation kit
  tools/holo_card_generator.py   — generate rappcards/1.1.2 card.json + holo.svg + holo-qr.svg
  tools/front_door_specs.py      — bundled specs/ that travel with each planting

HEARTBEAT / OBSERVATION
  bond_rhythm_agent              — BondRhythm.pulse_once (operator-mediated)
  tools/ecosystem_audit.py       — drift detector, stdlib-only, --offline default
  tools/sim/observe.py           — simulation observer (read state, suggest adjustments)

PER-KIND NATIVE PRIMITIVES
  ant_agent                      — drop a rapp-pheromone/1.0 (Issue + label)
  colony_observer_agent          — synthesize → data/aggregations/<utc>.json
  art_submit_agent               — open a PR adding submissions/<slug>/{meta.json, piece.<ext>}
  art_vote_agent                 — react on an Issue (🩵 / 👎)
  art_remix_agent                — submission with remix_of: <slug>
  braintrust_request_agent       — open a research request Issue
  braintrust_contribute_agent    — comment with rapp-braintrust-contribution/1.0 + citations
  braintrust_synthesize_agent    — aggregate → reports/<id>.md PR

CROSS-ORGANISM COMMS
  twin_agent                     — rapp-twin-chat/1.0 envelopes
  vbrainstem (browser)           — Playwright Chromium context; pre-set vbs_rappid to
                                   embody ANY planted twin (identity portable)
  tools/sim/tick_twin.py         — one autonomous claude CLI tick for one twin
  tools/sim/loop_orchestrator.sh — cron unit: tick all twins + push canvas + observe
  tools/sim/push_canvas.sh       — git push the local neighborhood to its public counterpart
  tests/osi/browser/cross-device.spec.mjs — N browser contexts join one neighborhood

DISCOVERY / RANKING
  proximity_discovery_agent      — geohash-prefix matching (Pizza Place layer)
  lineage_rollup_agent           — MMR aggregation across a lineage tree
  species_leaderboard_agent      — Herald → Immortal global ranking

CEREMONIES / RECOVERY
  resurrection_ceremony_agent    — stasis-recovery primitive (Art. XXXIV.5)
  Dream Catcher                  — frame-scope contradiction reassimilation

SCHEMAS YOU CAN COMPOSE WITH
  rapp-rhythm-pulse/1.0           rapp-art-submission/1.0
  rapp-pheromone/1.0              rapp-braintrust-contribution/1.0
  rapp-twin-chat/1.0              rappcards/1.1.2 (holocard data)
  rapp-vbrainstem-subscription/1.0
  rapp-colony-observation/1.0
""".strip()


_PLAN_INSTRUCTIONS = """
You are a CHAIN COMPOSER. The operator will give you a high-level request
("Weekly Heartbeat Self-Portrait", "spawn 10 twin ensemble", etc.). Your
job is to design a chain of RAPP primitives that achieves it.

Respond with ONE JSON object inside a single ```json fenced block. Schema:

```json
{
  "schema": "rapp-chain-plan/1.0",
  "name": "<short slug-friendly name>",
  "title": "<human title>",
  "user_request": "<verbatim of operator's prompt>",
  "trigger": {
    "kind": "cron | event | manual | proximity | issue-label",
    "spec": "<cron expr OR event description>"
  },
  "primitives_used": ["<list of canonical primitive names>"],
  "steps": [
    {
      "n": 1,
      "agent_or_tool": "<canonical name>",
      "action": "<what it does this step>",
      "inputs":  { ... },
      "outputs": { ... },
      "operator_approval_required": false
    }
  ],
  "expected_artifacts": [
    { "kind": "Issue | PR | submission | pheromone | aggregation | egg | report",
      "path_or_url_template": "<where it'll land>",
      "schema": "<which rapp-*/N.M envelope>" }
  ],
  "antipattern_checks": [
    "no fake mode (autonomous ticks are real LLM only)",
    "operator-mediated for global writes (push, merge, deploy)",
    "specs travel with any new planting"
  ],
  "rough_cost_estimate": {
    "llm_calls_per_run": <int>,
    "cost_usd_per_run":  "<rough range>",
    "wall_time_per_run": "<rough range>"
  },
  "executable_script_outline": [
    "<bash/python pseudocode line 1>",
    "<line 2>",
    "..."
  ],
  "operator_next_step": "<one sentence: what the operator does to actually run this>"
}
```

Hard constraints:
1. Every primitive you reference MUST be in the toolbox above. No invented agents.
2. No fake / deterministic / pre-scripted persona modes. Real LLM ticks always.
3. Operations affecting global state (push, merge, PR, deploy) must have
   operator_approval_required: true on that step.
4. Any new planting must include the holo card grail (card + holo.md +
   holo.svg + holo-qr + specs/).
5. Identity portability: when embodying a planted twin in a browser context,
   pre-set vbs_rappid to that twin's canonical rappid; never mint a new one
   when impersonating an existing identity.

Respond with ONLY the JSON block. No prose around it.
""".strip()


def _call_claude(prompt: str, timeout_s: int = _CLAUDE_TIMEOUT_S) -> str:
    cmd = ["claude", "--print", prompt]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_s)
    if p.returncode != 0:
        raise RuntimeError(f"claude exit {p.returncode}: {p.stderr[:500]}")
    return p.stdout


def _parse_plan(response: str) -> dict:
    m = re.search(r"```json\s*(\{.*?\})\s*```", response, re.DOTALL)
    if not m:
        # fall back to raw JSON
        return json.loads(response.strip())
    return json.loads(m.group(1))


def _validate_plan(plan: dict) -> tuple[bool, str]:
    for k in ("schema", "name", "title", "primitives_used", "steps", "expected_artifacts"):
        if k not in plan:
            return False, f"missing required field: {k!r}"
    if plan["schema"] != _PLAN_SCHEMA:
        return False, f"schema must be {_PLAN_SCHEMA!r}; got {plan['schema']!r}"
    if not plan["steps"]:
        return False, "steps[] must be non-empty"
    return True, "ok"


def _executable_script(plan: dict) -> str:
    """Generate a bash skeleton from the plan's executable_script_outline."""
    name = plan.get("name", "untitled-chain")
    title = plan.get("title", name)
    outline = plan.get("executable_script_outline", [])
    lines = [
        "#!/usr/bin/env bash",
        f"# {title}",
        f"# Generated by chain_composer_agent at {_now_iso()}",
        f"# Plan name: {name}",
        f"# User request: {plan.get('user_request','')[:120]}",
        "#",
        "# Operator-mediated: review each step before running. Steps marked",
        "# operator_approval_required=true should be checked + manually triggered.",
        "set -euo pipefail",
        "",
    ]
    for i, step in enumerate(plan.get("steps", []), start=1):
        lines.append(f"# Step {i}: {step.get('agent_or_tool','?')} — {step.get('action','')}")
        if step.get("operator_approval_required"):
            lines.append(f"echo 'STEP {i} requires operator approval — review:'")
            lines.append(f"echo '  inputs: {json.dumps(step.get('inputs',{}))}'")
            lines.append(f"read -p 'proceed? [y/N] ' -n 1 -r; echo; [[ $REPLY =~ ^[Yy]$ ]] || exit 1")
        if i - 1 < len(outline):
            lines.append(outline[i - 1])
        else:
            lines.append(f"echo 'Step {i}: invoke {step.get('agent_or_tool','?')} (fill in)'")
        lines.append("")
    if outline and len(outline) > len(plan.get("steps", [])):
        for extra in outline[len(plan.get("steps", [])):]:
            lines.append(extra)
    lines.append(f"echo '✓ chain {name} complete'")
    return "\n".join(lines) + "\n"


class ChainComposerAgent(BasicAgent):
    metadata = {
        "name": "ChainComposer",
        "description": (
            "Compose a multi-primitive chain plan from a high-level user prompt. "
            "Reads the canonical RAPP toolbox (BondRhythm, ant pheromones, art "
            "submissions, braintrust requests, vbrainstem, tick_twin, push_canvas, "
            "etc.) and designs a chain that achieves the request. Returns a "
            "rapp-chain-plan/1.0 envelope + writes an executable bash script the "
            "operator can review and run. Operator-mediated: never auto-runs. Use "
            "this when the operator gives you a creative or ambitious prompt that "
            "spans multiple primitives."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "user_prompt": {
                    "type": "string",
                    "description": "The operator's natural-language request to be composed into a chain.",
                },
                "out_dir": {
                    "type": "string",
                    "default": _DEFAULT_OUT_DIR,
                    "description": "Where to write the plan JSON + executable script.",
                },
                "dry_run": {
                    "type": "boolean",
                    "default": True,
                    "description": "Cosmetic — composer never auto-runs regardless. Always True.",
                },
                "timeout_s": {"type": "integer", "default": _CLAUDE_TIMEOUT_S},
            },
            "required": ["user_prompt"],
        },
    }

    def __init__(self):
        self.name = "ChainComposer"

    def perform(self, **kwargs) -> str:
        user_prompt = kwargs.get("user_prompt") or ""
        out_dir = kwargs.get("out_dir") or _DEFAULT_OUT_DIR
        timeout_s = int(kwargs.get("timeout_s") or _CLAUDE_TIMEOUT_S)

        if not user_prompt.strip():
            return json.dumps({"schema": _PLAN_SCHEMA, "ok": False,
                               "error": "user_prompt is required"}, indent=2)

        full_prompt = (
            f"{_PLAN_INSTRUCTIONS}\n\n"
            f"TOOLBOX:\n{_TOOLBOX_SUMMARY}\n\n"
            f"OPERATOR REQUEST:\n{user_prompt.strip()}\n"
        )

        try:
            response = _call_claude(full_prompt, timeout_s=timeout_s)
        except subprocess.TimeoutExpired:
            return json.dumps({"schema": _PLAN_SCHEMA, "ok": False,
                               "error": "claude CLI timed out", "timeout_s": timeout_s}, indent=2)
        except Exception as e:
            return json.dumps({"schema": _PLAN_SCHEMA, "ok": False,
                               "error": f"claude CLI failed: {e}"}, indent=2)

        try:
            plan = _parse_plan(response)
        except (ValueError, json.JSONDecodeError) as e:
            return json.dumps({"schema": _PLAN_SCHEMA, "ok": False,
                               "error": f"could not parse plan as JSON: {e}",
                               "raw_response_preview": response[:600]}, indent=2)

        ok, msg = _validate_plan(plan)
        if not ok:
            return json.dumps({"schema": _PLAN_SCHEMA, "ok": False,
                               "error": f"plan validation failed: {msg}",
                               "plan": plan}, indent=2)

        # Persist plan + executable script
        os.makedirs(out_dir, exist_ok=True)
        slug = _slugify(plan.get("name", "chain")) or "chain"
        utc_safe = _now_iso().replace(":", "-")
        plan_path = os.path.join(out_dir, f"{utc_safe}-{slug}.plan.json")
        script_path = os.path.join(out_dir, f"{utc_safe}-{slug}.sh")
        with open(plan_path, "w") as f:
            json.dump(plan, f, indent=2)
            f.write("\n")
        with open(script_path, "w") as f:
            f.write(_executable_script(plan))
        os.chmod(script_path, 0o755)

        return json.dumps({
            "schema":             _PLAN_SCHEMA,
            "ok":                 True,
            "composed_at":        _now_iso(),
            "plan_name":          plan.get("name"),
            "plan_title":         plan.get("title"),
            "primitives_used":    plan.get("primitives_used", []),
            "step_count":         len(plan.get("steps", [])),
            "approval_steps":     [i for i, s in enumerate(plan.get("steps", []), start=1)
                                   if s.get("operator_approval_required")],
            "expected_artifacts": plan.get("expected_artifacts", []),
            "trigger":            plan.get("trigger"),
            "rough_cost":         plan.get("rough_cost_estimate"),
            "operator_next_step": plan.get("operator_next_step"),
            "files_written": {
                "plan_json":         plan_path,
                "executable_script": script_path,
            },
            "_inline_plan":       plan,  # so callers don't need to read the file
        }, indent=2)
````

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

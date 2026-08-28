---
name: "rar-kody-w-chain-composer"
description: "Composes multi-primitive RAPP chain plans from a natural-language prompt via the claude CLI, writing a plan envelope and reviewable bash script."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/chain_composer_agent", "rar_sha256": "5c3eec3b482e9a812b963cfb7570175ec73fe1cec384269a9c9a0a9866347d18", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.1", "author": "kody-w", "tags": ["compose", "chain", "planning", "claude-cli", "operator-mediated", "meta"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/chain_composer_agent`. The original RAPP
agent is preserved byte-for-byte in `chain_composer_agent.py` and in the RCI capsule.

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

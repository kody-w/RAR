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
    "version": "1.0.0",
    "display_name": "Chain Composer",
    "description": "Compose multi-primitive chain plans from any high-level operator prompt. Reads the canonical RAPP toolbox (BondRhythm, ant pheromones, art submissions, braintrust requests, vbrainstem, tick_twin, push_canvas, holo card grail, etc.) and returns rapp-chain-plan/1.0 envelope + writes an executable bash script. Calls `claude` CLI under the hood. Operator-mediated: never auto-runs.",
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

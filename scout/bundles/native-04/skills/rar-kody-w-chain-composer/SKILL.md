---
name: "rar-kody-w-chain-composer"
description: "Composes multi-primitive RAPP chain plans from a natural-language prompt via the claude CLI, writing a plan envelope and reviewable bash script."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/chain_composer_agent", "rar_sha256": "2a6fe3cccb8c2ae3cb649def409dcbf714fea0e7760bbf0e3a95c989557f84a4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "kody-w", "tags": ["compose", "chain", "planning", "claude-cli", "operator-mediated", "meta"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `chain_composer_agent.py` and embedded as the fenced Python below (sha256 2a6fe3cccb8c2ae3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `chain_composer_agent.py` first:

```bash
python3 chain_composer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 chain_composer_agent.py   # or on stdin
python3 chain_composer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

````python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/ecosystem-grail-stack/chain_composer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/chain_composer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/chain_composer_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

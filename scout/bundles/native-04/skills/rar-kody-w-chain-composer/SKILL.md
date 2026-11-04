---
name: "rar-kody-w-chain-composer"
description: "Composes multi-primitive RAPP chain plans from a natural-language prompt via the claude CLI, writing a plan envelope and reviewable bash script."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/chain_composer_agent", "rar_sha256": "2a6fe3cccb8c2ae3cb649def409dcbf714fea0e7760bbf0e3a95c989557f84a4", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "kody-w", "tags": ["compose", "chain", "planning", "claude-cli", "operator-mediated", "meta"]}
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

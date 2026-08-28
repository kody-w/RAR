---
name: "rar-cowork-cookbook-demo-data-plan-aggregate-supply"
description: "Generates and creates realistic demo records for plan aggregate supply in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_aggregate_supply", "rar_sha256": "47c93d1f4dd4e7b353988cbce2469cf7877625e7ac122948ce77cc18094e3931", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_plan_aggregate_supply`. The original RAPP
agent is preserved byte-for-byte in `demo_data_plan_aggregate_supply_agent.py` and in the RCI capsule.

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

Plan aggregate supply Demo Data Generator — Generates and creates realistic demo records for plan aggregate supply in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-aggregate-supply
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_aggregate_supply_agent.py` and embedded as the fenced Python below (sha256 47c93d1f4dd4e7b3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_aggregate_supply_agent.py` first:

```bash
python3 demo_data_plan_aggregate_supply_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_plan_aggregate_supply_agent.py   # or on stdin
python3 demo_data_plan_aggregate_supply_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan aggregate supply Demo Data Generator — Generates and creates realistic demo records for plan aggregate supply in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-plan-aggregate-supply
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_plan_aggregate_supply',
    "version": '2.0.1',
    "display_name": 'Plan aggregate supply Demo Data Generator',
    "description": 'Generates and creates realistic demo records for plan aggregate supply in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'demo-data-plan-aggregate-supply',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-plan-aggregate-supply',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dcc03802bd8547af',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-aggregate-supply'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/demo-data-plan-aggregate-supply', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataPlanAggregateSupply(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPlanAggregateSupply'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(DemoDataPlanAggregateSupply().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

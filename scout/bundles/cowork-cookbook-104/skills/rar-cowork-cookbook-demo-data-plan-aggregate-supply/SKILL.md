---
name: "rar-cowork-cookbook-demo-data-plan-aggregate-supply"
description: "Generates and creates realistic demo records for plan aggregate supply in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_plan_aggregate_supply", "rar_sha256": "d7086b14b497ff08a65e09c0a6fafe6dda6673037abec220cd9b8f904f633c25", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_plan_aggregate_supply_agent.py` and embedded as the fenced Python below (sha256 d7086b14b497ff08…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_plan_aggregate_supply_agent.py` first:

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
    "version": '2.0.0',
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

---
name: "rar-cowork-cookbook-adaptive-card-plan-aggregate-supply"
description: "Produces a reusable Adaptive Card JSON snapshot of plan aggregate supply status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_aggregate_supply", "rar_sha256": "18c696c7336af7e70dcb21c0ce0f18dec3e5fc20e1efc22685f679e57c356825", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_aggregate_supply`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_aggregate_supply_agent.py` and in the RCI capsule.

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

Plan aggregate supply Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan aggregate supply status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-aggregate-supply
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_aggregate_supply_agent.py` and embedded as the fenced Python below (sha256 18c696c7336af7e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_aggregate_supply_agent.py` first:

```bash
python3 adaptive_card_plan_aggregate_supply_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_aggregate_supply_agent.py   # or on stdin
python3 adaptive_card_plan_aggregate_supply_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan aggregate supply Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan aggregate supply status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-aggregate-supply
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_aggregate_supply',
    "version": '2.0.1',
    "display_name": 'Plan aggregate supply Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of plan aggregate supply status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-plan-aggregate-supply',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-aggregate-supply',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e4d5b2f3ae9a833c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-aggregate-supply'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-plan-aggregate-supply', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardPlanAggregateSupply(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanAggregateSupply'
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
    print(AdaptiveCardPlanAggregateSupply().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-adaptive-card-plan-aggregate-supply"
description: "Produces a reusable Adaptive Card JSON snapshot of plan aggregate supply status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_aggregate_supply", "rar_sha256": "3b562931d14daa682abfee5d624f95239120da034bb06232fffd68e315e9ed1c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_aggregate_supply_agent.py` and embedded as the fenced Python below (sha256 3b562931d14daa68…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_aggregate_supply_agent.py` first:

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
    "version": '2.0.0',
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

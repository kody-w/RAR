---
name: "rar-cowork-cookbook-adaptive-card-plan-aggregate-supply"
description: "Produces a reusable Adaptive Card JSON snapshot of plan aggregate supply status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_aggregate_supply", "rar_sha256": "3b562931d14daa682abfee5d624f95239120da034bb06232fffd68e315e9ed1c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_plan_aggregate_supply_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-plan-aggregate-supply:21081b037103f540c7095f50eaa4b07e5c9d0d96eaa3f2c28e01894207c9106e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_plan_aggregate_supply`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_plan_aggregate_supply_agent.py` is
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

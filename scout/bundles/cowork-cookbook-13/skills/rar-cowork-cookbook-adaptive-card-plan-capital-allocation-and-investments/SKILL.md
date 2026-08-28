---
name: "rar-cowork-cookbook-adaptive-card-plan-capital-allocation-and-investments"
description: "Produces a reusable Adaptive Card JSON snapshot of plan capital allocation and investments status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_capital_allocation_and_investments", "rar_sha256": "1db6554e9f038b0bee4459071988d5cf52d57661455e80858197b6588ace281f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_plan_capital_allocation_and_investments`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_plan_capital_allocation_and_investments_agent.py` and in the RCI capsule.

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

Plan capital allocation and investments Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan capital allocation and investments status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-capital-allocation-and-investments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_capital_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 1db6554e9f038b0b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_capital_allocation_and_investments_agent.py` first:

```bash
python3 adaptive_card_plan_capital_allocation_and_investments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_plan_capital_allocation_and_investments_agent.py   # or on stdin
python3 adaptive_card_plan_capital_allocation_and_investments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan capital allocation and investments Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of plan capital allocation and investments status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-plan-capital-allocation-and-investments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_plan_capital_allocation_and_investments',
    "version": '2.0.1',
    "display_name": 'Plan capital allocation and investments Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of plan capital allocation and investments status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-plan-capital-allocation-and-investments',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-plan-capital-allocation-and-investments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '77132614c929d592',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-capital-allocation-and-investments'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/adaptive-card-plan-capital-allocation-and-investments', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardPlanCapitalAllocationAndInvestments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPlanCapitalAllocationAndInvestments'
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
    print(AdaptiveCardPlanCapitalAllocationAndInvestments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

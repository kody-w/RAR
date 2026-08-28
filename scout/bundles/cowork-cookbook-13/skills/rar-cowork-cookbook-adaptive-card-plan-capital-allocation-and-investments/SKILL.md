---
name: "rar-cowork-cookbook-adaptive-card-plan-capital-allocation-and-investments"
description: "Produces a reusable Adaptive Card JSON snapshot of plan capital allocation and investments status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_capital_allocation_and_investments", "rar_sha256": "0fa3821085dbf8b2da942a0d63a6d9aebf29b8df8b4694d3a93e40d551d72b91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_plan_capital_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 0fa3821085dbf8b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_plan_capital_allocation_and_investments_agent.py` first:

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
    "version": '2.0.0',
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

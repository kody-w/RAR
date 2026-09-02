---
name: "rar-cowork-cookbook-adaptive-card-plan-capital-allocation-and-investments"
description: "Produces a reusable Adaptive Card JSON snapshot of plan capital allocation and investments status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_plan_capital_allocation_and_investments", "rar_sha256": "0fa3821085dbf8b2da942a0d63a6d9aebf29b8df8b4694d3a93e40d551d72b91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_plan_capital_allocation_and_investments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-plan-capital-allocation-and-investments:cd5c79cb5dfd4f5c9f0c00136f2fd1cda4b74a14884319687c3eef332f10f23b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_plan_capital_allocation_and_investments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_plan_capital_allocation_and_investments_agent.py` is
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

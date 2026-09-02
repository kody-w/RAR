---
name: "rar-cowork-cookbook-bulk-update-plan-operational-allocation-and-investments"
description: "Applies a bulk field update across plan operational allocation and investments records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_operational_allocation_and_investments", "rar_sha256": "7bb9c843892d80d8771a744528f319586d989e8bb2ba64b9a53c4266dcbe7b3e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_plan_operational_allocation_and_investments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-plan-operational-allocation-and-investments:663f32ea07e3bf3ce49c8de8f495d6d98cdcd690d3e05052a10c8a99728a3ea5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_plan_operational_allocation_and_investments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_plan_operational_allocation_and_investments_agent.py` is
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

Plan operational allocation and investments Bulk Field Update — Applies a bulk field update across plan operational allocation and investments records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-operational-allocation-and-investments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_operational_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 7bb9c843892d80d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_operational_allocation_and_investments_agent.py` first:

```bash
python3 bulk_update_plan_operational_allocation_and_investments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_operational_allocation_and_investments_agent.py   # or on stdin
python3 bulk_update_plan_operational_allocation_and_investments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan operational allocation and investments Bulk Field Update — Applies a bulk field update across plan operational allocation and investments records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-operational-allocation-and-investments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_operational_allocation_and_investments',
    "version": '2.0.0',
    "display_name": 'Plan operational allocation and investments Bulk Field Update',
    "description": 'Applies a bulk field update across plan operational allocation and investments records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-operational-allocation-and-investments',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-operational-allocation-and-investments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '73afc7572a9c9736',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-operational-allocation-and-investments'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-plan-operational-allocation-and-investments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdatePlanOperationalAllocationAndInvestments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanOperationalAllocationAndInvestments'
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
    print(BulkUpdatePlanOperationalAllocationAndInvestments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

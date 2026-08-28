---
name: "rar-cowork-cookbook-bulk-update-plan-operational-allocation-and-investments"
description: "Applies a bulk field update across plan operational allocation and investments records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_operational_allocation_and_investments", "rar_sha256": "7bb9c843892d80d8771a744528f319586d989e8bb2ba64b9a53c4266dcbe7b3e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_operational_allocation_and_investments`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_operational_allocation_and_investments_agent.py` and in the RCI capsule.

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

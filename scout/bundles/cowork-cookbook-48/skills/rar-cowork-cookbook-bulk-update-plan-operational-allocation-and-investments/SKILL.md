---
name: "rar-cowork-cookbook-bulk-update-plan-operational-allocation-and-investments"
description: "Applies a bulk field update to Dynamics 365 plan operational allocation and investments records from a supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_operational_allocation_and_investments", "rar_sha256": "249489e357b15a71fb24ff70d9f0bb7f90fd5efcc3421f92a043bf7a5e9d4e0b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

Plan operational allocation and investments Bulk Field Update — Applies a bulk field update to Dynamics 365 plan operational allocation and investments records from a supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "approval": {
      "description": "Explicit go-ahead after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "field_updates": {
      "description": "The field(s) and new value(s) to apply to each record.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF (sandbox first).",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "record_ids": {
      "description": "List of record IDs for the plan operational allocation and investments records to update.",
      "type": "string"
    },
    "rollback_plan": {
      "description": "How changes will be reverted if the update goes wrong.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_operational_allocation_and_investments_agent.py` and embedded as the fenced Python below (sha256 249489e357b15a71…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_operational_allocation_and_investments_agent.py` first:

```bash
python3 bulk_update_plan_operational_allocation_and_investments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_operational_allocation_and_investments_agent.py   # or on stdin
python3 bulk_update_plan_operational_allocation_and_investments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan operational allocation and investments Bulk Field Update — Applies a bulk field update to Dynamics 365 plan operational allocation and investments records from a supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "version": '3.0.3',
    "display_name": 'Plan operational allocation and investments Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 plan operational allocation and investments records from a supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ebb89459208ba6c0',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'field_updates': 'The field(s) and new value(s) to apply to each record.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'record_ids': 'List of record IDs for the plan operational allocation and investments records to update.', 'rollback_plan': 'How changes will be reverted if the update goes wrong.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when plan operational allocation and investments records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to plan operational allocation and investments records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 plan operational allocation and investments records from a supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft', 'example_request': 'Bulk update these plan allocation record IDs in USMF sandbox to the new value — show me a dry-run first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'name': 'legal_entity'}, {'description': 'List of record IDs for the plan operational allocation and investments records to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'field_updates'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}, {'description': 'How changes will be reverted if the update goes wrong.', 'name': 'rollback_plan'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many plan operational allocation and investments records in D365 F&SCM (sandbox), with a reviewed dry-run before write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePlanOperationalAllocationAndInvestments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanOperationalAllocationAndInvestments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'field_updates': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF (sandbox first).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs for the plan operational allocation and investments records to update.', 'type': 'string'}, 'rollback_plan': {'description': 'How changes will be reverted if the update goes wrong.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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

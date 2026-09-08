---
name: "rar-cowork-cookbook-bulk-update-plan-operational-allocation-and-investments"
description: "Applies a bulk field update to Dynamics 365 plan operational allocation and investments records from a supplied ID list, producing a dry-run preview workbook for approval before committing and a confirmation workbook aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_operational_allocation_and_investments", "rar_sha256": "249489e357b15a71fb24ff70d9f0bb7f90fd5efcc3421f92a043bf7a5e9d4e0b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

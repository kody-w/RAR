---
name: "rar-cowork-cookbook-bulk-update-plan-loads"
description: "Applies a bulk field update to Dynamics 365 F&SCM plan loads records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and returns a confirmation"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_plan_loads", "rar_sha256": "d3b1e2ee71fe630a462ec7d68bd9a84029a9c196972d21f5b6d3f2ad69c1a681", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_plan_loads`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_plan_loads_agent.py` and in the RCI capsule.

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

Plan loads Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM plan loads records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and returns a confirmation

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-loads
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
      "description": "Explicit approval after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "field_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; sandbox only.",
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
      "description": "List of plan loads record IDs to update.",
      "type": "string"
    },
    "rollback_plan": {
      "description": "How changes will be reverted if the update is wrong.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_plan_loads_agent.py` and embedded as the fenced Python below (sha256 d3b1e2ee71fe630a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_plan_loads_agent.py` first:

```bash
python3 bulk_update_plan_loads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_plan_loads_agent.py   # or on stdin
python3 bulk_update_plan_loads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan loads Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM plan loads records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and returns a confirmation

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-plan-loads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_plan_loads',
    "version": '3.0.3',
    "display_name": 'Plan loads Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM plan loads records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and returns a confirmation',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-plan-loads',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-plan-loads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '46fae0057797d298',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/plan-loads'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-plan-loads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'field_values': 'The field(s) and new value(s) to apply to each record.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'record_ids': 'List of plan loads record IDs to update.', 'rollback_plan': 'How changes will be reverted if the update is wrong.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when plan loads records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to plan loads records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM plan loads records via the Cowork D365 ERP plugin: returns a dry-run preview workbook of before/after/status, waits for approval, then commits and returns a confirmation', 'example_request': 'Bulk update these plan loads record IDs in USMF sandbox to the new value — show me the dry-run preview first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'name': 'legal_entity'}, {'description': 'List of plan loads record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'field_values'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}, {'description': 'How changes will be reverted if the update is wrong.', 'name': 'rollback_plan'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change one or more fields on many plan loads records at once in a D365 sandbox legal entity and want a reviewable preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdatePlanLoads(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdatePlanLoads'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'field_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of plan loads record IDs to update.', 'type': 'string'}, 'rollback_plan': {'description': 'How changes will be reverted if the update is wrong.', 'type': 'string'}},
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
    print(BulkUpdatePlanLoads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

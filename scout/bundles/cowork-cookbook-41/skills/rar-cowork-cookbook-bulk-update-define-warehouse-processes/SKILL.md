---
name: "rar-cowork-cookbook-bulk-update-define-warehouse-processes"
description: "Applies a bulk field update to Dynamics 365 F&SCM warehouse process records from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_warehouse_processes", "rar_sha256": "727ada7d0e32a1a5ab6850c84fba6a4fd36d65ab0a93f2503bd5c0d6b2551bc5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_warehouse_processes`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_warehouse_processes_agent.py` and in the RCI capsule.

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

Define warehouse processes Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM warehouse process records from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-warehouse-processes
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
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); sandbox only.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
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
      "description": "List of warehouse process record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_warehouse_processes_agent.py` and embedded as the fenced Python below (sha256 727ada7d0e32a1a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_warehouse_processes_agent.py` first:

```bash
python3 bulk_update_define_warehouse_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_warehouse_processes_agent.py   # or on stdin
python3 bulk_update_define_warehouse_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse processes Bulk Field Update — Applies a bulk field update to Dynamics 365 F&SCM warehouse process records from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-warehouse-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_warehouse_processes',
    "version": '3.0.3',
    "display_name": 'Define warehouse processes Bulk Field Update',
    "description": 'Applies a bulk field update to Dynamics 365 F&SCM warehouse process records from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before committing changes.',
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
        "upstream_slug": 'bulk-update-define-warehouse-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-warehouse-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3f018a92c98024bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/define-warehouse-processes'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-define-warehouse-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); sandbox only.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of warehouse process record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when define warehouse processes records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to define warehouse processes records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to Dynamics 365 F&SCM warehouse process records from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk-update these warehouse process record IDs to the new value in USMF sandbox — show me a dry run first.', 'inputs': [{'description': 'List of warehouse process record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against (e.g. USMF); sandbox only.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many warehouse process records in D365 F&SCM and want a before/after preview before writing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateDefineWarehouseProcesses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineWarehouseProcesses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); sandbox only.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of warehouse process record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateDefineWarehouseProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

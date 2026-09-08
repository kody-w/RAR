---
name: "rar-cowork-cookbook-bulk-update-define-warehouse-processes"
description: "Applies a bulk field update to Dynamics 365 F&SCM warehouse process records from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_warehouse_processes", "rar_sha256": "727ada7d0e32a1a5ab6850c84fba6a4fd36d65ab0a93f2503bd5c0d6b2551bc5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

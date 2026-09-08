---
name: "rar-cowork-cookbook-bulk-update-process-inventory-movements"
description: "Applies a bulk field update to process inventory movements records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_process_inventory_movements", "rar_sha256": "272db7c8475a5d987e6d09cd1407fb68b679dc048136d38c4207d327c3c18a85", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_process_inventory_movements`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_process_inventory_movements_agent.py` and in the RCI capsule.

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

Process inventory movements Bulk Field Update — Applies a bulk field update to process inventory movements records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-process-inventory-movements
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; the recipe uses USMF sandbox.",
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
      "description": "List of process inventory movements record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_process_inventory_movements_agent.py` and embedded as the fenced Python below (sha256 272db7c8475a5d98…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_process_inventory_movements_agent.py` first:

```bash
python3 bulk_update_process_inventory_movements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_process_inventory_movements_agent.py   # or on stdin
python3 bulk_update_process_inventory_movements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process inventory movements Bulk Field Update — Applies a bulk field update to process inventory movements records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-process-inventory-movements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_process_inventory_movements',
    "version": '3.0.3',
    "display_name": 'Process inventory movements Bulk Field Update',
    "description": 'Applies a bulk field update to process inventory movements records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval',
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
        "upstream_slug": 'bulk-update-process-inventory-movements',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-process-inventory-movements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '667e31f5ce0064e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/process-inventory-movements'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-process-inventory-movements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; the recipe uses USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of process inventory movements record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when process inventory movements records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to process inventory movements records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to process inventory movements records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval', 'example_request': 'Bulk update these process inventory movement IDs in USMF sandbox with the new value — show me the dry-run preview first.', 'inputs': [{'description': 'List of process inventory movements record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; the recipe uses USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many process inventory movements records at once and want a reviewable before/after preview before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateProcessInventoryMovements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateProcessInventoryMovements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; the recipe uses USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of process inventory movements record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateProcessInventoryMovements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

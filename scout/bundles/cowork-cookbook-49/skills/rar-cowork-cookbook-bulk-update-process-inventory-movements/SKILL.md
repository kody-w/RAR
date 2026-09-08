---
name: "rar-cowork-cookbook-bulk-update-process-inventory-movements"
description: "Applies a bulk field update to process inventory movements records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_process_inventory_movements", "rar_sha256": "272db7c8475a5d987e6d09cd1407fb68b679dc048136d38c4207d327c3c18a85", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-bulk-update-allocate-inventory-to-sales-orders"
description: "Applies a bulk field update to inventory allocation sales order records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_allocate_inventory_to_sales_orders", "rar_sha256": "fdd58c60879cb9289ec30df164a1d91dfecd63a3d760bb1140f8ff629c0b4b5d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_allocate_inventory_to_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_allocate_inventory_to_sales_orders_agent.py` and in the RCI capsule.

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

Allocate inventory to sales orders Bulk Field Update — Applies a bulk field update to inventory allocation sales order records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-allocate-inventory-to-sales-orders
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
      "description": "D365 legal entity to run against, e.g. USMF; sandbox environment only.",
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
      "description": "List of record IDs for the allocate-inventory-to-sales-orders records to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_allocate_inventory_to_sales_orders_agent.py` and embedded as the fenced Python below (sha256 fdd58c60879cb928…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_allocate_inventory_to_sales_orders_agent.py` first:

```bash
python3 bulk_update_allocate_inventory_to_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_allocate_inventory_to_sales_orders_agent.py   # or on stdin
python3 bulk_update_allocate_inventory_to_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate inventory to sales orders Bulk Field Update — Applies a bulk field update to inventory allocation sales order records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-allocate-inventory-to-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_allocate_inventory_to_sales_orders',
    "version": '3.0.3',
    "display_name": 'Allocate inventory to sales orders Bulk Field Update',
    "description": 'Applies a bulk field update to inventory allocation sales order records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-allocate-inventory-to-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-allocate-inventory-to-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8508fc6ec02d27cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/allocate-inventory-to-sales-orders'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-allocate-inventory-to-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of record IDs for the allocate-inventory-to-sales-orders records to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when allocate inventory to sales orders records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to allocate inventory to sales orders records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to inventory allocation sales order records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk update these sales order allocation records in USMF sandbox to the new value — show me a dry run first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'name': 'legal_entity'}, {'description': 'List of record IDs for the allocate-inventory-to-sales-orders records to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to update a field across many sales order inventory allocation records in D365 (sandbox), with a before/after preview and approval step.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateAllocateInventoryToSalesOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAllocateInventoryToSalesOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox environment only.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of record IDs for the allocate-inventory-to-sales-orders records to update.', 'type': 'string'}},
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
    print(BulkUpdateAllocateInventoryToSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

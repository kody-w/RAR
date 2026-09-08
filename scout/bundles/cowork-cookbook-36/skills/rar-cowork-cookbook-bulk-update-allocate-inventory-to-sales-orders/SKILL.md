---
name: "rar-cowork-cookbook-bulk-update-allocate-inventory-to-sales-orders"
description: "Applies a bulk field update to inventory allocation sales order records in Dynamics 365 F&SCM via the Cowork ERP plugin, returning a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_allocate_inventory_to_sales_orders", "rar_sha256": "fdd58c60879cb9289ec30df164a1d91dfecd63a3d760bb1140f8ff629c0b4b5d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

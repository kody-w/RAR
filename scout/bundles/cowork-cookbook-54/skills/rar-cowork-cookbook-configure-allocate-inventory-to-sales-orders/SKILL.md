---
name: "rar-cowork-cookbook-configure-allocate-inventory-to-sales-orders"
description: "Reads an attached Excel file of allocate-inventory-to-sales-orders configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies chang"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_allocate_inventory_to_sales_orders", "rar_sha256": "193cc391956ec3a1c62a2717ff314dc306a24e77e680ac3288a9a3c5c3320d68", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_allocate_inventory_to_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `configure_allocate_inventory_to_sales_orders_agent.py` and in the RCI capsule.

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

Allocate inventory to sales orders Configuration Bulk Setup — Reads an attached Excel file of allocate-inventory-to-sales-orders configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies chang

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-allocate-inventory-to-sales-orders
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per allocate-inventory-to-sales-orders target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_allocate_inventory_to_sales_orders_agent.py` and embedded as the fenced Python below (sha256 193cc391956ec3a1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_allocate_inventory_to_sales_orders_agent.py` first:

```bash
python3 configure_allocate_inventory_to_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_allocate_inventory_to_sales_orders_agent.py   # or on stdin
python3 configure_allocate_inventory_to_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate inventory to sales orders Configuration Bulk Setup — Reads an attached Excel file of allocate-inventory-to-sales-orders configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies chang

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-allocate-inventory-to-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_allocate_inventory_to_sales_orders',
    "version": '3.0.3',
    "display_name": 'Allocate inventory to sales orders Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of allocate-inventory-to-sales-orders configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies chang',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-allocate-inventory-to-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-allocate-inventory-to-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b60727e947fce201',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/allocate-inventory-to-sales-orders'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-allocate-inventory-to-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per allocate-inventory-to-sales-orders target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for allocate inventory to sales orders, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per allocate inventory to sales orders target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of allocate-inventory-to-sales-orders configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies chang', 'example_request': 'Bulk-apply the allocate inventory to sales orders config in this Excel to USMF sandbox — validate first and wait for my approval.', 'inputs': [{'description': 'Attached Excel file with one row per allocate-inventory-to-sales-orders target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when bulk-applying allocate-inventory-to-sales-orders configuration changes in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureAllocateInventoryToSalesOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAllocateInventoryToSalesOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per allocate-inventory-to-sales-orders target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureAllocateInventoryToSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

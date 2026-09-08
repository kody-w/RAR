---
name: "rar-cowork-cookbook-configure-allocate-inventory-to-sales-orders"
description: "Reads an attached Excel file of allocate-inventory-to-sales-orders configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies chang"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_allocate_inventory_to_sales_orders", "rar_sha256": "193cc391956ec3a1c62a2717ff314dc306a24e77e680ac3288a9a3c5c3320d68", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

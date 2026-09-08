---
name: "rar-cowork-cookbook-configure-cancel-supplier-payments"
description: "Reads an attached configuration Excel file of cancel-supplier-payment rows in Dynamics 365 F&SCM (legal entity USMF), validates each row, returns a validation workbook, and after your approval applies the changes with a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_cancel_supplier_payments", "rar_sha256": "35998cf927bb2400e41536eb7293481818771d13a9fa3b49216b3544a6c578f8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_cancel_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `configure_cancel_supplier_payments_agent.py` and in the RCI capsule.

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

Cancel supplier payments Configuration Bulk Setup — Reads an attached configuration Excel file of cancel-supplier-payment rows in Dynamics 365 F&SCM (legal entity USMF), validates each row, returns a validation workbook, and after your approval applies the changes with a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-cancel-supplier-payments
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
      "description": "Explicit go-ahead after reviewing the validation workbook, required before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per cancel-supplier-payment target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_cancel_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 35998cf927bb2400…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_cancel_supplier_payments_agent.py` first:

```bash
python3 configure_cancel_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_cancel_supplier_payments_agent.py   # or on stdin
python3 configure_cancel_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cancel supplier payments Configuration Bulk Setup — Reads an attached configuration Excel file of cancel-supplier-payment rows in Dynamics 365 F&SCM (legal entity USMF), validates each row, returns a validation workbook, and after your approval applies the changes with a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-cancel-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_cancel_supplier_payments',
    "version": '3.0.3',
    "display_name": 'Cancel supplier payments Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of cancel-supplier-payment rows in Dynamics 365 F&SCM (legal entity USMF), validates each row, returns a validation workbook, and after your approval applies the changes with a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-cancel-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-cancel-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7ad2c38308f683e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/cancel-supplier-payments'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-cancel-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, required before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per cancel-supplier-payment target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for cancel supplier payments, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per cancel supplier payments target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of cancel-supplier-payment rows in Dynamics 365 F&SCM (legal entity USMF), validates each row, returns a validation workbook, and after your approval applies the changes with a', 'example_request': "Here's my cancel supplier payments sheet — validate it against USMF sandbox and show me what would fail before applying.", 'inputs': [{'description': 'Attached Excel file with one row per cancel-supplier-payment target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, required before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-cancel supplier payments in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any data is written.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureCancelSupplierPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureCancelSupplierPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, required before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per cancel-supplier-payment target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureCancelSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

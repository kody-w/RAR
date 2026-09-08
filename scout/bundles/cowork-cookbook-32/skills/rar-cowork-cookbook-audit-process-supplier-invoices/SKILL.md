---
name: "rar-cowork-cookbook-audit-process-supplier-invoices"
description: "Read-only audit of supplier invoice records in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workb"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_supplier_invoices", "rar_sha256": "3e28bc69eb3c70f948e96b583e97f85a911a5347c58020ec668a581c0b2b12c3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_supplier_invoices`. The original RAPP
agent is preserved byte-for-byte in `audit_process_supplier_invoices_agent.py` and in the RCI capsule.

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

Process supplier invoices Completeness Audit — Read-only audit of supplier invoice records in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workb

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-supplier-invoices
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "date_window": {
      "description": "Date range used to judge stale dates; USMF demo data is mostly FY2017.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit, e.g. USMF.",
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
    "output_filename": {
      "description": "Name of the Excel workbook to produce, e.g. audit-process-supplier-invoices-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_supplier_invoices_agent.py` and embedded as the fenced Python below (sha256 3e28bc69eb3c70f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_supplier_invoices_agent.py` first:

```bash
python3 audit_process_supplier_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_supplier_invoices_agent.py   # or on stdin
python3 audit_process_supplier_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process supplier invoices Completeness Audit — Read-only audit of supplier invoice records in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workb

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-supplier-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_supplier_invoices',
    "version": '3.0.3',
    "display_name": 'Process supplier invoices Completeness Audit',
    "description": 'Read-only audit of supplier invoice records in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workb',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-process-supplier-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-supplier-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b8ef41ffd280c95f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/process-supplier-invoices'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-process-supplier-invoices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-process-supplier-invoices-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit process supplier invoices records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to process supplier invoices. Output an Excel workbook 'audit-process-supplier-invoices-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no process supplier invoices data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads process supplier invoices records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of supplier invoice records in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workb', 'example_request': 'Audit supplier invoices in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-process-supplier-invoices-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance audit of D365 supplier invoice records, with findings exported to Excel and no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditProcessSupplierInvoices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessSupplierInvoices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-process-supplier-invoices-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditProcessSupplierInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

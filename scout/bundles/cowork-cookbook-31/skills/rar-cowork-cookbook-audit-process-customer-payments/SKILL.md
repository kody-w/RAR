---
name: "rar-cowork-cookbook-audit-process-customer-payments"
description: "Runs a read-only completeness and policy audit of process customer payments records in Dynamics 365 F&SCM via the ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_customer_payments", "rar_sha256": "922ebc43455218f8c1765f00b34f49859a7e3564dfd16b29fd2536cf253ff0e8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_process_customer_payments`. The original RAPP
agent is preserved byte-for-byte in `audit_process_customer_payments_agent.py` and in the RCI capsule.

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

Process customer payments Completeness Audit — Runs a read-only completeness and policy audit of process customer payments records in Dynamics 365 F&SCM via the ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-customer-payments
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
      "description": "Name of the Excel workbook to produce, e.g. audit-process-customer-payments-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_process_customer_payments_agent.py` and embedded as the fenced Python below (sha256 922ebc43455218f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_process_customer_payments_agent.py` first:

```bash
python3 audit_process_customer_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_process_customer_payments_agent.py   # or on stdin
python3 audit_process_customer_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer payments Completeness Audit — Runs a read-only completeness and policy audit of process customer payments records in Dynamics 365 F&SCM via the ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-process-customer-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_process_customer_payments',
    "version": '3.0.3',
    "display_name": 'Process customer payments Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of process customer payments records in Dynamics 365 F&SCM via the ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-process-customer-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-process-customer-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '466121e8b827f2f9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-payments'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-process-customer-payments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-process-customer-payments-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit process customer payments records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to process customer payments. Output an Excel workbook 'audit-process-customer-payments-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no process customer payments data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads process customer payments records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of process customer payments records in Dynamics 365 F&SCM via the ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet.', 'example_request': 'Audit process customer payments in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-process-customer-payments-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants process customer payments records checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditProcessCustomerPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditProcessCustomerPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-process-customer-payments-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditProcessCustomerPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

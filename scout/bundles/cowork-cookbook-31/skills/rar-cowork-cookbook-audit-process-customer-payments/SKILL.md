---
name: "rar-cowork-cookbook-audit-process-customer-payments"
description: "Runs a read-only completeness and policy audit of process customer payments records in Dynamics 365 F&SCM via the ERP plugin, returning an Excel workbook with one sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_process_customer_payments", "rar_sha256": "922ebc43455218f8c1765f00b34f49859a7e3564dfd16b29fd2536cf253ff0e8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

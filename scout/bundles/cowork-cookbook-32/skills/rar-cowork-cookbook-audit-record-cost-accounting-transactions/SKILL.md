---
name: "rar-cowork-cookbook-audit-record-cost-accounting-transactions"
description: "Runs a read-only completeness and policy audit of cost accounting transaction records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_cost_accounting_transactions", "rar_sha256": "b5956212db42f94ab38a63edef963d96317092e9ff7ca6b71b576e844e31958f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_record_cost_accounting_transactions`. The original RAPP
agent is preserved byte-for-byte in `audit_record_cost_accounting_transactions_agent.py` and in the RCI capsule.

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

Record cost accounting transactions Completeness Audit — Runs a read-only completeness and policy audit of cost accounting transaction records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-cost-accounting-transactions
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
      "description": "Date range to treat as current vs stale (USMF demo data is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-record-cost-accounting-transactions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_cost_accounting_transactions_agent.py` and embedded as the fenced Python below (sha256 b5956212db42f94a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_cost_accounting_transactions_agent.py` first:

```bash
python3 audit_record_cost_accounting_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_record_cost_accounting_transactions_agent.py   # or on stdin
python3 audit_record_cost_accounting_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record cost accounting transactions Completeness Audit — Runs a read-only completeness and policy audit of cost accounting transaction records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-cost-accounting-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_record_cost_accounting_transactions',
    "version": '3.0.3',
    "display_name": 'Record cost accounting transactions Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of cost accounting transaction records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-record-cost-accounting-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-record-cost-accounting-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '21ace83a85006d82',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-cost-accounting-transactions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-record-cost-accounting-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to treat as current vs stale (USMF demo data is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-record-cost-accounting-transactions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit record cost accounting transactions records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to record cost accounting transactions. Output an Excel workbook 'audit-record-cost-accounting-transactions-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no record cost accounting transactions data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads record cost accounting transactions records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of cost accounting transaction records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.', 'example_request': 'Audit cost accounting transactions in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range to treat as current vs stale (USMF demo data is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-record-cost-accounting-transactions-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants cost accounting transactions checked for missing fields, stale dates, blank descriptions, inactive-entity references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditRecordCostAccountingTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRecordCostAccountingTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to treat as current vs stale (USMF demo data is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-record-cost-accounting-transactions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditRecordCostAccountingTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

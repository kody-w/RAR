---
name: "rar-cowork-cookbook-audit-record-cost-accounting-transactions"
description: "Runs a read-only completeness and policy audit of cost accounting transaction records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_cost_accounting_transactions", "rar_sha256": "b5956212db42f94ab38a63edef963d96317092e9ff7ca6b71b576e844e31958f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

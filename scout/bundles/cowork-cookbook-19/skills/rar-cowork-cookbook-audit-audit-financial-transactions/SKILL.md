---
name: "rar-cowork-cookbook-audit-audit-financial-transactions"
description: "Read-only audit of financial transaction records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Excel workb"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_audit_financial_transactions", "rar_sha256": "d5615d7ae6488bf11ec537ed399d08d2e6084f73d3060036cb7299e805b888a8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_audit_financial_transactions`. The original RAPP
agent is preserved byte-for-byte in `audit_audit_financial_transactions_agent.py` and in the RCI capsule.

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

Audit financial transactions Completeness Audit — Read-only audit of financial transaction records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Excel workb

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-financial-transactions
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
      "description": "Date range to treat as current vs stale; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-audit-financial-transactions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_audit_financial_transactions_agent.py` and embedded as the fenced Python below (sha256 d5615d7ae6488bf1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_audit_financial_transactions_agent.py` first:

```bash
python3 audit_audit_financial_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_audit_financial_transactions_agent.py   # or on stdin
python3 audit_audit_financial_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial transactions Completeness Audit — Read-only audit of financial transaction records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Excel workb

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-financial-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_audit_financial_transactions',
    "version": '3.0.2',
    "display_name": 'Audit financial transactions Completeness Audit',
    "description": 'Read-only audit of financial transaction records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Excel workb',
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
        "upstream_slug": 'audit-audit-financial-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-audit-financial-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd8016fcdb344728d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-transactions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-audit-financial-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-audit-financial-transactions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit audit financial transactions records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to audit financial transactions. Output an Excel workbook 'audit-audit-financial-transactions-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no audit financial transactions data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads audit financial transactions records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of financial transaction records in a Dynamics 365 F&SCM legal entity, flagging missing fields, stale dates, blank descriptions, inactive-entity references, and policy violations, output as an Excel workb', 'example_request': 'Audit financial transactions in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-audit-financial-transactions-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance review of D365 financial transactions with an Excel findings workbook and no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditAuditFinancialTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAuditFinancialTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to treat as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-audit-financial-transactions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditAuditFinancialTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

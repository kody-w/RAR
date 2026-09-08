---
name: "rar-cowork-cookbook-audit-invoice-project-transactions"
description: "Runs a read-only completeness and policy audit of invoice project transactions in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of count"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_invoice_project_transactions", "rar_sha256": "004e32a140fd2f0618dc34c540c60d42d27ad09c995d07a991e3d8a75ef766f1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_invoice_project_transactions`. The original RAPP
agent is preserved byte-for-byte in `audit_invoice_project_transactions_agent.py` and in the RCI capsule.

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

Invoice project transactions Completeness Audit — Runs a read-only completeness and policy audit of invoice project transactions in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of count

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-invoice-project-transactions
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
      "description": "Date range treated as current vs stale; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-invoice-project-transactions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_invoice_project_transactions_agent.py` and embedded as the fenced Python below (sha256 004e32a140fd2f06…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_invoice_project_transactions_agent.py` first:

```bash
python3 audit_invoice_project_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_invoice_project_transactions_agent.py   # or on stdin
python3 audit_invoice_project_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Invoice project transactions Completeness Audit — Runs a read-only completeness and policy audit of invoice project transactions in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of count

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-invoice-project-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_invoice_project_transactions',
    "version": '3.0.3',
    "display_name": 'Invoice project transactions Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of invoice project transactions in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of count',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-invoice-project-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-invoice-project-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd019057b2fb4ac68',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/invoice-project-transactions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/audit-invoice-project-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range treated as current vs stale; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-invoice-project-transactions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit invoice project transactions records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to invoice project transactions. Output an Excel workbook 'audit-invoice-project-transactions-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no invoice project transactions data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads invoice project transactions records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of invoice project transactions in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of count', 'example_request': 'Audit invoice project transactions in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range treated as current vs stale; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-invoice-project-transactions-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants invoice project transactions checked for missing fields, stale dates, blank descriptions, inactive references, or policy violations, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditInvoiceProjectTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditInvoiceProjectTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range treated as current vs stale; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-invoice-project-transactions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditInvoiceProjectTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

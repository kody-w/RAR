---
name: "rar-cowork-cookbook-audit-invoice-project-transactions"
description: "Runs a read-only completeness and policy audit of invoice project transactions in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary sheet of count"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_invoice_project_transactions", "rar_sha256": "004e32a140fd2f0618dc34c540c60d42d27ad09c995d07a991e3d8a75ef766f1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

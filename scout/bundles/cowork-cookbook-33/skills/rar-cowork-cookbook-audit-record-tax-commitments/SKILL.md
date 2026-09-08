---
name: "rar-cowork-cookbook-audit-record-tax-commitments"
description: "Read-only audit of record tax commitments in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_tax_commitments", "rar_sha256": "fc6dc035dfe1a4df7f661fe346fe837032bdc987b54c74a6d2025b5981cd84f4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_record_tax_commitments`. The original RAPP
agent is preserved byte-for-byte in `audit_record_tax_commitments_agent.py` and in the RCI capsule.

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

Record tax commitments Completeness Audit — Read-only audit of record tax commitments in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-tax-commitments
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
      "description": "Name of the Excel workbook to produce, e.g. audit-record-tax-commitments-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_tax_commitments_agent.py` and embedded as the fenced Python below (sha256 fc6dc035dfe1a4df…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_tax_commitments_agent.py` first:

```bash
python3 audit_record_tax_commitments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_record_tax_commitments_agent.py   # or on stdin
python3 audit_record_tax_commitments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record tax commitments Completeness Audit — Read-only audit of record tax commitments in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-tax-commitments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_record_tax_commitments',
    "version": '3.0.3',
    "display_name": 'Record tax commitments Completeness Audit',
    "description": 'Read-only audit of record tax commitments in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workboo',
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
        "upstream_slug": 'audit-record-tax-commitments',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-record-tax-commitments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4cb825c002b8c354',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-tax-commitments'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-record-tax-commitments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-record-tax-commitments-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit record tax commitments records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to record tax commitments. Output an Excel workbook 'audit-record-tax-commitments-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no record tax commitments data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads record tax commitments records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Read-only audit of record tax commitments in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workboo', 'example_request': 'Audit record tax commitments in USMF for completeness and give me the findings as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-record-tax-commitments-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a completeness and policy-compliance check of record tax commitments data in D365 ERP, with findings exported to Excel and no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditRecordTaxCommitments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRecordTaxCommitments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-record-tax-commitments-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditRecordTaxCommitments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

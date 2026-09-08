---
name: "rar-cowork-cookbook-audit-record-tax-commitments"
description: "Read-only audit of record tax commitments in Dynamics 365 F&SCM (legal entity USMF) that flags missing fields, stale dates, blank descriptions, inactive-entity references and policy violations, returning an Excel workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_tax_commitments", "rar_sha256": "fc6dc035dfe1a4df7f661fe346fe837032bdc987b54c74a6d2025b5981cd84f4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

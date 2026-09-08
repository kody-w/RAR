---
name: "rar-cowork-cookbook-audit-manage-supplier-risk"
description: "Audits supplier risk records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_supplier_risk", "rar_sha256": "6df5a21ce69b789420d464a38a04c978c04cc2c8060110d624ba5ed18dbbd98c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_manage_supplier_risk`. The original RAPP
agent is preserved byte-for-byte in `audit_manage_supplier_risk_agent.py` and in the RCI capsule.

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

Manage supplier risk Completeness Audit — Audits supplier risk records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-supplier-risk
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
      "description": "Excel workbook name, e.g. audit-manage-supplier-risk-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_manage_supplier_risk_agent.py` and embedded as the fenced Python below (sha256 6df5a21ce69b7894…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_manage_supplier_risk_agent.py` first:

```bash
python3 audit_manage_supplier_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_manage_supplier_risk_agent.py   # or on stdin
python3 audit_manage_supplier_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier risk Completeness Audit — Audits supplier risk records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-manage-supplier-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_manage_supplier_risk',
    "version": '3.0.3',
    "display_name": 'Manage supplier risk Completeness Audit',
    "description": 'Audits supplier risk records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook.',
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
        "upstream_slug": 'audit-manage-supplier-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-manage-supplier-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ce5de9cb287c2eb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-risk'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/audit-manage-supplier-risk', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. audit-manage-supplier-risk-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit manage supplier risk records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to manage supplier risk. Output an Excel workbook 'audit-manage-supplier-risk-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no manage supplier risk data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads manage supplier risk records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits supplier risk records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook.', 'example_request': 'Audit supplier risk records in USMF for completeness and give me an Excel workbook of the findings.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-manage-supplier-risk-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness and policy-compliance audit of supplier risk records in D365, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditManageSupplierRisk(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditManageSupplierRisk'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used to judge stale dates; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-manage-supplier-risk-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditManageSupplierRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

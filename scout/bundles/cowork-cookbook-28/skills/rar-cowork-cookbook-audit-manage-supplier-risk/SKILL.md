---
name: "rar-cowork-cookbook-audit-manage-supplier-risk"
description: "Audits supplier risk records in Dynamics 365 F&SCM (legal entity USMF) for missing fields, stale dates, blank descriptions, inactive references, and policy violations, returning a read-only Excel workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_manage_supplier_risk", "rar_sha256": "6df5a21ce69b789420d464a38a04c978c04cc2c8060110d624ba5ed18dbbd98c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

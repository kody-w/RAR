---
name: "rar-cowork-cookbook-audit-define-kpis-for-call-center-performance"
description: "Runs a read-only completeness and policy audit of call center KPI records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_kpis_for_call_center_performance", "rar_sha256": "748c2beb662654ec7abea01a5cc2df0417b1365184a4372aca6b9e8fb6062662", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_define_kpis_for_call_center_performance`. The original RAPP
agent is preserved byte-for-byte in `audit_define_kpis_for_call_center_performance_agent.py` and in the RCI capsule.

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

Define KPIs for call center performance Completeness Audit — Runs a read-only completeness and policy audit of call center KPI records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-kpis-for-call-center-performance
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
      "description": "Date range used for stale-date checks; USMF demo data is mostly FY2017.",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-define-kpis-for-call-center-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_define_kpis_for_call_center_performance_agent.py` and embedded as the fenced Python below (sha256 748c2beb662654ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_define_kpis_for_call_center_performance_agent.py` first:

```bash
python3 audit_define_kpis_for_call_center_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_define_kpis_for_call_center_performance_agent.py   # or on stdin
python3 audit_define_kpis_for_call_center_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define KPIs for call center performance Completeness Audit — Runs a read-only completeness and policy audit of call center KPI records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-define-kpis-for-call-center-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_define_kpis_for_call_center_performance',
    "version": '3.0.2',
    "display_name": 'Define KPIs for call center performance Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of call center KPI records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-define-kpis-for-call-center-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-define-kpis-for-call-center-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5ed54d0281889efe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-kpis-for-call-center-performance'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-define-kpis-for-call-center-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range used for stale-date checks; USMF demo data is mostly FY2017.', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-define-kpis-for-call-center-performance-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit define KPIs for call center performance records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to define KPIs for call center performance. Output an Excel workbook 'audit-define-kpis-for-call-center-performance-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no define KPIs for call center performance data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define KPIs for call center performance records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of call center KPI records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet.', 'example_request': 'Audit the call center KPI records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-define-kpis-for-call-center-performance-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Date range used for stale-date checks; USMF demo data is mostly FY2017.', 'name': 'date_window'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to audit call center KPI records in D365 F&SCM for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditDefineKpisForCallCenterPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDefineKpisForCallCenterPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range used for stale-date checks; USMF demo data is mostly FY2017.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-define-kpis-for-call-center-performance-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditDefineKpisForCallCenterPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

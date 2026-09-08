---
name: "rar-cowork-cookbook-audit-define-kpis-for-call-center-performance"
description: "Runs a read-only completeness and policy audit of call center KPI records in Dynamics 365 F&SCM for a given legal entity, returning an Excel workbook with a sheet per finding category plus a Summary sheet."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_define_kpis_for_call_center_performance", "rar_sha256": "748c2beb662654ec7abea01a5cc2df0417b1365184a4372aca6b9e8fb6062662", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

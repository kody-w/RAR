---
name: "rar-cowork-cookbook-audit-configure-and-manage-reporting-and-analytics"
description: "Runs a read-only completeness and policy audit of Dynamics 365 F&SCM reporting-and-analytics configuration records for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics", "rar_sha256": "3f837a389b6dcf0e3a8e47267b609d81cc2702ab52ebe335758fb0be780502be", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics`. The original RAPP
agent is preserved byte-for-byte in `audit_configure_and_manage_reporting_and_analytics_agent.py` and in the RCI capsule.

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

Configure and manage reporting and analytics Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 F&SCM reporting-and-analytics configuration records for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics
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
      "description": "Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).",
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
      "description": "Name of the Excel workbook to produce, e.g. audit-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_configure_and_manage_reporting_and_analytics_agent.py` and embedded as the fenced Python below (sha256 3f837a389b6dcf0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_configure_and_manage_reporting_and_analytics_agent.py` first:

```bash
python3 audit_configure_and_manage_reporting_and_analytics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_configure_and_manage_reporting_and_analytics_agent.py   # or on stdin
python3 audit_configure_and_manage_reporting_and_analytics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage reporting and analytics Completeness Audit — Runs a read-only completeness and policy audit of Dynamics 365 F&SCM reporting-and-analytics configuration records for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_configure_and_manage_reporting_and_analytics',
    "version": '3.0.2',
    "display_name": 'Configure and manage reporting and analytics Completeness Audit',
    "description": 'Runs a read-only completeness and policy audit of Dynamics 365 F&SCM reporting-and-analytics configuration records for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-configure-and-manage-reporting-and-analytics',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-configure-and-manage-reporting-and-analytics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e0351063000da1cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-reporting-and-analytics'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-configure-and-manage-reporting-and-analytics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'legal_entity': 'D365 legal entity to audit, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit configure and manage reporting and analytics records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to configure and manage reporting and analytics. Output an Excel workbook 'audit-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no configure and manage reporting and analytics data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads configure and manage reporting and analytics records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a read-only completeness and policy audit of Dynamics 365 F&SCM reporting-and-analytics configuration records for a given legal entity, returning an Excel workbook with one sheet per finding category plus a Summary', 'example_request': 'Audit the reporting and analytics setup records in USMF for completeness and give me the findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'name': 'date_window'}, {'description': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-change audit of D365 reporting/analytics setup records for missing fields, stale dates, blank descriptions, inactive references, or policy violations.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditConfigureAndManageReportingAndAnalytics(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditConfigureAndManageReportingAndAnalytics'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range treated as current when flagging stale dates (USMF demo data is mostly FY2017).', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. audit-configure-and-manage-reporting-and-analytics-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(AuditConfigureAndManageReportingAndAnalytics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

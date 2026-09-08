---
name: "rar-cowork-cookbook-audit-record-employee-time"
description: "Audits employee time records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy compliance, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_employee_time", "rar_sha256": "45cf4444d17ca9195f02cb40561720fa9c3754dc5bcb92e04302cdcabe95dd81", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_record_employee_time`. The original RAPP
agent is preserved byte-for-byte in `audit_record_employee_time_agent.py` and in the RCI capsule.

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

Record employee time Completeness Audit — Audits employee time records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy compliance, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-employee-time
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
      "description": "Date range to audit; USMF demo data is mostly FY2017, so adjust accordingly.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to audit; the recipe uses USMF.",
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
      "description": "Excel workbook name, e.g. audit-record-employee-time-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_employee_time_agent.py` and embedded as the fenced Python below (sha256 45cf4444d17ca919…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_employee_time_agent.py` first:

```bash
python3 audit_record_employee_time_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_record_employee_time_agent.py   # or on stdin
python3 audit_record_employee_time_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record employee time Completeness Audit — Audits employee time records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy compliance, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.

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
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-employee-time
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_record_employee_time',
    "version": '3.0.3',
    "display_name": 'Record employee time Completeness Audit',
    "description": 'Audits employee time records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy compliance, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-record-employee-time',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-record-employee-time',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b474e98edc67f758',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/record-employee-time'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/audit-record-employee-time', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'date_window': 'Date range to audit; USMF demo data is mostly FY2017, so adjust accordingly.', 'legal_entity': 'D365 legal entity to audit; the recipe uses USMF.', 'output_filename': 'Excel workbook name, e.g. audit-record-employee-time-2026-05-24.xlsx, saved to Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Reduces audit findings and prevents downstream errors by surfacing missing fields, stale records, and out-of-policy entries while there is still time to fix them at the source.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, audit record employee time records for completeness. For each record, flag: missing required fields, stale dates, blank descriptions, references to inactive entities, and any policy violations specific to record employee time. Output an Excel workbook 'audit-record-employee-time-2026-05-24.xlsx' with one sheet per finding category, plus a Summary sheet with counts. Do not modify any data. If the tenant has no record employee time data, honestly report that and stop. (Tenant note: USMF demo data is mostly FY2017 - adjust your date window accordingly.)", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads record employee time records, runs a rule-based completeness audit, and emits an exceptions workbook.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Audits employee time records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy compliance, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts.', 'example_request': 'Audit employee time records in USMF for completeness and give me the Excel findings workbook.', 'inputs': [{'description': 'D365 legal entity to audit; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Date range to audit; USMF demo data is mostly FY2017, so adjust accordingly.', 'name': 'date_window'}, {'description': 'Excel workbook name, e.g. audit-record-employee-time-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a read-only completeness/policy audit of employee time records in D365 F&SCM and an Excel findings workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AuditRecordEmployeeTime(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRecordEmployeeTime'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'date_window': {'description': 'Date range to audit; USMF demo data is mostly FY2017, so adjust accordingly.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to audit; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. audit-record-employee-time-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}},
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
    print(AuditRecordEmployeeTime().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

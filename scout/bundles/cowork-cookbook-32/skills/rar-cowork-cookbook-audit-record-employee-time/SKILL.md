---
name: "rar-cowork-cookbook-audit-record-employee-time"
description: "Audits employee time records in Dynamics 365 F&SCM (legal entity USMF) read-only for completeness and policy compliance, returning an Excel workbook with one sheet per finding category plus a Summary sheet of counts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_employee_time", "rar_sha256": "45cf4444d17ca9195f02cb40561720fa9c3754dc5bcb92e04302cdcabe95dd81", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

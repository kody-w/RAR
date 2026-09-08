---
name: "rar-cowork-cookbook-report-record-employee-absences"
description: "Builds a read-only employee absence summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_employee_absences", "rar_sha256": "b0af915c4b86db946033c51aa022d122eca0b8e0e5a6be7f5ca0b2db5529d806", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_record_employee_absences`. The original RAPP
agent is preserved byte-for-byte in `report_record_employee_absences_agent.py` and in the RCI capsule.

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

Record employee absences Summary Report — Builds a read-only employee absence summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-record-employee-absences
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
    "breakdown_dimensions": {
      "description": "Dimensions for breakdowns where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-record-employee-absences-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_record_employee_absences_agent.py` and embedded as the fenced Python below (sha256 b0af915c4b86db94…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_record_employee_absences_agent.py` first:

```bash
python3 report_record_employee_absences_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_record_employee_absences_agent.py   # or on stdin
python3 report_record_employee_absences_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record employee absences Summary Report — Builds a read-only employee absence summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-record-employee-absences
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_record_employee_absences',
    "version": '3.0.3',
    "display_name": 'Record employee absences Summary Report',
    "description": 'Builds a read-only employee absence summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-record-employee-absences',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-record-employee-absences',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cc525302ee0b07a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/record-employee-absences'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-record-employee-absences', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-record-employee-absences-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where record employee absences stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of record employee absences for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-record-employee-absences-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads record employee absences records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only employee absence summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build an employee absence summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-record-employee-absences-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of recorded employee absences from D365 ERP with totals, dimension breakdowns, and a top-10-by-value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportRecordEmployeeAbsences(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRecordEmployeeAbsences'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-record-employee-absences-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportRecordEmployeeAbsences().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

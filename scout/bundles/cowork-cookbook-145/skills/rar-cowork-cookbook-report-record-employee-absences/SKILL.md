---
name: "rar-cowork-cookbook-report-record-employee-absences"
description: "Builds a read-only employee absence summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_employee_absences", "rar_sha256": "b0af915c4b86db946033c51aa022d122eca0b8e0e5a6be7f5ca0b2db5529d806", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

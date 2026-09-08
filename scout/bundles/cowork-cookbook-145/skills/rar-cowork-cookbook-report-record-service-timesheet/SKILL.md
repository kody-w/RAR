---
name: "rar-cowork-cookbook-report-record-service-timesheet"
description: "Builds a read-only summary report of record service timesheet activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_service_timesheet", "rar_sha256": "e3983f3bbe7f3fda15aa31d47e3d6e8b8b88fa52cc21124ac21520f86faea16e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_record_service_timesheet`. The original RAPP
agent is preserved byte-for-byte in `report_record_service_timesheet_agent.py` and in the RCI capsule.

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

Record service timesheet Summary Report — Builds a read-only summary report of record service timesheet activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-record-service-timesheet
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
      "description": "Dimensions to break down by where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-record-service-timesheet-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_record_service_timesheet_agent.py` and embedded as the fenced Python below (sha256 e3983f3bbe7f3fda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_record_service_timesheet_agent.py` first:

```bash
python3 report_record_service_timesheet_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_record_service_timesheet_agent.py   # or on stdin
python3 report_record_service_timesheet_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record service timesheet Summary Report — Builds a read-only summary report of record service timesheet activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-record-service-timesheet
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_record_service_timesheet',
    "version": '3.0.3',
    "display_name": 'Record service timesheet Summary Report',
    "description": 'Builds a read-only summary report of record service timesheet activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-record-service-timesheet',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-record-service-timesheet',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e851e33689a35412',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/record-service-timesheet'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-record-service-timesheet', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-record-service-timesheet-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where record service timesheet stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of record service timesheet for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-record-service-timesheet-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads record service timesheet records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of record service timesheet activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a record service timesheet summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-record-service-timesheet-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write timesheet summary from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list exported to Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportRecordServiceTimesheet(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRecordServiceTimesheet'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-record-service-timesheet-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportRecordServiceTimesheet().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

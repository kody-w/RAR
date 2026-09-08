---
name: "rar-cowork-cookbook-report-schedule-production-jobs"
description: "Builds a read-only summary report of schedule production jobs from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_schedule_production_jobs", "rar_sha256": "4fe9d8a10bf7634cf704039e2790fb46c917412ed07cb25e2f324d2c0928746a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_schedule_production_jobs`. The original RAPP
agent is preserved byte-for-byte in `report_schedule_production_jobs_agent.py` and in the RCI capsule.

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

Schedule production jobs Summary Report — Builds a read-only summary report of schedule production jobs from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-production-jobs
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Excel workbook filename, e.g. report-schedule-production-jobs-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_schedule_production_jobs_agent.py` and embedded as the fenced Python below (sha256 4fe9d8a10bf7634c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_schedule_production_jobs_agent.py` first:

```bash
python3 report_schedule_production_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_schedule_production_jobs_agent.py   # or on stdin
python3 report_schedule_production_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule production jobs Summary Report — Builds a read-only summary report of schedule production jobs from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-production-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_schedule_production_jobs',
    "version": '3.0.3',
    "display_name": 'Schedule production jobs Summary Report',
    "description": 'Builds a read-only summary report of schedule production jobs from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-schedule-production-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-schedule-production-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b89a8b7b3e17b5b7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/schedule-production-jobs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-schedule-production-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-schedule-production-jobs-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where schedule production jobs stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of schedule production jobs for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-schedule-production-jobs-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads schedule production jobs records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of schedule production jobs from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a schedule production jobs summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook filename, e.g. report-schedule-production-jobs-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of schedule production jobs activity from D365 ERP with totals, breakdowns, and a top-10-by-value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportScheduleProductionJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportScheduleProductionJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-schedule-production-jobs-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportScheduleProductionJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

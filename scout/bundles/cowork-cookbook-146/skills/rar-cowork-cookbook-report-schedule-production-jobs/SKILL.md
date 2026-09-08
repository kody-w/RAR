---
name: "rar-cowork-cookbook-report-schedule-production-jobs"
description: "Builds a read-only summary report of schedule production jobs from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_schedule_production_jobs", "rar_sha256": "4fe9d8a10bf7634cf704039e2790fb46c917412ed07cb25e2f324d2c0928746a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

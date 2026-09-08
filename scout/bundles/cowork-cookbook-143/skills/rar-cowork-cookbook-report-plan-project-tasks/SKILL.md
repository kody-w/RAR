---
name: "rar-cowork-cookbook-report-plan-project-tasks"
description: "Builds a read-only summary report of plan project tasks from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_project_tasks", "rar_sha256": "f395f63d30389ee6aa69c489b58e639cc004b12417cf7496cbad8c301c517ee7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_plan_project_tasks`. The original RAPP
agent is preserved byte-for-byte in `report_plan_project_tasks_agent.py` and in the RCI capsule.

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

Plan project tasks Summary Report — Builds a read-only summary report of plan project tasks from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-project-tasks
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.",
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
      "description": "Excel workbook filename, e.g. report-plan-project-tasks-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_project_tasks_agent.py` and embedded as the fenced Python below (sha256 f395f63d30389ee6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_project_tasks_agent.py` first:

```bash
python3 report_plan_project_tasks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_project_tasks_agent.py   # or on stdin
python3 report_plan_project_tasks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan project tasks Summary Report — Builds a read-only summary report of plan project tasks from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-project-tasks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_project_tasks',
    "version": '3.0.3',
    "display_name": 'Plan project tasks Summary Report',
    "description": 'Builds a read-only summary report of plan project tasks from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-plan-project-tasks',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-project-tasks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7fb2981d004ea401',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/plan-project-tasks'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-plan-project-tasks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-plan-project-tasks-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where plan project tasks stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of plan project tasks for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-plan-project-tasks-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan project tasks records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of plan project tasks from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a plan project tasks summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook filename, e.g. report-plan-project-tasks-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of plan project tasks activity from D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportPlanProjectTasks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanProjectTasks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-plan-project-tasks-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportPlanProjectTasks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

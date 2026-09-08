---
name: "rar-cowork-cookbook-report-plan-workforce-capacity"
description: "Builds a read-only workforce capacity planning summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_workforce_capacity", "rar_sha256": "331bc66384c3e6cfa4564dbdd37cf60a7b0946c3d6ba3538f1a799dc7c3e3220", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_plan_workforce_capacity`. The original RAPP
agent is preserved byte-for-byte in `report_plan_workforce_capacity_agent.py` and in the RCI capsule.

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

Plan workforce capacity Summary Report — Builds a read-only workforce capacity planning summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-workforce-capacity
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
      "description": "Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-plan-workforce-capacity-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_workforce_capacity_agent.py` and embedded as the fenced Python below (sha256 331bc66384c3e6cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_workforce_capacity_agent.py` first:

```bash
python3 report_plan_workforce_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_workforce_capacity_agent.py   # or on stdin
python3 report_plan_workforce_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce capacity Summary Report — Builds a read-only workforce capacity planning summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-workforce-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_workforce_capacity',
    "version": '3.0.3',
    "display_name": 'Plan workforce capacity Summary Report',
    "description": 'Builds a read-only workforce capacity planning summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-plan-workforce-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-workforce-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9213285756918adc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-workforce-capacity'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-plan-workforce-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-plan-workforce-capacity-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where plan workforce capacity stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of plan workforce capacity for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-plan-workforce-capacity-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan workforce capacity records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only workforce capacity planning summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': "Build a plan workforce capacity summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-plan-workforce-capacity-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of plan workforce capacity from Dynamics 365 ERP with totals, dimension breakdowns, and a top-10 list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportPlanWorkforceCapacity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanWorkforceCapacity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-plan-workforce-capacity-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportPlanWorkforceCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-plan-workforce-capacity"
description: "Builds a read-only workforce capacity planning summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_workforce_capacity", "rar_sha256": "331bc66384c3e6cfa4564dbdd37cf60a7b0946c3d6ba3538f1a799dc7c3e3220", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

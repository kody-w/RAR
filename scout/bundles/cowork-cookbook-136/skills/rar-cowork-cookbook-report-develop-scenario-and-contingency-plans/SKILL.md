---
name: "rar-cowork-cookbook-report-develop-scenario-and-contingency-plans"
description: "Builds a read-only scenario and contingency planning summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_scenario_and_contingency_plans", "rar_sha256": "e0c17621509be2e112dff1bc3efbfff5af29fc6d091ffd59ba3cb032b170dc1c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_scenario_and_contingency_plans`. The original RAPP
agent is preserved byte-for-byte in `report_develop_scenario_and_contingency_plans_agent.py` and in the RCI capsule.

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

Develop scenario and contingency plans Summary Report — Builds a read-only scenario and contingency planning summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-scenario-and-contingency-plans
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
      "description": "Name of the Excel workbook to produce, e.g. report-develop-scenario-and-contingency-plans-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_scenario_and_contingency_plans_agent.py` and embedded as the fenced Python below (sha256 e0c17621509be2e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_scenario_and_contingency_plans_agent.py` first:

```bash
python3 report_develop_scenario_and_contingency_plans_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_scenario_and_contingency_plans_agent.py   # or on stdin
python3 report_develop_scenario_and_contingency_plans_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop scenario and contingency plans Summary Report — Builds a read-only scenario and contingency planning summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-scenario-and-contingency-plans
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_scenario_and_contingency_plans',
    "version": '3.0.3',
    "display_name": 'Develop scenario and contingency plans Summary Report',
    "description": 'Builds a read-only scenario and contingency planning summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-develop-scenario-and-contingency-plans',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-scenario-and-contingency-plans',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9bfe912c4b19d927',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-scenario-and-contingency-plans'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-develop-scenario-and-contingency-plans', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-develop-scenario-and-contingency-plans-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop scenario and contingency plans stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop scenario and contingency plans for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-scenario-and-contingency-plans-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop scenario and contingency plans records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only scenario and contingency planning summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a scenario and contingency plans summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-develop-scenario-and-contingency-plans-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, trends, and by-dimension breakdown report of develop scenario and contingency plans activity from D365 ERP, exported to Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopScenarioAndContingencyPlans(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopScenarioAndContingencyPlans'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-develop-scenario-and-contingency-plans-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportDevelopScenarioAndContingencyPlans().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

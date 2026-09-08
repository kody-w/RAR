---
name: "rar-cowork-cookbook-report-develop-scenario-and-contingency-plans"
description: "Builds a read-only scenario and contingency planning summary report from Dynamics 365 F&SCM data for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_scenario_and_contingency_plans", "rar_sha256": "e0c17621509be2e112dff1bc3efbfff5af29fc6d091ffd59ba3cb032b170dc1c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-report-forecast-revenue"
description: "Builds a read-only forecast revenue summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_forecast_revenue", "rar_sha256": "fc85c0dd398e51f7d0da9bd2f044ba341397b6d8647df9fb364646b59a1fc07c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_forecast_revenue`. The original RAPP
agent is preserved byte-for-byte in `report_forecast_revenue_agent.py` and in the RCI capsule.

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

Forecast revenue Summary Report — Builds a read-only forecast revenue summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-forecast-revenue
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
      "description": "Name of the Excel workbook to produce, e.g. report-forecast-revenue-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_forecast_revenue_agent.py` and embedded as the fenced Python below (sha256 fc85c0dd398e51f7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_forecast_revenue_agent.py` first:

```bash
python3 report_forecast_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_forecast_revenue_agent.py   # or on stdin
python3 report_forecast_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast revenue Summary Report — Builds a read-only forecast revenue summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-forecast-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_forecast_revenue',
    "version": '3.0.3',
    "display_name": 'Forecast revenue Summary Report',
    "description": 'Builds a read-only forecast revenue summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-forecast-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-forecast-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0a3355097efd3fd1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/forecast-revenue'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-forecast-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-forecast-revenue-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where forecast revenue stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of forecast revenue for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-forecast-revenue-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast revenue records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only forecast revenue summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a forecast revenue summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-forecast-revenue-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a forecast revenue summary report with totals, by-dimension breakdowns, and top 10 by value, exported to Excel, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportForecastRevenue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportForecastRevenue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-forecast-revenue-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportForecastRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

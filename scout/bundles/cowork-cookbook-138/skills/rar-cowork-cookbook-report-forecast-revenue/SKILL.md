---
name: "rar-cowork-cookbook-report-forecast-revenue"
description: "Builds a read-only forecast revenue summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_forecast_revenue", "rar_sha256": "fc85c0dd398e51f7d0da9bd2f044ba341397b6d8647df9fb364646b59a1fc07c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-report-forecast-service-parts-demand"
description: "Builds a read-only summary report of forecast service parts demand from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_forecast_service_parts_demand", "rar_sha256": "991baaae3dc0b52dbd4faeb08bd98fce2c18e977ff8279be5ef7bc8bf121d6bf", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_forecast_service_parts_demand`. The original RAPP
agent is preserved byte-for-byte in `report_forecast_service_parts_demand_agent.py` and in the RCI capsule.

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

Forecast service parts demand Summary Report — Builds a read-only summary report of forecast service parts demand from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-forecast-service-parts-demand
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
      "description": "Name of the Excel workbook to produce, e.g. report-forecast-service-parts-demand-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_forecast_service_parts_demand_agent.py` and embedded as the fenced Python below (sha256 991baaae3dc0b52d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_forecast_service_parts_demand_agent.py` first:

```bash
python3 report_forecast_service_parts_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_forecast_service_parts_demand_agent.py   # or on stdin
python3 report_forecast_service_parts_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast service parts demand Summary Report — Builds a read-only summary report of forecast service parts demand from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-forecast-service-parts-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_forecast_service_parts_demand',
    "version": '3.0.3',
    "display_name": 'Forecast service parts demand Summary Report',
    "description": 'Builds a read-only summary report of forecast service parts demand from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-forecast-service-parts-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-forecast-service-parts-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '602c1a257c4ec81f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/forecast-service-parts-demand'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-forecast-service-parts-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-forecast-service-parts-demand-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where forecast service parts demand stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of forecast service parts demand for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-forecast-service-parts-demand-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast service parts demand records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of forecast service parts demand from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a forecast service parts demand summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-forecast-service-parts-demand-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write forecast service parts demand summary from D365 ERP with totals, dimension breakdowns, and a Top 10 by value section.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportForecastServicePartsDemand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportForecastServicePartsDemand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-forecast-service-parts-demand-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportForecastServicePartsDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

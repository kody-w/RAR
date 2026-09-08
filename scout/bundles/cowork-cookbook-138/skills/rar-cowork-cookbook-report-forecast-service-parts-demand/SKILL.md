---
name: "rar-cowork-cookbook-report-forecast-service-parts-demand"
description: "Builds a read-only summary report of forecast service parts demand from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_forecast_service_parts_demand", "rar_sha256": "991baaae3dc0b52dbd4faeb08bd98fce2c18e977ff8279be5ef7bc8bf121d6bf", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

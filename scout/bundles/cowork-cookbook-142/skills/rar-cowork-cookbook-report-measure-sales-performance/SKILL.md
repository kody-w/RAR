---
name: "rar-cowork-cookbook-report-measure-sales-performance"
description: "Builds a read-only sales performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_measure_sales_performance", "rar_sha256": "4858dc996ccf2d84a7d3e4829293d9c076e63f1366845e0b8665b7891a5e157a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_measure_sales_performance`. The original RAPP
agent is preserved byte-for-byte in `report_measure_sales_performance_agent.py` and in the RCI capsule.

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

Measure sales performance Summary Report — Builds a read-only sales performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-measure-sales-performance
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
      "description": "Name of the Excel workbook to produce, e.g. report-measure-sales-performance-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_measure_sales_performance_agent.py` and embedded as the fenced Python below (sha256 4858dc996ccf2d84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_measure_sales_performance_agent.py` first:

```bash
python3 report_measure_sales_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_measure_sales_performance_agent.py   # or on stdin
python3 report_measure_sales_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure sales performance Summary Report — Builds a read-only sales performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-measure-sales-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_measure_sales_performance',
    "version": '3.0.3',
    "display_name": 'Measure sales performance Summary Report',
    "description": 'Builds a read-only sales performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-measure-sales-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-measure-sales-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '91a1a4b737ff91fb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/measure-sales-performance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-measure-sales-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-measure-sales-performance-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where measure sales performance stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of measure sales performance for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-measure-sales-performance-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads measure sales performance records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only sales performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a sales performance summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-measure-sales-performance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write sales performance summary from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportMeasureSalesPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMeasureSalesPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-measure-sales-performance-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportMeasureSalesPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

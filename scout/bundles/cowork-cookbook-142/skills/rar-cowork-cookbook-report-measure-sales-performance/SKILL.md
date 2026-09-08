---
name: "rar-cowork-cookbook-report-measure-sales-performance"
description: "Builds a read-only sales performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_measure_sales_performance", "rar_sha256": "4858dc996ccf2d84a7d3e4829293d9c076e63f1366845e0b8665b7891a5e157a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

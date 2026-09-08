---
name: "rar-cowork-cookbook-report-measure-and-analyze-procurement-spend"
description: "Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_measure_and_analyze_procurement_spend", "rar_sha256": "a0ea2fb627d3b5a87e42104fee8a77bd3d06cc37d0cc307ed2f66f0f46b2d49a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_measure_and_analyze_procurement_spend`. The original RAPP
agent is preserved byte-for-byte in `report_measure_and_analyze_procurement_spend_agent.py` and in the RCI capsule.

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

Measure and analyze procurement spend Summary Report — Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-measure-and-analyze-procurement-spend
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
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-measure-and-analyze-procurement-spend-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to analyze; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_measure_and_analyze_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 a0ea2fb627d3b5a8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_measure_and_analyze_procurement_spend_agent.py` first:

```bash
python3 report_measure_and_analyze_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_measure_and_analyze_procurement_spend_agent.py   # or on stdin
python3 report_measure_and_analyze_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure and analyze procurement spend Summary Report — Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-measure-and-analyze-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_measure_and_analyze_procurement_spend',
    "version": '3.0.3',
    "display_name": 'Measure and analyze procurement spend Summary Report',
    "description": 'Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-measure-and-analyze-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-measure-and-analyze-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '806d48b955741e77',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/measure-and-analyze-procurement-spend'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-measure-and-analyze-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-measure-and-analyze-procurement-spend-2026-05-24.xlsx.', 'period': 'Posted period to analyze; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where measure and analyze procurement spend stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of measure and analyze procurement spend for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-measure-and-analyze-procurement-spend-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads measure and analyze procurement spend records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a procurement spend summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to analyze; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-measure-and-analyze-procurement-spend-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a procurement spend summary with totals, by-dimension breakdowns, and a top 10 list exported to Excel from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportMeasureAndAnalyzeProcurementSpend(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMeasureAndAnalyzeProcurementSpend'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-measure-and-analyze-procurement-spend-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to analyze; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportMeasureAndAnalyzeProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-measure-and-analyze-procurement-spend"
description: "Builds a read-only procurement spend summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_measure_and_analyze_procurement_spend", "rar_sha256": "a0ea2fb627d3b5a87e42104fee8a77bd3d06cc37d0cc307ed2f66f0f46b2d49a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

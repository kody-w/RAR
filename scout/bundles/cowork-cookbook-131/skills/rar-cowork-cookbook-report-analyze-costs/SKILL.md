---
name: "rar-cowork-cookbook-report-analyze-costs"
description: "Builds a read-only cost analysis summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_costs", "rar_sha256": "ba364188a56e604d1027b118461e1e1aa102dd77e29948802cf284d1274a1ba5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_analyze_costs`. The original RAPP
agent is preserved byte-for-byte in `report_analyze_costs_agent.py` and in the RCI capsule.

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

Analyze costs Summary Report — Builds a read-only cost analysis summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-costs
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
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
      "description": "Excel workbook name, e.g. report-analyze-costs-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_costs_agent.py` and embedded as the fenced Python below (sha256 ba364188a56e604d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_costs_agent.py` first:

```bash
python3 report_analyze_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_costs_agent.py   # or on stdin
python3 report_analyze_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze costs Summary Report — Builds a read-only cost analysis summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_costs',
    "version": '3.0.3',
    "display_name": 'Analyze costs Summary Report',
    "description": "Builds a read-only cost analysis summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-analyze-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '95a87615191a17f4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-costs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-analyze-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-analyze-costs-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where analyze costs stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of analyze costs for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-analyze-costs-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze costs records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only cost analysis summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.", 'example_request': "Build a cost analysis summary report for USMF's latest posted period as an Excel workbook with a Top 10 sheet.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-analyze-costs-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write cost analysis summary from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list exported to Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportAnalyzeCosts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-analyze-costs-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportAnalyzeCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-analyze-costs"
description: "Builds a read-only cost analysis summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_costs", "rar_sha256": "ba364188a56e604d1027b118461e1e1aa102dd77e29948802cf284d1274a1ba5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

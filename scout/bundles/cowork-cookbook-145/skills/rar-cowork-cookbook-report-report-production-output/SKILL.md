---
name: "rar-cowork-cookbook-report-report-production-output"
description: "Builds a read-only summary report of production output from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_production_output", "rar_sha256": "034aeabf1076afa239773a1cf79bbcfbdb24f106cb3eb18280ec33517b35031b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_report_production_output`. The original RAPP
agent is preserved byte-for-byte in `report_report_production_output_agent.py` and in the RCI capsule.

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

Report production output Summary Report — Builds a read-only summary report of production output from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-report-production-output
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
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Excel workbook name, e.g. report-report-production-output-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_report_production_output_agent.py` and embedded as the fenced Python below (sha256 034aeabf1076afa2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_report_production_output_agent.py` first:

```bash
python3 report_report_production_output_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_report_production_output_agent.py   # or on stdin
python3 report_report_production_output_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production output Summary Report — Builds a read-only summary report of production output from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-report-production-output
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_report_production_output',
    "version": '3.0.3',
    "display_name": 'Report production output Summary Report',
    "description": 'Builds a read-only summary report of production output from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-report-production-output',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-report-production-output',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f60e3979ca66cd7b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/report-production-output'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-report-production-output', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Excel workbook name, e.g. report-report-production-output-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where report production output stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of report production output for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-report-production-output-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads report production output records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of production output from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a production output summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook name, e.g. report-report-production-output-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP production output summary with totals, dimension breakdowns, and a Top 10 by value list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportReportProductionOutput(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReportProductionOutput'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-report-production-output-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportReportProductionOutput().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

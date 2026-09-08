---
name: "rar-cowork-cookbook-report-monitor-operational-performance"
description: "Builds a read-only operational performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_operational_performance", "rar_sha256": "4c31d47625dae818e238ed9c983151dc7fa8d2c0c54ea78229dcbc5a76edb6a7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_monitor_operational_performance`. The original RAPP
agent is preserved byte-for-byte in `report_monitor_operational_performance_agent.py` and in the RCI capsule.

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

Monitor operational performance Summary Report — Builds a read-only operational performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-operational-performance
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-monitor-operational-performance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_operational_performance_agent.py` and embedded as the fenced Python below (sha256 4c31d47625dae818…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_operational_performance_agent.py` first:

```bash
python3 report_monitor_operational_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_monitor_operational_performance_agent.py   # or on stdin
python3 report_monitor_operational_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor operational performance Summary Report — Builds a read-only operational performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-operational-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_monitor_operational_performance',
    "version": '3.0.3',
    "display_name": 'Monitor operational performance Summary Report',
    "description": 'Builds a read-only operational performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-monitor-operational-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-monitor-operational-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eccac21aa2e626d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/monitor-operational-performance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-monitor-operational-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-monitor-operational-performance-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where monitor operational performance stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of monitor operational performance for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-monitor-operational-performance-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor operational performance records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only operational performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a monitor operational performance summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-monitor-operational-performance-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of monitor operational performance from D365 ERP data, with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportMonitorOperationalPerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMonitorOperationalPerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-monitor-operational-performance-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportMonitorOperationalPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

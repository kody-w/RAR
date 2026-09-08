---
name: "rar-cowork-cookbook-report-monitor-operational-performance"
description: "Builds a read-only operational performance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_operational_performance", "rar_sha256": "4c31d47625dae818e238ed9c983151dc7fa8d2c0c54ea78229dcbc5a76edb6a7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

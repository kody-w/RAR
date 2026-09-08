---
name: "rar-cowork-cookbook-report-plan-procurement"
description: "Builds a read-only plan procurement summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_procurement", "rar_sha256": "8c32025fec2546fb25f79e489bc745cf64299b86eb2c25664d95920dd05f44b0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_plan_procurement`. The original RAPP
agent is preserved byte-for-byte in `report_plan_procurement_agent.py` and in the RCI capsule.

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

Plan procurement Summary Report — Builds a read-only plan procurement summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-procurement
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
      "description": "Name of the Excel workbook to produce, e.g. report-plan-procurement-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_procurement_agent.py` and embedded as the fenced Python below (sha256 8c32025fec2546fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_procurement_agent.py` first:

```bash
python3 report_plan_procurement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_procurement_agent.py   # or on stdin
python3 report_plan_procurement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan procurement Summary Report — Builds a read-only plan procurement summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-procurement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_procurement',
    "version": '3.0.3',
    "display_name": 'Plan procurement Summary Report',
    "description": 'Builds a read-only plan procurement summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-plan-procurement',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-procurement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '27038b58ec305698',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-procurement'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-plan-procurement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-plan-procurement-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where plan procurement stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of plan procurement for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-plan-procurement-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan procurement records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only plan procurement summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a plan procurement summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-plan-procurement-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a plan procurement summary with totals, by-dimension breakdowns, and a top-10-by-value list exported to Excel from D365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportPlanProcurement(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanProcurement'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-plan-procurement-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportPlanProcurement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-plan-procurement"
description: "Builds a read-only plan procurement summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_procurement", "rar_sha256": "8c32025fec2546fb25f79e489bc745cf64299b86eb2c25664d95920dd05f44b0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

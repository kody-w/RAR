---
name: "rar-cowork-cookbook-report-plan-workforce-development"
description: "Builds a read-only workforce development summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_workforce_development", "rar_sha256": "705513cff2ee0eb8957fe250e8e11146f5190483f40c4d6ce3a04a4b02d36635", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_plan_workforce_development`. The original RAPP
agent is preserved byte-for-byte in `report_plan_workforce_development_agent.py` and in the RCI capsule.

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

Plan workforce development Summary Report — Builds a read-only workforce development summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-workforce-development
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
      "description": "Dimensions to break down by where applicable: department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-plan-workforce-development-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_workforce_development_agent.py` and embedded as the fenced Python below (sha256 705513cff2ee0eb8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_workforce_development_agent.py` first:

```bash
python3 report_plan_workforce_development_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_workforce_development_agent.py   # or on stdin
python3 report_plan_workforce_development_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce development Summary Report — Builds a read-only workforce development summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-workforce-development
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_workforce_development',
    "version": '3.0.3',
    "display_name": 'Plan workforce development Summary Report',
    "description": 'Builds a read-only workforce development summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-plan-workforce-development',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-workforce-development',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5d530bbabe21e8d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-workforce-development'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-plan-workforce-development', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-plan-workforce-development-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where plan workforce development stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of plan workforce development for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-plan-workforce-development-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan workforce development records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only workforce development summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a workforce development summary report from D365 for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-plan-workforce-development-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a workforce development summary report from D365 ERP data with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportPlanWorkforceDevelopment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanWorkforceDevelopment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-plan-workforce-development-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportPlanWorkforceDevelopment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-plan-workforce-development"
description: "Builds a read-only workforce development summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_workforce_development", "rar_sha256": "705513cff2ee0eb8957fe250e8e11146f5190483f40c4d6ce3a04a4b02d36635", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

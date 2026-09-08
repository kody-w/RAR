---
name: "rar-cowork-cookbook-report-set-strategic-goals-and-incentives"
description: "Builds a read-only summary report of set strategic goals and incentives activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_set_strategic_goals_and_incentives", "rar_sha256": "601ef4e08a305ed0281b789d2d779a95535dbde0ba1ae4a891417bcbd6fb7749", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_set_strategic_goals_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `report_set_strategic_goals_and_incentives_agent.py` and in the RCI capsule.

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

Set strategic goals and incentives Summary Report — Builds a read-only summary report of set strategic goals and incentives activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-set-strategic-goals-and-incentives
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
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Excel workbook filename, e.g. report-set-strategic-goals-and-incentives-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_set_strategic_goals_and_incentives_agent.py` and embedded as the fenced Python below (sha256 601ef4e08a305ed0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_set_strategic_goals_and_incentives_agent.py` first:

```bash
python3 report_set_strategic_goals_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_set_strategic_goals_and_incentives_agent.py   # or on stdin
python3 report_set_strategic_goals_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set strategic goals and incentives Summary Report — Builds a read-only summary report of set strategic goals and incentives activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-set-strategic-goals-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_set_strategic_goals_and_incentives',
    "version": '3.0.3',
    "display_name": 'Set strategic goals and incentives Summary Report',
    "description": 'Builds a read-only summary report of set strategic goals and incentives activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-set-strategic-goals-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-set-strategic-goals-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f2d1605e3b7230d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/set-strategic-goals-and-incentives'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-set-strategic-goals-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-set-strategic-goals-and-incentives-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where set strategic goals and incentives stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of set strategic goals and incentives for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-set-strategic-goals-and-incentives-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads set strategic goals and incentives records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of set strategic goals and incentives activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a strategic goals and incentives summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook filename, e.g. report-set-strategic-goals-and-incentives-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary of strategic goals and incentives activity with totals, dimension breakdowns, and a top-10-by-value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportSetStrategicGoalsAndIncentives(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportSetStrategicGoalsAndIncentives'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-set-strategic-goals-and-incentives-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportSetStrategicGoalsAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

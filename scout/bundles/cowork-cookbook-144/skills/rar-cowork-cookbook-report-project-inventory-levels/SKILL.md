---
name: "rar-cowork-cookbook-report-project-inventory-levels"
description: "Builds a read-only project inventory levels summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_project_inventory_levels", "rar_sha256": "537ba769d2882f6c33c68bf8ed32c593e58887acd07836010383fff7894c4be7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_project_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `report_project_inventory_levels_agent.py` and in the RCI capsule.

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

Project inventory levels Summary Report — Builds a read-only project inventory levels summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-project-inventory-levels
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.",
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
      "description": "Name of the Excel workbook to write, e.g. report-project-inventory-levels-2026-05-24.xlsx.",
      "type": "string"
    },
    "posting_period": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_project_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 537ba769d2882f6c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_project_inventory_levels_agent.py` first:

```bash
python3 report_project_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_project_inventory_levels_agent.py   # or on stdin
python3 report_project_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Project inventory levels Summary Report — Builds a read-only project inventory levels summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-project-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_project_inventory_levels',
    "version": '3.0.3',
    "display_name": 'Project inventory levels Summary Report',
    "description": 'Builds a read-only project inventory levels summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-project-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-project-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '36722dccea828127',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/project-inventory-levels'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-project-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to write, e.g. report-project-inventory-levels-2026-05-24.xlsx.', 'posting_period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where project inventory levels stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of project inventory levels for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-project-inventory-levels-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads project inventory levels records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only project inventory levels summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a project inventory levels summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'posting_period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to write, e.g. report-project-inventory-levels-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write inventory levels summary from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportProjectInventoryLevels(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportProjectInventoryLevels'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to write, e.g. report-project-inventory-levels-2026-05-24.xlsx.', 'type': 'string'}, 'posting_period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportProjectInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

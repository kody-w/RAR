---
name: "rar-cowork-cookbook-report-project-inventory-levels"
description: "Builds a read-only project inventory levels summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_project_inventory_levels", "rar_sha256": "537ba769d2882f6c33c68bf8ed32c593e58887acd07836010383fff7894c4be7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

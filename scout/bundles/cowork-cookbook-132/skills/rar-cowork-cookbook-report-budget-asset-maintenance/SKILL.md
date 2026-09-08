---
name: "rar-cowork-cookbook-report-budget-asset-maintenance"
description: "Builds a read-only budget asset maintenance summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_budget_asset_maintenance", "rar_sha256": "ad115f36cca85a505821d5880868c8fd857abcabf24599110422e0edaee1b032", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_budget_asset_maintenance`. The original RAPP
agent is preserved byte-for-byte in `report_budget_asset_maintenance_agent.py` and in the RCI capsule.

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

Budget asset maintenance Summary Report — Builds a read-only budget asset maintenance summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-budget-asset-maintenance
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
      "description": "Dimensions to break totals down by, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-budget-asset-maintenance-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_budget_asset_maintenance_agent.py` and embedded as the fenced Python below (sha256 ad115f36cca85a50…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_budget_asset_maintenance_agent.py` first:

```bash
python3 report_budget_asset_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_budget_asset_maintenance_agent.py   # or on stdin
python3 report_budget_asset_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget asset maintenance Summary Report — Builds a read-only budget asset maintenance summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-budget-asset-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_budget_asset_maintenance',
    "version": '3.0.3',
    "display_name": 'Budget asset maintenance Summary Report',
    "description": 'Builds a read-only budget asset maintenance summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-budget-asset-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-budget-asset-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1d593e2c3b5bbaec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/budget-asset-maintenance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-budget-asset-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break totals down by, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-budget-asset-maintenance-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where budget asset maintenance stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of budget asset maintenance for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-budget-asset-maintenance-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads budget asset maintenance records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only budget asset maintenance summary from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a budget asset maintenance summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions to break totals down by, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-budget-asset-maintenance-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of budget asset maintenance from D365 ERP, with totals, by-dimension breakdowns, and a top-10-by-value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportBudgetAssetMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportBudgetAssetMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break totals down by, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-budget-asset-maintenance-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportBudgetAssetMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

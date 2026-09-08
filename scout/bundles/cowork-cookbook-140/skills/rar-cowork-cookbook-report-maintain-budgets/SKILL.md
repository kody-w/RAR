---
name: "rar-cowork-cookbook-report-maintain-budgets"
description: "Builds a read-only budget-maintenance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_budgets", "rar_sha256": "4fcccf0dec826337acffcb0eb84341f3cd3d272b0d2b07bdf467c754679792cd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_maintain_budgets`. The original RAPP
agent is preserved byte-for-byte in `report_maintain_budgets_agent.py` and in the RCI capsule.

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

Maintain budgets Summary Report — Builds a read-only budget-maintenance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-budgets
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
      "description": "Excel workbook name, e.g. report-maintain-budgets-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_maintain_budgets_agent.py` and embedded as the fenced Python below (sha256 4fcccf0dec826337…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_maintain_budgets_agent.py` first:

```bash
python3 report_maintain_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_maintain_budgets_agent.py   # or on stdin
python3 report_maintain_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain budgets Summary Report — Builds a read-only budget-maintenance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_maintain_budgets',
    "version": '3.0.3',
    "display_name": 'Maintain budgets Summary Report',
    "description": 'Builds a read-only budget-maintenance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-maintain-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-maintain-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a876a2411755b18a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/maintain-budgets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-maintain-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-maintain-budgets-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where maintain budgets stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of maintain budgets for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-maintain-budgets-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads maintain budgets records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only budget-maintenance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a maintain budgets summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-maintain-budgets-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of maintain budgets activity with totals, by-dimension breakdowns, and top 10 by value as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportMaintainBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMaintainBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-maintain-budgets-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportMaintainBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

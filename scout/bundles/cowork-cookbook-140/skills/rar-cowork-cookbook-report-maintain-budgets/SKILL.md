---
name: "rar-cowork-cookbook-report-maintain-budgets"
description: "Builds a read-only budget-maintenance summary report from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_budgets", "rar_sha256": "4fcccf0dec826337acffcb0eb84341f3cd3d272b0d2b07bdf467c754679792cd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

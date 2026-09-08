---
name: "rar-cowork-cookbook-report-correct-project-transactions"
description: "Generates a read-only summary report of correct project transactions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_correct_project_transactions", "rar_sha256": "032ac744f36b6da623a654efd4da72ae8e156f983890cacbe474c6efc4fbeba3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_correct_project_transactions`. The original RAPP
agent is preserved byte-for-byte in `report_correct_project_transactions_agent.py` and in the RCI capsule.

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

Correct project transactions Summary Report — Generates a read-only summary report of correct project transactions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-correct-project-transactions
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
      "description": "Dimensions for breakdowns where applicable: department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-correct-project-transactions-2026-05-24.xlsx.",
      "type": "string"
    },
    "posted_period": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_correct_project_transactions_agent.py` and embedded as the fenced Python below (sha256 032ac744f36b6da6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_correct_project_transactions_agent.py` first:

```bash
python3 report_correct_project_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_correct_project_transactions_agent.py   # or on stdin
python3 report_correct_project_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct project transactions Summary Report — Generates a read-only summary report of correct project transactions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-correct-project-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_correct_project_transactions',
    "version": '3.0.3',
    "display_name": 'Correct project transactions Summary Report',
    "description": 'Generates a read-only summary report of correct project transactions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-correct-project-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-correct-project-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2d3450a62ba2149d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/correct-project-transactions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-correct-project-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-correct-project-transactions-2026-05-24.xlsx.', 'posted_period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where correct project transactions stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of correct project transactions for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-correct-project-transactions-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads correct project transactions records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only summary report of correct project transactions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a correct project transactions summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'posted_period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-correct-project-transactions-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, by-dimension breakdown, and Top 10 by value report of correct project transactions from D365 ERP, with no data changes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportCorrectProjectTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCorrectProjectTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-correct-project-transactions-2026-05-24.xlsx.', 'type': 'string'}, 'posted_period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportCorrectProjectTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

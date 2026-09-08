---
name: "rar-cowork-cookbook-report-correct-project-transactions"
description: "Generates a read-only summary report of correct project transactions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_correct_project_transactions", "rar_sha256": "032ac744f36b6da623a654efd4da72ae8e156f983890cacbe474c6efc4fbeba3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

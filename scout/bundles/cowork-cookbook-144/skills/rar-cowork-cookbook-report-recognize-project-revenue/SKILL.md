---
name: "rar-cowork-cookbook-report-recognize-project-revenue"
description: "Builds a read-only project revenue recognition summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_recognize_project_revenue", "rar_sha256": "2eb131d950d3f7da66b018c7f73fba3227285412b3fbc51587cd53a19bd1b4fc", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_recognize_project_revenue`. The original RAPP
agent is preserved byte-for-byte in `report_recognize_project_revenue_agent.py` and in the RCI capsule.

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

Recognize project revenue Summary Report — Builds a read-only project revenue recognition summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-recognize-project-revenue
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
      "description": "Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-recognize-project-revenue-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_recognize_project_revenue_agent.py` and embedded as the fenced Python below (sha256 2eb131d950d3f7da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_recognize_project_revenue_agent.py` first:

```bash
python3 report_recognize_project_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_recognize_project_revenue_agent.py   # or on stdin
python3 report_recognize_project_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Recognize project revenue Summary Report — Builds a read-only project revenue recognition summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-recognize-project-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_recognize_project_revenue',
    "version": '3.0.3',
    "display_name": 'Recognize project revenue Summary Report',
    "description": 'Builds a read-only project revenue recognition summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-recognize-project-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-recognize-project-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd2bddbe7a72fd62d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/recognize-project-revenue'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-recognize-project-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-recognize-project-revenue-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where recognize project revenue stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of recognize project revenue for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-recognize-project-revenue-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads recognize project revenue records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only project revenue recognition summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a recognize project revenue summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-recognize-project-revenue-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-changes summary of recognized project revenue with totals, by-dimension breakdowns, and a top-10 list exported to Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportRecognizeProjectRevenue(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRecognizeProjectRevenue'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-recognize-project-revenue-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportRecognizeProjectRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

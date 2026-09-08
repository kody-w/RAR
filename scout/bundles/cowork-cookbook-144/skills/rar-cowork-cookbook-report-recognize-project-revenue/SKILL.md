---
name: "rar-cowork-cookbook-report-recognize-project-revenue"
description: "Builds a read-only project revenue recognition summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_recognize_project_revenue", "rar_sha256": "2eb131d950d3f7da66b018c7f73fba3227285412b3fbc51587cd53a19bd1b4fc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-report-budget-fixed-assets"
description: "Builds a read-only summary report of budget fixed assets from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_budget_fixed_assets", "rar_sha256": "2f99f6a537cf2393d5e92da29d43c05c97ce2510efb9aa7a8b6ddfb12c1c5419", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_budget_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `report_budget_fixed_assets_agent.py` and in the RCI capsule.

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

Budget fixed assets Summary Report — Builds a read-only summary report of budget fixed assets from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-budget-fixed-assets
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
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-budget-fixed-assets-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_budget_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 2f99f6a537cf2393…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_budget_fixed_assets_agent.py` first:

```bash
python3 report_budget_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_budget_fixed_assets_agent.py   # or on stdin
python3 report_budget_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget fixed assets Summary Report — Builds a read-only summary report of budget fixed assets from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-budget-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_budget_fixed_assets',
    "version": '3.0.3',
    "display_name": 'Budget fixed assets Summary Report',
    "description": 'Builds a read-only summary report of budget fixed assets from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-budget-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-budget-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '76be741686bc0a73',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/budget-fixed-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-budget-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-budget-fixed-assets-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where budget fixed assets stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of budget fixed assets for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-budget-fixed-assets-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads budget fixed assets records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of budget fixed assets from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': "Build a budget fixed assets summary report for USMF's latest posted period as an Excel file with a Top 10 sheet.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-budget-fixed-assets-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of budget fixed assets activity with totals, by-dimension breakdowns, and a top-10 list exported to Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportBudgetFixedAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportBudgetFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-budget-fixed-assets-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportBudgetFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

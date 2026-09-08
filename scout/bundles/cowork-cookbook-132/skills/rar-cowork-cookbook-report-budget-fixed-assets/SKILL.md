---
name: "rar-cowork-cookbook-report-budget-fixed-assets"
description: "Builds a read-only summary report of budget fixed assets from Dynamics 365 F&SCM for a legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_budget_fixed_assets", "rar_sha256": "2f99f6a537cf2393d5e92da29d43c05c97ce2510efb9aa7a8b6ddfb12c1c5419", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

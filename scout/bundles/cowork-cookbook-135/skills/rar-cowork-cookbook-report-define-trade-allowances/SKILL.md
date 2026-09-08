---
name: "rar-cowork-cookbook-report-define-trade-allowances"
description: "Builds a read-only trade allowances summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_trade_allowances", "rar_sha256": "65d3e61e6c688f560dcd2bf2a8c4a309564372be841a983aa19c344c07b3a313", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_trade_allowances`. The original RAPP
agent is preserved byte-for-byte in `report_define_trade_allowances_agent.py` and in the RCI capsule.

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

Define trade allowances Summary Report — Builds a read-only trade allowances summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-trade-allowances
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
      "description": "Excel workbook filename, e.g. report-define-trade-allowances-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_trade_allowances_agent.py` and embedded as the fenced Python below (sha256 65d3e61e6c688f56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_trade_allowances_agent.py` first:

```bash
python3 report_define_trade_allowances_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_trade_allowances_agent.py   # or on stdin
python3 report_define_trade_allowances_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define trade allowances Summary Report — Builds a read-only trade allowances summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-trade-allowances
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_trade_allowances',
    "version": '3.0.3',
    "display_name": 'Define trade allowances Summary Report',
    "description": 'Builds a read-only trade allowances summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-trade-allowances',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-trade-allowances',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '47be7ed39674ee89',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/define-trade-allowances'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-define-trade-allowances', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-define-trade-allowances-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define trade allowances stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define trade allowances for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-trade-allowances-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define trade allowances records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only trade allowances summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a trade allowances summary report for USMF for the latest posted period as an Excel workbook with a top 10 sheet.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook filename, e.g. report-define-trade-allowances-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of define trade allowances activity in D365 F&SCM with totals, dimension breakdowns, and top-10 by value as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineTradeAllowances(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineTradeAllowances'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-define-trade-allowances-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDefineTradeAllowances().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-define-trade-allowances"
description: "Builds a read-only trade allowances summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_trade_allowances", "rar_sha256": "65d3e61e6c688f560dcd2bf2a8c4a309564372be841a983aa19c344c07b3a313", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-report-pay-taxes"
description: "Builds a read-only pay taxes summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_pay_taxes", "rar_sha256": "233cb48c67c1cac5fd0a719d8139de0a2efe23e66113f2355d1f06ef254cfef8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_pay_taxes`. The original RAPP
agent is preserved byte-for-byte in `report_pay_taxes_agent.py` and in the RCI capsule.

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

Pay taxes Summary Report — Builds a read-only pay taxes summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-pay-taxes
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
      "description": "Name of the Excel workbook to produce, e.g. report-pay-taxes-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_pay_taxes_agent.py` and embedded as the fenced Python below (sha256 233cb48c67c1cac5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_pay_taxes_agent.py` first:

```bash
python3 report_pay_taxes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_pay_taxes_agent.py   # or on stdin
python3 report_pay_taxes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Pay taxes Summary Report — Builds a read-only pay taxes summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-pay-taxes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_pay_taxes',
    "version": '3.0.3',
    "display_name": 'Pay taxes Summary Report',
    "description": 'Builds a read-only pay taxes summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-pay-taxes',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-pay-taxes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a2b5ebeb5c0f9ed1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/pay-taxes'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-pay-taxes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-pay-taxes-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where pay taxes stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of pay taxes for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-pay-taxes-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads pay taxes records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only pay taxes summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a pay taxes summary report for USMF's latest posted period as an Excel workbook with Summary, Detail, and Top10 sheets.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-pay-taxes-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write pay taxes summary for a D365 legal entity, with totals, by-dimension breakdowns, and a Top 10 by value list in Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportPayTaxes(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPayTaxes'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-pay-taxes-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportPayTaxes().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-pay-taxes"
description: "Builds a read-only pay taxes summary report from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_pay_taxes", "rar_sha256": "233cb48c67c1cac5fd0a719d8139de0a2efe23e66113f2355d1f06ef254cfef8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

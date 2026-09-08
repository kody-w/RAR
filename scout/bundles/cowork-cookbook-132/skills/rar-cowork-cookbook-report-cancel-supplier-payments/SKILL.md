---
name: "rar-cowork-cookbook-report-cancel-supplier-payments"
description: "Builds a read-only summary report of cancel supplier payments from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_cancel_supplier_payments", "rar_sha256": "08f16b50e789c4577a309089f5751da83cc492efac45e8310172a2db2babd894", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_cancel_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `report_cancel_supplier_payments_agent.py` and in the RCI capsule.

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

Cancel supplier payments Summary Report — Builds a read-only summary report of cancel supplier payments from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-cancel-supplier-payments
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
      "description": "Name of the Excel workbook to produce, e.g. report-cancel-supplier-payments-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_cancel_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 08f16b50e789c457…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_cancel_supplier_payments_agent.py` first:

```bash
python3 report_cancel_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_cancel_supplier_payments_agent.py   # or on stdin
python3 report_cancel_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cancel supplier payments Summary Report — Builds a read-only summary report of cancel supplier payments from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-cancel-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_cancel_supplier_payments',
    "version": '3.0.3',
    "display_name": 'Cancel supplier payments Summary Report',
    "description": 'Builds a read-only summary report of cancel supplier payments from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-cancel-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-cancel-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31ef394803a13ac9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/cancel-supplier-payments'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-cancel-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-cancel-supplier-payments-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where cancel supplier payments stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of cancel supplier payments for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-cancel-supplier-payments-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads cancel supplier payments records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of cancel supplier payments from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a cancel supplier payments summary report for USMF with top 10 by value as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-cancel-supplier-payments-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, breakdown, and top-10-by-value summary of cancel supplier payments activity from D365 ERP as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportCancelSupplierPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCancelSupplierPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-cancel-supplier-payments-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportCancelSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

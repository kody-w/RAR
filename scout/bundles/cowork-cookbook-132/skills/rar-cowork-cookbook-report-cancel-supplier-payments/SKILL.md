---
name: "rar-cowork-cookbook-report-cancel-supplier-payments"
description: "Builds a read-only summary report of cancel supplier payments from Dynamics 365 F&SCM for a given legal entity and posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_cancel_supplier_payments", "rar_sha256": "08f16b50e789c4577a309089f5751da83cc492efac45e8310172a2db2babd894", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

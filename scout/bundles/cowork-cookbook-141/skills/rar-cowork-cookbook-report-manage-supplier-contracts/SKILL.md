---
name: "rar-cowork-cookbook-report-manage-supplier-contracts"
description: "Builds a read-only supplier contract summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_supplier_contracts", "rar_sha256": "8c25a38ef92095e5a1876d91345a06f95112f56c18308aa90f1e3bf65f4aedfa", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_supplier_contracts`. The original RAPP
agent is preserved byte-for-byte in `report_manage_supplier_contracts_agent.py` and in the RCI capsule.

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

Manage supplier contracts Summary Report — Builds a read-only supplier contract summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-supplier-contracts
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
      "description": "Dimensions to break down by, such as department, category, or responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-supplier-contracts-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_supplier_contracts_agent.py` and embedded as the fenced Python below (sha256 8c25a38ef92095e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_supplier_contracts_agent.py` first:

```bash
python3 report_manage_supplier_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_supplier_contracts_agent.py   # or on stdin
python3 report_manage_supplier_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier contracts Summary Report — Builds a read-only supplier contract summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-supplier-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_supplier_contracts',
    "version": '3.0.3',
    "display_name": 'Manage supplier contracts Summary Report',
    "description": 'Builds a read-only supplier contract summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-supplier-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-supplier-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5682b5e1d87f4d3c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-contracts'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-manage-supplier-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-supplier-contracts-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage supplier contracts stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage supplier contracts for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-supplier-contracts-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage supplier contracts records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only supplier contract summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a supplier contract summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions to break down by, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-supplier-contracts-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a supplier contract activity summary from D365 ERP with totals, dimension breakdowns, and a top-10-by-value list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageSupplierContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageSupplierContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-supplier-contracts-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageSupplierContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

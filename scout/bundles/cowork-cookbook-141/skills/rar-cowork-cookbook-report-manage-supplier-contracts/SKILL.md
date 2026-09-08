---
name: "rar-cowork-cookbook-report-manage-supplier-contracts"
description: "Builds a read-only supplier contract summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_supplier_contracts", "rar_sha256": "8c25a38ef92095e5a1876d91345a06f95112f56c18308aa90f1e3bf65f4aedfa", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-report-document-warehouse-policies"
description: "Builds a read-only summary report of document warehouse policies from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_document_warehouse_policies", "rar_sha256": "91a88f7e753702b0ae28c154397335a83d2030cda2f455dfcc501d38940993d0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_document_warehouse_policies`. The original RAPP
agent is preserved byte-for-byte in `report_document_warehouse_policies_agent.py` and in the RCI capsule.

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

Document warehouse policies Summary Report — Builds a read-only summary report of document warehouse policies from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-document-warehouse-policies
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
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-document-warehouse-policies-2026-05-24.xlsx.",
      "type": "string"
    },
    "posted_period": {
      "description": "The posted period to summarize; defaults to the most recent available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_document_warehouse_policies_agent.py` and embedded as the fenced Python below (sha256 91a88f7e753702b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_document_warehouse_policies_agent.py` first:

```bash
python3 report_document_warehouse_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_document_warehouse_policies_agent.py   # or on stdin
python3 report_document_warehouse_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Document warehouse policies Summary Report — Builds a read-only summary report of document warehouse policies from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-document-warehouse-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_document_warehouse_policies',
    "version": '3.0.3',
    "display_name": 'Document warehouse policies Summary Report',
    "description": 'Builds a read-only summary report of document warehouse policies from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-document-warehouse-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-document-warehouse-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '285ff197a052b9c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/document-warehouse-policies'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-document-warehouse-policies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-document-warehouse-policies-2026-05-24.xlsx.', 'posted_period': 'The posted period to summarize; defaults to the most recent available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where document warehouse policies stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of document warehouse policies for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-document-warehouse-policies-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads document warehouse policies records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of document warehouse policies from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a document warehouse policies summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The posted period to summarize; defaults to the most recent available in the tenant.', 'name': 'posted_period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-document-warehouse-policies-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write Excel summary of document warehouse policies activity from D365 ERP, with totals, dimension breakdowns, and a Top 10 by value.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDocumentWarehousePolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDocumentWarehousePolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-document-warehouse-policies-2026-05-24.xlsx.', 'type': 'string'}, 'posted_period': {'description': 'The posted period to summarize; defaults to the most recent available in the tenant.', 'type': 'string'}},
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
    print(ReportDocumentWarehousePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

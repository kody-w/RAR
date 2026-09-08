---
name: "rar-cowork-cookbook-report-document-warehouse-policies"
description: "Builds a read-only summary report of document warehouse policies from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_document_warehouse_policies", "rar_sha256": "91a88f7e753702b0ae28c154397335a83d2030cda2f455dfcc501d38940993d0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

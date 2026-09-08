---
name: "rar-cowork-cookbook-report-allocate-service-parts-inventory"
description: "Builds a read-only summary report of allocate service parts inventory from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_allocate_service_parts_inventory", "rar_sha256": "702c1c37103fbd8e9200dcb84c3295304a72d96cd986f62a300a6daef788b902", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_allocate_service_parts_inventory`. The original RAPP
agent is preserved byte-for-byte in `report_allocate_service_parts_inventory_agent.py` and in the RCI capsule.

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

Allocate service parts inventory Summary Report — Builds a read-only summary report of allocate service parts inventory from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-allocate-service-parts-inventory
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
      "description": "Name of the Excel workbook to produce, e.g. report-allocate-service-parts-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_allocate_service_parts_inventory_agent.py` and embedded as the fenced Python below (sha256 702c1c37103fbd8e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_allocate_service_parts_inventory_agent.py` first:

```bash
python3 report_allocate_service_parts_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_allocate_service_parts_inventory_agent.py   # or on stdin
python3 report_allocate_service_parts_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate service parts inventory Summary Report — Builds a read-only summary report of allocate service parts inventory from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-allocate-service-parts-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_allocate_service_parts_inventory',
    "version": '3.0.3',
    "display_name": 'Allocate service parts inventory Summary Report',
    "description": 'Builds a read-only summary report of allocate service parts inventory from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-allocate-service-parts-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-allocate-service-parts-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5b2b9057ea51908f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/allocate-service-parts-inventory'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-allocate-service-parts-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-allocate-service-parts-inventory-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where allocate service parts inventory stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of allocate service parts inventory for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-allocate-service-parts-inventory-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads allocate service parts inventory records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of allocate service parts inventory from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build an allocate service parts inventory summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-allocate-service-parts-inventory-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, by-dimension breakdown, and Top 10 by value report of allocate service parts inventory activity from D365 ERP, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportAllocateServicePartsInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAllocateServicePartsInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-allocate-service-parts-inventory-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportAllocateServicePartsInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

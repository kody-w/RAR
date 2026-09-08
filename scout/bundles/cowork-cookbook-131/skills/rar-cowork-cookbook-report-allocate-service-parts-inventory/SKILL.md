---
name: "rar-cowork-cookbook-report-allocate-service-parts-inventory"
description: "Builds a read-only summary report of allocate service parts inventory from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_allocate_service_parts_inventory", "rar_sha256": "702c1c37103fbd8e9200dcb84c3295304a72d96cd986f62a300a6daef788b902", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

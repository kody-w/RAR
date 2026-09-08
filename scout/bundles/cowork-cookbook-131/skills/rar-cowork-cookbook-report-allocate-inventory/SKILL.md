---
name: "rar-cowork-cookbook-report-allocate-inventory"
description: "Builds a read-only allocate inventory summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_allocate_inventory", "rar_sha256": "70015336d1ae19e195dbd7d966918c86b786a1536a7dc77211faf81bb0e927cc", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_allocate_inventory`. The original RAPP
agent is preserved byte-for-byte in `report_allocate_inventory_agent.py` and in the RCI capsule.

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

Allocate inventory Summary Report — Builds a read-only allocate inventory summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-allocate-inventory
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
      "description": "Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-allocate-inventory-2026-05-24.xlsx.",
      "type": "string"
    },
    "posted_period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_allocate_inventory_agent.py` and embedded as the fenced Python below (sha256 70015336d1ae19e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_allocate_inventory_agent.py` first:

```bash
python3 report_allocate_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_allocate_inventory_agent.py   # or on stdin
python3 report_allocate_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate inventory Summary Report — Builds a read-only allocate inventory summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-allocate-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_allocate_inventory',
    "version": '3.0.3',
    "display_name": 'Allocate inventory Summary Report',
    "description": 'Builds a read-only allocate inventory summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-allocate-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-allocate-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a740e02d0c538647',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/allocate-inventory'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-allocate-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-allocate-inventory-2026-05-24.xlsx.', 'posted_period': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where allocate inventory stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of allocate inventory for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-allocate-inventory-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads allocate inventory records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only allocate inventory summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build an allocate inventory summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'name': 'posted_period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-allocate-inventory-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of allocate inventory activity with totals, by-dimension breakdowns, and a Top 10 by value list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportAllocateInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAllocateInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-allocate-inventory-2026-05-24.xlsx.', 'type': 'string'}, 'posted_period': {'description': 'Posted period to summarize; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportAllocateInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

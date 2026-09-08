---
name: "rar-cowork-cookbook-report-report-on-inventory-quality"
description: "Builds a read-only inventory quality summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_on_inventory_quality", "rar_sha256": "42efb89d2cb8ce6003d927e8e3b443568638b471753de51a9682a6b3477e665e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_report_on_inventory_quality`. The original RAPP
agent is preserved byte-for-byte in `report_report_on_inventory_quality_agent.py` and in the RCI capsule.

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

Report on inventory quality Summary Report — Builds a read-only inventory quality summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-report-on-inventory-quality
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
      "description": "Name of the Excel workbook to produce, e.g. report-report-on-inventory-quality-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_report_on_inventory_quality_agent.py` and embedded as the fenced Python below (sha256 42efb89d2cb8ce60…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_report_on_inventory_quality_agent.py` first:

```bash
python3 report_report_on_inventory_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_report_on_inventory_quality_agent.py   # or on stdin
python3 report_report_on_inventory_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on inventory quality Summary Report — Builds a read-only inventory quality summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-report-on-inventory-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_report_on_inventory_quality',
    "version": '3.0.3',
    "display_name": 'Report on inventory quality Summary Report',
    "description": 'Builds a read-only inventory quality summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-report-on-inventory-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-report-on-inventory-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f6fad5073fcd82d7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/report-on-inventory-quality'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-report-on-inventory-quality', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-report-on-inventory-quality-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where report on inventory quality stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of report on inventory quality for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-report-on-inventory-quality-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads report on inventory quality records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only inventory quality summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build an inventory quality summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-report-on-inventory-quality-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write inventory quality summary from D365 ERP with totals, dimension breakdowns, and a Top 10 by value list as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportReportOnInventoryQuality(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReportOnInventoryQuality'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-report-on-inventory-quality-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportReportOnInventoryQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

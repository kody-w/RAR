---
name: "rar-cowork-cookbook-report-report-on-inventory-quality"
description: "Builds a read-only inventory quality summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_on_inventory_quality", "rar_sha256": "42efb89d2cb8ce6003d927e8e3b443568638b471753de51a9682a6b3477e665e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

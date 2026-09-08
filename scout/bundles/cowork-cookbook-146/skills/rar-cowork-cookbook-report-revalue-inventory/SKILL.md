---
name: "rar-cowork-cookbook-report-revalue-inventory"
description: "Builds a read-only inventory revaluation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_revalue_inventory", "rar_sha256": "742c9c2c751857c054907e119a8f58570825dce4b2f04d6434be9877be6aacbe", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_revalue_inventory`. The original RAPP
agent is preserved byte-for-byte in `report_revalue_inventory_agent.py` and in the RCI capsule.

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

Revalue inventory Summary Report — Builds a read-only inventory revaluation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-revalue-inventory
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
      "description": "Dimensions to break totals out by, such as department, category, or responsible owner, where applicable.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-revalue-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_revalue_inventory_agent.py` and embedded as the fenced Python below (sha256 742c9c2c751857c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_revalue_inventory_agent.py` first:

```bash
python3 report_revalue_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_revalue_inventory_agent.py   # or on stdin
python3 report_revalue_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue inventory Summary Report — Builds a read-only inventory revaluation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-revalue-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_revalue_inventory',
    "version": '3.0.3',
    "display_name": 'Revalue inventory Summary Report',
    "description": 'Builds a read-only inventory revaluation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-revalue-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-revalue-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '41417110dbf7ea60',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/revalue-inventory'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-revalue-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break totals out by, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-revalue-inventory-2026-05-24.xlsx.', 'posted_period': 'The posted period to summarize; defaults to the most recent available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where revalue inventory stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of revalue inventory for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-revalue-inventory-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads revalue inventory records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only inventory revaluation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a revalue inventory summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'The posted period to summarize; defaults to the most recent available in the tenant.', 'name': 'posted_period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-revalue-inventory-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break totals out by, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of revalue inventory activity from D365 ERP, with totals, dimension breakdowns, and a top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportRevalueInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRevalueInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break totals out by, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-revalue-inventory-2026-05-24.xlsx.', 'type': 'string'}, 'posted_period': {'description': 'The posted period to summarize; defaults to the most recent available in the tenant.', 'type': 'string'}},
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
    print(ReportRevalueInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

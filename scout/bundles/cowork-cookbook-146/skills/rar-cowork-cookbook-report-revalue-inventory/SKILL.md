---
name: "rar-cowork-cookbook-report-revalue-inventory"
description: "Builds a read-only inventory revaluation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, producing an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_revalue_inventory", "rar_sha256": "742c9c2c751857c054907e119a8f58570825dce4b2f04d6434be9877be6aacbe", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

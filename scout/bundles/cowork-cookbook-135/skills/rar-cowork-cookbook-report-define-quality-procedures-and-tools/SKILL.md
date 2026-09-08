---
name: "rar-cowork-cookbook-report-define-quality-procedures-and-tools"
description: "Builds a read-only summary report of define quality procedures and tools activity from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_quality_procedures_and_tools", "rar_sha256": "099bdc6d7feb1436358cfc6ef4cb87c05ab361f3c6be4e17ffe5b41c51727f4c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_quality_procedures_and_tools`. The original RAPP
agent is preserved byte-for-byte in `report_define_quality_procedures_and_tools_agent.py` and in the RCI capsule.

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

Define quality procedures and tools Summary Report — Builds a read-only summary report of define quality procedures and tools activity from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-quality-procedures-and-tools
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
      "description": "Name of the Excel workbook to produce, e.g. report-define-quality-procedures-and-tools-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_quality_procedures_and_tools_agent.py` and embedded as the fenced Python below (sha256 099bdc6d7feb1436…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_quality_procedures_and_tools_agent.py` first:

```bash
python3 report_define_quality_procedures_and_tools_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_quality_procedures_and_tools_agent.py   # or on stdin
python3 report_define_quality_procedures_and_tools_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define quality procedures and tools Summary Report — Builds a read-only summary report of define quality procedures and tools activity from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-quality-procedures-and-tools
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_quality_procedures_and_tools',
    "version": '3.0.3',
    "display_name": 'Define quality procedures and tools Summary Report',
    "description": 'Builds a read-only summary report of define quality procedures and tools activity from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-define-quality-procedures-and-tools',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-quality-procedures-and-tools',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0202ccfbb914b21e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/define-quality-procedures-and-tools'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-define-quality-procedures-and-tools', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-define-quality-procedures-and-tools-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define quality procedures and tools stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define quality procedures and tools for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-quality-procedures-and-tools-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define quality procedures and tools records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of define quality procedures and tools activity from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a quality procedures and tools summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-define-quality-procedures-and-tools-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of define quality procedures and tools from D365 ERP data, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineQualityProceduresAndTools(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineQualityProceduresAndTools'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-define-quality-procedures-and-tools-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDefineQualityProceduresAndTools().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

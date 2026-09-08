---
name: "rar-cowork-cookbook-report-define-quality-procedures-and-tools"
description: "Builds a read-only summary report of define quality procedures and tools activity from Dynamics 365 F&SCM for a given legal entity and posted period, exporting an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_quality_procedures_and_tools", "rar_sha256": "099bdc6d7feb1436358cfc6ef4cb87c05ab361f3c6be4e17ffe5b41c51727f4c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

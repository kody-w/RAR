---
name: "rar-cowork-cookbook-report-manage-the-recurring-synchronization-of-data"
description: "Builds a read-only Excel summary report of recurring data synchronization activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_the_recurring_synchronization_of_data", "rar_sha256": "5ccf883eb549a1aca0e1f91fc1266ace8728061e037de6d7e73e626950f30299", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_the_recurring_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `report_manage_the_recurring_synchronization_of_data_agent.py` and in the RCI capsule.

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

Manage the recurring synchronization of data Summary Report — Builds a read-only Excel summary report of recurring data synchronization activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-the-recurring-synchronization-of-data
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-the-recurring-synchronization-of-data-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_the_recurring_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 5ccf883eb549a1ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_the_recurring_synchronization_of_data_agent.py` first:

```bash
python3 report_manage_the_recurring_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_the_recurring_synchronization_of_data_agent.py   # or on stdin
python3 report_manage_the_recurring_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the recurring synchronization of data Summary Report — Builds a read-only Excel summary report of recurring data synchronization activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-the-recurring-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_the_recurring_synchronization_of_data',
    "version": '3.0.3',
    "display_name": 'Manage the recurring synchronization of data Summary Report',
    "description": "Builds a read-only Excel summary report of recurring data synchronization activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, with Summary, Detail, and Top10 sheets.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-the-recurring-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-the-recurring-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b4ac1f6946419a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-recurring-synchronization-of-data'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-manage-the-recurring-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-the-recurring-synchronization-of-data-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage the recurring synchronization of data stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage the recurring synchronization of data for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-the-recurring-synchronization-of-data-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage the recurring synchronization of data records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only Excel summary report of recurring data synchronization activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, with Summary, Detail, and Top10 sheets.", 'example_request': "Build a recurring data sync summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-the-recurring-synchronization-of-data-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of recurring data synchronization activity from D365 ERP exported as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageTheRecurringSynchronizationOfData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageTheRecurringSynchronizationOfData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-the-recurring-synchronization-of-data-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageTheRecurringSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-schedule-frontline-workers"
description: "Builds a read-only schedule frontline workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_schedule_frontline_workers", "rar_sha256": "852f206be110820cfe6e14ed9cc66f1a11c31873fadeb462bedd7a4601496679", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_schedule_frontline_workers`. The original RAPP
agent is preserved byte-for-byte in `report_schedule_frontline_workers_agent.py` and in the RCI capsule.

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

Schedule frontline workers Summary Report — Builds a read-only schedule frontline workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-frontline-workers
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
      "description": "Dimensions to break down by where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Excel workbook to generate, e.g. report-schedule-frontline-workers-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_schedule_frontline_workers_agent.py` and embedded as the fenced Python below (sha256 852f206be110820c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_schedule_frontline_workers_agent.py` first:

```bash
python3 report_schedule_frontline_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_schedule_frontline_workers_agent.py   # or on stdin
python3 report_schedule_frontline_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule frontline workers Summary Report — Builds a read-only schedule frontline workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-frontline-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_schedule_frontline_workers',
    "version": '3.0.3',
    "display_name": 'Schedule frontline workers Summary Report',
    "description": 'Builds a read-only schedule frontline workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-schedule-frontline-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-schedule-frontline-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '91898da0b306aac9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/schedule-frontline-workers'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-schedule-frontline-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to generate, e.g. report-schedule-frontline-workers-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where schedule frontline workers stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of schedule frontline workers for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-schedule-frontline-workers-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads schedule frontline workers records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only schedule frontline workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a schedule frontline workers summary report for USMF from the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to generate, e.g. report-schedule-frontline-workers-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of frontline worker scheduling activity from D365 ERP, with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportScheduleFrontlineWorkers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportScheduleFrontlineWorkers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to generate, e.g. report-schedule-frontline-workers-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportScheduleFrontlineWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

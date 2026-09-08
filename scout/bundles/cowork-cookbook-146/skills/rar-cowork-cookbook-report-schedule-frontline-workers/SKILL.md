---
name: "rar-cowork-cookbook-report-schedule-frontline-workers"
description: "Builds a read-only schedule frontline workers summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_schedule_frontline_workers", "rar_sha256": "852f206be110820cfe6e14ed9cc66f1a11c31873fadeb462bedd7a4601496679", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

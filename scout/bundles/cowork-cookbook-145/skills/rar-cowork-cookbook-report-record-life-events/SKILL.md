---
name: "rar-cowork-cookbook-report-record-life-events"
description: "Builds a read-only summary report of record life events from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_life_events", "rar_sha256": "cede434df245acebf18e1eb25b65ec82d09dd7149fe4a745324cc07deff55ea8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_record_life_events`. The original RAPP
agent is preserved byte-for-byte in `report_record_life_events_agent.py` and in the RCI capsule.

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

Record life events Summary Report — Builds a read-only summary report of record life events from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-record-life-events
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
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-record-life-events-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_record_life_events_agent.py` and embedded as the fenced Python below (sha256 cede434df245aceb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_record_life_events_agent.py` first:

```bash
python3 report_record_life_events_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_record_life_events_agent.py   # or on stdin
python3 report_record_life_events_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record life events Summary Report — Builds a read-only summary report of record life events from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-record-life-events
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_record_life_events',
    "version": '3.0.3',
    "display_name": 'Record life events Summary Report',
    "description": 'Builds a read-only summary report of record life events from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-record-life-events',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-record-life-events',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8de7df3431f41f99',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/record-life-events'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-record-life-events', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-record-life-events-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where record life events stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of record life events for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-record-life-events-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads record life events records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of record life events from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': "Build a record life events summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-record-life-events-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a record life events summary report from D365 ERP with totals, dimension breakdowns, and a top-10-by-value list, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportRecordLifeEvents(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRecordLifeEvents'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-record-life-events-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportRecordLifeEvents().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

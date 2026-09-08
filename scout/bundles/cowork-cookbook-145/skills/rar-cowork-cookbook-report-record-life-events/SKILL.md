---
name: "rar-cowork-cookbook-report-record-life-events"
description: "Builds a read-only summary report of record life events from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_life_events", "rar_sha256": "cede434df245acebf18e1eb25b65ec82d09dd7149fe4a745324cc07deff55ea8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

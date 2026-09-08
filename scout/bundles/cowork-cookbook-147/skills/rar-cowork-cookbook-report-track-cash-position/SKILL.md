---
name: "rar-cowork-cookbook-report-track-cash-position"
description: "Builds a read-only cash position summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_cash_position", "rar_sha256": "04efc5e1a8d6ac143ca8abb71d1cb28cf94190bca541824713655cb399b4f85d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_track_cash_position`. The original RAPP
agent is preserved byte-for-byte in `report_track_cash_position_agent.py` and in the RCI capsule.

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

Track cash position Summary Report — Builds a read-only cash position summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-track-cash-position
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
      "description": "Name of the Excel workbook to produce, e.g. report-track-cash-position-2026-05-24.xlsx.",
      "type": "string"
    },
    "posting_period": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_track_cash_position_agent.py` and embedded as the fenced Python below (sha256 04efc5e1a8d6ac14…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_track_cash_position_agent.py` first:

```bash
python3 report_track_cash_position_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_track_cash_position_agent.py   # or on stdin
python3 report_track_cash_position_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track cash position Summary Report — Builds a read-only cash position summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-track-cash-position
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_track_cash_position',
    "version": '3.0.3',
    "display_name": 'Track cash position Summary Report',
    "description": 'Builds a read-only cash position summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-track-cash-position',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-track-cash-position',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '478259cebf6ddbfd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/track-cash-position'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-track-cash-position', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-track-cash-position-2026-05-24.xlsx.', 'posting_period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where track cash position stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of track cash position for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-track-cash-position-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads track cash position records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only cash position summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a cash position summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'posting_period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-track-cash-position-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a cash position summary report with totals, dimension breakdowns, and top 10 by value exported to Excel from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportTrackCashPosition(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTrackCashPosition'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-track-cash-position-2026-05-24.xlsx.', 'type': 'string'}, 'posting_period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportTrackCashPosition().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

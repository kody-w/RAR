---
name: "rar-cowork-cookbook-report-track-cash-position"
description: "Builds a read-only cash position summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_cash_position", "rar_sha256": "04efc5e1a8d6ac143ca8abb71d1cb28cf94190bca541824713655cb399b4f85d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

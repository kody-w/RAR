---
name: "rar-cowork-cookbook-report-track-project-fees"
description: "Builds a read-only summary report of track project fees from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_project_fees", "rar_sha256": "965935fb3f96d3b4488fa85ddef96a67ac81ce4870e398fbfd8f7da60b0f2261", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_track_project_fees`. The original RAPP
agent is preserved byte-for-byte in `report_track_project_fees_agent.py` and in the RCI capsule.

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

Track project fees Summary Report — Builds a read-only summary report of track project fees from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-track-project-fees
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
      "description": "Dimensions to break down by where applicable, e.g. department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-track-project-fees-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_track_project_fees_agent.py` and embedded as the fenced Python below (sha256 965935fb3f96d3b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_track_project_fees_agent.py` first:

```bash
python3 report_track_project_fees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_track_project_fees_agent.py   # or on stdin
python3 report_track_project_fees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track project fees Summary Report — Builds a read-only summary report of track project fees from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-track-project-fees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_track_project_fees',
    "version": '3.0.3',
    "display_name": 'Track project fees Summary Report',
    "description": 'Builds a read-only summary report of track project fees from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-track-project-fees',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-track-project-fees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '43c0f49d0f581df5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/track-project-fees'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-track-project-fees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-track-project-fees-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where track project fees stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of track project fees for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-track-project-fees-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads track project fees records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of track project fees from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a track project fees summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions to break down by where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-track-project-fees-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/breakdown/top-10 report of track project fees from D365 ERP data, without modifying any records.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportTrackProjectFees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTrackProjectFees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-track-project-fees-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportTrackProjectFees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

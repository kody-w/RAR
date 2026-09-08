---
name: "rar-cowork-cookbook-report-re-assign-case-to-another-team-individual"
description: "Builds a read-only Excel summary report of case re-assignment activity from Dynamics 365 F&SCM via the Cowork ERP plugin, with Summary, Detail, and Top 10 by value sheets for a given legal entity and posted period."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_re_assign_case_to_another_team_individual", "rar_sha256": "80adcc241b1d6c9634ec3c6d2d0b1d2b85dcf8ceb6cbaa9b6e4e6f954ce6902d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_re_assign_case_to_another_team_individual`. The original RAPP
agent is preserved byte-for-byte in `report_re_assign_case_to_another_team_individual_agent.py` and in the RCI capsule.

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

Re-assign case to another team/individual Summary Report — Builds a read-only Excel summary report of case re-assignment activity from Dynamics 365 F&SCM via the Cowork ERP plugin, with Summary, Detail, and Top 10 by value sheets for a given legal entity and posted period.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-re-assign-case-to-another-team-individual
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
      "description": "D365 legal entity to report against (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-re-assign-case-to-another-team-individual-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_re_assign_case_to_another_team_individual_agent.py` and embedded as the fenced Python below (sha256 80adcc241b1d6c96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_re_assign_case_to_another_team_individual_agent.py` first:

```bash
python3 report_re_assign_case_to_another_team_individual_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_re_assign_case_to_another_team_individual_agent.py   # or on stdin
python3 report_re_assign_case_to_another_team_individual_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Re-assign case to another team/individual Summary Report — Builds a read-only Excel summary report of case re-assignment activity from Dynamics 365 F&SCM via the Cowork ERP plugin, with Summary, Detail, and Top 10 by value sheets for a given legal entity and posted period.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-re-assign-case-to-another-team-individual
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_re_assign_case_to_another_team_individual',
    "version": '3.0.3',
    "display_name": 'Re-assign case to another team/individual Summary Report',
    "description": 'Builds a read-only Excel summary report of case re-assignment activity from Dynamics 365 F&SCM via the Cowork ERP plugin, with Summary, Detail, and Top 10 by value sheets for a given legal entity and posted period.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-re-assign-case-to-another-team-individual',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-re-assign-case-to-another-team-individual',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1e3120f35f10b67c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/re-assign-case-to-another-team-individual'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-re-assign-case-to-another-team-individual', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-re-assign-case-to-another-team-individual-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where re-assign case to another team/individual stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of re-assign case to another team/individual for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-re-assign-case-to-another-team-individual-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads re-assign case to another team/individual records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only Excel summary report of case re-assignment activity from Dynamics 365 F&SCM via the Cowork ERP plugin, with Summary, Detail, and Top 10 by value sheets for a given legal entity and posted period.', 'example_request': 'Build a re-assign case summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-re-assign-case-to-another-team-individual-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of re-assign-case-to-another-team/individual activity from D365 ERP data, with totals, breakdowns, and a top-10 list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportReAssignCaseToAnotherTeamIndividual(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReAssignCaseToAnotherTeamIndividual'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-re-assign-case-to-another-team-individual-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportReAssignCaseToAnotherTeamIndividual().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

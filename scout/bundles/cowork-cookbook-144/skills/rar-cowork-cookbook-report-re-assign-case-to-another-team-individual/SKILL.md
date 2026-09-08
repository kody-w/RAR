---
name: "rar-cowork-cookbook-report-re-assign-case-to-another-team-individual"
description: "Builds a read-only Excel summary report of case re-assignment activity from Dynamics 365 F&SCM via the Cowork ERP plugin, with Summary, Detail, and Top 10 by value sheets for a given legal entity and posted period."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_re_assign_case_to_another_team_individual", "rar_sha256": "80adcc241b1d6c9634ec3c6d2d0b1d2b85dcf8ceb6cbaa9b6e4e6f954ce6902d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-report-track-skills-and-competencies"
description: "Builds a read-only skills and competencies summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_skills_and_competencies", "rar_sha256": "269c5813f42e1a4f74e447afc92dc6de40fd7adc6f1dbcbdd3a759a6cb8d4282", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_track_skills_and_competencies`. The original RAPP
agent is preserved byte-for-byte in `report_track_skills_and_competencies_agent.py` and in the RCI capsule.

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

Track skills and competencies Summary Report — Builds a read-only skills and competencies summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-track-skills-and-competencies
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
      "description": "Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-track-skills-and-competencies-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_track_skills_and_competencies_agent.py` and embedded as the fenced Python below (sha256 269c5813f42e1a4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_track_skills_and_competencies_agent.py` first:

```bash
python3 report_track_skills_and_competencies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_track_skills_and_competencies_agent.py   # or on stdin
python3 report_track_skills_and_competencies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track skills and competencies Summary Report — Builds a read-only skills and competencies summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-track-skills-and-competencies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_track_skills_and_competencies',
    "version": '3.0.3',
    "display_name": 'Track skills and competencies Summary Report',
    "description": 'Builds a read-only skills and competencies summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-track-skills-and-competencies',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-track-skills-and-competencies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9240700c6425078f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/track-skills-and-competencies'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-track-skills-and-competencies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-track-skills-and-competencies-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where track skills and competencies stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of track skills and competencies for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-track-skills-and-competencies-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads track skills and competencies records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only skills and competencies summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a skills and competencies summary report for USMF from the latest posted period as an Excel file with a Top 10 sheet.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-track-skills-and-competencies-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary report of tracked skills and competencies with totals, dimension breakdowns, and a top-10 list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportTrackSkillsAndCompetencies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTrackSkillsAndCompetencies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-track-skills-and-competencies-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportTrackSkillsAndCompetencies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-track-skills-and-competencies"
description: "Builds a read-only skills and competencies summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_skills_and_competencies", "rar_sha256": "269c5813f42e1a4f74e447afc92dc6de40fd7adc6f1dbcbdd3a759a6cb8d4282", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

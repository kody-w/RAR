---
name: "rar-cowork-cookbook-report-govern-projects"
description: "Builds a read-only summary report of govern projects from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_govern_projects", "rar_sha256": "89de3e553fe05f46b74057e3d3312014dbc1417b346e66500bd103ed8b81b928", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_govern_projects`. The original RAPP
agent is preserved byte-for-byte in `report_govern_projects_agent.py` and in the RCI capsule.

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

Govern projects Summary Report — Builds a read-only summary report of govern projects from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-govern-projects
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
      "description": "Excel workbook filename, e.g. report-govern-projects-2026-05-24.xlsx.",
      "type": "string"
    },
    "posted_period": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_govern_projects_agent.py` and embedded as the fenced Python below (sha256 89de3e553fe05f46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_govern_projects_agent.py` first:

```bash
python3 report_govern_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_govern_projects_agent.py   # or on stdin
python3 report_govern_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Govern projects Summary Report — Builds a read-only summary report of govern projects from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-govern-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_govern_projects',
    "version": '3.0.3',
    "display_name": 'Govern projects Summary Report',
    "description": 'Builds a read-only summary report of govern projects from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-govern-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-govern-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a31e7bc334f90655',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/govern-projects'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-govern-projects', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-govern-projects-2026-05-24.xlsx.', 'posted_period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where govern projects stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of govern projects for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-govern-projects-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads govern projects records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of govern projects from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': "Build a govern projects summary report for USMF's latest posted period as an Excel workbook with Summary, Detail, and Top10 sheets.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'posted_period'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook filename, e.g. report-govern-projects-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write govern projects summary from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportGovernProjects(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportGovernProjects'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-govern-projects-2026-05-24.xlsx.', 'type': 'string'}, 'posted_period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportGovernProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

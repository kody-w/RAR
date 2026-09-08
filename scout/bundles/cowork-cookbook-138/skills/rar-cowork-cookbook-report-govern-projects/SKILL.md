---
name: "rar-cowork-cookbook-report-govern-projects"
description: "Builds a read-only summary report of govern projects from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_govern_projects", "rar_sha256": "89de3e553fe05f46b74057e3d3312014dbc1417b346e66500bd103ed8b81b928", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

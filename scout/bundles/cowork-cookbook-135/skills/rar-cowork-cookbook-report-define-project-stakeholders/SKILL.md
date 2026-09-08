---
name: "rar-cowork-cookbook-report-define-project-stakeholders"
description: "Builds a read-only summary report of define project stakeholders activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_project_stakeholders", "rar_sha256": "a3e22d961139f4e8cf983a32fac117afd5550d1685a782e2031f00ccbf696c98", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_project_stakeholders`. The original RAPP
agent is preserved byte-for-byte in `report_define_project_stakeholders_agent.py` and in the RCI capsule.

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

Define project stakeholders Summary Report — Builds a read-only summary report of define project stakeholders activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-project-stakeholders
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-define-project-stakeholders-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_project_stakeholders_agent.py` and embedded as the fenced Python below (sha256 a3e22d961139f4e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_project_stakeholders_agent.py` first:

```bash
python3 report_define_project_stakeholders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_project_stakeholders_agent.py   # or on stdin
python3 report_define_project_stakeholders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project stakeholders Summary Report — Builds a read-only summary report of define project stakeholders activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-project-stakeholders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_project_stakeholders',
    "version": '3.0.3',
    "display_name": 'Define project stakeholders Summary Report',
    "description": 'Builds a read-only summary report of define project stakeholders activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-define-project-stakeholders',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-project-stakeholders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93bb1960c479c4f6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/define-project-stakeholders'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-define-project-stakeholders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-define-project-stakeholders-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define project stakeholders stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define project stakeholders for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-project-stakeholders-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define project stakeholders records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of define project stakeholders activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a define project stakeholders summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-define-project-stakeholders-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, breakdown, and top-10 summary report of define project stakeholders activity from D365 ERP data, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineProjectStakeholders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineProjectStakeholders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-define-project-stakeholders-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDefineProjectStakeholders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

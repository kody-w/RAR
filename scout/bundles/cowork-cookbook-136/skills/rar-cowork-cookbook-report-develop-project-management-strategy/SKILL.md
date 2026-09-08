---
name: "rar-cowork-cookbook-report-develop-project-management-strategy"
description: "Builds a read-only project management strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_project_management_strategy", "rar_sha256": "22081b6306a11a4d6f8e34c282e16d71d4d5ea258b7e7a0842eb3a30be802824", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_project_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_develop_project_management_strategy_agent.py` and in the RCI capsule.

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

Develop project management strategy Summary Report — Builds a read-only project management strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-project-management-strategy
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
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against (default USMF).",
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
      "description": "Excel workbook name, e.g. report-develop-project-management-strategy-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_project_management_strategy_agent.py` and embedded as the fenced Python below (sha256 22081b6306a11a4d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_project_management_strategy_agent.py` first:

```bash
python3 report_develop_project_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_project_management_strategy_agent.py   # or on stdin
python3 report_develop_project_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project management strategy Summary Report — Builds a read-only project management strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-project-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_project_management_strategy',
    "version": '3.0.3',
    "display_name": 'Develop project management strategy Summary Report',
    "description": 'Builds a read-only project management strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-develop-project-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-project-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07b330edd148c31f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-management-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-develop-project-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against (default USMF).', 'output_filename': 'Excel workbook name, e.g. report-develop-project-management-strategy-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop project management strategy stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop project management strategy for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-project-management-strategy-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop project management strategy records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only project management strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a develop project management strategy summary report for USMF and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook name, e.g. report-develop-project-management-strategy-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, by-dimension breakdown, and Top 10 by value report of develop project management strategy activity from D365 ERP data, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopProjectManagementStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopProjectManagementStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-develop-project-management-strategy-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDevelopProjectManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

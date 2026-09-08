---
name: "rar-cowork-cookbook-report-develop-project-management-strategy"
description: "Builds a read-only project management strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_project_management_strategy", "rar_sha256": "22081b6306a11a4d6f8e34c282e16d71d4d5ea258b7e7a0842eb3a30be802824", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

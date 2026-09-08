---
name: "rar-cowork-cookbook-report-develop-budgeting-strategy"
description: "Builds a read-only budgeting-strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_budgeting_strategy", "rar_sha256": "e3e41c5b88444db9540769a464bf4a213110f1bb7b42242a4d615b97489671f0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_budgeting_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_develop_budgeting_strategy_agent.py` and in the RCI capsule.

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

Develop budgeting strategy Summary Report — Builds a read-only budgeting-strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-budgeting-strategy
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on; the recipe uses USMF.",
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
      "description": "Excel workbook name, e.g. report-develop-budgeting-strategy-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
      "type": "string"
    },
    "period": {
      "description": "Posting period to summarize; defaults to the most recent posted period available (USMF demo data is mostly FY2017).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_budgeting_strategy_agent.py` and embedded as the fenced Python below (sha256 e3e41c5b88444db9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_budgeting_strategy_agent.py` first:

```bash
python3 report_develop_budgeting_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_budgeting_strategy_agent.py   # or on stdin
python3 report_develop_budgeting_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop budgeting strategy Summary Report — Builds a read-only budgeting-strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-budgeting-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_budgeting_strategy',
    "version": '3.0.3',
    "display_name": 'Develop budgeting strategy Summary Report',
    "description": 'Builds a read-only budgeting-strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-develop-budgeting-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-budgeting-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1148c1d57c23a189',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-budgeting-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-develop-budgeting-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on; the recipe uses USMF.', 'output_filename': 'Excel workbook name, e.g. report-develop-budgeting-strategy-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'period': 'Posting period to summarize; defaults to the most recent posted period available (USMF demo data is mostly FY2017).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop budgeting strategy stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop budgeting strategy for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-budgeting-strategy-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads develop budgeting strategy records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only budgeting-strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a budgeting strategy summary report from D365 for USMF, latest posted period, as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Posting period to summarize; defaults to the most recent posted period available (USMF demo data is mostly FY2017).', 'name': 'period'}, {'description': 'Excel workbook name, e.g. report-develop-budgeting-strategy-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-changes summary report of develop budgeting strategy activity from D365 ERP, with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopBudgetingStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopBudgetingStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-develop-budgeting-strategy-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}, 'period': {'description': 'Posting period to summarize; defaults to the most recent posted period available (USMF demo data is mostly FY2017).', 'type': 'string'}},
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
    print(ReportDevelopBudgetingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

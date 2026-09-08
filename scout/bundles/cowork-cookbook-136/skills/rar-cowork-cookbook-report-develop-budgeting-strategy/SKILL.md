---
name: "rar-cowork-cookbook-report-develop-budgeting-strategy"
description: "Builds a read-only budgeting-strategy summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_budgeting_strategy", "rar_sha256": "e3e41c5b88444db9540769a464bf4a213110f1bb7b42242a4d615b97489671f0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

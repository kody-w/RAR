---
name: "rar-cowork-cookbook-report-prepare-financial-statements"
description: "Builds a read-only summary report of prepare-financial-statements activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_prepare_financial_statements", "rar_sha256": "dbde340643f509268cab70380affdf4f58fa4c24dc39b120480fae7b8ea3e6ba", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_prepare_financial_statements`. The original RAPP
agent is preserved byte-for-byte in `report_prepare_financial_statements_agent.py` and in the RCI capsule.

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

Prepare financial statements Summary Report — Builds a read-only summary report of prepare-financial-statements activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-prepare-financial-statements
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
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Excel workbook filename, e.g. report-prepare-financial-statements-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_prepare_financial_statements_agent.py` and embedded as the fenced Python below (sha256 dbde340643f50926…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_prepare_financial_statements_agent.py` first:

```bash
python3 report_prepare_financial_statements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_prepare_financial_statements_agent.py   # or on stdin
python3 report_prepare_financial_statements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare financial statements Summary Report — Builds a read-only summary report of prepare-financial-statements activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-prepare-financial-statements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_prepare_financial_statements',
    "version": '3.0.3',
    "display_name": 'Prepare financial statements Summary Report',
    "description": "Builds a read-only summary report of prepare-financial-statements activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.",
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
        "upstream_slug": 'report-prepare-financial-statements',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-prepare-financial-statements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3990fe8f6fa4ac8c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/prepare-financial-statements'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-prepare-financial-statements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Excel workbook filename, e.g. report-prepare-financial-statements-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where prepare financial statements stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of prepare financial statements for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-prepare-financial-statements-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads prepare financial statements records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only summary report of prepare-financial-statements activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets.", 'example_request': 'Build a prepare financial statements summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook filename, e.g. report-prepare-financial-statements-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write financial statement preparation summary from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportPrepareFinancialStatements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPrepareFinancialStatements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-prepare-financial-statements-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportPrepareFinancialStatements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-prepare-financial-statements"
description: "Builds a read-only summary report of prepare-financial-statements activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_prepare_financial_statements", "rar_sha256": "dbde340643f509268cab70380affdf4f58fa4c24dc39b120480fae7b8ea3e6ba", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

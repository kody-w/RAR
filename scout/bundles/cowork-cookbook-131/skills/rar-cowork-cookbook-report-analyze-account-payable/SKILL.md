---
name: "rar-cowork-cookbook-report-analyze-account-payable"
description: "Builds a read-only accounts payable summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_account_payable", "rar_sha256": "bf8ec0952e575aaf4a25d26c16272bc926311458b7d5d695a73f7633f492ffd1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_analyze_account_payable`. The original RAPP
agent is preserved byte-for-byte in `report_analyze_account_payable_agent.py` and in the RCI capsule.

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

Analyze account payable Summary Report — Builds a read-only accounts payable summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-account-payable
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
      "description": "Dimensions for breakdowns where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-analyze-account-payable-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_account_payable_agent.py` and embedded as the fenced Python below (sha256 bf8ec0952e575aaf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_account_payable_agent.py` first:

```bash
python3 report_analyze_account_payable_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_account_payable_agent.py   # or on stdin
python3 report_analyze_account_payable_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze account payable Summary Report — Builds a read-only accounts payable summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-account-payable
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_account_payable',
    "version": '3.0.3',
    "display_name": 'Analyze account payable Summary Report',
    "description": "Builds a read-only accounts payable summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-analyze-account-payable',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-account-payable',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4d483a7154bc92c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-account-payable'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-analyze-account-payable', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-analyze-account-payable-2026-05-24.xlsx.', 'period': 'Posted period to report; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where analyze account payable stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of analyze account payable for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-analyze-account-payable-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads analyze account payable records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only accounts payable summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.", 'example_request': "Build an accounts payable summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-analyze-account-payable-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants an accounts payable summary with totals, by-dimension breakdowns, and a Top 10 by value list exported to Excel from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportAnalyzeAccountPayable(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeAccountPayable'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-analyze-account-payable-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportAnalyzeAccountPayable().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

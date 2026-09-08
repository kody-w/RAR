---
name: "rar-cowork-cookbook-report-analyze-account-payable"
description: "Builds a read-only accounts payable summary report from Dynamics 365 F&SCM for a legal entity's most recent posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_account_payable", "rar_sha256": "bf8ec0952e575aaf4a25d26c16272bc926311458b7d5d695a73f7633f492ffd1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

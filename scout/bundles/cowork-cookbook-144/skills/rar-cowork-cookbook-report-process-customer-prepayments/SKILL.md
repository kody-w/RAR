---
name: "rar-cowork-cookbook-report-process-customer-prepayments"
description: "Builds a read-only summary report of customer prepayment activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_customer_prepayments", "rar_sha256": "2dc7f9395e5d66546c5b6d3a0f612fd8e33b3ac690a96d32be2e87b4740136ee", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_process_customer_prepayments`. The original RAPP
agent is preserved byte-for-byte in `report_process_customer_prepayments_agent.py` and in the RCI capsule.

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

Process customer prepayments Summary Report — Builds a read-only summary report of customer prepayment activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-process-customer-prepayments
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
      "description": "Name of the Excel workbook to produce, e.g. report-process-customer-prepayments-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_process_customer_prepayments_agent.py` and embedded as the fenced Python below (sha256 2dc7f9395e5d6654…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_process_customer_prepayments_agent.py` first:

```bash
python3 report_process_customer_prepayments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_process_customer_prepayments_agent.py   # or on stdin
python3 report_process_customer_prepayments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer prepayments Summary Report — Builds a read-only summary report of customer prepayment activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-process-customer-prepayments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_process_customer_prepayments',
    "version": '3.0.3',
    "display_name": 'Process customer prepayments Summary Report',
    "description": 'Builds a read-only summary report of customer prepayment activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-process-customer-prepayments',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-process-customer-prepayments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c9f757779b912cc0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-prepayments'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-process-customer-prepayments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-process-customer-prepayments-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where process customer prepayments stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of process customer prepayments for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-process-customer-prepayments-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads process customer prepayments records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of customer prepayment activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a customer prepayments summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-process-customer-prepayments-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-data-changes Excel summary of processed customer prepayments in D365 F&SCM, with totals, dimension breakdowns, and top 10 by value.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportProcessCustomerPrepayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportProcessCustomerPrepayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-process-customer-prepayments-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportProcessCustomerPrepayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

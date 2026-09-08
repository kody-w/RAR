---
name: "rar-cowork-cookbook-report-process-customer-prepayments"
description: "Builds a read-only summary report of customer prepayment activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_customer_prepayments", "rar_sha256": "2dc7f9395e5d66546c5b6d3a0f612fd8e33b3ac690a96d32be2e87b4740136ee", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

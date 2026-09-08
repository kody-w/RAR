---
name: "rar-cowork-cookbook-report-process-customer-rebates"
description: "Builds a read-only customer rebate summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_customer_rebates", "rar_sha256": "ce2d52eec2f623287289fe8814dbcceee0636178fb87a82323e019f1d8709b97", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_process_customer_rebates`. The original RAPP
agent is preserved byte-for-byte in `report_process_customer_rebates_agent.py` and in the RCI capsule.

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

Process customer rebates Summary Report — Builds a read-only customer rebate summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-process-customer-rebates
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-process-customer-rebates-2026-05-24.xlsx.",
      "type": "string"
    },
    "posted_period": {
      "description": "Posted period to report on; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_process_customer_rebates_agent.py` and embedded as the fenced Python below (sha256 ce2d52eec2f62328…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_process_customer_rebates_agent.py` first:

```bash
python3 report_process_customer_rebates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_process_customer_rebates_agent.py   # or on stdin
python3 report_process_customer_rebates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer rebates Summary Report — Builds a read-only customer rebate summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-process-customer-rebates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_process_customer_rebates',
    "version": '3.0.3',
    "display_name": 'Process customer rebates Summary Report',
    "description": 'Builds a read-only customer rebate summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-process-customer-rebates',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-process-customer-rebates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '55f5709d236baf5b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-rebates'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-process-customer-rebates', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-process-customer-rebates-2026-05-24.xlsx.', 'posted_period': 'Posted period to report on; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where process customer rebates stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of process customer rebates for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-process-customer-rebates-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process customer rebates records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only customer rebate summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a customer rebate summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'name': 'posted_period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-process-customer-rebates-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of customer rebate activity from D365 ERP with totals, by-dimension breakdowns, and a top-10 list as an Excel file.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportProcessCustomerRebates(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportProcessCustomerRebates'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-process-customer-rebates-2026-05-24.xlsx.', 'type': 'string'}, 'posted_period': {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportProcessCustomerRebates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

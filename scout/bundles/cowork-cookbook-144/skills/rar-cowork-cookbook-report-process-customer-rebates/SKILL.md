---
name: "rar-cowork-cookbook-report-process-customer-rebates"
description: "Builds a read-only customer rebate summary report from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_customer_rebates", "rar_sha256": "ce2d52eec2f623287289fe8814dbcceee0636178fb87a82323e019f1d8709b97", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

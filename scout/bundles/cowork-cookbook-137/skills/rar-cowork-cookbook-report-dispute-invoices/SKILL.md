---
name: "rar-cowork-cookbook-report-dispute-invoices"
description: "Builds a read-only dispute invoices summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_dispute_invoices", "rar_sha256": "1954507c36c583a552a5a8d3c256747d062e79e85d9b2a4a07f54731caece16e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_dispute_invoices`. The original RAPP
agent is preserved byte-for-byte in `report_dispute_invoices_agent.py` and in the RCI capsule.

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

Dispute invoices Summary Report — Builds a read-only dispute invoices summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-dispute-invoices
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
      "description": "Name of the Excel workbook to write, e.g. report-dispute-invoices-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_dispute_invoices_agent.py` and embedded as the fenced Python below (sha256 1954507c36c583a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_dispute_invoices_agent.py` first:

```bash
python3 report_dispute_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_dispute_invoices_agent.py   # or on stdin
python3 report_dispute_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Dispute invoices Summary Report — Builds a read-only dispute invoices summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-dispute-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_dispute_invoices',
    "version": '3.0.3',
    "display_name": 'Dispute invoices Summary Report',
    "description": 'Builds a read-only dispute invoices summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-dispute-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-dispute-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fb8fb6d1c7947498',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/dispute-invoices'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-dispute-invoices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to write, e.g. report-dispute-invoices-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where dispute invoices stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of dispute invoices for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-dispute-invoices-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads dispute invoices records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only dispute invoices summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a dispute invoices summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to write, e.g. report-dispute-invoices-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a dispute invoices summary with totals, dimension breakdowns, and top-10-by-value exported to Excel from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDisputeInvoices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDisputeInvoices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to write, e.g. report-dispute-invoices-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDisputeInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

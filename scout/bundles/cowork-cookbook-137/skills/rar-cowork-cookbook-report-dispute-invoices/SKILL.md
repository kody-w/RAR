---
name: "rar-cowork-cookbook-report-dispute-invoices"
description: "Builds a read-only dispute invoices summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_dispute_invoices", "rar_sha256": "1954507c36c583a552a5a8d3c256747d062e79e85d9b2a4a07f54731caece16e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-report-reconcile-ledger-and-subledger"
description: "Builds a read-only ledger-to-subledger reconciliation summary from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_reconcile_ledger_and_subledger", "rar_sha256": "43e8fd001dfafd1bb9e0e0f8eaa4bcc17795b206576e558355ca9837d029582a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_reconcile_ledger_and_subledger`. The original RAPP
agent is preserved byte-for-byte in `report_reconcile_ledger_and_subledger_agent.py` and in the RCI capsule.

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

Reconcile ledger and subledger Summary Report — Builds a read-only ledger-to-subledger reconciliation summary from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-reconcile-ledger-and-subledger
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
      "description": "Name of the Excel workbook to produce, e.g. report-reconcile-ledger-and-subledger-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_reconcile_ledger_and_subledger_agent.py` and embedded as the fenced Python below (sha256 43e8fd001dfafd1b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_reconcile_ledger_and_subledger_agent.py` first:

```bash
python3 report_reconcile_ledger_and_subledger_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_reconcile_ledger_and_subledger_agent.py   # or on stdin
python3 report_reconcile_ledger_and_subledger_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile ledger and subledger Summary Report — Builds a read-only ledger-to-subledger reconciliation summary from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-reconcile-ledger-and-subledger
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_reconcile_ledger_and_subledger',
    "version": '3.0.3',
    "display_name": 'Reconcile ledger and subledger Summary Report',
    "description": 'Builds a read-only ledger-to-subledger reconciliation summary from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-reconcile-ledger-and-subledger',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-reconcile-ledger-and-subledger',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8e56fbc47e28bd2c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/reconcile-ledger-and-subledger'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-reconcile-ledger-and-subledger', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-reconcile-ledger-and-subledger-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where reconcile ledger and subledger stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of reconcile ledger and subledger for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-reconcile-ledger-and-subledger-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads reconcile ledger and subledger records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only ledger-to-subledger reconciliation summary from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Run a ledger and subledger reconciliation summary for USMF for the latest posted period and give me the Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-reconcile-ledger-and-subledger-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a reconciliation summary report of ledger vs subledger activity from D365 ERP, with totals, dimension breakdowns, and top-10-by-value, without changing data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportReconcileLedgerAndSubledger(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReconcileLedgerAndSubledger'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-reconcile-ledger-and-subledger-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportReconcileLedgerAndSubledger().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

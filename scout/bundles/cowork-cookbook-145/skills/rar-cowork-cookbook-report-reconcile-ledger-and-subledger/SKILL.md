---
name: "rar-cowork-cookbook-report-reconcile-ledger-and-subledger"
description: "Builds a read-only ledger-to-subledger reconciliation summary from Dynamics 365 F&SCM for a legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_reconcile_ledger_and_subledger", "rar_sha256": "43e8fd001dfafd1bb9e0e0f8eaa4bcc17795b206576e558355ca9837d029582a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

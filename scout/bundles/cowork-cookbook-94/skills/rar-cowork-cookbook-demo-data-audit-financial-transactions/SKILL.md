---
name: "rar-cowork-cookbook-demo-data-audit-financial-transactions"
description: "Generates 25 realistic demo audit financial transaction records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_financial_transactions", "rar_sha256": "46185e1cbd4a4f155f6adee02ae8570068a7a1ed2b3a7c8d7a7f34e77cca2f14", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_audit_financial_transactions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_audit_financial_transactions_agent.py` and in the RCI capsule.

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

Audit financial transactions Demo Data Generator — Generates 25 realistic demo audit financial transaction records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions
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
      "description": "Sandbox D365 legal entity to create records in (default USMF); must not be production.",
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
    "record_count": {
      "description": "Number of demo records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-audit-financial-transactions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_financial_transactions_agent.py` and embedded as the fenced Python below (sha256 46185e1cbd4a4f15…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_financial_transactions_agent.py` first:

```bash
python3 demo_data_audit_financial_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_audit_financial_transactions_agent.py   # or on stdin
python3 demo_data_audit_financial_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial transactions Demo Data Generator — Generates 25 realistic demo audit financial transaction records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_audit_financial_transactions',
    "version": '3.0.3',
    "display_name": 'Audit financial transactions Demo Data Generator',
    "description": "Generates 25 realistic demo audit financial transaction records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-audit-financial-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e5e5780c8805b5b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-transactions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-audit-financial-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-audit-financial-transactions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic audit financial transactions data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for audit financial transactions. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-audit-financial-transactions-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic audit financial transactions records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo audit financial transaction records via the Dynamics 365 ERP plugin, stages them in an Excel workbook, creates them in a sandbox legal entity, and returns each new record's primary key.", 'example_request': 'Generate 25 demo audit financial transactions in the USMF sandbox and stage them in Excel first.', 'inputs': [{'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-audit-financial-transactions-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need demo audit financial transaction data in a D365 sandbox legal entity for training or pilot scenarios. Never run against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataAuditFinancialTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAuditFinancialTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to create records in (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-audit-financial-transactions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataAuditFinancialTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

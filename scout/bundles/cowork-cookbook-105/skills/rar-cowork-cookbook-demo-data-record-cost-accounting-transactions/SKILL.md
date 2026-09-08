---
name: "rar-cowork-cookbook-demo-data-record-cost-accounting-transactions"
description: "Generates 25 realistic demo cost accounting transaction records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_cost_accounting_transactions", "rar_sha256": "b894cd2dc7a7625e71784a81da98d28b41d425aa94907287afe7841803561687", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_record_cost_accounting_transactions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_record_cost_accounting_transactions_agent.py` and in the RCI capsule.

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

Record cost accounting transactions Demo Data Generator — Generates 25 realistic demo cost accounting transaction records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-cost-accounting-transactions
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
      "description": "Sandbox D365 legal entity to target (default USMF); must not be production.",
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
      "description": "How many demo records to generate (recipe default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-record-cost-accounting-transactions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_record_cost_accounting_transactions_agent.py` and embedded as the fenced Python below (sha256 b894cd2dc7a7625e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_record_cost_accounting_transactions_agent.py` first:

```bash
python3 demo_data_record_cost_accounting_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_record_cost_accounting_transactions_agent.py   # or on stdin
python3 demo_data_record_cost_accounting_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record cost accounting transactions Demo Data Generator — Generates 25 realistic demo cost accounting transaction records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-cost-accounting-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_record_cost_accounting_transactions',
    "version": '3.0.3',
    "display_name": 'Record cost accounting transactions Demo Data Generator',
    "description": "Generates 25 realistic demo cost accounting transaction records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-record-cost-accounting-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-record-cost-accounting-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7db58461da35394b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-cost-accounting-transactions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-record-cost-accounting-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'How many demo records to generate (recipe default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-record-cost-accounting-transactions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic record cost accounting transactions data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for record cost accounting transactions. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-record-cost-accounting-transactions-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic record cost accounting transactions records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo cost accounting transaction records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo cost accounting transactions in the USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo records to generate (recipe default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-record-cost-accounting-transactions-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or pilot cost accounting transaction data created in a D365 sandbox legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataRecordCostAccountingTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRecordCostAccountingTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo records to generate (recipe default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-record-cost-accounting-transactions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataRecordCostAccountingTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

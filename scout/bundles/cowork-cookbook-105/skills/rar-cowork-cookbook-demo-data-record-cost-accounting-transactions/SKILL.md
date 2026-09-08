---
name: "rar-cowork-cookbook-demo-data-record-cost-accounting-transactions"
description: "Generates 25 realistic demo cost accounting transaction records in a sandbox D365 legal entity (default USMF), stages them in a dated Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_cost_accounting_transactions", "rar_sha256": "b894cd2dc7a7625e71784a81da98d28b41d425aa94907287afe7841803561687", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

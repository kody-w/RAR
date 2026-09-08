---
name: "rar-cowork-cookbook-demo-data-invoice-project-transactions"
description: "Generates 25 realistic demo invoice project transaction records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_invoice_project_transactions", "rar_sha256": "f9020a40e8308e9f0d525f05224a01a9d4ab9a3b855582109d55ae7bb3f3a79c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_invoice_project_transactions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_invoice_project_transactions_agent.py` and in the RCI capsule.

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

Invoice project transactions Demo Data Generator — Generates 25 realistic demo invoice project transaction records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-invoice-project-transactions
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
      "description": "Sandbox D365 legal entity to write to (default USMF); must not be production.",
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
      "description": "Excel staging file name, e.g. demo-data-invoice-project-transactions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_invoice_project_transactions_agent.py` and embedded as the fenced Python below (sha256 f9020a40e8308e9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_invoice_project_transactions_agent.py` first:

```bash
python3 demo_data_invoice_project_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_invoice_project_transactions_agent.py   # or on stdin
python3 demo_data_invoice_project_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Invoice project transactions Demo Data Generator — Generates 25 realistic demo invoice project transaction records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-invoice-project-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_invoice_project_transactions',
    "version": '3.0.3',
    "display_name": 'Invoice project transactions Demo Data Generator',
    "description": "Generates 25 realistic demo invoice project transaction records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-invoice-project-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-invoice-project-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd89cda0e34292c83',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/invoice-project-transactions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/demo-data-invoice-project-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'record_count': 'Number of demo records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-invoice-project-transactions-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic invoice project transactions data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for invoice project transactions. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-invoice-project-transactions-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic invoice project transactions records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo invoice project transaction records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.", 'example_request': 'Generate 25 demo invoice project transactions in USMF sandbox, stage them in Excel first, then create them.', 'inputs': [{'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-invoice-project-transactions-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training invoice project transaction data created in a sandbox D365 legal entity — never against production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataInvoiceProjectTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataInvoiceProjectTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write to (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-invoice-project-transactions-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataInvoiceProjectTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

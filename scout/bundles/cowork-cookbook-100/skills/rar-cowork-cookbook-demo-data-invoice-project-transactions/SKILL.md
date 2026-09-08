---
name: "rar-cowork-cookbook-demo-data-invoice-project-transactions"
description: "Generates 25 realistic demo invoice project transaction records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_invoice_project_transactions", "rar_sha256": "f9020a40e8308e9f0d525f05224a01a9d4ab9a3b855582109d55ae7bb3f3a79c", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

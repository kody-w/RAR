---
name: "rar-cowork-cookbook-demo-data-process-freight-invoices"
description: "Generates 25 realistic demo freight invoice records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_process_freight_invoices", "rar_sha256": "5dc1930d39b953e43b037740efb01bbd0c0b2f29d4f1c2aae58f47847016146f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_process_freight_invoices`. The original RAPP
agent is preserved byte-for-byte in `demo_data_process_freight_invoices_agent.py` and in the RCI capsule.

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

Process freight invoices Demo Data Generator — Generates 25 realistic demo freight invoice records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-process-freight-invoices
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
      "description": "How many demo freight invoice records to generate (default 25).",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-process-freight-invoices-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_process_freight_invoices_agent.py` and embedded as the fenced Python below (sha256 5dc1930d39b953e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_process_freight_invoices_agent.py` first:

```bash
python3 demo_data_process_freight_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_process_freight_invoices_agent.py   # or on stdin
python3 demo_data_process_freight_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process freight invoices Demo Data Generator — Generates 25 realistic demo freight invoice records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-process-freight-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_process_freight_invoices',
    "version": '3.0.3',
    "display_name": 'Process freight invoices Demo Data Generator',
    "description": "Generates 25 realistic demo freight invoice records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-process-freight-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-process-freight-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d571c19b18e71a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/process-freight-invoices'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-process-freight-invoices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'record_count': 'How many demo freight invoice records to generate (default 25).', 'workbook_name': 'Excel staging file name, e.g. demo-data-process-freight-invoices-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic process freight invoices data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for process freight invoices. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-process-freight-invoices-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic process freight invoices records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic demo freight invoice records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key.", 'example_request': 'Generate 25 demo freight invoices in the USMF sandbox, stage them in Excel first, then create them and list the keys.', 'inputs': [{'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'name': 'legal_entity'}, {'description': 'How many demo freight invoice records to generate (default 25).', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-process-freight-invoices-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo/training freight invoice data created in a D365 F&SCM sandbox legal entity — never production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataProcessFreightInvoices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataProcessFreightInvoices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to target (default USMF); must not be production.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'How many demo freight invoice records to generate (default 25).', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-process-freight-invoices-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataProcessFreightInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

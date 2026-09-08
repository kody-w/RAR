---
name: "rar-cowork-cookbook-demo-data-process-freight-invoices"
description: "Generates 25 realistic demo freight invoice records in a sandbox D365 legal entity (default USMF), stages them in an Excel workbook first, creates them, then returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_process_freight_invoices", "rar_sha256": "5dc1930d39b953e43b037740efb01bbd0c0b2f29d4f1c2aae58f47847016146f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

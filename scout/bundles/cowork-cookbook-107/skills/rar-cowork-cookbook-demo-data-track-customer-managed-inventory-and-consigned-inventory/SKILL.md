---
name: "rar-cowork-cookbook-demo-data-track-customer-managed-inventory-and-consigned-inventory"
description: "Generates 25 realistic consigned/customer-managed inventory demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_customer_managed_inventory_and_consigned_inventory", "rar_sha256": "5c8637bbb598a2ec4874338e45c84949b44d91148a043d17e76bdb27b34259b0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_track_customer_managed_inventory_and_consigned_inventory`. The original RAPP
agent is preserved byte-for-byte in `demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py` and in the RCI capsule.

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

Track customer managed inventory and consigned inventory Demo Data Generator — Generates 25 realistic consigned/customer-managed inventory demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-customer-managed-inventory-and-consigned-inventory
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
      "description": "Sandbox D365 legal entity to write into; defaults to USMF. Production entities are not allowed.",
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
      "description": "Number of demo records to generate; defaults to 25.",
      "type": "string"
    },
    "workbook_name": {
      "description": "Excel staging file name, e.g. demo-data-track-customer-managed-inventory-and-consigned-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py` and embedded as the fenced Python below (sha256 5c8637bbb598a2ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py` first:

```bash
python3 demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py   # or on stdin
python3 demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track customer managed inventory and consigned inventory Demo Data Generator — Generates 25 realistic consigned/customer-managed inventory demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.

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
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-customer-managed-inventory-and-consigned-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_customer_managed_inventory_and_consigned_inventory',
    "version": '3.0.3',
    "display_name": 'Track customer managed inventory and consigned inventory Demo Data Generator',
    "description": "Generates 25 realistic consigned/customer-managed inventory demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.",
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
        "upstream_slug": 'demo-data-track-customer-managed-inventory-and-consigned-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-customer-managed-inventory-and-consigned-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5aa3fca219fbfc7b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/track-customer-managed-inventory-and-consigned-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-track-customer-managed-inventory-and-consigned-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Sandbox D365 legal entity to write into; defaults to USMF. Production entities are not allowed.', 'record_count': 'Number of demo records to generate; defaults to 25.', 'workbook_name': 'Excel staging file name, e.g. demo-data-track-customer-managed-inventory-and-consigned-inventory-2026-05-24.xlsx.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Eliminates the 'no data to demo with' blocker for trainers, implementation partners, and pilot programs by populating realistic but synthetic track customer managed inventory and consigned inventory data in minutes.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against a SANDBOX legal entity (default USMF), generate 25 realistic demo records for track customer managed inventory and consigned inventory. Use plausible values for every required field, vary the data so it looks organic, and stage them in an Excel workbook 'demo-data-track-customer-managed-inventory-and-consigned-inventory-2026-05-24.xlsx' BEFORE creating. Then create the records in D365. After creation, output a confirmation list with each new record's primary key. WARNING: this recipe creates data - run in sandbox only, and never against a production legal entity.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates a configurable number of realistic track customer managed inventory and consigned inventory records and creates them via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Generates 25 realistic consigned/customer-managed inventory demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key.", 'example_request': 'Generate 25 demo consigned inventory records in USMF sandbox, stage them in Excel, then create them in D365.', 'inputs': [{'description': 'Sandbox D365 legal entity to write into; defaults to USMF. Production entities are not allowed.', 'name': 'legal_entity'}, {'description': 'Number of demo records to generate; defaults to 25.', 'name': 'record_count'}, {'description': 'Excel staging file name, e.g. demo-data-track-customer-managed-inventory-and-consigned-inventory-2026-05-24.xlsx.', 'name': 'workbook_name'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need demo or pilot data for customer managed and consigned inventory tracking in a D365 sandbox legal entity — never production.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DemoDataTrackCustomerManagedInventoryAndConsignedInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackCustomerManagedInventoryAndConsignedInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Sandbox D365 legal entity to write into; defaults to USMF. Production entities are not allowed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_count': {'description': 'Number of demo records to generate; defaults to 25.', 'type': 'string'}, 'workbook_name': {'description': 'Excel staging file name, e.g. demo-data-track-customer-managed-inventory-and-consigned-inventory-2026-05-24.xlsx.', 'type': 'string'}},
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
    print(DemoDataTrackCustomerManagedInventoryAndConsignedInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

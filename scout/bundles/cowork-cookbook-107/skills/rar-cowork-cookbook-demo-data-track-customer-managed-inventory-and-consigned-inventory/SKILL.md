---
name: "rar-cowork-cookbook-demo-data-track-customer-managed-inventory-and-consigned-inventory"
description: "Generates 25 realistic consigned/customer-managed inventory demo records in a sandbox D365 F&SCM legal entity (default USMF), stages them in an Excel workbook, creates them, and returns each new record's primary key."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_customer_managed_inventory_and_consigned_inventory", "rar_sha256": "5c8637bbb598a2ec4874338e45c84949b44d91148a043d17e76bdb27b34259b0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-configure-process-inventory-movements"
description: "Reads an attached configuration Excel file of process inventory movement changes for a D365 F&SCM legal entity, validates each row, returns a validation workbook, and after your approval applies the changes with a before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_inventory_movements", "rar_sha256": "ab56cf6d25ebbb99eeb898169469e987766c98354c32c7978cfc8c712938f57b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_process_inventory_movements`. The original RAPP
agent is preserved byte-for-byte in `configure_process_inventory_movements_agent.py` and in the RCI capsule.

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

Process inventory movements Configuration Bulk Setup — Reads an attached configuration Excel file of process inventory movement changes for a D365 F&SCM legal entity, validates each row, returns a validation workbook, and after your approval applies the changes with a before

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-inventory-movements
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
    "approval": {
      "description": "Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_workbook": {
      "description": "Attached Excel file with one row per process inventory movements target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_process_inventory_movements_agent.py` and embedded as the fenced Python below (sha256 ab56cf6d25ebbb99…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_process_inventory_movements_agent.py` first:

```bash
python3 configure_process_inventory_movements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_process_inventory_movements_agent.py   # or on stdin
python3 configure_process_inventory_movements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process inventory movements Configuration Bulk Setup — Reads an attached configuration Excel file of process inventory movement changes for a D365 F&SCM legal entity, validates each row, returns a validation workbook, and after your approval applies the changes with a before

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-inventory-movements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_process_inventory_movements',
    "version": '3.0.3',
    "display_name": 'Process inventory movements Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of process inventory movement changes for a D365 F&SCM legal entity, validates each row, returns a validation workbook, and after your approval applies the changes with a before',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-process-inventory-movements',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-process-inventory-movements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ae1c1794ed30478e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/process-inventory-movements'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-process-inventory-movements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_workbook': 'Attached Excel file with one row per process inventory movements target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for process inventory movements, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per process inventory movements target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of process inventory movement changes for a D365 F&SCM legal entity, validates each row, returns a validation workbook, and after your approval applies the changes with a before', 'example_request': 'Bulk-update process inventory movements config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per process inventory movements target and the new field values.', 'name': 'configuration_workbook'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply process inventory movement configuration changes in Dynamics 365 F&SCM from a spreadsheet, with validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureProcessInventoryMovements(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureProcessInventoryMovements'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_workbook': {'description': 'Attached Excel file with one row per process inventory movements target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureProcessInventoryMovements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

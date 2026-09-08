---
name: "rar-cowork-cookbook-configure-process-inventory-movements"
description: "Reads an attached configuration Excel file of process inventory movement changes for a D365 F&SCM legal entity, validates each row, returns a validation workbook, and after your approval applies the changes with a before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_inventory_movements", "rar_sha256": "ab56cf6d25ebbb99eeb898169469e987766c98354c32c7978cfc8c712938f57b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

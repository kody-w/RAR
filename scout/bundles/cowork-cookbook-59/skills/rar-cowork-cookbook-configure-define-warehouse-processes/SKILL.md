---
name: "rar-cowork-cookbook-configure-define-warehouse-processes"
description: "Bulk-applies warehouse process configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_warehouse_processes", "rar_sha256": "80edd9b8c9040fe2eb3e19d5585c42469fb84706f15f7d28c700a52e80b12db6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_warehouse_processes`. The original RAPP
agent is preserved byte-for-byte in `configure_define_warehouse_processes_agent.py` and in the RCI capsule.

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

Define warehouse processes Configuration Bulk Setup — Bulk-applies warehouse process configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-warehouse-processes
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per warehouse process target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; use sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_warehouse_processes_agent.py` and embedded as the fenced Python below (sha256 80edd9b8c9040fe2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_warehouse_processes_agent.py` first:

```bash
python3 configure_define_warehouse_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_warehouse_processes_agent.py   # or on stdin
python3 configure_define_warehouse_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse processes Configuration Bulk Setup — Bulk-applies warehouse process configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-warehouse-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_warehouse_processes',
    "version": '3.0.3',
    "display_name": 'Define warehouse processes Configuration Bulk Setup',
    "description": 'Bulk-applies warehouse process configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after',
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
        "upstream_slug": 'configure-define-warehouse-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-warehouse-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '81bb93b904be0aa2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/define-warehouse-processes'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-define-warehouse-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Attached Excel file with one row per warehouse process target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; use sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for define warehouse processes, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per define warehouse processes target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies warehouse process configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after', 'example_request': 'Run the warehouse process bulk setup in USMF sandbox using my attached config Excel — validate first and wait for my approval.', 'inputs': [{'description': 'Attached Excel file with one row per warehouse process target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; use sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to define or update warehouse processes in bulk from a spreadsheet in D365 F&SCM, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDefineWarehouseProcesses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineWarehouseProcesses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per warehouse process target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; use sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDefineWarehouseProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

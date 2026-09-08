---
name: "rar-cowork-cookbook-configure-define-warehouse-processes"
description: "Bulk-applies warehouse process configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_warehouse_processes", "rar_sha256": "80edd9b8c9040fe2eb3e19d5585c42469fb84706f15f7d28c700a52e80b12db6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

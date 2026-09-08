---
name: "rar-cowork-cookbook-configure-manage-the-recurring-synchronization-of-data"
description: "Applies a bulk configuration change for recurring data synchronization in Dynamics 365 F&SCM from an Excel file: validates every row, emits a validation workbook, waits for approval, then applies changes with a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data", "rar_sha256": "543905e76d3c30cb6bb1a69ab600b8472ca66c9f9df7166dffe6628fda890e5b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_the_recurring_synchronization_of_data_agent.py` and in the RCI capsule.

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

Manage the recurring synchronization of data Configuration Bulk Setup — Applies a bulk configuration change for recurring data synchronization in Dynamics 365 F&SCM from an Excel file: validates every row, emits a validation workbook, waits for approval, then applies changes with a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-the-recurring-synchronization-of-data
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
      "description": "Explicit user approval after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per recurring synchronization target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; sandbox first before production.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_the_recurring_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 543905e76d3c30cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_the_recurring_synchronization_of_data_agent.py` first:

```bash
python3 configure_manage_the_recurring_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_the_recurring_synchronization_of_data_agent.py   # or on stdin
python3 configure_manage_the_recurring_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the recurring synchronization of data Configuration Bulk Setup — Applies a bulk configuration change for recurring data synchronization in Dynamics 365 F&SCM from an Excel file: validates every row, emits a validation workbook, waits for approval, then applies changes with a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-the-recurring-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data',
    "version": '3.0.3',
    "display_name": 'Manage the recurring synchronization of data Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change for recurring data synchronization in Dynamics 365 F&SCM from an Excel file: validates every row, emits a validation workbook, waits for approval, then applies changes with a before/af',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-the-recurring-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-the-recurring-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f42be209c31d8d63',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-recurring-synchronization-of-data'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-manage-the-recurring-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per recurring synchronization target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage the recurring synchronization of data, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage the recurring synchronization of data target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk configuration change for recurring data synchronization in Dynamics 365 F&SCM from an Excel file: validates every row, emits a validation workbook, waits for approval, then applies changes with a before/af', 'example_request': 'Bulk-update our recurring data sync config in USMF sandbox from this Excel file — validate first and let me approve.', 'inputs': [{'description': 'Attached Excel file with one row per recurring synchronization target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-update recurring data synchronization settings in D365 F&SCM from a spreadsheet, with dry-run validation and approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageTheRecurringSynchronizationOfData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageTheRecurringSynchronizationOfData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per recurring synchronization target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageTheRecurringSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

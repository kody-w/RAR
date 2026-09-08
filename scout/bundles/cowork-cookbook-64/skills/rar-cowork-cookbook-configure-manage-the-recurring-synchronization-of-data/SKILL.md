---
name: "rar-cowork-cookbook-configure-manage-the-recurring-synchronization-of-data"
description: "Applies a bulk configuration change for recurring data synchronization in Dynamics 365 F&SCM from an Excel file: validates every row, emits a validation workbook, waits for approval, then applies changes with a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_the_recurring_synchronization_of_data", "rar_sha256": "543905e76d3c30cb6bb1a69ab600b8472ca66c9f9df7166dffe6628fda890e5b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

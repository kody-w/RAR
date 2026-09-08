---
name: "rar-cowork-cookbook-configure-record-service-timesheet"
description: "Reads an attached Excel file of record service timesheet configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_record_service_timesheet", "rar_sha256": "f6dabd75e59830f88aae4bde2d6275443a3a6a3b6e3b928117ddf95bdcf4deef", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_record_service_timesheet`. The original RAPP
agent is preserved byte-for-byte in `configure_record_service_timesheet_agent.py` and in the RCI capsule.

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

Record service timesheet Configuration Bulk Setup — Reads an attached Excel file of record service timesheet configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-record-service-timesheet
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
      "description": "Explicit confirmation to apply changes after reviewing the validation workbook.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per record service timesheet target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment \u2014 sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_record_service_timesheet_agent.py` and embedded as the fenced Python below (sha256 f6dabd75e59830f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_record_service_timesheet_agent.py` first:

```bash
python3 configure_record_service_timesheet_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_record_service_timesheet_agent.py   # or on stdin
python3 configure_record_service_timesheet_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record service timesheet Configuration Bulk Setup — Reads an attached Excel file of record service timesheet configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-record-service-timesheet
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_record_service_timesheet',
    "version": '3.0.3',
    "display_name": 'Record service timesheet Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of record service timesheet configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-record-service-timesheet',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-record-service-timesheet',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a20c42e2acdf4422',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/record-service-timesheet'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-record-service-timesheet', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation to apply changes after reviewing the validation workbook.', 'configuration_excel_file': 'Attached Excel file with one row per record service timesheet target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for record service timesheet, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per record service timesheet target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of record service timesheet configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with', 'example_request': 'Bulk-update record service timesheet config in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per record service timesheet target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit confirmation to apply changes after reviewing the validation workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update record service timesheet configuration in D365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureRecordServiceTimesheet(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRecordServiceTimesheet'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation to apply changes after reviewing the validation workbook.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per record service timesheet target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureRecordServiceTimesheet().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

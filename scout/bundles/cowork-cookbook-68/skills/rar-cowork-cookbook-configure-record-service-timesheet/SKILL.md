---
name: "rar-cowork-cookbook-configure-record-service-timesheet"
description: "Reads an attached Excel file of record service timesheet configuration rows in Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, and after your approval applies the changes with"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_record_service_timesheet", "rar_sha256": "f6dabd75e59830f88aae4bde2d6275443a3a6a3b6e3b928117ddf95bdcf4deef", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-configure-perform-corrective-maintenance"
description: "Validates an attached Excel file of corrective-maintenance configuration changes row by row against Dynamics 365 F&SCM (legal entity USMF), emits a validation workbook, pauses for approval, then applies changes with a be"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_perform_corrective_maintenance", "rar_sha256": "d56e4a0497aa07c79129b1a9b3fb1073edacaeabbb2221831011578011ef4457", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_perform_corrective_maintenance`. The original RAPP
agent is preserved byte-for-byte in `configure_perform_corrective_maintenance_agent.py` and in the RCI capsule.

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

Perform corrective maintenance Configuration Bulk Setup — Validates an attached Excel file of corrective-maintenance configuration changes row by row against Dynamics 365 F&SCM (legal entity USMF), emits a validation workbook, pauses for approval, then applies changes with a be

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-perform-corrective-maintenance
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
      "description": "Explicit user approval after reviewing the validation workbook, required before changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Excel file with one row per corrective maintenance target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_perform_corrective_maintenance_agent.py` and embedded as the fenced Python below (sha256 d56e4a0497aa07c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_perform_corrective_maintenance_agent.py` first:

```bash
python3 configure_perform_corrective_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_perform_corrective_maintenance_agent.py   # or on stdin
python3 configure_perform_corrective_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform corrective maintenance Configuration Bulk Setup — Validates an attached Excel file of corrective-maintenance configuration changes row by row against Dynamics 365 F&SCM (legal entity USMF), emits a validation workbook, pauses for approval, then applies changes with a be

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-perform-corrective-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_perform_corrective_maintenance',
    "version": '3.0.3',
    "display_name": 'Perform corrective maintenance Configuration Bulk Setup',
    "description": 'Validates an attached Excel file of corrective-maintenance configuration changes row by row against Dynamics 365 F&SCM (legal entity USMF), emits a validation workbook, pauses for approval, then applies changes with a be',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-perform-corrective-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-perform-corrective-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fa35f9f1d6d8941d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-corrective-maintenance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-perform-corrective-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'configuration_file': 'Excel file with one row per corrective maintenance target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for perform corrective maintenance, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per perform corrective maintenance target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Validates an attached Excel file of corrective-maintenance configuration changes row by row against Dynamics 365 F&SCM (legal entity USMF), emits a validation workbook, pauses for approval, then applies changes with a be', 'example_request': 'Bulk-apply the corrective maintenance config changes in this Excel file to USMF sandbox — validate first.', 'inputs': [{'description': 'Excel file with one row per corrective maintenance target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-apply corrective maintenance configuration changes in D365 from a spreadsheet, with dry-run validation and explicit approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePerformCorrectiveMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePerformCorrectiveMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per corrective maintenance target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePerformCorrectiveMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

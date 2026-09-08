---
name: "rar-cowork-cookbook-configure-perform-corrective-maintenance"
description: "Validates an attached Excel file of corrective-maintenance configuration changes row by row against Dynamics 365 F&SCM (legal entity USMF), emits a validation workbook, pauses for approval, then applies changes with a be"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_perform_corrective_maintenance", "rar_sha256": "d56e4a0497aa07c79129b1a9b3fb1073edacaeabbb2221831011578011ef4457", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

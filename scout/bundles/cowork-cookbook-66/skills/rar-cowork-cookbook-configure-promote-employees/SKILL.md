---
name: "rar-cowork-cookbook-configure-promote-employees"
description: "Reads an attached configuration Excel file of employee promotion rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and emit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_promote_employees", "rar_sha256": "974705bcb67e8b3222a704eacbd8e16ad903e13471cbad73e076d9d890d88c90", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_promote_employees`. The original RAPP
agent is preserved byte-for-byte in `configure_promote_employees_agent.py` and in the RCI capsule.

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

Promote employees Configuration Bulk Setup — Reads an attached configuration Excel file of employee promotion rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and emit

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-promote-employees
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
    "configuration_file": {
      "description": "Excel file with one row per promote-employees target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_promote_employees_agent.py` and embedded as the fenced Python below (sha256 974705bcb67e8b32…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_promote_employees_agent.py` first:

```bash
python3 configure_promote_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_promote_employees_agent.py   # or on stdin
python3 configure_promote_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Promote employees Configuration Bulk Setup — Reads an attached configuration Excel file of employee promotion rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and emit

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-promote-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_promote_employees',
    "version": '3.0.3',
    "display_name": 'Promote employees Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of employee promotion rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and emit',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-promote-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-promote-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'df932011af67945b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/promote-employees'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/configure-promote-employees', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_file': 'Excel file with one row per promote-employees target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment — sandbox first before production.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for promote employees, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per promote employees target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of employee promotion rows against Dynamics 365 F&SCM (legal entity USMF), validates every row, returns a validation workbook, pauses for approval, then applies changes and emit', 'example_request': 'Bulk promote the employees in this Excel file in USMF sandbox — validate first and show me before I approve.', 'inputs': [{'description': 'Excel file with one row per promote-employees target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Target environment — sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-promote employees in D365 F&SCM from a spreadsheet, with row validation, an approval gate, and before/after confirmation output.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePromoteEmployees(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePromoteEmployees'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per promote-employees target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment — sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePromoteEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

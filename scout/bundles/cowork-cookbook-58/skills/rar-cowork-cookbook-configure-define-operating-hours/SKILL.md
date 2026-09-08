---
name: "rar-cowork-cookbook-configure-define-operating-hours"
description: "Bulk-applies operating hours configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_operating_hours", "rar_sha256": "03bf2675a4fff693828c3ecb674438cbe9d62f6ca34c340297cdabca6f927c2e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_operating_hours`. The original RAPP
agent is preserved byte-for-byte in `configure_define_operating_hours_agent.py` and in the RCI capsule.

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

Define operating hours Configuration Bulk Setup — Bulk-applies operating hours configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-operating-hours
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
    "configuration_excel_file": {
      "description": "Attached workbook with one row per operating-hours target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Sandbox or production target; sandbox first as this recipe modifies data.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_operating_hours_agent.py` and embedded as the fenced Python below (sha256 03bf2675a4fff693…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_operating_hours_agent.py` first:

```bash
python3 configure_define_operating_hours_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_operating_hours_agent.py   # or on stdin
python3 configure_define_operating_hours_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define operating hours Configuration Bulk Setup — Bulk-applies operating hours configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-operating-hours
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_operating_hours',
    "version": '3.0.3',
    "display_name": 'Define operating hours Configuration Bulk Setup',
    "description": 'Bulk-applies operating hours configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-operating-hours',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-operating-hours',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ef6c4899c82d8e94',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-operating-hours'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-define-operating-hours', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached workbook with one row per operating-hours target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Sandbox or production target; sandbox first as this recipe modifies data.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for define operating hours, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per define operating hours target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies operating hours configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before', 'example_request': 'Run the operating hours bulk setup on USMF sandbox using this attached config file — validate first and show me the preview.', 'inputs': [{'description': 'Attached workbook with one row per operating-hours target and the new field values.', 'name': 'configuration Excel file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal entity'}, {'description': 'Sandbox or production target; sandbox first as this recipe modifies data.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to set or update operating hours for many records at once in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDefineOperatingHours(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineOperatingHours'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached workbook with one row per operating-hours target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Sandbox or production target; sandbox first as this recipe modifies data.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDefineOperatingHours().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

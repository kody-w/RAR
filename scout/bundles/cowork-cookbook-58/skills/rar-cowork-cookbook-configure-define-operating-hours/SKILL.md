---
name: "rar-cowork-cookbook-configure-define-operating-hours"
description: "Bulk-applies operating hours configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_operating_hours", "rar_sha256": "03bf2675a4fff693828c3ecb674438cbe9d62f6ca34c340297cdabca6f927c2e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

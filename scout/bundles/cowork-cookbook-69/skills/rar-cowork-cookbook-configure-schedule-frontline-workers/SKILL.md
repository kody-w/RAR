---
name: "rar-cowork-cookbook-configure-schedule-frontline-workers"
description: "Reads an attached Excel file of schedule frontline worker configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_schedule_frontline_workers", "rar_sha256": "cdd0118dfe688e3a9556169999ef21ef0bbf5b5e84a38ecc770e76a9fbb01f39", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_schedule_frontline_workers`. The original RAPP
agent is preserved byte-for-byte in `configure_schedule_frontline_workers_agent.py` and in the RCI capsule.

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

Schedule frontline workers Configuration Bulk Setup — Reads an attached Excel file of schedule frontline worker configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-schedule-frontline-workers
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel workbook with one row per schedule frontline worker target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_schedule_frontline_workers_agent.py` and embedded as the fenced Python below (sha256 cdd0118dfe688e3a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_schedule_frontline_workers_agent.py` first:

```bash
python3 configure_schedule_frontline_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_schedule_frontline_workers_agent.py   # or on stdin
python3 configure_schedule_frontline_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule frontline workers Configuration Bulk Setup — Reads an attached Excel file of schedule frontline worker configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-schedule-frontline-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_schedule_frontline_workers',
    "version": '3.0.3',
    "display_name": 'Schedule frontline workers Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of schedule frontline worker configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before',
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
        "upstream_slug": 'configure-schedule-frontline-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-schedule-frontline-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2bf94c6efec8481f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/schedule-frontline-workers'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-schedule-frontline-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel workbook with one row per schedule frontline worker target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for schedule frontline workers, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per schedule frontline workers target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of schedule frontline worker configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before', 'example_request': 'Bulk-update schedule frontline worker config in USMF sandbox from this Excel file - validate first and show me before I approve.', 'inputs': [{'description': 'Attached Excel workbook with one row per schedule frontline worker target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update schedule frontline worker configuration in Dynamics 365 F&SCM from a spreadsheet, with row validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureScheduleFrontlineWorkers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureScheduleFrontlineWorkers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel workbook with one row per schedule frontline worker target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureScheduleFrontlineWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-configure-schedule-frontline-workers"
description: "Reads an attached Excel file of schedule frontline worker configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_schedule_frontline_workers", "rar_sha256": "cdd0118dfe688e3a9556169999ef21ef0bbf5b5e84a38ecc770e76a9fbb01f39", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

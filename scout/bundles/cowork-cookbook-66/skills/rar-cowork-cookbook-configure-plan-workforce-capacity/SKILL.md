---
name: "rar-cowork-cookbook-configure-plan-workforce-capacity"
description: "Applies bulk workforce capacity configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_workforce_capacity", "rar_sha256": "7edc0175b659b1e2bc25a63b21ab6fcadc74f16e4e5ef26beff063f3efba4899", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_workforce_capacity`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_workforce_capacity_agent.py` and in the RCI capsule.

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

Plan workforce capacity Configuration Bulk Setup — Applies bulk workforce capacity configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-capacity
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
      "description": "Your explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Excel file with one row per plan workforce capacity target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; run sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_workforce_capacity_agent.py` and embedded as the fenced Python below (sha256 7edc0175b659b1e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_workforce_capacity_agent.py` first:

```bash
python3 configure_plan_workforce_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_workforce_capacity_agent.py   # or on stdin
python3 configure_plan_workforce_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce capacity Configuration Bulk Setup — Applies bulk workforce capacity configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_workforce_capacity',
    "version": '3.0.3',
    "display_name": 'Plan workforce capacity Configuration Bulk Setup',
    "description": 'Applies bulk workforce capacity configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/after',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-workforce-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-workforce-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e0a2114da667878',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-workforce-capacity'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-workforce-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Excel file with one row per plan workforce capacity target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for plan workforce capacity, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per plan workforce capacity target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk workforce capacity configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/after', 'example_request': 'Bulk-update workforce capacity in D365 USMF sandbox from this Excel file - validate first and let me approve.', 'inputs': [{'description': 'Excel file with one row per plan workforce capacity target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update plan workforce capacity records in D365 from a spreadsheet, with row-level validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePlanWorkforceCapacity(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanWorkforceCapacity'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Your explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Excel file with one row per plan workforce capacity target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePlanWorkforceCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

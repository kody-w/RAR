---
name: "rar-cowork-cookbook-configure-plan-workforce-capacity"
description: "Applies bulk workforce capacity configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies and returns before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_workforce_capacity", "rar_sha256": "7edc0175b659b1e2bc25a63b21ab6fcadc74f16e4e5ef26beff063f3efba4899", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

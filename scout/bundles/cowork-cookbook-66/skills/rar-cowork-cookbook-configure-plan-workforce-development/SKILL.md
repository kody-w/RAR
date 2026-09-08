---
name: "rar-cowork-cookbook-configure-plan-workforce-development"
description: "Applies bulk workforce development plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_workforce_development", "rar_sha256": "447f00a007972ba9520a53649b13d0cb68472e8dd624cca35acea324cd7e5d68", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_workforce_development`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_workforce_development_agent.py` and in the RCI capsule.

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

Plan workforce development Configuration Bulk Setup — Applies bulk workforce development plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-development
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
      "description": "Attached Excel file with one row per plan workforce development target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_workforce_development_agent.py` and embedded as the fenced Python below (sha256 447f00a007972ba9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_workforce_development_agent.py` first:

```bash
python3 configure_plan_workforce_development_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_workforce_development_agent.py   # or on stdin
python3 configure_plan_workforce_development_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce development Configuration Bulk Setup — Applies bulk workforce development plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-workforce-development
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_workforce_development',
    "version": '3.0.3',
    "display_name": 'Plan workforce development Configuration Bulk Setup',
    "description": 'Applies bulk workforce development plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirma',
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
        "upstream_slug": 'configure-plan-workforce-development',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-workforce-development',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '14a5789061ffa81a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-workforce-development'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-workforce-development', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per plan workforce development target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for plan workforce development, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per plan workforce development target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk workforce development plan configuration changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then emits a before/after confirma', 'example_request': 'Bulk-update our workforce development plan config in USMF sandbox from this Excel file — validate first and let me approve.', 'inputs': [{'description': 'Attached Excel file with one row per plan workforce development target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update workforce development plan configuration in D365 F&SCM from a spreadsheet, with row validation, approval gate, and before/after output.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePlanWorkforceDevelopment(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanWorkforceDevelopment'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per plan workforce development target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePlanWorkforceDevelopment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

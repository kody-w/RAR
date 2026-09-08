---
name: "rar-cowork-cookbook-configure-develop-scenario-and-contingency-plans"
description: "Reads an attached configuration Excel file of scenario and contingency planning rows against a Dynamics 365 F&SCM legal entity, validates each row, emits a validation workbook, and after your approval applies changes wit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_scenario_and_contingency_plans", "rar_sha256": "d852dc64712be40e6db74084a68ec76057b406d08ba92a84193066d77f4e938a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_scenario_and_contingency_plans`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_scenario_and_contingency_plans_agent.py` and in the RCI capsule.

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

Develop scenario and contingency plans Configuration Bulk Setup — Reads an attached configuration Excel file of scenario and contingency planning rows against a Dynamics 365 F&SCM legal entity, validates each row, emits a validation workbook, and after your approval applies changes wit

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-scenario-and-contingency-plans
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
      "description": "Explicit confirmation after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_workbook": {
      "description": "Attached Excel file with one row per target, containing the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_scenario_and_contingency_plans_agent.py` and embedded as the fenced Python below (sha256 d852dc64712be40e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_scenario_and_contingency_plans_agent.py` first:

```bash
python3 configure_develop_scenario_and_contingency_plans_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_scenario_and_contingency_plans_agent.py   # or on stdin
python3 configure_develop_scenario_and_contingency_plans_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop scenario and contingency plans Configuration Bulk Setup — Reads an attached configuration Excel file of scenario and contingency planning rows against a Dynamics 365 F&SCM legal entity, validates each row, emits a validation workbook, and after your approval applies changes wit

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-scenario-and-contingency-plans
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_scenario_and_contingency_plans',
    "version": '3.0.3',
    "display_name": 'Develop scenario and contingency plans Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of scenario and contingency planning rows against a Dynamics 365 F&SCM legal entity, validates each row, emits a validation workbook, and after your approval applies changes wit',
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
        "upstream_slug": 'configure-develop-scenario-and-contingency-plans',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-scenario-and-contingency-plans',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b180d9c52aa553b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-scenario-and-contingency-plans'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-develop-scenario-and-contingency-plans', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the validation workbook, before any changes are applied.', 'configuration_workbook': 'Attached Excel file with one row per target, containing the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop scenario and contingency plans, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop scenario and contingency plans target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of scenario and contingency planning rows against a Dynamics 365 F&SCM legal entity, validates each row, emits a validation workbook, and after your approval applies changes wit', 'example_request': 'Bulk-apply this scenario planning config sheet in USMF sandbox — validate first and show me the dry run before writing.', 'inputs': [{'description': 'Attached Excel file with one row per target, containing the new field values.', 'name': 'configuration_workbook'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit confirmation after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-apply scenario/contingency planning configuration changes in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and approval first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopScenarioAndContingencyPlans(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopScenarioAndContingencyPlans'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_workbook': {'description': 'Attached Excel file with one row per target, containing the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopScenarioAndContingencyPlans().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

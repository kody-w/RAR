---
name: "rar-cowork-cookbook-configure-develop-scenario-and-contingency-plans"
description: "Reads an attached configuration Excel file of scenario and contingency planning rows against a Dynamics 365 F&SCM legal entity, validates each row, emits a validation workbook, and after your approval applies changes wit"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_scenario_and_contingency_plans", "rar_sha256": "d852dc64712be40e6db74084a68ec76057b406d08ba92a84193066d77f4e938a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

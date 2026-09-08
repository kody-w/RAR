---
name: "rar-cowork-cookbook-configure-plan-projects"
description: "Applies bulk configuration changes to plan projects in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_projects", "rar_sha256": "ecf37b51851485441da2ecf2adcacd884bc4bd61630fc2d12a2ec082af9cbf48", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_projects`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_projects_agent.py` and in the RCI capsule.

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

Plan projects Configuration Bulk Setup — Applies bulk configuration changes to plan projects in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-projects
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
      "description": "Explicit approval after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per plan projects target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_projects_agent.py` and embedded as the fenced Python below (sha256 ecf37b5185148544…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_projects_agent.py` first:

```bash
python3 configure_plan_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_projects_agent.py   # or on stdin
python3 configure_plan_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan projects Configuration Bulk Setup — Applies bulk configuration changes to plan projects in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_projects',
    "version": '3.0.3',
    "display_name": 'Plan projects Configuration Bulk Setup',
    "description": 'Applies bulk configuration changes to plan projects in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/af',
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
        "upstream_slug": 'configure-plan-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e63b1ba96e9defd9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-projects'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-projects', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'configuration_excel': 'Attached Excel file with one row per plan projects target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for plan projects, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per plan projects target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk configuration changes to plan projects in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies changes and returns a before/af', 'example_request': 'Bulk update plan project config from this Excel in USMF sandbox — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per plan projects target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update plan project field values in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePlanProjects(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProjects'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per plan projects target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePlanProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

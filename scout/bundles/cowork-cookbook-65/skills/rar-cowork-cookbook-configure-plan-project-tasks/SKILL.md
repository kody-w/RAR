---
name: "rar-cowork-cookbook-configure-plan-project-tasks"
description: "Reads an attached Excel file of plan project task configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_project_tasks", "rar_sha256": "9b2af0391da5dfb8bb3ef0410586d6b99be7d01b3086d07cdbe25047eb2d7dc5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_project_tasks`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_project_tasks_agent.py` and in the RCI capsule.

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

Plan project tasks Configuration Bulk Setup — Reads an attached Excel file of plan project task configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-project-tasks
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
      "description": "Explicit confirmation after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Attached Excel file with one row per plan project task target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_project_tasks_agent.py` and embedded as the fenced Python below (sha256 9b2af0391da5dfb8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_project_tasks_agent.py` first:

```bash
python3 configure_plan_project_tasks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_project_tasks_agent.py   # or on stdin
python3 configure_plan_project_tasks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan project tasks Configuration Bulk Setup — Reads an attached Excel file of plan project task configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-project-tasks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_project_tasks',
    "version": '3.0.3',
    "display_name": 'Plan project tasks Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of plan project task configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-plan-project-tasks',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-project-tasks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea430b85ce742e4e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/plan-project-tasks'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/configure-plan-project-tasks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Attached Excel file with one row per plan project task target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for plan project tasks, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per plan project tasks target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of plan project task configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/', 'example_request': 'Bulk update plan project tasks in USMF sandbox from this attached config spreadsheet — validate first and show me the dry run.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Attached Excel file with one row per plan project task target and the new field values.', 'name': 'configuration_file'}, {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when applying a bulk configuration change to plan project tasks in Dynamics 365 F&SCM from a spreadsheet, with validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePlanProjectTasks(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProjectTasks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Attached Excel file with one row per plan project task target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePlanProjectTasks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

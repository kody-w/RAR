---
name: "rar-cowork-cookbook-configure-plan-project-tasks"
description: "Reads an attached Excel file of plan project task configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, waits for your approval, then applies changes and emits a before/"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_project_tasks", "rar_sha256": "9b2af0391da5dfb8bb3ef0410586d6b99be7d01b3086d07cdbe25047eb2d7dc5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

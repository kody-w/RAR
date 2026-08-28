---
name: "rar-cowork-cookbook-configure-plan-project-tasks"
description: "Applies a bulk configuration change to plan project tasks from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_project_tasks", "rar_sha256": "0ace5071a7d8a219fa49afd77c211b56adce388a17426e114b7c59bd4f7fcc33", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

Plan project tasks Configuration Bulk Setup — Applies a bulk configuration change to plan project tasks from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_project_tasks_agent.py` and embedded as the fenced Python below (sha256 0ace5071a7d8a219…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_project_tasks_agent.py` first:

```bash
python3 configure_plan_project_tasks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_project_tasks_agent.py   # or on stdin
python3 configure_plan_project_tasks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan project tasks Configuration Bulk Setup — Applies a bulk configuration change to plan project tasks from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.0',
    "display_name": 'Plan project tasks Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan project tasks from an input Excel file, with validation and rollback support.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'caeb3df6a02c3a94',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigurePlanProjectTasks(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProjectTasks'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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

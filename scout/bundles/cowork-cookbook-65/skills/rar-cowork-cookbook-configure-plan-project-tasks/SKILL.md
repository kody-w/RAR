---
name: "rar-cowork-cookbook-configure-plan-project-tasks"
description: "Applies a bulk configuration change to plan project tasks from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_project_tasks", "rar_sha256": "61a4842cc2f8168f98e75fdb95ffe7671ecb484f45b8f597244e46c8585cdf2c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_project_tasks_agent.py` and embedded as the fenced Python below (sha256 61a4842cc2f8168f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_project_tasks_agent.py` first:

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
    "version": '2.0.1',
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

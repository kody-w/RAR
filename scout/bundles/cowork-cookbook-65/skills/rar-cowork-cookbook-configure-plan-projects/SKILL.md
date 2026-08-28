---
name: "rar-cowork-cookbook-configure-plan-projects"
description: "Applies a bulk configuration change to plan projects from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_projects", "rar_sha256": "aac6b33a0290b7e8ad59ce0150d41ff1139c808be6a93488322f20399259df37", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

Plan projects Configuration Bulk Setup — Applies a bulk configuration change to plan projects from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_projects_agent.py` and embedded as the fenced Python below (sha256 aac6b33a0290b7e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_projects_agent.py` first:

```bash
python3 configure_plan_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_projects_agent.py   # or on stdin
python3 configure_plan_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan projects Configuration Bulk Setup — Applies a bulk configuration change to plan projects from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.0',
    "display_name": 'Plan projects Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan projects from an input Excel file, with validation and rollback support.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '42eeaf215e578e2d',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigurePlanProjects(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanProjects'
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
    print(ConfigurePlanProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

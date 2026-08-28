---
name: "rar-cowork-cookbook-configure-plan-workforce-capacity"
description: "Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_workforce_capacity", "rar_sha256": "3e569d3e925c7e19e6e73746a5c5623ca3fab2903de54d21c38ba4a5a90ec87e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

Plan workforce capacity Configuration Bulk Setup — Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_workforce_capacity_agent.py` and embedded as the fenced Python below (sha256 3e569d3e925c7e19…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_workforce_capacity_agent.py` first:

```bash
python3 configure_plan_workforce_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_workforce_capacity_agent.py   # or on stdin
python3 configure_plan_workforce_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce capacity Configuration Bulk Setup — Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.1',
    "display_name": 'Plan workforce capacity Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan workforce capacity from an input Excel file, with validation and rollback support.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aba204977e09b4b4',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigurePlanWorkforceCapacity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanWorkforceCapacity'
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
    print(ConfigurePlanWorkforceCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

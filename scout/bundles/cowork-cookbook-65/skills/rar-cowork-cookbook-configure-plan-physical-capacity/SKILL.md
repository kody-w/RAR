---
name: "rar-cowork-cookbook-configure-plan-physical-capacity"
description: "Applies a bulk configuration change to plan physical capacity from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_physical_capacity", "rar_sha256": "ed5a08473cb6778e316b2cd2bfa0ec8ff186aff0e1a753e91878252687e3c749", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_plan_physical_capacity`. The original RAPP
agent is preserved byte-for-byte in `configure_plan_physical_capacity_agent.py` and in the RCI capsule.

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

Plan physical capacity Configuration Bulk Setup — Applies a bulk configuration change to plan physical capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-physical-capacity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_physical_capacity_agent.py` and embedded as the fenced Python below (sha256 ed5a08473cb6778e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_physical_capacity_agent.py` first:

```bash
python3 configure_plan_physical_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_plan_physical_capacity_agent.py   # or on stdin
python3 configure_plan_physical_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan physical capacity Configuration Bulk Setup — Applies a bulk configuration change to plan physical capacity from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-plan-physical-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_plan_physical_capacity',
    "version": '2.0.1',
    "display_name": 'Plan physical capacity Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to plan physical capacity from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-plan-physical-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-plan-physical-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ba50831c57a3072c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-physical-capacity'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/configure-plan-physical-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigurePlanPhysicalCapacity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePlanPhysicalCapacity'
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
    print(ConfigurePlanPhysicalCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

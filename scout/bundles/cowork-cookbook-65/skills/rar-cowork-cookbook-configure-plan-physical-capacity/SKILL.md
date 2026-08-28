---
name: "rar-cowork-cookbook-configure-plan-physical-capacity"
description: "Applies a bulk configuration change to plan physical capacity from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_physical_capacity", "rar_sha256": "4d2f687a0069a4c043674b81583e1ee2a230d3b105f1e806b7c8d478a1a1b0e7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_plan_physical_capacity_agent.py` and embedded as the fenced Python below (sha256 4d2f687a0069a4c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_plan_physical_capacity_agent.py` first:

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
    "version": '2.0.0',
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

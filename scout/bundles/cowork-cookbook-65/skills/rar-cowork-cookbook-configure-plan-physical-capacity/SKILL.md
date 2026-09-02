---
name: "rar-cowork-cookbook-configure-plan-physical-capacity"
description: "Applies a bulk configuration change to plan physical capacity from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_plan_physical_capacity", "rar_sha256": "4d2f687a0069a4c043674b81583e1ee2a230d3b105f1e806b7c8d478a1a1b0e7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_plan_physical_capacity_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-plan-physical-capacity:c4bd8572930d139dd67a5de366f9a9ea5bd69bbd04bdb0b1aaa1c46350105051", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_plan_physical_capacity`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_plan_physical_capacity_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

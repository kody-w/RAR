---
name: "rar-cowork-cookbook-configure-schedule-frontline-workers"
description: "Applies a bulk configuration change to schedule frontline workers from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_schedule_frontline_workers", "rar_sha256": "24c98af707d8650c19bcb803c5ece6cdb50244b00459f5d2c66fd390850fc6d6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_schedule_frontline_workers`. The original RAPP
agent is preserved byte-for-byte in `configure_schedule_frontline_workers_agent.py` and in the RCI capsule.

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

Schedule frontline workers Configuration Bulk Setup — Applies a bulk configuration change to schedule frontline workers from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-schedule-frontline-workers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_schedule_frontline_workers_agent.py` and embedded as the fenced Python below (sha256 24c98af707d8650c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_schedule_frontline_workers_agent.py` first:

```bash
python3 configure_schedule_frontline_workers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_schedule_frontline_workers_agent.py   # or on stdin
python3 configure_schedule_frontline_workers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule frontline workers Configuration Bulk Setup — Applies a bulk configuration change to schedule frontline workers from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-schedule-frontline-workers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_schedule_frontline_workers',
    "version": '2.0.1',
    "display_name": 'Schedule frontline workers Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to schedule frontline workers from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-schedule-frontline-workers',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-schedule-frontline-workers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2dea52d7fe335355',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/schedule-frontline-workers'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-schedule-frontline-workers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureScheduleFrontlineWorkers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureScheduleFrontlineWorkers'
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
    print(ConfigureScheduleFrontlineWorkers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

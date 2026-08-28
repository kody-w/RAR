---
name: "rar-cowork-cookbook-configure-schedule-frontline-workers"
description: "Applies a bulk configuration change to schedule frontline workers from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_schedule_frontline_workers", "rar_sha256": "730b4142576e0fa26e488a9d3c6eed1ec4451e1f0ab0dc5029c1c9a937db0f3e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_schedule_frontline_workers_agent.py` and embedded as the fenced Python below (sha256 730b4142576e0fa2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_schedule_frontline_workers_agent.py` first:

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
    "version": '2.0.0',
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

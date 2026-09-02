---
name: "rar-cowork-cookbook-configure-schedule-frontline-workers"
description: "Applies a bulk configuration change to schedule frontline workers from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_schedule_frontline_workers", "rar_sha256": "730b4142576e0fa26e488a9d3c6eed1ec4451e1f0ab0dc5029c1c9a937db0f3e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_schedule_frontline_workers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-schedule-frontline-workers:16e4d7751da87b8953965193732a417c82ec671e23f7884296c7cb1e5752e13d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_schedule_frontline_workers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_schedule_frontline_workers_agent.py` is
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

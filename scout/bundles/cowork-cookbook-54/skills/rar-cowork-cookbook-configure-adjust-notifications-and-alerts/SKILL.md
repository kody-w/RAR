---
name: "rar-cowork-cookbook-configure-adjust-notifications-and-alerts"
description: "Applies a bulk configuration change to adjust notifications and alerts from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_adjust_notifications_and_alerts", "rar_sha256": "8447bc2d87b01439368247670a26e34e13ae8e2f43adc7dcb3c1f5ec7d6c0422", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_adjust_notifications_and_alerts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-adjust-notifications-and-alerts:e26526e37996a965d24bd33ebc0a3212f78353e754c42568b3aff5b72b88a988", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_adjust_notifications_and_alerts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_adjust_notifications_and_alerts_agent.py` is
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

Adjust notifications and alerts Configuration Bulk Setup — Applies a bulk configuration change to adjust notifications and alerts from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-adjust-notifications-and-alerts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_adjust_notifications_and_alerts_agent.py` and embedded as the fenced Python below (sha256 8447bc2d87b01439…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_adjust_notifications_and_alerts_agent.py` first:

```bash
python3 configure_adjust_notifications_and_alerts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_adjust_notifications_and_alerts_agent.py   # or on stdin
python3 configure_adjust_notifications_and_alerts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Adjust notifications and alerts Configuration Bulk Setup — Applies a bulk configuration change to adjust notifications and alerts from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-adjust-notifications-and-alerts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_adjust_notifications_and_alerts',
    "version": '2.0.0',
    "display_name": 'Adjust notifications and alerts Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to adjust notifications and alerts from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-adjust-notifications-and-alerts',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-adjust-notifications-and-alerts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '263a6a2962d62d7c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/adjust-notifications-and-alerts'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-adjust-notifications-and-alerts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAdjustNotificationsAndAlerts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAdjustNotificationsAndAlerts'
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
    print(ConfigureAdjustNotificationsAndAlerts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

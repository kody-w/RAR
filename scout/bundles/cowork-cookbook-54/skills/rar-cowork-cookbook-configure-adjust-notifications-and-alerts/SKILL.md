---
name: "rar-cowork-cookbook-configure-adjust-notifications-and-alerts"
description: "Applies a bulk configuration change to adjust notifications and alerts from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_adjust_notifications_and_alerts", "rar_sha256": "8447bc2d87b01439368247670a26e34e13ae8e2f43adc7dcb3c1f5ec7d6c0422", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_adjust_notifications_and_alerts`. The original RAPP
agent is preserved byte-for-byte in `configure_adjust_notifications_and_alerts_agent.py` and in the RCI capsule.

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

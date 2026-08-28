---
name: "rar-cowork-cookbook-configure-adjust-notifications-and-alerts"
description: "Applies a bulk configuration change to adjust notifications and alerts from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_adjust_notifications_and_alerts", "rar_sha256": "6e8a52528983ccab3306031ccef179628f493d229a243b590040c9e384654c85", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_adjust_notifications_and_alerts_agent.py` and embedded as the fenced Python below (sha256 6e8a52528983ccab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_adjust_notifications_and_alerts_agent.py` first:

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
    "version": '2.0.1',
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

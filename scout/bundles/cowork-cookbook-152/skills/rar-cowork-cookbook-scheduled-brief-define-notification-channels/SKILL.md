---
name: "rar-cowork-cookbook-scheduled-brief-define-notification-channels"
description: "Schedulable morning-brief email summarizing define notification channels for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_notification_channels", "rar_sha256": "b6ecd95608ed0e439c9ade6b007394f10df0b09fc0be3c0266f47b778bf0f6af", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_notification_channels`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_notification_channels_agent.py` and in the RCI capsule.

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

Define notification channels Scheduled Email Brief — Schedulable morning-brief email summarizing define notification channels for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-notification-channels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_notification_channels_agent.py` and embedded as the fenced Python below (sha256 b6ecd95608ed0e43…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_notification_channels_agent.py` first:

```bash
python3 scheduled_brief_define_notification_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_notification_channels_agent.py   # or on stdin
python3 scheduled_brief_define_notification_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define notification channels Scheduled Email Brief — Schedulable morning-brief email summarizing define notification channels for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-notification-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_notification_channels',
    "version": '2.0.1',
    "display_name": 'Define notification channels Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define notification channels for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-notification-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-notification-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '822f222251c3244e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/define-notification-channels'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-define-notification-channels', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDefineNotificationChannels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineNotificationChannels'
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
    print(ScheduledBriefDefineNotificationChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

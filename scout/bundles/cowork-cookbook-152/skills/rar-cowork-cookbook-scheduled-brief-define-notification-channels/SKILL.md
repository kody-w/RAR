---
name: "rar-cowork-cookbook-scheduled-brief-define-notification-channels"
description: "Schedulable morning-brief email summarizing define notification channels for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_notification_channels", "rar_sha256": "ae402389888c1ab7778ac3389f95c35f4be1d3446c178cf0ee852c739d0f5a6c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_notification_channels_agent.py` and embedded as the fenced Python below (sha256 ae402389888c1ab7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_notification_channels_agent.py` first:

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
    "version": '2.0.0',
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

---
name: "rar-cowork-cookbook-scheduled-brief-define-notification-channels"
description: "Schedulable morning-brief email summarizing define notification channels for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_notification_channels", "rar_sha256": "ae402389888c1ab7778ac3389f95c35f4be1d3446c178cf0ee852c739d0f5a6c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_notification_channels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-notification-channels:7188fa650ceb2f3991dc50fadc943ef212ba7466b30539be1eabb4fb63bb3481", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_notification_channels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_notification_channels_agent.py` is
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

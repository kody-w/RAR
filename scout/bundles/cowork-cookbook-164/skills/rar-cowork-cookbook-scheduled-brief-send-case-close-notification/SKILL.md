---
name: "rar-cowork-cookbook-scheduled-brief-send-case-close-notification"
description: "Schedulable morning-brief email summarizing send case close notification for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_send_case_close_notification", "rar_sha256": "0bb76737f05b5718d7c862553aa1f42a68a5534f68e7f73f0b6be468713e1dc0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_send_case_close_notification_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-send-case-close-notification:5f2c9c19e79d3237645760e3cb40eb5c3c18006daa33f919fcfbfe5f58d8124c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_send_case_close_notification`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_send_case_close_notification_agent.py` is
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

Send case close notification Scheduled Email Brief — Schedulable morning-brief email summarizing send case close notification for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-send-case-close-notification
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_send_case_close_notification_agent.py` and embedded as the fenced Python below (sha256 0bb76737f05b5718…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_send_case_close_notification_agent.py` first:

```bash
python3 scheduled_brief_send_case_close_notification_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_send_case_close_notification_agent.py   # or on stdin
python3 scheduled_brief_send_case_close_notification_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send case close notification Scheduled Email Brief — Schedulable morning-brief email summarizing send case close notification for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-send-case-close-notification
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_send_case_close_notification',
    "version": '2.0.0',
    "display_name": 'Send case close notification Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing send case close notification for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-send-case-close-notification',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-send-case-close-notification',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '90574b1db3f34fd9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/send-case-close-notification'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-send-case-close-notification', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefSendCaseCloseNotification(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefSendCaseCloseNotification'
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
    print(ScheduledBriefSendCaseCloseNotification().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

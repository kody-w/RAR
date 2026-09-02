---
name: "rar-cat-agent-skills-conditional-chat-reminder"
description: "Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conditional_chat_reminder", "rar_sha256": "2ff960cf9799c7e9336fd4eea85e8acf88d5d9ebf2ff5c3a52dce0da0f069171", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "conditional_chat_reminder_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/conditional-chat-reminder:c6e9b38300f6bac337831cfd9cfc2bf57e2abaabd89b828001ac3a9a120ddee3", "kind": "skill"}, "version": "2.0.0", "author": "Giorgio Ughini", "tags": ["automation", "teams", "reminders", "follow_up", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/conditional_chat_reminder`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `conditional_chat_reminder_agent.py` is
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

Conditional Chat Reminder — Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#conditional-chat-reminder
  Upstream author: Giorgio Ughini
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `conditional_chat_reminder_agent.py` and embedded as the fenced Python below (sha256 2ff960cf9799c7e9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `conditional_chat_reminder_agent.py` first:

```bash
python3 conditional_chat_reminder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 conditional_chat_reminder_agent.py   # or on stdin
python3 conditional_chat_reminder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conditional Chat Reminder — Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#conditional-chat-reminder
  Upstream author: Giorgio Ughini
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/conditional_chat_reminder',
    "version": '2.0.0',
    "display_name": 'Conditional Chat Reminder',
    "description": 'Schedule a Teams reminder that sends only when the expected person has not already posted a relevant update.',
    "author": 'Giorgio Ughini',
    "tags": ['automation', 'teams', 'reminders', 'follow_up', 'productivity'],
    "category": 'integrations',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'conditional-chat-reminder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#conditional-chat-reminder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'a519bd3119d92722',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Scout'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConditionalChatReminder(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConditionalChatReminder'
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
    print(ConditionalChatReminder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

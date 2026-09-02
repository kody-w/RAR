---
name: "rar-cat-agent-skills-awaiting-reply"
description: "A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/awaiting_reply", "rar_sha256": "fbd75b3e3e375301db703b7b0f2205c47d0a33f8b137b721c7380dfac54b5193", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "awaiting_reply_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/awaiting-reply:048382f79b64c28c04eb4986125a21db4b06a58ebcb4278c112b603528ebc4a1", "kind": "skill"}, "version": "2.0.0", "author": "Allan De Castro", "tags": ["email", "follow_up", "automation", "productivity", "inbox", "reminder", "multilingual"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/awaiting_reply`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `awaiting_reply_agent.py` is
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

Awaiting Reply — A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#awaiting-reply
  Upstream author: Allan De Castro
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `awaiting_reply_agent.py` and embedded as the fenced Python below (sha256 fbd75b3e3e375301…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `awaiting_reply_agent.py` first:

```bash
python3 awaiting_reply_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 awaiting_reply_agent.py   # or on stdin
python3 awaiting_reply_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Awaiting Reply — A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#awaiting-reply
  Upstream author: Allan De Castro
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/awaiting_reply',
    "version": '2.0.0',
    "display_name": 'Awaiting Reply',
    "description": "A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends.",
    "author": 'Allan De Castro',
    "tags": ['email', 'follow_up', 'automation', 'productivity', 'inbox', 'reminder', 'multilingual'],
    "category": 'productivity',
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
        "upstream_slug": 'awaiting-reply',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#awaiting-reply',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd269450ca78b236a',
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.636, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'kind:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AwaitingReply(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AwaitingReply'
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
    print(AwaitingReply().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

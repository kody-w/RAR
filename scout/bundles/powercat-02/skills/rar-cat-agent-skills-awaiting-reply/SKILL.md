---
name: "rar-cat-agent-skills-awaiting-reply"
description: "A weekday-morning Scout automation that finds emails you sent that asked for something and never got an answer, reports how many are waiting, and prepares follow-up drafts in each thread's own language that it never sends."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/awaiting_reply", "rar_sha256": "fbd75b3e3e375301db703b7b0f2205c47d0a33f8b137b721c7380dfac54b5193", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Allan De Castro", "tags": ["email", "follow_up", "automation", "productivity", "inbox", "reminder", "multilingual"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/awaiting_reply`. The original RAPP
agent is preserved byte-for-byte in `awaiting_reply_agent.py` and in the RCI capsule.

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

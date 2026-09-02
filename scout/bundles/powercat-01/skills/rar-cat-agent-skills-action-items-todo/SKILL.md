---
name: "rar-cat-agent-skills-action-items-todo"
description: "Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/action_items_todo", "rar_sha256": "9d5f391acb6541f4471f568aae5a21b0216275c8609ea54200778c77c080756d", "source_kind": "rar-agent", "source_commit": "657d2bb31e7d75b8fe4216443a5336cb035c07c9", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "action_items_todo_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/action-items-todo:639882e7e147a46153000177e067b787807de4891db8dc0b73e137e6bdf88f04", "kind": "skill"}, "version": "2.0.0", "author": "Matteo Pagani", "tags": ["productivity", "automation", "tasks", "teams", "email", "meetings", "microsoft_365", "action_items"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/action_items_todo`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `action_items_todo_agent.py` is
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

Action Items to To Do — Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#action-items-todo
  Upstream author: Matteo Pagani
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `action_items_todo_agent.py` and embedded as the fenced Python below (sha256 9d5f391acb6541f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `action_items_todo_agent.py` first:

```bash
python3 action_items_todo_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 action_items_todo_agent.py   # or on stdin
python3 action_items_todo_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Action Items to To Do — Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#action-items-todo
  Upstream author: Matteo Pagani
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/action_items_todo',
    "version": '2.0.0',
    "display_name": 'Action Items to To Do',
    "description": 'Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link.',
    "author": 'Matteo Pagani',
    "tags": ['productivity', 'automation', 'tasks', 'teams', 'email', 'meetings', 'microsoft_365', 'action_items'],
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
        "upstream_slug": 'action-items-todo',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#action-items-todo',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ad7ddb14bd369108',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:email'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ActionItemsTodo(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ActionItemsTodo'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ActionItemsTodo().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

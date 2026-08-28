---
name: "rar-cat-agent-skills-action-items-todo"
description: "Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/action_items_todo", "rar_sha256": "9d5f391acb6541f4471f568aae5a21b0216275c8609ea54200778c77c080756d", "source_kind": "rar-agent", "source_commit": "657d2bb31e7d75b8fe4216443a5336cb035c07c9", "version": "2.0.0", "author": "Matteo Pagani", "tags": ["productivity", "automation", "tasks", "teams", "email", "meetings", "microsoft_365", "action_items"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/action_items_todo`. The original RAPP
agent is preserved byte-for-byte in `action_items_todo_agent.py` and in the RCI capsule.

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

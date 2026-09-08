---
name: "rar-cat-agent-skills-action-items-todo"
description: "Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/action_items_todo", "rar_sha256": "1c5c79a035333e0169c363cc1f60b4849ce2a8297ef496801fa6e95e5988e3ed", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Matteo Pagani", "tags": ["productivity", "automation", "tasks", "teams", "email", "meetings", "microsoft_365", "action_items"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `action_items_todo_agent.py` and embedded as the fenced Python below (sha256 1c5c79a035333e01…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `action_items_todo_agent.py` first:

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
    "version": '3.0.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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

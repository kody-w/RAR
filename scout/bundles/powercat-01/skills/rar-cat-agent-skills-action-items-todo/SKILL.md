---
name: "rar-cat-agent-skills-action-items-todo"
description: "Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/action_items_todo", "rar_sha256": "e25f86131c9f129f445e79151a7dc8cce0859a7e1025062b538fc7c5fb142929", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Matteo Pagani", "tags": ["productivity", "automation", "tasks", "teams", "email", "meetings", "microsoft_365", "action_items"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `action_items_todo_agent.py` and embedded as the fenced Python below (sha256 e25f86131c9f129f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `action_items_todo_agent.py` first:

```bash
python3 action_items_todo_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 action_items_todo_agent.py   # or on stdin
python3 action_items_todo_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/action_items_todo_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/action_items_todo_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/action_items_todo/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

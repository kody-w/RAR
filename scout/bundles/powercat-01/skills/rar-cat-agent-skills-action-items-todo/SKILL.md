---
name: "rar-cat-agent-skills-action-items-todo"
description: "Watches your Teams chats, meeting transcripts, and Outlook mail for things people actually asked you to do, and files each one as a Microsoft To Do task with a due date, priority, and source link."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/action_items_todo", "rar_sha256": "e25f86131c9f129f445e79151a7dc8cce0859a7e1025062b538fc7c5fb142929", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Matteo Pagani", "tags": ["productivity", "automation", "tasks", "teams", "email", "meetings", "microsoft_365", "action_items"]}
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

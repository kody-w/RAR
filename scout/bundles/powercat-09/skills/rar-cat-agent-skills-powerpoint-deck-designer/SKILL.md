---
name: "rar-cat-agent-skills-powerpoint-deck-designer"
description: "Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/powerpoint_deck_designer", "rar_sha256": "eb611944514156ad3588142f26e0526500af98a8a80fd3ce408ee6b0451c6c80", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "powerpoint_deck_designer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/powerpoint-deck-designer:41a1e0c5a5f8702f34a4d08e195aa85a0feaa822e26a068a0fffbbac43857fd5", "kind": "skill"}, "version": "2.0.0", "author": "Ferran Chopo", "tags": ["powerpoint", "presentations", "python", "charts"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/powerpoint_deck_designer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `powerpoint_deck_designer_agent.py` is
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

PowerPoint Deck Designer — Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#powerpoint-deck-designer
  Upstream author: Ferran Chopo
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `powerpoint_deck_designer_agent.py` and embedded as the fenced Python below (sha256 eb611944514156ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `powerpoint_deck_designer_agent.py` first:

```bash
python3 powerpoint_deck_designer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 powerpoint_deck_designer_agent.py   # or on stdin
python3 powerpoint_deck_designer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
PowerPoint Deck Designer — Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#powerpoint-deck-designer
  Upstream author: Ferran Chopo
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/powerpoint_deck_designer',
    "version": '2.0.0',
    "display_name": 'PowerPoint Deck Designer',
    "description": "Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants).",
    "author": 'Ferran Chopo',
    "tags": ['powerpoint', 'presentations', 'python', 'charts'],
    "category": 'devtools',
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
        "upstream_slug": 'powerpoint-deck-designer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#powerpoint-deck-designer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '13a4c71ffb14ed1c',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations', 'word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PowerpointDeckDesigner(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PowerpointDeckDesigner'
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
    print(PowerpointDeckDesigner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

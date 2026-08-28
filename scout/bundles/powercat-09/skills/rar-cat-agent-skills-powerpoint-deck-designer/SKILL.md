---
name: "rar-cat-agent-skills-powerpoint-deck-designer"
description: "Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/powerpoint_deck_designer", "rar_sha256": "eb611944514156ad3588142f26e0526500af98a8a80fd3ce408ee6b0451c6c80", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Ferran Chopo", "tags": ["powerpoint", "presentations", "python", "charts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/powerpoint_deck_designer`. The original RAPP
agent is preserved byte-for-byte in `powerpoint_deck_designer_agent.py` and in the RCI capsule.

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

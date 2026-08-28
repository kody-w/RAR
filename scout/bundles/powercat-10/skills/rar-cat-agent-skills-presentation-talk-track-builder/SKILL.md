---
name: "rar-cat-agent-skills-presentation-talk-track-builder"
description: "Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/presentation_talk_track_builder", "rar_sha256": "0b292d4a5a102713a81298e77e673258e3e9dc9d67595b37b4afadf58449e531", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Jagmeet Chabra", "tags": ["presentations", "speaker_notes", "powerpoint", "writing", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/presentation_talk_track_builder`. The original RAPP
agent is preserved byte-for-byte in `presentation_talk_track_builder_agent.py` and in the RCI capsule.

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

Presentation Talk Track Builder — Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#presentation-talk-track-builder
  Upstream author: Jagmeet Chabra
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `presentation_talk_track_builder_agent.py` and embedded as the fenced Python below (sha256 0b292d4a5a102713…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `presentation_talk_track_builder_agent.py` first:

```bash
python3 presentation_talk_track_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 presentation_talk_track_builder_agent.py   # or on stdin
python3 presentation_talk_track_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Presentation Talk Track Builder — Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#presentation-talk-track-builder
  Upstream author: Jagmeet Chabra
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/presentation_talk_track_builder',
    "version": '2.0.0',
    "display_name": 'Presentation Talk Track Builder',
    "description": 'Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content.',
    "author": 'Jagmeet Chabra',
    "tags": ['presentations', 'speaker_notes', 'powerpoint', 'writing', 'productivity'],
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
        "upstream_slug": 'presentation-talk-track-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#presentation-talk-track-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '10389b967a5e68a1',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations', 'tag:writing', 'word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PresentationTalkTrackBuilder(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PresentationTalkTrackBuilder'
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
    print(PresentationTalkTrackBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

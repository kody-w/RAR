---
name: "rar-cat-agent-skills-presentation-talk-track-builder"
description: "Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/presentation_talk_track_builder", "rar_sha256": "0b292d4a5a102713a81298e77e673258e3e9dc9d67595b37b4afadf58449e531", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "presentation_talk_track_builder_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/presentation-talk-track-builder:f16221796e51f3fa83948f3270e2977e48fa30a7a94c20220be602734062be3b", "kind": "skill"}, "version": "2.0.0", "author": "Jagmeet Chabra", "tags": ["presentations", "speaker_notes", "powerpoint", "writing", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/presentation_talk_track_builder`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `presentation_talk_track_builder_agent.py` is
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

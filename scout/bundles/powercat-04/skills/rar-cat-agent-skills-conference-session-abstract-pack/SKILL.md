---
name: "rar-cat-agent-skills-conference-session-abstract-pack"
description: "Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conference_session_abstract_pack", "rar_sha256": "1555f077ef0d78b201887122101980ce639036b47f08e647ccded556eebc4070", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Simon Owen", "tags": ["writing", "conference", "abstract", "speaking", "content", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/conference_session_abstract_pack`. The original RAPP
agent is preserved byte-for-byte in `conference_session_abstract_pack_agent.py` and in the RCI capsule.

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

Conference Session Abstract Pack — Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#conference-session-abstract-pack
  Upstream author: Simon Owen
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `conference_session_abstract_pack_agent.py` and embedded as the fenced Python below (sha256 1555f077ef0d78b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `conference_session_abstract_pack_agent.py` first:

```bash
python3 conference_session_abstract_pack_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 conference_session_abstract_pack_agent.py   # or on stdin
python3 conference_session_abstract_pack_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conference Session Abstract Pack — Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#conference-session-abstract-pack
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/conference_session_abstract_pack',
    "version": '1.1.0',
    "display_name": 'Conference Session Abstract Pack',
    "description": 'Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic.',
    "author": 'Simon Owen',
    "tags": ['writing', 'conference', 'abstract', 'speaking', 'content', 'productivity'],
    "category": 'general',
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
        "upstream_slug": 'conference-session-abstract-pack',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#conference-session-abstract-pack',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '79b0788cb04dc619',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ConferenceSessionAbstractPack(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConferenceSessionAbstractPack'
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
    print(ConferenceSessionAbstractPack().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

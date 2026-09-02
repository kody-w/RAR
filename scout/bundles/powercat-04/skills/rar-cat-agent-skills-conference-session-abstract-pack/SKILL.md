---
name: "rar-cat-agent-skills-conference-session-abstract-pack"
description: "Create CFP-ready talk titles, abstracts, takeaways, speaker notes, and submission copy from a topic."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/conference_session_abstract_pack", "rar_sha256": "1555f077ef0d78b201887122101980ce639036b47f08e647ccded556eebc4070", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "conference_session_abstract_pack_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/conference-session-abstract-pack:6c4b171c564d217ef4ee170f7d910b5f013fe1161cedb2e0edabb87dd303cef2", "kind": "skill"}, "version": "1.1.0", "author": "Simon Owen", "tags": ["writing", "conference", "abstract", "speaking", "content", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/conference_session_abstract_pack`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `conference_session_abstract_pack_agent.py` is
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

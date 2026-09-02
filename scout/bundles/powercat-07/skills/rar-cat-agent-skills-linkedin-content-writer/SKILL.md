---
name: "rar-cat-agent-skills-linkedin-content-writer"
description: "Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_writer", "rar_sha256": "2e8b65f13ef8f8b4f9470b5fcd78960b3d95028cd00408c86e07adcf1724fab5", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "linkedin_content_writer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/linkedin-content-writer:a33a80047491b6aae05cf062faf7201bb3098ff0a2af36c7de923371ef37b8cf", "kind": "skill"}, "version": "2.0.1", "author": "Becky Still, Digital Boop Ltd", "tags": ["linkedin", "social_media", "writing", "content"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/linkedin_content_writer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `linkedin_content_writer_agent.py` is
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

LinkedIn Content Writer — Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-writer
  Upstream author: Becky Still, Digital Boop Ltd
  Upstream version: 1.0.1
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `linkedin_content_writer_agent.py` and embedded as the fenced Python below (sha256 2e8b65f13ef8f8b4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `linkedin_content_writer_agent.py` first:

```bash
python3 linkedin_content_writer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 linkedin_content_writer_agent.py   # or on stdin
python3 linkedin_content_writer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
LinkedIn Content Writer — Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#linkedin-content-writer
  Upstream author: Becky Still, Digital Boop Ltd
  Upstream version: 1.0.1
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/linkedin_content_writer',
    "version": '2.0.1',
    "display_name": 'LinkedIn Content Writer',
    "description": 'Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence.',
    "author": 'Becky Still, Digital Boop Ltd',
    "tags": ['linkedin', 'social_media', 'writing', 'content'],
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
        "upstream_slug": 'linkedin-content-writer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#linkedin-content-writer',
        "upstream_version": '1.0.1',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b67b1c225f5d7237',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class LinkedinContentWriter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'LinkedinContentWriter'
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
    print(LinkedinContentWriter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

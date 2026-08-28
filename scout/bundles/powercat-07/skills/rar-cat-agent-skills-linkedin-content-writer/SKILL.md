---
name: "rar-cat-agent-skills-linkedin-content-writer"
description: "Create credible LinkedIn content from facts, notes or drafts, with configurable voice and no invented evidence."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/linkedin_content_writer", "rar_sha256": "2e8b65f13ef8f8b4f9470b5fcd78960b3d95028cd00408c86e07adcf1724fab5", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.1", "author": "Becky Still, Digital Boop Ltd", "tags": ["linkedin", "social_media", "writing", "content"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/linkedin_content_writer`. The original RAPP
agent is preserved byte-for-byte in `linkedin_content_writer_agent.py` and in the RCI capsule.

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

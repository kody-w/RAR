---
name: "rar-cat-agent-skills-whiteboard-to-infographic"
description: "Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/whiteboard_to_infographic", "rar_sha256": "b4b6836d3126428ba7cb3ba517721d886362be50d8ef10c3de03706a275330e5", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "whiteboard_to_infographic_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/whiteboard-to-infographic:8085836a0d483347849aa37dc5e2407bd8400ea8d1529047e85cc1566160708e", "kind": "skill"}, "version": "2.0.0", "author": "Andy Zehr", "tags": ["infographic", "whiteboard", "powerpoint", "presentations", "diagrams", "design", "consulting"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/whiteboard_to_infographic`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `whiteboard_to_infographic_agent.py` is
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

Whiteboard to Infographic — Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic
  Upstream author: Andy Zehr
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `whiteboard_to_infographic_agent.py` and embedded as the fenced Python below (sha256 b4b6836d3126428b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `whiteboard_to_infographic_agent.py` first:

```bash
python3 whiteboard_to_infographic_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 whiteboard_to_infographic_agent.py   # or on stdin
python3 whiteboard_to_infographic_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Whiteboard to Infographic — Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic
  Upstream author: Andy Zehr
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/whiteboard_to_infographic',
    "version": '2.0.0',
    "display_name": 'Whiteboard to Infographic',
    "description": "Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.",
    "author": 'Andy Zehr',
    "tags": ['infographic', 'whiteboard', 'powerpoint', 'presentations', 'diagrams', 'design', 'consulting'],
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
        "upstream_slug": 'whiteboard-to-infographic',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '8ba98fb5f2eb84f8',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.571, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class WhiteboardToInfographic(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WhiteboardToInfographic'
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
    print(WhiteboardToInfographic().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

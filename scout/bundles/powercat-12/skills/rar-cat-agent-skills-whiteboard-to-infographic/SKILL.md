---
name: "rar-cat-agent-skills-whiteboard-to-infographic"
description: "Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/whiteboard_to_infographic", "rar_sha256": "b4b6836d3126428ba7cb3ba517721d886362be50d8ef10c3de03706a275330e5", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Andy Zehr", "tags": ["infographic", "whiteboard", "powerpoint", "presentations", "diagrams", "design", "consulting"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/whiteboard_to_infographic`. The original RAPP
agent is preserved byte-for-byte in `whiteboard_to_infographic_agent.py` and in the RCI capsule.

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

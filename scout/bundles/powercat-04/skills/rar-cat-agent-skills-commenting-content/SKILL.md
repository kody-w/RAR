---
name: "rar-cat-agent-skills-commenting-content"
description: "Comments Word or PowerPoint files with Comments."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/commenting_content", "rar_sha256": "187b091fcba2f8fb7bbd54d2846dd5fa025aafe300aaf05cb4e79baa06416c15", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/commenting_content`. The original RAPP
agent is preserved byte-for-byte in `commenting_content_agent.py` and in the RCI capsule.

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

Commenting Content — Comments Word or PowerPoint files with Comments.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#commenting-content
  Upstream author: AndrewHessMSFT
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commenting_content_agent.py` and embedded as the fenced Python below (sha256 187b091fcba2f8fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commenting_content_agent.py` first:

```bash
python3 commenting_content_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 commenting_content_agent.py   # or on stdin
python3 commenting_content_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Commenting Content — Comments Word or PowerPoint files with Comments.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#commenting-content
  Upstream author: AndrewHessMSFT
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/commenting_content',
    "version": '2.0.0',
    "display_name": 'Commenting Content',
    "description": 'Comments Word or PowerPoint files with Comments.',
    "author": 'AndrewHessMSFT',
    "tags": ['documents', 'productivity'],
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
        "upstream_slug": 'commenting-content',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#commenting-content',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'fcac24466182f80a',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class CommentingContent(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CommentingContent'
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
    print(CommentingContent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

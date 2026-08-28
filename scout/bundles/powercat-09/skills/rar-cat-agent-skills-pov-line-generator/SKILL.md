---
name: "rar-cat-agent-skills-pov-line-generator"
description: "Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pov_line_generator", "rar_sha256": "181aaa29ab74475fe1d1b73cbfec45f0cdd31f3016bbf34eabcaf3ec23213ded", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Simon Owen", "tags": ["writing", "positioning", "marketing", "content", "social_media"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/pov_line_generator`. The original RAPP
agent is preserved byte-for-byte in `pov_line_generator_agent.py` and in the RCI capsule.

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

POV Line Generator — Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pov-line-generator
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pov_line_generator_agent.py` and embedded as the fenced Python below (sha256 181aaa29ab74475f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pov_line_generator_agent.py` first:

```bash
python3 pov_line_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pov_line_generator_agent.py   # or on stdin
python3 pov_line_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
POV Line Generator — Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pov-line-generator
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/pov_line_generator',
    "version": '1.1.0',
    "display_name": 'POV Line Generator',
    "description": 'Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work.',
    "author": 'Simon Owen',
    "tags": ['writing', 'positioning', 'marketing', 'content', 'social_media'],
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
        "upstream_slug": 'pov-line-generator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#pov-line-generator',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'bf492abfe32d66ad',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing', 'word:generate'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PovLineGenerator(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PovLineGenerator'
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
    print(PovLineGenerator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

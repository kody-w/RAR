---
name: "rar-cat-agent-skills-pov-line-generator"
description: "Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pov_line_generator", "rar_sha256": "181aaa29ab74475fe1d1b73cbfec45f0cdd31f3016bbf34eabcaf3ec23213ded", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "pov_line_generator_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/pov-line-generator:a54cecad40aaa4bbf23937a474b975147bf60251155c58d1e5e305c0b88fec2a", "kind": "skill"}, "version": "1.1.0", "author": "Simon Owen", "tags": ["writing", "positioning", "marketing", "content", "social_media"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/pov_line_generator`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `pov_line_generator_agent.py` is
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

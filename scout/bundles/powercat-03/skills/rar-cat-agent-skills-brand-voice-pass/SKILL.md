---
name: "rar-cat-agent-skills-brand-voice-pass"
description: "Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_voice_pass", "rar_sha256": "3635849b3dcd5b55c5f9f9d6f3ec7e7a977033ca09ab57020fe9b172e8901cf4", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "brand_voice_pass_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/brand-voice-pass:173d55f46050dcd8ac8c30eb0403a27e51ee3cc6da3036ded66434000f3d1d1a", "kind": "skill"}, "version": "1.1.0", "author": "Simon Owen", "tags": ["writing", "content", "voice", "authoring", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/brand_voice_pass`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `brand_voice_pass_agent.py` is
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

Brand Voice Pass — Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#brand-voice-pass
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `brand_voice_pass_agent.py` and embedded as the fenced Python below (sha256 3635849b3dcd5b55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `brand_voice_pass_agent.py` first:

```bash
python3 brand_voice_pass_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 brand_voice_pass_agent.py   # or on stdin
python3 brand_voice_pass_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Brand Voice Pass — Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#brand-voice-pass
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/brand_voice_pass',
    "version": '1.1.0',
    "display_name": 'Brand Voice Pass',
    "description": 'Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing.',
    "author": 'Simon Owen',
    "tags": ['writing', 'content', 'voice', 'authoring', 'productivity'],
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
        "upstream_slug": 'brand-voice-pass',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#brand-voice-pass',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ab6312662367dcfc',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.8, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class BrandVoicePass(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BrandVoicePass'
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
    print(BrandVoicePass().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

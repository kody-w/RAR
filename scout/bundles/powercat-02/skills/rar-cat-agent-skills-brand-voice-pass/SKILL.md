---
name: "rar-cat-agent-skills-brand-voice-pass"
description: "Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_voice_pass", "rar_sha256": "3635849b3dcd5b55c5f9f9d6f3ec7e7a977033ca09ab57020fe9b172e8901cf4", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Simon Owen", "tags": ["writing", "content", "voice", "authoring", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/brand_voice_pass`. The original RAPP
agent is preserved byte-for-byte in `brand_voice_pass_agent.py` and in the RCI capsule.

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

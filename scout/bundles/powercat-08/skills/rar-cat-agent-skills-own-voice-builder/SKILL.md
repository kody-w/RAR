---
name: "rar-cat-agent-skills-own-voice-builder"
description: "Mines your sent emails to extract your real writing voice \u2014 languages, tone modes, structure, vocabulary, taboo phrases \u2014 and generates a personal voice skill that makes every email and Teams draft sound like you."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/own_voice_builder", "rar_sha256": "c94c678de5a3bd69cf2f1f4e4b50b38cdd931bfcd23aeec345fb3263b86df1b0", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Marcel", "tags": ["writing", "voice", "email", "teams", "productivity", "microsoft_365"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/own_voice_builder`. The original RAPP
agent is preserved byte-for-byte in `own_voice_builder_agent.py` and in the RCI capsule.

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

Own Voice Builder — Mines your sent emails to extract your real writing voice — languages, tone modes, structure, vocabulary, taboo phrases — and generates a personal voice skill that makes every email and Teams draft sound like you.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#own-voice-builder
  Upstream author: Marcel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `own_voice_builder_agent.py` and embedded as the fenced Python below (sha256 c94c678de5a3bd69…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `own_voice_builder_agent.py` first:

```bash
python3 own_voice_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 own_voice_builder_agent.py   # or on stdin
python3 own_voice_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Own Voice Builder — Mines your sent emails to extract your real writing voice — languages, tone modes, structure, vocabulary, taboo phrases — and generates a personal voice skill that makes every email and Teams draft sound like you.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#own-voice-builder
  Upstream author: Marcel
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/own_voice_builder',
    "version": '2.0.0',
    "display_name": 'Own Voice Builder',
    "description": 'Mines your sent emails to extract your real writing voice — languages, tone modes, structure, vocabulary, taboo phrases — and generates a personal voice skill that makes every email and Teams draft sound like you.',
    "author": 'Marcel',
    "tags": ['writing', 'voice', 'email', 'teams', 'productivity', 'microsoft_365'],
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
        "upstream_slug": 'own-voice-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#own-voice-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '45c780ef5e1ffdad',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.714, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:email', 'tag:writing', 'word:draft'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class OwnVoiceBuilder(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'OwnVoiceBuilder'
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
    print(OwnVoiceBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

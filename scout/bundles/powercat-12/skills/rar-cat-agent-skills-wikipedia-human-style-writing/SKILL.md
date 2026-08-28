---
name: "rar-cat-agent-skills-wikipedia-human-style-writing"
description: "Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wikipedia_human_style_writing", "rar_sha256": "1f50f40dc28b1760c266836dc179d8cb5be8ca2151a339e00fe612af9c163131", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Chris Garty", "tags": ["writing", "content", "editing", "style", "humanize", "ai_detection", "wikipedia"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/wikipedia_human_style_writing`. The original RAPP
agent is preserved byte-for-byte in `wikipedia_human_style_writing_agent.py` and in the RCI capsule.

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

Wikipedia Human Style Writing — Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing
  Upstream author: Chris Garty
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wikipedia_human_style_writing_agent.py` and embedded as the fenced Python below (sha256 1f50f40dc28b1760…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wikipedia_human_style_writing_agent.py` first:

```bash
python3 wikipedia_human_style_writing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wikipedia_human_style_writing_agent.py   # or on stdin
python3 wikipedia_human_style_writing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Wikipedia Human Style Writing — Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing
  Upstream author: Chris Garty
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/wikipedia_human_style_writing',
    "version": '1.1.0',
    "display_name": 'Wikipedia Human Style Writing',
    "description": "Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.",
    "author": 'Chris Garty',
    "tags": ['writing', 'content', 'editing', 'style', 'humanize', 'ai_detection', 'wikipedia'],
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
        "upstream_slug": 'wikipedia-human-style-writing',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4a55ea6837b037ca',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing', 'word:draft'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class WikipediaHumanStyleWriting(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WikipediaHumanStyleWriting'
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
    print(WikipediaHumanStyleWriting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

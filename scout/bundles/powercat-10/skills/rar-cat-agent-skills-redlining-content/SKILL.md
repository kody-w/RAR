---
name: "rar-cat-agent-skills-redlining-content"
description: "Redlines a document based on changes from a template with Track Changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/redlining_content", "rar_sha256": "1196f5449b1e765cd968e70f0a5568c40598968414f4ffb10380e02b9bdfed98", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/redlining_content`. The original RAPP
agent is preserved byte-for-byte in `redlining_content_agent.py` and in the RCI capsule.

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

Redlining Content — Redlines a document based on changes from a template with Track Changes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#redlining-content
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `redlining_content_agent.py` and embedded as the fenced Python below (sha256 1196f5449b1e765c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `redlining_content_agent.py` first:

```bash
python3 redlining_content_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 redlining_content_agent.py   # or on stdin
python3 redlining_content_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Redlining Content — Redlines a document based on changes from a template with Track Changes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#redlining-content
  Upstream author: AndrewHessMSFT
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/redlining_content',
    "version": '2.0.0',
    "display_name": 'Redlining Content',
    "description": 'Redlines a document based on changes from a template with Track Changes.',
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
        "upstream_slug": 'redlining-content',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#redlining-content',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '1c2ec4d219101bd1',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class RedliningContent(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RedliningContent'
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
    print(RedliningContent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

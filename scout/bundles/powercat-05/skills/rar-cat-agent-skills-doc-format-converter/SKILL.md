---
name: "rar-cat-agent-skills-doc-format-converter"
description: "Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text \u2014 fully offline, using only the libraries already in the agent sandbox."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/doc_format_converter", "rar_sha256": "fe4a32bfd496ea42fe68d4815d3f6835297ca9434e9a3c72129873a4b5ea0f3a", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Andreas Adner", "tags": ["documents", "conversion", "markdown", "pdf", "office", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/doc_format_converter`. The original RAPP
agent is preserved byte-for-byte in `doc_format_converter_agent.py` and in the RCI capsule.

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

Universal Document Converter — Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text — fully offline, using only the libraries already in the agent sandbox.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#doc-format-converter
  Upstream author: Andreas Adner
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `doc_format_converter_agent.py` and embedded as the fenced Python below (sha256 fe4a32bfd496ea42…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `doc_format_converter_agent.py` first:

```bash
python3 doc_format_converter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 doc_format_converter_agent.py   # or on stdin
python3 doc_format_converter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Universal Document Converter — Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text — fully offline, using only the libraries already in the agent sandbox.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#doc-format-converter
  Upstream author: Andreas Adner
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/doc_format_converter',
    "version": '2.0.0',
    "display_name": 'Universal Document Converter',
    "description": 'Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text — fully offline, using only the libraries already in the agent sandbox.',
    "author": 'Andreas Adner',
    "tags": ['documents', 'conversion', 'markdown', 'pdf', 'office', 'scripts'],
    "category": 'devtools',
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
        "upstream_slug": 'doc-format-converter',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#doc-format-converter',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd1c0d69a8989af49',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.375, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class DocFormatConverter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DocFormatConverter'
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
    print(DocFormatConverter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

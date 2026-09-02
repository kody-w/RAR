---
name: "rar-cat-agent-skills-doc-format-converter"
description: "Convert documents between Markdown, HTML, PDF, Word, PowerPoint, Excel/CSV and text \u2014 fully offline, using only the libraries already in the agent sandbox."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/doc_format_converter", "rar_sha256": "fe4a32bfd496ea42fe68d4815d3f6835297ca9434e9a3c72129873a4b5ea0f3a", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "doc_format_converter_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/doc-format-converter:d3f9b152b65dbfb2c24473f2f9093c0a74ae690e9864b46db4acf837cb0e546e", "kind": "skill"}, "version": "2.0.0", "author": "Andreas Adner", "tags": ["documents", "conversion", "markdown", "pdf", "office", "scripts"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/doc_format_converter`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `doc_format_converter_agent.py` is
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

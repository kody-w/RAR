---
name: "rar-cat-agent-skills-anonymised-case-study-writer"
description: "Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/anonymised_case_study_writer", "rar_sha256": "acca33c8954fc23a9d6b76b4ab200a7bf5a076cd44c2200f1c42565e98f20361", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Simon Owen", "tags": ["writing", "case_study", "marketing", "documents", "content", "privacy"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/anonymised_case_study_writer`. The original RAPP
agent is preserved byte-for-byte in `anonymised_case_study_writer_agent.py` and in the RCI capsule.

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

Anonymised Case Study Writer — Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `anonymised_case_study_writer_agent.py` and embedded as the fenced Python below (sha256 acca33c8954fc23a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `anonymised_case_study_writer_agent.py` first:

```bash
python3 anonymised_case_study_writer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 anonymised_case_study_writer_agent.py   # or on stdin
python3 anonymised_case_study_writer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Anonymised Case Study Writer — Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/anonymised_case_study_writer',
    "version": '1.1.0',
    "display_name": 'Anonymised Case Study Writer',
    "description": 'Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details.',
    "author": 'Simon Owen',
    "tags": ['writing', 'case_study', 'marketing', 'documents', 'content', 'privacy'],
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
        "upstream_slug": 'anonymised-case-study-writer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#anonymised-case-study-writer',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '30ca39e3e8405c3e',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.857, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:documents', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AnonymisedCaseStudyWriter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AnonymisedCaseStudyWriter'
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
    print(AnonymisedCaseStudyWriter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

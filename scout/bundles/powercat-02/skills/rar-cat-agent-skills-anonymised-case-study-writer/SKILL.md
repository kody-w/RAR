---
name: "rar-cat-agent-skills-anonymised-case-study-writer"
description: "Turn engagement notes into anonymised, publishable case studies without exposing client-confidential details."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/anonymised_case_study_writer", "rar_sha256": "acca33c8954fc23a9d6b76b4ab200a7bf5a076cd44c2200f1c42565e98f20361", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "anonymised_case_study_writer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/anonymised-case-study-writer:9c3cf74e60df2ffae80a8423fc80fe176c0dc436afc143499ccbfb21458d6520", "kind": "skill"}, "version": "1.1.0", "author": "Simon Owen", "tags": ["writing", "case_study", "marketing", "documents", "content", "privacy"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/anonymised_case_study_writer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `anonymised_case_study_writer_agent.py` is
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

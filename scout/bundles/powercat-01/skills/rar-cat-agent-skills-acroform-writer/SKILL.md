---
name: "rar-cat-agent-skills-acroform-writer"
description: "Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/acroform_writer", "rar_sha256": "40d2f38bf76d47a54b443ea70f777001ac77ae612979550aab56a5bf2147f8d4", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "acroform_writer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/acroform-writer:743c13049f4482bfcbd41d5c94be55c0b44d93bfe78f62861419da8ca32fcff8", "kind": "skill"}, "version": "2.0.0", "author": "Sandeep Angara", "tags": ["acroform", "pdf", "forms", "python", "documents"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/acroform_writer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `acroform_writer_agent.py` is
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

AcroForm Writer — Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#acroform-writer
  Upstream author: Sandeep Angara
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `acroform_writer_agent.py` and embedded as the fenced Python below (sha256 40d2f38bf76d47a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `acroform_writer_agent.py` first:

```bash
python3 acroform_writer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 acroform_writer_agent.py   # or on stdin
python3 acroform_writer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AcroForm Writer — Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#acroform-writer
  Upstream author: Sandeep Angara
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/acroform_writer',
    "version": '2.0.0',
    "display_name": 'AcroForm Writer',
    "description": "Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF",
    "author": 'Sandeep Angara',
    "tags": ['acroform', 'pdf', 'forms', 'python', 'documents'],
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
        "upstream_slug": 'acroform-writer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#acroform-writer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b96d3187f92bf269',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.667, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AcroformWriter(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AcroformWriter'
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
    print(AcroformWriter().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

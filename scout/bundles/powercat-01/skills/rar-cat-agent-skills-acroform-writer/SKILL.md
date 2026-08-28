---
name: "rar-cat-agent-skills-acroform-writer"
description: "Fill an existing AcroForm PDF's real form fields from supplied data and flatten the result into a finished, non-editable PDF"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/acroform_writer", "rar_sha256": "40d2f38bf76d47a54b443ea70f777001ac77ae612979550aab56a5bf2147f8d4", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Sandeep Angara", "tags": ["acroform", "pdf", "forms", "python", "documents"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/acroform_writer`. The original RAPP
agent is preserved byte-for-byte in `acroform_writer_agent.py` and in the RCI capsule.

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

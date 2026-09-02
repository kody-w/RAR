---
name: "rar-cat-agent-skills-accessibility-pass"
description: "Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/accessibility_pass", "rar_sha256": "78b164685399af6a913c512c893a064b71d4476f161bb1f868bf8cd03156ee76", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "accessibility_pass_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/accessibility-pass:00faa42862cceb5a32d8d40004a0e4412aa3a652248799b758cdae85cf653368", "kind": "skill"}, "version": "2.0.0", "author": "Tim Karlsson", "tags": ["accessibility", "documents", "presentations", "powerpoint", "quality", "scripts"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/accessibility_pass`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `accessibility_pass_agent.py` is
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

Accessibility Pass — Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#accessibility-pass
  Upstream author: Tim Karlsson
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `accessibility_pass_agent.py` and embedded as the fenced Python below (sha256 78b164685399af6a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `accessibility_pass_agent.py` first:

```bash
python3 accessibility_pass_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 accessibility_pass_agent.py   # or on stdin
python3 accessibility_pass_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Accessibility Pass — Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#accessibility-pass
  Upstream author: Tim Karlsson
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/accessibility_pass',
    "version": '2.0.0',
    "display_name": 'Accessibility Pass',
    "description": "Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds.",
    "author": 'Tim Karlsson',
    "tags": ['accessibility', 'documents', 'presentations', 'powerpoint', 'quality', 'scripts'],
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
        "upstream_slug": 'accessibility-pass',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#accessibility-pass',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '183550ba28bed17f',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio', 'Cowork'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.471, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents', 'tag:powerpoint', 'tag:presentations', 'word:deck', 'word:document'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AccessibilityPass(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AccessibilityPass'
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
    print(AccessibilityPass().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

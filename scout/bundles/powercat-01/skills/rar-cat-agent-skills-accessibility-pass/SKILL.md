---
name: "rar-cat-agent-skills-accessibility-pass"
description: "Check a PowerPoint deck, Word document, HTML page, or Markdown file against Microsoft's Accessibility Checker rules (missing alt text, untitled slides, headerless tables, low contrast, illogical reading order) and fix what it finds."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/accessibility_pass", "rar_sha256": "78b164685399af6a913c512c893a064b71d4476f161bb1f868bf8cd03156ee76", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Tim Karlsson", "tags": ["accessibility", "documents", "presentations", "powerpoint", "quality", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/accessibility_pass`. The original RAPP
agent is preserved byte-for-byte in `accessibility_pass_agent.py` and in the RCI capsule.

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

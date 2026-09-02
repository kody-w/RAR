---
name: "rar-cat-agent-skills-rich-html-presentation"
description: "Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/rich_html_presentation", "rar_sha256": "3d19b945bbfafa005314156f60b03bb2f0361556e9f269fae151015b8e007ec8", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rich_html_presentation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/rich-html-presentation:85317476d161c81f9bb288b710576f054bbeee9524041c8fd3026cf1a2c8cd50", "kind": "skill"}, "version": "2.2.0", "author": "Henry Jammes", "tags": ["presentations", "html", "design", "productivity", "writing"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/rich_html_presentation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rich_html_presentation_agent.py` is
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

Rich HTML Presentation — Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#rich-html-presentation
  Upstream author: Henry Jammes
  Upstream version: 1.2.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rich_html_presentation_agent.py` and embedded as the fenced Python below (sha256 3d19b945bbfafa00…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rich_html_presentation_agent.py` first:

```bash
python3 rich_html_presentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rich_html_presentation_agent.py   # or on stdin
python3 rich_html_presentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Rich HTML Presentation — Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#rich-html-presentation
  Upstream author: Henry Jammes
  Upstream version: 1.2.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/rich_html_presentation',
    "version": '2.2.0',
    "display_name": 'Rich HTML Presentation',
    "description": 'Create polished, self-contained HTML slide decks with keynote-style visuals, keyboard navigation, themes, animations, and reusable presentation components.',
    "author": 'Henry Jammes',
    "tags": ['presentations', 'html', 'design', 'productivity', 'writing'],
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
        "upstream_slug": 'rich-html-presentation',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#rich-html-presentation',
        "upstream_version": '1.2.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'dc40638371835363',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.667, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:presentations', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class RichHtmlPresentation(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RichHtmlPresentation'
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
    print(RichHtmlPresentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

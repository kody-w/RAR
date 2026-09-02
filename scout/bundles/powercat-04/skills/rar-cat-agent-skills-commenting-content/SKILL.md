---
name: "rar-cat-agent-skills-commenting-content"
description: "Comments Word or PowerPoint files with Comments."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/commenting_content", "rar_sha256": "187b091fcba2f8fb7bbd54d2846dd5fa025aafe300aaf05cb4e79baa06416c15", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "commenting_content_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/commenting-content:ce1466220c5933852adffe6a295b574675b93f7fc397d6aa02c47d75cebb7aa6", "kind": "skill"}, "version": "2.0.0", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/commenting_content`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `commenting_content_agent.py` is
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

Commenting Content — Comments Word or PowerPoint files with Comments.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#commenting-content
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commenting_content_agent.py` and embedded as the fenced Python below (sha256 187b091fcba2f8fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commenting_content_agent.py` first:

```bash
python3 commenting_content_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 commenting_content_agent.py   # or on stdin
python3 commenting_content_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Commenting Content — Comments Word or PowerPoint files with Comments.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#commenting-content
  Upstream author: AndrewHessMSFT
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/commenting_content',
    "version": '2.0.0',
    "display_name": 'Commenting Content',
    "description": 'Comments Word or PowerPoint files with Comments.',
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
        "upstream_slug": 'commenting-content',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#commenting-content',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'fcac24466182f80a',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class CommentingContent(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CommentingContent'
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
    print(CommentingContent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

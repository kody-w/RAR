---
name: "rar-cat-agent-skills-blog-post-structure-pass"
description: "Restructure draft or existing blog posts into a stronger narrative without inventing new claims."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_post_structure_pass", "rar_sha256": "b337e49ea0b120fa4994304c114666c76182f2b76b6081e1c3d478d82ee4b5b5", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "blog_post_structure_pass_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/blog-post-structure-pass:a652a12e0227893abb676ba9f93cff7eb1a844c154c5f2ca0b8ed0b7bc2bcaf3", "kind": "skill"}, "version": "1.1.0", "author": "Simon Owen", "tags": ["blog", "writing", "authoring", "content", "structure", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/blog_post_structure_pass`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `blog_post_structure_pass_agent.py` is
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

Blog Post Structure Pass — Restructure draft or existing blog posts into a stronger narrative without inventing new claims.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#blog-post-structure-pass
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blog_post_structure_pass_agent.py` and embedded as the fenced Python below (sha256 b337e49ea0b120fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blog_post_structure_pass_agent.py` first:

```bash
python3 blog_post_structure_pass_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blog_post_structure_pass_agent.py   # or on stdin
python3 blog_post_structure_pass_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Blog Post Structure Pass — Restructure draft or existing blog posts into a stronger narrative without inventing new claims.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#blog-post-structure-pass
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/blog_post_structure_pass',
    "version": '1.1.0',
    "display_name": 'Blog Post Structure Pass',
    "description": 'Restructure draft or existing blog posts into a stronger narrative without inventing new claims.',
    "author": 'Simon Owen',
    "tags": ['blog', 'writing', 'authoring', 'content', 'structure', 'productivity'],
    "category": 'general',
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
        "upstream_slug": 'blog-post-structure-pass',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#blog-post-structure-pass',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'bae79e6f9e5b1b0c',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.714, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing', 'word:draft'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class BlogPostStructurePass(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlogPostStructurePass'
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
    print(BlogPostStructurePass().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

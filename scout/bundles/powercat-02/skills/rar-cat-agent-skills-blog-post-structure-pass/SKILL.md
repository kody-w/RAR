---
name: "rar-cat-agent-skills-blog-post-structure-pass"
description: "Restructure draft or existing blog posts into a stronger narrative without inventing new claims."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_post_structure_pass", "rar_sha256": "b337e49ea0b120fa4994304c114666c76182f2b76b6081e1c3d478d82ee4b5b5", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Simon Owen", "tags": ["blog", "writing", "authoring", "content", "structure", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/blog_post_structure_pass`. The original RAPP
agent is preserved byte-for-byte in `blog_post_structure_pass_agent.py` and in the RCI capsule.

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

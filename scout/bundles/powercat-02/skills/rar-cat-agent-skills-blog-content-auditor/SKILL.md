---
name: "rar-cat-agent-skills-blog-content-auditor"
description: "Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_content_auditor", "rar_sha256": "ba98bc211f37593e39cd7bdcd7c53edd1db5e2484a9378500c897505f902b262", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "blog_content_auditor_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/blog-content-auditor:4235deb0d1619539975082a4aace512167010387ee792cb877ad42a9f0c55071", "kind": "skill"}, "version": "1.1.0", "author": "Simon Owen", "tags": ["blog", "content", "audit", "writing", "seo", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/blog_content_auditor`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `blog_content_auditor_agent.py` is
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

Blog Content Auditor — Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#blog-content-auditor
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blog_content_auditor_agent.py` and embedded as the fenced Python below (sha256 ba98bc211f37593e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blog_content_auditor_agent.py` first:

```bash
python3 blog_content_auditor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blog_content_auditor_agent.py   # or on stdin
python3 blog_content_auditor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Blog Content Auditor — Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#blog-content-auditor
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/blog_content_auditor',
    "version": '1.1.0',
    "display_name": 'Blog Content Auditor',
    "description": 'Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority.',
    "author": 'Simon Owen',
    "tags": ['blog', 'content', 'audit', 'writing', 'seo', 'productivity'],
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
        "upstream_slug": 'blog-content-auditor',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#blog-content-auditor',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'a5c6bd31581e4eda',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class BlogContentAuditor(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlogContentAuditor'
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
    print(BlogContentAuditor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

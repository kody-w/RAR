---
name: "rar-cat-agent-skills-blog-content-auditor"
description: "Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_content_auditor", "rar_sha256": "ba98bc211f37593e39cd7bdcd7c53edd1db5e2484a9378500c897505f902b262", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "1.1.0", "author": "Simon Owen", "tags": ["blog", "content", "audit", "writing", "seo", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/blog_content_auditor`. The original RAPP
agent is preserved byte-for-byte in `blog_content_auditor_agent.py` and in the RCI capsule.

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

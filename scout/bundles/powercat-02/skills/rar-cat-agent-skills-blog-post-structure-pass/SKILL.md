---
name: "rar-cat-agent-skills-blog-post-structure-pass"
description: "Restructure draft or existing blog posts into a stronger narrative without inventing new claims."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_post_structure_pass", "rar_sha256": "7aa974d9e64cd44bf8b7d1c0b45c56396849d26beefbdb9d853de01547392519", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["blog", "writing", "authoring", "content", "structure", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blog_post_structure_pass_agent.py` and embedded as the fenced Python below (sha256 7aa974d9e64cd44b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blog_post_structure_pass_agent.py` first:

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
    "version": '2.1.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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

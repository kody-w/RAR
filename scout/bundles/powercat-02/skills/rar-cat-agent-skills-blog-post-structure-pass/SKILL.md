---
name: "rar-cat-agent-skills-blog-post-structure-pass"
description: "Restructure draft or existing blog posts into a stronger narrative without inventing new claims."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_post_structure_pass", "rar_sha256": "7aa974d9e64cd44bf8b7d1c0b45c56396849d26beefbdb9d853de01547392519", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Simon Owen", "tags": ["blog", "writing", "authoring", "content", "structure", "productivity"]}
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

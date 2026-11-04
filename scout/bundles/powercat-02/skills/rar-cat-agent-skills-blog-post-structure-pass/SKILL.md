---
name: "rar-cat-agent-skills-blog-post-structure-pass"
description: "Restructure draft or existing blog posts into a stronger narrative without inventing new claims."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_post_structure_pass", "rar_sha256": "43bbdec88cbd22f1df3c807a5ec76ded944fe911c957b5b1f5eb84cc660be546", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Simon Owen", "tags": ["blog", "writing", "authoring", "content", "structure", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blog_post_structure_pass_agent.py` and embedded as the fenced Python below (sha256 43bbdec88cbd22f1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blog_post_structure_pass_agent.py` first:

```bash
python3 blog_post_structure_pass_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blog_post_structure_pass_agent.py   # or on stdin
python3 blog_post_structure_pass_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/blog_post_structure_pass_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/blog_post_structure_pass_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/blog_post_structure_pass/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

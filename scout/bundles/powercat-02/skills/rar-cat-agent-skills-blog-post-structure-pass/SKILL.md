---
name: "rar-cat-agent-skills-blog-post-structure-pass"
description: "Restructure draft or existing blog posts into a stronger narrative without inventing new claims."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_post_structure_pass", "rar_sha256": "43bbdec88cbd22f1df3c807a5ec76ded944fe911c957b5b1f5eb84cc660be546", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["blog", "writing", "authoring", "content", "structure", "productivity"]}
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

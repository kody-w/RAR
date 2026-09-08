---
name: "rar-cat-agent-skills-blog-content-auditor"
description: "Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_content_auditor", "rar_sha256": "d164db261994db6d69cdd075d45da8ad058dc87bea407088e9fe06935dbd58d7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Simon Owen", "tags": ["blog", "content", "audit", "writing", "seo", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blog_content_auditor_agent.py` and embedded as the fenced Python below (sha256 d164db261994db6d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blog_content_auditor_agent.py` first:

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
    "version": '2.1.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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
    print(BlogContentAuditor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

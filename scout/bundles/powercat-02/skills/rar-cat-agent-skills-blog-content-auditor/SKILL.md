---
name: "rar-cat-agent-skills-blog-content-auditor"
description: "Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_content_auditor", "rar_sha256": "902a9938856104a577bedd98478f6436adf0d6c55935978ff18563beec80d169", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Simon Owen", "tags": ["blog", "content", "audit", "writing", "seo", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blog_content_auditor_agent.py` and embedded as the fenced Python below (sha256 902a9938856104a5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blog_content_auditor_agent.py` first:

```bash
python3 blog_content_auditor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blog_content_auditor_agent.py   # or on stdin
python3 blog_content_auditor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/blog_content_auditor_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/blog_content_auditor_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/blog_content_auditor/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

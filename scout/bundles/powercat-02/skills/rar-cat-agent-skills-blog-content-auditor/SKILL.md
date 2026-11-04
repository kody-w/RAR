---
name: "rar-cat-agent-skills-blog-content-auditor"
description: "Audit blog posts or a blog library for clarity, structure, evidence, audience fit, and improvement priority."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/blog_content_auditor", "rar_sha256": "902a9938856104a577bedd98478f6436adf0d6c55935978ff18563beec80d169", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["blog", "content", "audit", "writing", "seo", "productivity"]}
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

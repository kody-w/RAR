---
name: "rar-cat-agent-skills-commenting-content"
description: "Comments Word or PowerPoint files with Comments."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/commenting_content", "rar_sha256": "896dfb9f478e7ef61d68fb5008dbe8c805c595a8217abc0e5c3a29e685322821", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/commenting_content`. The original RAPP
agent is preserved byte-for-byte in `commenting_content_agent.py` and in the RCI capsule.

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

Commenting Content — Comments Word or PowerPoint files with Comments.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#commenting-content
  Upstream author: AndrewHessMSFT
  Upstream version: 1.0.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `commenting_content_agent.py` and embedded as the fenced Python below (sha256 896dfb9f478e7ef6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `commenting_content_agent.py` first:

```bash
python3 commenting_content_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 commenting_content_agent.py   # or on stdin
python3 commenting_content_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Commenting Content — Comments Word or PowerPoint files with Comments.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#commenting-content
  Upstream author: AndrewHessMSFT
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/commenting_content',
    "version": '3.0.2',
    "display_name": 'Commenting Content',
    "description": 'Comments Word or PowerPoint files with Comments.',
    "author": 'AndrewHessMSFT',
    "tags": ['documents', 'productivity'],
    "category": 'productivity',
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
        "upstream_slug": 'commenting-content',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#commenting-content',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'fcac24466182f80a',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:documents'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class CommentingContent(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CommentingContent'
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
    print(CommentingContent().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cat-agent-skills-commenting-content"
description: "Comments Word or PowerPoint files with Comments."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/commenting_content", "rar_sha256": "896dfb9f478e7ef61d68fb5008dbe8c805c595a8217abc0e5c3a29e685322821", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "AndrewHessMSFT", "tags": ["documents", "productivity"]}
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

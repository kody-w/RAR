---
name: "rar-cat-agent-skills-wikipedia-human-style-writing"
description: "Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wikipedia_human_style_writing", "rar_sha256": "fd27623e4e77260d8a51a01f90010f62888a7b07f3eb2d4dbd7363d5ccf6e8bd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Chris Garty", "tags": ["writing", "content", "editing", "style", "humanize", "ai_detection", "wikipedia"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/wikipedia_human_style_writing`. The original RAPP
agent is preserved byte-for-byte in `wikipedia_human_style_writing_agent.py` and in the RCI capsule.

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

Wikipedia Human Style Writing — Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing
  Upstream author: Chris Garty
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `wikipedia_human_style_writing_agent.py` and embedded as the fenced Python below (sha256 fd27623e4e77260d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `wikipedia_human_style_writing_agent.py` first:

```bash
python3 wikipedia_human_style_writing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 wikipedia_human_style_writing_agent.py   # or on stdin
python3 wikipedia_human_style_writing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Wikipedia Human Style Writing — Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing
  Upstream author: Chris Garty
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/wikipedia_human_style_writing',
    "version": '2.1.2',
    "display_name": 'Wikipedia Human Style Writing',
    "description": "Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide.",
    "author": 'Chris Garty',
    "tags": ['writing', 'content', 'editing', 'style', 'humanize', 'ai_detection', 'wikipedia'],
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
        "upstream_slug": 'wikipedia-human-style-writing',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#wikipedia-human-style-writing',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '4a55ea6837b037ca',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing', 'word:draft'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class WikipediaHumanStyleWriting(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WikipediaHumanStyleWriting'
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
    print(WikipediaHumanStyleWriting().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

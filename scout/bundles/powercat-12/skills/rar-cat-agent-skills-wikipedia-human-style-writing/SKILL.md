---
name: "rar-cat-agent-skills-wikipedia-human-style-writing"
description: "Rewrite or draft prose so it avoids the tell-tale signs of AI writing, using Wikipedia's 'Signs of AI writing' field guide."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/wikipedia_human_style_writing", "rar_sha256": "fd27623e4e77260d8a51a01f90010f62888a7b07f3eb2d4dbd7363d5ccf6e8bd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Chris Garty", "tags": ["writing", "content", "editing", "style", "humanize", "ai_detection", "wikipedia"]}
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

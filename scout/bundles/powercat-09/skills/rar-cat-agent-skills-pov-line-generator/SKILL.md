---
name: "rar-cat-agent-skills-pov-line-generator"
description: "Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pov_line_generator", "rar_sha256": "cbe57f8ea3671d17ab8daec288c8f57ce7641a9c070570cc3fb0e36ade9117d8", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "positioning", "marketing", "content", "social_media"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/pov_line_generator`. The original RAPP
agent is preserved byte-for-byte in `pov_line_generator_agent.py` and in the RCI capsule.

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

POV Line Generator — Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pov-line-generator
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `pov_line_generator_agent.py` and embedded as the fenced Python below (sha256 cbe57f8ea3671d17…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `pov_line_generator_agent.py` first:

```bash
python3 pov_line_generator_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 pov_line_generator_agent.py   # or on stdin
python3 pov_line_generator_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
POV Line Generator — Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#pov-line-generator
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/pov_line_generator',
    "version": '2.1.2',
    "display_name": 'POV Line Generator',
    "description": 'Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work.',
    "author": 'Simon Owen',
    "tags": ['writing', 'positioning', 'marketing', 'content', 'social_media'],
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
        "upstream_slug": 'pov-line-generator',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#pov-line-generator',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'bf492abfe32d66ad',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing', 'word:generate'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PovLineGenerator(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PovLineGenerator'
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
    print(PovLineGenerator().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

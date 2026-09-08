---
name: "rar-cat-agent-skills-pov-line-generator"
description: "Generate sharp, specific point-of-view lines for posts, slides, talks, campaigns, or positioning work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/pov_line_generator", "rar_sha256": "cbe57f8ea3671d17ab8daec288c8f57ce7641a9c070570cc3fb0e36ade9117d8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "positioning", "marketing", "content", "social_media"]}
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

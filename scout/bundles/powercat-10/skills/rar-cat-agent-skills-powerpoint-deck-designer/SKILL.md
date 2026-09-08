---
name: "rar-cat-agent-skills-powerpoint-deck-designer"
description: "Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/powerpoint_deck_designer", "rar_sha256": "9cac059a7de8f0fdec2dc6744e1bcee1a2b344cf30fa5e31763619598e6298ea", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Ferran Chopo", "tags": ["powerpoint", "presentations", "python", "charts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/powerpoint_deck_designer`. The original RAPP
agent is preserved byte-for-byte in `powerpoint_deck_designer_agent.py` and in the RCI capsule.

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

PowerPoint Deck Designer — Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#powerpoint-deck-designer
  Upstream author: Ferran Chopo
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `powerpoint_deck_designer_agent.py` and embedded as the fenced Python below (sha256 9cac059a7de8f0fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `powerpoint_deck_designer_agent.py` first:

```bash
python3 powerpoint_deck_designer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 powerpoint_deck_designer_agent.py   # or on stdin
python3 powerpoint_deck_designer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
PowerPoint Deck Designer — Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants).

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#powerpoint-deck-designer
  Upstream author: Ferran Chopo
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/powerpoint_deck_designer',
    "version": '3.0.2',
    "display_name": 'PowerPoint Deck Designer',
    "description": "Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants).",
    "author": 'Ferran Chopo',
    "tags": ['powerpoint', 'presentations', 'python', 'charts'],
    "category": 'devtools',
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
        "upstream_slug": 'powerpoint-deck-designer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#powerpoint-deck-designer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '13a4c71ffb14ed1c',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations', 'word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PowerpointDeckDesigner(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PowerpointDeckDesigner'
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
    print(PowerpointDeckDesigner().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cat-agent-skills-powerpoint-deck-designer"
description: "Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/powerpoint_deck_designer", "rar_sha256": "9cac059a7de8f0fdec2dc6744e1bcee1a2b344cf30fa5e31763619598e6298ea", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Ferran Chopo", "tags": ["powerpoint", "presentations", "python", "charts"]}
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

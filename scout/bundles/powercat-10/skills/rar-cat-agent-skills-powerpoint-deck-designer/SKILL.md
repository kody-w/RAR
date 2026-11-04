---
name: "rar-cat-agent-skills-powerpoint-deck-designer"
description: "Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/powerpoint_deck_designer", "rar_sha256": "b9c8aa7b2f3052164205c19ea8e9ca9271e45709807145a51465b9618f906336", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Ferran Chopo", "tags": ["powerpoint", "presentations", "python", "charts"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `powerpoint_deck_designer_agent.py` and embedded as the fenced Python below (sha256 b9c8aa7b2f305216…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `powerpoint_deck_designer_agent.py` first:

```bash
python3 powerpoint_deck_designer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 powerpoint_deck_designer_agent.py   # or on stdin
python3 powerpoint_deck_designer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/powerpoint_deck_designer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/powerpoint_deck_designer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/powerpoint_deck_designer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

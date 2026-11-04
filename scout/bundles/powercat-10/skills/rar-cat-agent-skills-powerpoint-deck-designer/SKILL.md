---
name: "rar-cat-agent-skills-powerpoint-deck-designer"
description: "Creates polished PowerPoint decks from a JSON specification using python-pptx. Designed as a Copilot Studio Skill that runs natively inside the agent's Python container (no Azure Function or custom connector required). Supports 8 layouts plus native charts (bar, column, line, pie, donut with stacked / 100% stacked variants)."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/powerpoint_deck_designer", "rar_sha256": "b9c8aa7b2f3052164205c19ea8e9ca9271e45709807145a51465b9618f906336", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Ferran Chopo", "tags": ["powerpoint", "presentations", "python", "charts"]}
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

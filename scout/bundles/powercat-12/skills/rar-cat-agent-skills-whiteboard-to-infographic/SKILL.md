---
name: "rar-cat-agent-skills-whiteboard-to-infographic"
description: "Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/whiteboard_to_infographic", "rar_sha256": "0d39d06f2819bbe36cb4e09d6d08401cba0232f23a379f9af09035cb7ba4af4b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Andy Zehr", "tags": ["infographic", "whiteboard", "powerpoint", "presentations", "diagrams", "design", "consulting"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/whiteboard_to_infographic`. The original RAPP
agent is preserved byte-for-byte in `whiteboard_to_infographic_agent.py` and in the RCI capsule.

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

Whiteboard to Infographic — Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic
  Upstream author: Andy Zehr
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `whiteboard_to_infographic_agent.py` and embedded as the fenced Python below (sha256 0d39d06f2819bbe3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `whiteboard_to_infographic_agent.py` first:

```bash
python3 whiteboard_to_infographic_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 whiteboard_to_infographic_agent.py   # or on stdin
python3 whiteboard_to_infographic_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/whiteboard_to_infographic_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/whiteboard_to_infographic_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/whiteboard_to_infographic/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Whiteboard to Infographic — Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic
  Upstream author: Andy Zehr
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/whiteboard_to_infographic',
    "version": '3.0.2',
    "display_name": 'Whiteboard to Infographic',
    "description": "Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container.",
    "author": 'Andy Zehr',
    "tags": ['infographic', 'whiteboard', 'powerpoint', 'presentations', 'diagrams', 'design', 'consulting'],
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
        "upstream_slug": 'whiteboard-to-infographic',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#whiteboard-to-infographic',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '8ba98fb5f2eb84f8',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.571, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class WhiteboardToInfographic(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WhiteboardToInfographic'
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
    print(WhiteboardToInfographic().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

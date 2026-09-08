---
name: "rar-cat-agent-skills-whiteboard-to-infographic"
description: "Turn a photo of a hand-drawn whiteboard or process sketch into a polished, client-ready infographic slide (.pptx), generated natively in the agent's Python container."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/whiteboard_to_infographic", "rar_sha256": "11818cb6790bb3fa12ce584fccfe160c66297eecba69ae252c3de296a25c47a8", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Andy Zehr", "tags": ["infographic", "whiteboard", "powerpoint", "presentations", "diagrams", "design", "consulting"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `whiteboard_to_infographic_agent.py` and embedded as the fenced Python below (sha256 11818cb6790bb3fa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `whiteboard_to_infographic_agent.py` first:

```bash
python3 whiteboard_to_infographic_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 whiteboard_to_infographic_agent.py   # or on stdin
python3 whiteboard_to_infographic_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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

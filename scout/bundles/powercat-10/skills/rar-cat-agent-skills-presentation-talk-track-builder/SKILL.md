---
name: "rar-cat-agent-skills-presentation-talk-track-builder"
description: "Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/presentation_talk_track_builder", "rar_sha256": "461da3b8ecd91d4ae5cc1ae9bc856fda9995910e9ab1048863a1b4435f9c04a0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Jagmeet Chabra", "tags": ["presentations", "speaker_notes", "powerpoint", "writing", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/presentation_talk_track_builder`. The original RAPP
agent is preserved byte-for-byte in `presentation_talk_track_builder_agent.py` and in the RCI capsule.

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

Presentation Talk Track Builder — Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#presentation-talk-track-builder
  Upstream author: Jagmeet Chabra
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `presentation_talk_track_builder_agent.py` and embedded as the fenced Python below (sha256 461da3b8ecd91d4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `presentation_talk_track_builder_agent.py` first:

```bash
python3 presentation_talk_track_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 presentation_talk_track_builder_agent.py   # or on stdin
python3 presentation_talk_track_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Presentation Talk Track Builder — Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#presentation-talk-track-builder
  Upstream author: Jagmeet Chabra
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/presentation_talk_track_builder',
    "version": '3.0.2',
    "display_name": 'Presentation Talk Track Builder',
    "description": 'Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content.',
    "author": 'Jagmeet Chabra',
    "tags": ['presentations', 'speaker_notes', 'powerpoint', 'writing', 'productivity'],
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
        "upstream_slug": 'presentation-talk-track-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#presentation-talk-track-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '10389b967a5e68a1',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations', 'tag:writing', 'word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class PresentationTalkTrackBuilder(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PresentationTalkTrackBuilder'
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
    print(PresentationTalkTrackBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

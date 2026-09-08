---
name: "rar-cat-agent-skills-presentation-talk-track-builder"
description: "Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/presentation_talk_track_builder", "rar_sha256": "461da3b8ecd91d4ae5cc1ae9bc856fda9995910e9ab1048863a1b4435f9c04a0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Jagmeet Chabra", "tags": ["presentations", "speaker_notes", "powerpoint", "writing", "productivity"]}
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

---
name: "rar-cat-agent-skills-presentation-talk-track-builder"
description: "Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/presentation_talk_track_builder", "rar_sha256": "f164a6beb6d907f4b605378966693ea50532a14d39c7bb7d8b1c5a66e65a2794", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Jagmeet Chabra", "tags": ["presentations", "speaker_notes", "powerpoint", "writing", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `presentation_talk_track_builder_agent.py` and embedded as the fenced Python below (sha256 f164a6beb6d907f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `presentation_talk_track_builder_agent.py` first:

```bash
python3 presentation_talk_track_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 presentation_talk_track_builder_agent.py   # or on stdin
python3 presentation_talk_track_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/presentation_talk_track_builder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/presentation_talk_track_builder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/presentation_talk_track_builder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

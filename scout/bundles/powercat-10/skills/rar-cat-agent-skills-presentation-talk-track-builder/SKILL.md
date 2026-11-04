---
name: "rar-cat-agent-skills-presentation-talk-track-builder"
description: "Writes natural, first-person spoken presenter scripts for the slides in a deck. Treats existing speaker notes as authoritative when they contradict slide text. Calibrates length to a target duration and speaking pace and returns a timing table. Never modifies visible slide content."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/presentation_talk_track_builder", "rar_sha256": "f164a6beb6d907f4b605378966693ea50532a14d39c7bb7d8b1c5a66e65a2794", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Jagmeet Chabra", "tags": ["presentations", "speaker_notes", "powerpoint", "writing", "productivity"]}
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

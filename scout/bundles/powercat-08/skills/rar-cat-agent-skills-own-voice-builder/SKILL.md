---
name: "rar-cat-agent-skills-own-voice-builder"
description: "Mines your sent emails to extract your real writing voice \u2014 languages, tone modes, structure, vocabulary, taboo phrases \u2014 and generates a personal voice skill that makes every email and Teams draft sound like you."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/own_voice_builder", "rar_sha256": "e93e7c7eaf21c72cb54ae3b66789bc10826ea31a644041608de32228d84a5ee5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Marcel", "tags": ["writing", "voice", "email", "teams", "productivity", "microsoft_365"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/own_voice_builder`. The original RAPP
agent is preserved byte-for-byte in `own_voice_builder_agent.py` and in the RCI capsule.

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

Own Voice Builder — Mines your sent emails to extract your real writing voice — languages, tone modes, structure, vocabulary, taboo phrases — and generates a personal voice skill that makes every email and Teams draft sound like you.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#own-voice-builder
  Upstream author: Marcel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `own_voice_builder_agent.py` and embedded as the fenced Python below (sha256 e93e7c7eaf21c72c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `own_voice_builder_agent.py` first:

```bash
python3 own_voice_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 own_voice_builder_agent.py   # or on stdin
python3 own_voice_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Own Voice Builder — Mines your sent emails to extract your real writing voice — languages, tone modes, structure, vocabulary, taboo phrases — and generates a personal voice skill that makes every email and Teams draft sound like you.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#own-voice-builder
  Upstream author: Marcel
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/own_voice_builder',
    "version": '3.0.2',
    "display_name": 'Own Voice Builder',
    "description": 'Mines your sent emails to extract your real writing voice — languages, tone modes, structure, vocabulary, taboo phrases — and generates a personal voice skill that makes every email and Teams draft sound like you.',
    "author": 'Marcel',
    "tags": ['writing', 'voice', 'email', 'teams', 'productivity', 'microsoft_365'],
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
        "upstream_slug": 'own-voice-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#own-voice-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '45c780ef5e1ffdad',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.714, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:email', 'tag:writing', 'word:draft'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class OwnVoiceBuilder(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'OwnVoiceBuilder'
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
    print(OwnVoiceBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

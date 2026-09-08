---
name: "rar-cat-agent-skills-own-voice-builder"
description: "Mines your sent emails to extract your real writing voice \u2014 languages, tone modes, structure, vocabulary, taboo phrases \u2014 and generates a personal voice skill that makes every email and Teams draft sound like you."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/own_voice_builder", "rar_sha256": "e93e7c7eaf21c72cb54ae3b66789bc10826ea31a644041608de32228d84a5ee5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Marcel", "tags": ["writing", "voice", "email", "teams", "productivity", "microsoft_365"]}
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

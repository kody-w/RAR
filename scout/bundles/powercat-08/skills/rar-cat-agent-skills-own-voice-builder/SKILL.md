---
name: "rar-cat-agent-skills-own-voice-builder"
description: "Mines your sent emails to extract your real writing voice \u2014 languages, tone modes, structure, vocabulary, taboo phrases \u2014 and generates a personal voice skill that makes every email and Teams draft sound like you."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/own_voice_builder", "rar_sha256": "119badda228da2db2f7f2f54e60355d7fa9a424acd2f954acb659a9e41b4b498", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Marcel", "tags": ["writing", "voice", "email", "teams", "productivity", "microsoft_365"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `own_voice_builder_agent.py` and embedded as the fenced Python below (sha256 119badda228da2db…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `own_voice_builder_agent.py` first:

```bash
python3 own_voice_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 own_voice_builder_agent.py   # or on stdin
python3 own_voice_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/own_voice_builder_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/own_voice_builder_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/own_voice_builder/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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

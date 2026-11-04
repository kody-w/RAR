---
name: "rar-cat-agent-skills-own-voice-builder"
description: "Mines your sent emails to extract your real writing voice \u2014 languages, tone modes, structure, vocabulary, taboo phrases \u2014 and generates a personal voice skill that makes every email and Teams draft sound like you."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/own_voice_builder", "rar_sha256": "119badda228da2db2f7f2f54e60355d7fa9a424acd2f954acb659a9e41b4b498", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Marcel", "tags": ["writing", "voice", "email", "teams", "productivity", "microsoft_365"]}
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

---
name: "rar-cat-agent-skills-brand-voice-pass"
description: "Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_voice_pass", "rar_sha256": "8fe0e9ae3edc03da2cc0329fd08af34c4871530aa826d606972e1d38bf2c5127", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "content", "voice", "authoring", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/brand_voice_pass`. The original RAPP
agent is preserved byte-for-byte in `brand_voice_pass_agent.py` and in the RCI capsule.

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

Brand Voice Pass — Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#brand-voice-pass
  Upstream author: Simon Owen
  Upstream version: 0.1.0
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `brand_voice_pass_agent.py` and embedded as the fenced Python below (sha256 8fe0e9ae3edc03da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `brand_voice_pass_agent.py` first:

```bash
python3 brand_voice_pass_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 brand_voice_pass_agent.py   # or on stdin
python3 brand_voice_pass_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/brand_voice_pass_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/brand_voice_pass_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/brand_voice_pass/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Brand Voice Pass — Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#brand-voice-pass
  Upstream author: Simon Owen
  Upstream version: 0.1.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/brand_voice_pass',
    "version": '2.1.2',
    "display_name": 'Brand Voice Pass',
    "description": 'Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing.',
    "author": 'Simon Owen',
    "tags": ['writing', 'content', 'voice', 'authoring', 'productivity'],
    "category": 'general',
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
        "upstream_slug": 'brand-voice-pass',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#brand-voice-pass',
        "upstream_version": '0.1.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'ab6312662367dcfc',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.8, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class BrandVoicePass(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BrandVoicePass'
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
    print(BrandVoicePass().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

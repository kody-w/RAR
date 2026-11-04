---
name: "rar-cat-agent-skills-brand-voice-pass"
description: "Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_voice_pass", "rar_sha256": "8fe0e9ae3edc03da2cc0329fd08af34c4871530aa826d606972e1d38bf2c5127", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "content", "voice", "authoring", "productivity"]}
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

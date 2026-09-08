---
name: "rar-cat-agent-skills-brand-voice-pass"
description: "Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_voice_pass", "rar_sha256": "6637408a4175858b78cf4da9cb7fac9012e301e6577cc18e2064dca8629caa63", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "content", "voice", "authoring", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `brand_voice_pass_agent.py` and embedded as the fenced Python below (sha256 6637408a4175858b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `brand_voice_pass_agent.py` first:

```bash
python3 brand_voice_pass_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 brand_voice_pass_agent.py   # or on stdin
python3 brand_voice_pass_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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

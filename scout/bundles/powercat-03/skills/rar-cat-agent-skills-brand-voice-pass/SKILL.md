---
name: "rar-cat-agent-skills-brand-voice-pass"
description: "Rewrite drafts into a configurable house style, preserving meaning while removing generic AI phrasing."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/brand_voice_pass", "rar_sha256": "6637408a4175858b78cf4da9cb7fac9012e301e6577cc18e2064dca8629caa63", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "2.1.2", "author": "Simon Owen", "tags": ["writing", "content", "voice", "authoring", "productivity"]}
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

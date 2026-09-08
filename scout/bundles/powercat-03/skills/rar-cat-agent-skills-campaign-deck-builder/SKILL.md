---
name: "rar-cat-agent-skills-campaign-deck-builder"
description: "Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/campaign_deck_builder", "rar_sha256": "e7d5cb5432ba712afe2da34ab2bec2654a82864cd513b584af374c5a67f49e33", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["marketing", "presentations", "powerpoint", "automation", "scripts"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/campaign_deck_builder`. The original RAPP
agent is preserved byte-for-byte in `campaign_deck_builder_agent.py` and in the RCI capsule.

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

Campaign Deck Builder — Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder
  Upstream author: Adi Leibowitz
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `campaign_deck_builder_agent.py` and embedded as the fenced Python below (sha256 e7d5cb5432ba712a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `campaign_deck_builder_agent.py` first:

```bash
python3 campaign_deck_builder_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 campaign_deck_builder_agent.py   # or on stdin
python3 campaign_deck_builder_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Campaign Deck Builder — Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/campaign_deck_builder',
    "version": '3.0.2',
    "display_name": 'Campaign Deck Builder',
    "description": 'Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template.',
    "author": 'Adi Leibowitz',
    "tags": ['marketing', 'presentations', 'powerpoint', 'automation', 'scripts'],
    "category": 'devtools',
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
        "upstream_slug": 'campaign-deck-builder',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#campaign-deck-builder',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": '23b22be138aae9b6',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:powerpoint', 'tag:presentations', 'word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class CampaignDeckBuilder(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CampaignDeckBuilder'
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
    print(CampaignDeckBuilder().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

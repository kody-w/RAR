---
name: "rar-cat-agent-skills-campaign-deck-builder"
description: "Turn a short interview into a charming, vibrant 3-slide marketing-campaign deck by filling a bundled PowerPoint template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/campaign_deck_builder", "rar_sha256": "e7d5cb5432ba712afe2da34ab2bec2654a82864cd513b584af374c5a67f49e33", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["marketing", "presentations", "powerpoint", "automation", "scripts"]}
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

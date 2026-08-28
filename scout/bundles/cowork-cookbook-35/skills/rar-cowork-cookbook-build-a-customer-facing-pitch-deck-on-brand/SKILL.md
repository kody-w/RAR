---
name: "rar-cowork-cookbook-build-a-customer-facing-pitch-deck-on-brand"
description: "Hand the field a customer-facing pitch deck that's on-brand, on-message, and tailored to a specific exec audience - instead of letting every team rebuild from a generic template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_customer_facing_pitch_deck_on_brand", "rar_sha256": "d0e1fd32dbd0055ffb9ebd47aa7ffc02740bc74a24ba328fd91c24d04352e3a0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/build_a_customer_facing_pitch_deck_on_brand`. The original RAPP
agent is preserved byte-for-byte in `build_a_customer_facing_pitch_deck_on_brand_agent.py` and in the RCI capsule.

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

Build a customer-facing pitch deck on brand — Hand the field a customer-facing pitch deck that's on-brand, on-message, and tailored to a specific exec audience - instead of letting every team rebuild from a generic template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-a-customer-facing-pitch-deck-on-brand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_a_customer_facing_pitch_deck_on_brand_agent.py` and embedded as the fenced Python below (sha256 d0e1fd32dbd0055f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_a_customer_facing_pitch_deck_on_brand_agent.py` first:

```bash
python3 build_a_customer_facing_pitch_deck_on_brand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 build_a_customer_facing_pitch_deck_on_brand_agent.py   # or on stdin
python3 build_a_customer_facing_pitch_deck_on_brand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a customer-facing pitch deck on brand — Hand the field a customer-facing pitch deck that's on-brand, on-message, and tailored to a specific exec audience - instead of letting every team rebuild from a generic template.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/build-a-customer-facing-pitch-deck-on-brand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/build_a_customer_facing_pitch_deck_on_brand',
    "version": '2.0.1',
    "display_name": 'Build a customer-facing pitch deck on brand',
    "description": "Hand the field a customer-facing pitch deck that's on-brand, on-message, and tailored to a specific exec audience - instead of letting every team rebuild from a generic template.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'beginner', 'read_only'],
    "category": 'general',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'build-a-customer-facing-pitch-deck-on-brand',
        "upstream_url": 'https://coworkcookbook.com/recipes/build-a-customer-facing-pitch-deck-on-brand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5221a5283c2153e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/build-a-customer-facing-pitch-deck-on-brand', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Email', 'Meetings', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['word:deck'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class BuildACustomerFacingPitchDeckOnBrand(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BuildACustomerFacingPitchDeckOnBrand'
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(BuildACustomerFacingPitchDeckOnBrand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-build-a-customer-facing-pitch-deck-on-brand"
description: "Hand the field a customer-facing pitch deck that's on-brand, on-message, and tailored to a specific exec audience - instead of letting every team rebuild from a generic template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_customer_facing_pitch_deck_on_brand", "rar_sha256": "2abe5c63fe631d55484440bad066ff0b96ca7057832867788e634b0a7749a34e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "read_only"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `build_a_customer_facing_pitch_deck_on_brand_agent.py` and embedded as the fenced Python below (sha256 2abe5c63fe631d55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `build_a_customer_facing_pitch_deck_on_brand_agent.py` first:

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
    "version": '2.0.0',
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

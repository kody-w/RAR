---
name: "rar-cowork-cookbook-build-a-customer-facing-pitch-deck-on-brand"
description: "Hand the field a customer-facing pitch deck that's on-brand, on-message, and tailored to a specific exec audience - instead of letting every team rebuild from a generic template."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/build_a_customer_facing_pitch_deck_on_brand", "rar_sha256": "2abe5c63fe631d55484440bad066ff0b96ca7057832867788e634b0a7749a34e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "build_a_customer_facing_pitch_deck_on_brand_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/build-a-customer-facing-pitch-deck-on-brand:2d2127f84ecd8d9401b1724a7f7727600c31b9d5183fd922dbb226b365f8b3f7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "beginner", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/build_a_customer_facing_pitch_deck_on_brand`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `build_a_customer_facing_pitch_deck_on_brand_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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

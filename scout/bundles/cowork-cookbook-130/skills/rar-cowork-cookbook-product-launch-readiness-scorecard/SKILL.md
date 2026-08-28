---
name: "rar-cowork-cookbook-product-launch-readiness-scorecard"
description: "Scores released products on launch readiness based on setup completeness (dimensions, pricing, BOM, tax, default order settings) and produces a scorecard."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/product_launch_readiness_scorecard", "rar_sha256": "ecac137e00cb742291d86d01ee9b95165333e82459b6f9a917034b711a2417fe", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/product_launch_readiness_scorecard`. The original RAPP
agent is preserved byte-for-byte in `product_launch_readiness_scorecard_agent.py` and in the RCI capsule.

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

Released Product Launch Readiness Scorecard — Scores released products on launch readiness based on setup completeness (dimensions, pricing, BOM, tax, default order settings) and produces a scorecard.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/product-launch-readiness-scorecard
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `product_launch_readiness_scorecard_agent.py` and embedded as the fenced Python below (sha256 ecac137e00cb7422…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `product_launch_readiness_scorecard_agent.py` first:

```bash
python3 product_launch_readiness_scorecard_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 product_launch_readiness_scorecard_agent.py   # or on stdin
python3 product_launch_readiness_scorecard_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Released Product Launch Readiness Scorecard — Scores released products on launch readiness based on setup completeness (dimensions, pricing, BOM, tax, default order settings) and produces a scorecard.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/product-launch-readiness-scorecard
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/product_launch_readiness_scorecard',
    "version": '2.0.1',
    "display_name": 'Released Product Launch Readiness Scorecard',
    "description": 'Scores released products on launch readiness based on setup completeness (dimensions, pricing, BOM, tax, default order settings) and produces a scorecard.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'product-launch-readiness-scorecard',
        "upstream_url": 'https://coworkcookbook.com/recipes/product-launch-readiness-scorecard',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07c7efc65e507d80',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/product-launch-readiness-scorecard', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ProductLaunchReadinessScorecard(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ProductLaunchReadinessScorecard'
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
    print(ProductLaunchReadinessScorecard().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

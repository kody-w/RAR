---
name: "rar-cowork-cookbook-product-launch-readiness-scorecard"
description: "Scores released products on launch readiness based on setup completeness (dimensions, pricing, BOM, tax, default order settings) and produces a scorecard."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/product_launch_readiness_scorecard", "rar_sha256": "26a8baac5f7a3ac17f0ffa8ec43de81ab6789469c41f12e717f2a6e189b31fed", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "product_launch_readiness_scorecard_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/product-launch-readiness-scorecard:c8c8fe669b8ac888ebbea626b1fa4a7cab154d9a0dc7e419f7802a119b105439", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/product_launch_readiness_scorecard`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `product_launch_readiness_scorecard_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `product_launch_readiness_scorecard_agent.py` and embedded as the fenced Python below (sha256 26a8baac5f7a3ac1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `product_launch_readiness_scorecard_agent.py` first:

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
    "version": '2.0.0',
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

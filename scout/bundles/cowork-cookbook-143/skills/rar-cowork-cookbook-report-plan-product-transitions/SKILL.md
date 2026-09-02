---
name: "rar-cowork-cookbook-report-plan-product-transitions"
description: "Builds a structured summary report of plan product transitions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_product_transitions", "rar_sha256": "7855ff6fcc67087236be0d96a3313a87a2cecf282e1fc3205424047000dc261d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_plan_product_transitions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-plan-product-transitions:570122eca8b6d92a91e4c08b8dc7ff254eb28e72ef2b31291c6b6065d4cad26b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_plan_product_transitions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_plan_product_transitions_agent.py` is
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

Plan product transitions Summary Report — Builds a structured summary report of plan product transitions activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-product-transitions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_product_transitions_agent.py` and embedded as the fenced Python below (sha256 7855ff6fcc670872…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_product_transitions_agent.py` first:

```bash
python3 report_plan_product_transitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_product_transitions_agent.py   # or on stdin
python3 report_plan_product_transitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan product transitions Summary Report — Builds a structured summary report of plan product transitions activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-product-transitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_product_transitions',
    "version": '2.0.0',
    "display_name": 'Plan product transitions Summary Report',
    "description": 'Builds a structured summary report of plan product transitions activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
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
        "upstream_slug": 'report-plan-product-transitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-product-transitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ace3fa6288b538ce',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/plan-product-transitions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-plan-product-transitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportPlanProductTransitions(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanProductTransitions'
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
    print(ReportPlanProductTransitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-plan-product-transitions"
description: "Builds a structured summary report of plan product transitions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_product_transitions", "rar_sha256": "7855ff6fcc67087236be0d96a3313a87a2cecf282e1fc3205424047000dc261d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_plan_product_transitions`. The original RAPP
agent is preserved byte-for-byte in `report_plan_product_transitions_agent.py` and in the RCI capsule.

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

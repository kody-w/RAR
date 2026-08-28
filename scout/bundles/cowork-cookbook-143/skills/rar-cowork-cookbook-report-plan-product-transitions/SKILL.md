---
name: "rar-cowork-cookbook-report-plan-product-transitions"
description: "Builds a structured summary report of plan product transitions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_product_transitions", "rar_sha256": "371f4b2fd4e4c53fd456ab4d835ed06645325539cd0a423d183d6039325c0103", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_product_transitions_agent.py` and embedded as the fenced Python below (sha256 371f4b2fd4e4c53f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_product_transitions_agent.py` first:

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
    "version": '2.0.1',
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

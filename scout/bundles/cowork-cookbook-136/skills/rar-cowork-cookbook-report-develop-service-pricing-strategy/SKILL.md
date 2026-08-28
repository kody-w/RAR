---
name: "rar-cowork-cookbook-report-develop-service-pricing-strategy"
description: "Builds a structured summary report of develop service pricing strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_service_pricing_strategy", "rar_sha256": "11d563262cb110058c4d0d8169b3d7d500bc1ea84154cccf587f4799b7606611", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_service_pricing_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_develop_service_pricing_strategy_agent.py` and in the RCI capsule.

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

Develop service pricing strategy Summary Report — Builds a structured summary report of develop service pricing strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-service-pricing-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_service_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 11d563262cb11005…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_service_pricing_strategy_agent.py` first:

```bash
python3 report_develop_service_pricing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_service_pricing_strategy_agent.py   # or on stdin
python3 report_develop_service_pricing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service pricing strategy Summary Report — Builds a structured summary report of develop service pricing strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-service-pricing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_service_pricing_strategy',
    "version": '2.0.1',
    "display_name": 'Develop service pricing strategy Summary Report',
    "description": 'Builds a structured summary report of develop service pricing strategy activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-service-pricing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-service-pricing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '87ec553bd8a9e3a9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-pricing-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-develop-service-pricing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDevelopServicePricingStrategy(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopServicePricingStrategy'
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
    print(ReportDevelopServicePricingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

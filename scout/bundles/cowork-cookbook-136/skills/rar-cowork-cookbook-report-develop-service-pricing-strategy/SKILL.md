---
name: "rar-cowork-cookbook-report-develop-service-pricing-strategy"
description: "Builds a structured summary report of develop service pricing strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_service_pricing_strategy", "rar_sha256": "a34845adfa4ef750233b5938f40dd85e9f15e835566fe9e30afd55f00b12782a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_service_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 a34845adfa4ef750…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_service_pricing_strategy_agent.py` first:

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
    "version": '2.0.0',
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

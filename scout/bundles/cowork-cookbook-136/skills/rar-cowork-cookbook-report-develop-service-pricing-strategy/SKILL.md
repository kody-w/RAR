---
name: "rar-cowork-cookbook-report-develop-service-pricing-strategy"
description: "Builds a structured summary report of develop service pricing strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_service_pricing_strategy", "rar_sha256": "a34845adfa4ef750233b5938f40dd85e9f15e835566fe9e30afd55f00b12782a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_develop_service_pricing_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-develop-service-pricing-strategy:7371530c2c8a0ab2542d395efd1b59813ed10f4d4e225974fa38c2349acf763a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_develop_service_pricing_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_develop_service_pricing_strategy_agent.py` is
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

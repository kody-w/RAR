---
name: "rar-cowork-cookbook-report-develop-scenario-and-contingency-plans"
description: "Builds a structured summary report of develop scenario and contingency plans activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_scenario_and_contingency_plans", "rar_sha256": "286036fe9c48499521d15d90efcb8e32fbf83b8422e11953e26ded939152c4c3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_develop_scenario_and_contingency_plans_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-develop-scenario-and-contingency-plans:b2a2f661cb6d617d8580f05786d51433f7271d93a0cc2ac288f5deb97ea0583c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_develop_scenario_and_contingency_plans`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_develop_scenario_and_contingency_plans_agent.py` is
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

Develop scenario and contingency plans Summary Report — Builds a structured summary report of develop scenario and contingency plans activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-scenario-and-contingency-plans
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_scenario_and_contingency_plans_agent.py` and embedded as the fenced Python below (sha256 286036fe9c484995…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_scenario_and_contingency_plans_agent.py` first:

```bash
python3 report_develop_scenario_and_contingency_plans_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_scenario_and_contingency_plans_agent.py   # or on stdin
python3 report_develop_scenario_and_contingency_plans_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop scenario and contingency plans Summary Report — Builds a structured summary report of develop scenario and contingency plans activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-scenario-and-contingency-plans
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_scenario_and_contingency_plans',
    "version": '2.0.0',
    "display_name": 'Develop scenario and contingency plans Summary Report',
    "description": 'Builds a structured summary report of develop scenario and contingency plans activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-scenario-and-contingency-plans',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-scenario-and-contingency-plans',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6b43db9ae4839cb9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-scenario-and-contingency-plans'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-develop-scenario-and-contingency-plans', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDevelopScenarioAndContingencyPlans(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopScenarioAndContingencyPlans'
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
    print(ReportDevelopScenarioAndContingencyPlans().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

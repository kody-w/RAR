---
name: "rar-cowork-cookbook-report-develop-scenario-and-contingency-plans"
description: "Builds a structured summary report of develop scenario and contingency plans activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_scenario_and_contingency_plans", "rar_sha256": "286036fe9c48499521d15d90efcb8e32fbf83b8422e11953e26ded939152c4c3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_scenario_and_contingency_plans`. The original RAPP
agent is preserved byte-for-byte in `report_develop_scenario_and_contingency_plans_agent.py` and in the RCI capsule.

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

---
name: "rar-cowork-cookbook-report-develop-scenario-and-contingency-plans"
description: "Builds a structured summary report of develop scenario and contingency plans activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_scenario_and_contingency_plans", "rar_sha256": "767a210b2d39abe9bb49e75497df2fb0c6e77775bb780259a4822a136d0b0c41", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_scenario_and_contingency_plans_agent.py` and embedded as the fenced Python below (sha256 767a210b2d39abe9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_scenario_and_contingency_plans_agent.py` first:

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
    "version": '2.0.1',
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

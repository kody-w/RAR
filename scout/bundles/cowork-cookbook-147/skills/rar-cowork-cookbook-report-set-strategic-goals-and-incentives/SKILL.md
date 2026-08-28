---
name: "rar-cowork-cookbook-report-set-strategic-goals-and-incentives"
description: "Builds a structured summary report of set strategic goals and incentives activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_set_strategic_goals_and_incentives", "rar_sha256": "6c2d63fda97279e72dcea27fa0ba4b6aa6a864c25141c3f9cfcf38b9550a7811", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_set_strategic_goals_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `report_set_strategic_goals_and_incentives_agent.py` and in the RCI capsule.

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

Set strategic goals and incentives Summary Report — Builds a structured summary report of set strategic goals and incentives activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-set-strategic-goals-and-incentives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_set_strategic_goals_and_incentives_agent.py` and embedded as the fenced Python below (sha256 6c2d63fda97279e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_set_strategic_goals_and_incentives_agent.py` first:

```bash
python3 report_set_strategic_goals_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_set_strategic_goals_and_incentives_agent.py   # or on stdin
python3 report_set_strategic_goals_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set strategic goals and incentives Summary Report — Builds a structured summary report of set strategic goals and incentives activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-set-strategic-goals-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_set_strategic_goals_and_incentives',
    "version": '2.0.0',
    "display_name": 'Set strategic goals and incentives Summary Report',
    "description": 'Builds a structured summary report of set strategic goals and incentives activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-set-strategic-goals-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-set-strategic-goals-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1821dd6962e79866',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/set-strategic-goals-and-incentives'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-set-strategic-goals-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportSetStrategicGoalsAndIncentives(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportSetStrategicGoalsAndIncentives'
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
    print(ReportSetStrategicGoalsAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

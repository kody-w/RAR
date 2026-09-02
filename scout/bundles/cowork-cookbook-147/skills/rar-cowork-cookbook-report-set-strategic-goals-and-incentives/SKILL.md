---
name: "rar-cowork-cookbook-report-set-strategic-goals-and-incentives"
description: "Builds a structured summary report of set strategic goals and incentives activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_set_strategic_goals_and_incentives", "rar_sha256": "6c2d63fda97279e72dcea27fa0ba4b6aa6a864c25141c3f9cfcf38b9550a7811", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_set_strategic_goals_and_incentives_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-set-strategic-goals-and-incentives:485773086cce90d38f108d545a20cb7c329eb9f16d0e48bb79373ead089903fd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_set_strategic_goals_and_incentives`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_set_strategic_goals_and_incentives_agent.py` is
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

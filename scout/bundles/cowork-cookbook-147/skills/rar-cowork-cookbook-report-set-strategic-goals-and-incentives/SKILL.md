---
name: "rar-cowork-cookbook-report-set-strategic-goals-and-incentives"
description: "Builds a structured summary report of set strategic goals and incentives activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_set_strategic_goals_and_incentives", "rar_sha256": "f18f6516439af10340e35ad2f901c2b48de6e8d23368bfbe5dc4ec7935feeaaf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_set_strategic_goals_and_incentives_agent.py` and embedded as the fenced Python below (sha256 f18f6516439af103…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_set_strategic_goals_and_incentives_agent.py` first:

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
    "version": '2.0.1',
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

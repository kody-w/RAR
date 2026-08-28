---
name: "rar-cowork-cookbook-report-plan-workforce-capacity"
description: "Builds a structured summary report of plan workforce capacity activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_workforce_capacity", "rar_sha256": "eb3592627fb0cf2ebbac2f2057883614bd7304776da3c50ac7931462680cd45f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_plan_workforce_capacity`. The original RAPP
agent is preserved byte-for-byte in `report_plan_workforce_capacity_agent.py` and in the RCI capsule.

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

Plan workforce capacity Summary Report — Builds a structured summary report of plan workforce capacity activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-workforce-capacity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_workforce_capacity_agent.py` and embedded as the fenced Python below (sha256 eb3592627fb0cf2e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_workforce_capacity_agent.py` first:

```bash
python3 report_plan_workforce_capacity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_workforce_capacity_agent.py   # or on stdin
python3 report_plan_workforce_capacity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce capacity Summary Report — Builds a structured summary report of plan workforce capacity activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-workforce-capacity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_workforce_capacity',
    "version": '2.0.1',
    "display_name": 'Plan workforce capacity Summary Report',
    "description": 'Builds a structured summary report of plan workforce capacity activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-plan-workforce-capacity',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-workforce-capacity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0ad804255ec698eb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/plan-workforce-capacity'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-plan-workforce-capacity', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportPlanWorkforceCapacity(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanWorkforceCapacity'
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
    print(ReportPlanWorkforceCapacity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

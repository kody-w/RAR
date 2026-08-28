---
name: "rar-cowork-cookbook-report-plan-workforce-capacity"
description: "Builds a structured summary report of plan workforce capacity activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_workforce_capacity", "rar_sha256": "5ec24ed50604bdf64c49c5e9eb23e46ef12d58e10dc4103e5254da807a54b344", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_workforce_capacity_agent.py` and embedded as the fenced Python below (sha256 5ec24ed50604bdf6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_workforce_capacity_agent.py` first:

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
    "version": '2.0.0',
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

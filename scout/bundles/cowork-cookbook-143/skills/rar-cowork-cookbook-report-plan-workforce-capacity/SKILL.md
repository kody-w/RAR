---
name: "rar-cowork-cookbook-report-plan-workforce-capacity"
description: "Builds a structured summary report of plan workforce capacity activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_workforce_capacity", "rar_sha256": "5ec24ed50604bdf64c49c5e9eb23e46ef12d58e10dc4103e5254da807a54b344", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_plan_workforce_capacity_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-plan-workforce-capacity:14623012964feac38b18c888e35c6ad50beb89b47c78315b0f6918f0f7ed18e6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_plan_workforce_capacity`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_plan_workforce_capacity_agent.py` is
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

---
name: "rar-cowork-cookbook-report-plan-project-tasks"
description: "Builds a structured summary report of plan project tasks activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_project_tasks", "rar_sha256": "0c1da496a250d707e4466167e9f495bcd60fffb7db23f7cb41dd21cb4e5d7755", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_plan_project_tasks_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-plan-project-tasks:ef2c7feb070372f553f2cc8144e62a0d75d6419518d508268a9e2107d25f3b3d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_plan_project_tasks`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_plan_project_tasks_agent.py` is
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

Plan project tasks Summary Report — Builds a structured summary report of plan project tasks activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-project-tasks
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_project_tasks_agent.py` and embedded as the fenced Python below (sha256 0c1da496a250d707…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_project_tasks_agent.py` first:

```bash
python3 report_plan_project_tasks_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_project_tasks_agent.py   # or on stdin
python3 report_plan_project_tasks_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan project tasks Summary Report — Builds a structured summary report of plan project tasks activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-project-tasks
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_project_tasks',
    "version": '2.0.0',
    "display_name": 'Plan project tasks Summary Report',
    "description": 'Builds a structured summary report of plan project tasks activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-plan-project-tasks',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-project-tasks',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ba696189863b94e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/plan-project-tasks'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-plan-project-tasks', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportPlanProjectTasks(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanProjectTasks'
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
    print(ReportPlanProjectTasks().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

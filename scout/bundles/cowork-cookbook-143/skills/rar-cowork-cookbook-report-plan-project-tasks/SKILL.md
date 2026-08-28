---
name: "rar-cowork-cookbook-report-plan-project-tasks"
description: "Builds a structured summary report of plan project tasks activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_project_tasks", "rar_sha256": "0c1da496a250d707e4466167e9f495bcd60fffb7db23f7cb41dd21cb4e5d7755", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_plan_project_tasks`. The original RAPP
agent is preserved byte-for-byte in `report_plan_project_tasks_agent.py` and in the RCI capsule.

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

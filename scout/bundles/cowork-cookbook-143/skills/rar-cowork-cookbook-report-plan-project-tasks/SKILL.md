---
name: "rar-cowork-cookbook-report-plan-project-tasks"
description: "Builds a structured summary report of plan project tasks activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_project_tasks", "rar_sha256": "5998ebf74023b2c169368e48aef8f18cb1ce186a70d5cdde22b8aa9fca0416f7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_project_tasks_agent.py` and embedded as the fenced Python below (sha256 5998ebf74023b2c1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_project_tasks_agent.py` first:

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
    "version": '2.0.1',
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

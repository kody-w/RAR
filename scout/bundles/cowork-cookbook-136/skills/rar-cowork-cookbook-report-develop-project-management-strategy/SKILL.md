---
name: "rar-cowork-cookbook-report-develop-project-management-strategy"
description: "Builds a structured summary report of develop project management strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_project_management_strategy", "rar_sha256": "e50d4b60068fe0962b99c61d3f27de226daf37ea33c49b6ebf7335d523ac207a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_project_management_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_develop_project_management_strategy_agent.py` and in the RCI capsule.

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

Develop project management strategy Summary Report — Builds a structured summary report of develop project management strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-project-management-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_project_management_strategy_agent.py` and embedded as the fenced Python below (sha256 e50d4b60068fe096…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_project_management_strategy_agent.py` first:

```bash
python3 report_develop_project_management_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_project_management_strategy_agent.py   # or on stdin
python3 report_develop_project_management_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop project management strategy Summary Report — Builds a structured summary report of develop project management strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-project-management-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_project_management_strategy',
    "version": '2.0.0',
    "display_name": 'Develop project management strategy Summary Report',
    "description": 'Builds a structured summary report of develop project management strategy activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-develop-project-management-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-project-management-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9dae150a2212296e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/develop-project-strategy/develop-project-management-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-develop-project-management-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDevelopProjectManagementStrategy(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopProjectManagementStrategy'
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
    print(ReportDevelopProjectManagementStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

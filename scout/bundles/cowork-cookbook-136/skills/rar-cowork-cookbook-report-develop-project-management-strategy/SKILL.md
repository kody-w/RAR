---
name: "rar-cowork-cookbook-report-develop-project-management-strategy"
description: "Builds a structured summary report of develop project management strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_project_management_strategy", "rar_sha256": "38f22edb5f86952398226d95d29dda43a1263402945fc5962bcf36583bf0998b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_project_management_strategy_agent.py` and embedded as the fenced Python below (sha256 38f22edb5f869523…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_project_management_strategy_agent.py` first:

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
    "version": '2.0.1',
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

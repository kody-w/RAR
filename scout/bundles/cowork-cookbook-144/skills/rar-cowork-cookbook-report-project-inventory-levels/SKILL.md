---
name: "rar-cowork-cookbook-report-project-inventory-levels"
description: "Builds a structured summary report of project inventory levels activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_project_inventory_levels", "rar_sha256": "1cebf21a33727807ee4abfed3a6a5d7c12be45a9926a1667db6fbf3eab20245f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_project_inventory_levels`. The original RAPP
agent is preserved byte-for-byte in `report_project_inventory_levels_agent.py` and in the RCI capsule.

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

Project inventory levels Summary Report — Builds a structured summary report of project inventory levels activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-project-inventory-levels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_project_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 1cebf21a33727807…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_project_inventory_levels_agent.py` first:

```bash
python3 report_project_inventory_levels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_project_inventory_levels_agent.py   # or on stdin
python3 report_project_inventory_levels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Project inventory levels Summary Report — Builds a structured summary report of project inventory levels activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-project-inventory-levels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_project_inventory_levels',
    "version": '2.0.0',
    "display_name": 'Project inventory levels Summary Report',
    "description": 'Builds a structured summary report of project inventory levels activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-project-inventory-levels',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-project-inventory-levels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd703a8cb6fb52009',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/project-inventory-levels'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-project-inventory-levels', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportProjectInventoryLevels(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportProjectInventoryLevels'
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
    print(ReportProjectInventoryLevels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

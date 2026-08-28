---
name: "rar-cowork-cookbook-report-project-inventory-levels"
description: "Builds a structured summary report of project inventory levels activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_project_inventory_levels", "rar_sha256": "fce330ad5a282dff585728b0a22f239a3c755a0216e4eae00b0be8f609c147e6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_project_inventory_levels_agent.py` and embedded as the fenced Python below (sha256 fce330ad5a282dff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_project_inventory_levels_agent.py` first:

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
    "version": '2.0.1',
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

---
name: "rar-cowork-cookbook-report-project-inventory-levels"
description: "Builds a structured summary report of project inventory levels activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_project_inventory_levels", "rar_sha256": "1cebf21a33727807ee4abfed3a6a5d7c12be45a9926a1667db6fbf3eab20245f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_project_inventory_levels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-project-inventory-levels:b7ba9bd86ca6b977cd07731d0f7dc5949da48c11d005d9759d707086628f4d0b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_project_inventory_levels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_project_inventory_levels_agent.py` is
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

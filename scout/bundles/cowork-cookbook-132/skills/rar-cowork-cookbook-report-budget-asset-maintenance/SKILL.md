---
name: "rar-cowork-cookbook-report-budget-asset-maintenance"
description: "Builds a structured summary report of budget asset maintenance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_budget_asset_maintenance", "rar_sha256": "6a3bf315aac0ddbf23517aea387fe24c9f571f788405bbffdcbf35f97c283b82", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_budget_asset_maintenance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-budget-asset-maintenance:c4f3f253f46fb4087053b855b39c68ad6f20bac4a581d30f512dee5ad86f57ea", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_budget_asset_maintenance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_budget_asset_maintenance_agent.py` is
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

Budget asset maintenance Summary Report — Builds a structured summary report of budget asset maintenance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-budget-asset-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_budget_asset_maintenance_agent.py` and embedded as the fenced Python below (sha256 6a3bf315aac0ddbf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_budget_asset_maintenance_agent.py` first:

```bash
python3 report_budget_asset_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_budget_asset_maintenance_agent.py   # or on stdin
python3 report_budget_asset_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget asset maintenance Summary Report — Builds a structured summary report of budget asset maintenance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-budget-asset-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_budget_asset_maintenance',
    "version": '2.0.0',
    "display_name": 'Budget asset maintenance Summary Report',
    "description": 'Builds a structured summary report of budget asset maintenance activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-budget-asset-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-budget-asset-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'be61a2cf6c82ee36',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/budget-asset-maintenance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-budget-asset-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportBudgetAssetMaintenance(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportBudgetAssetMaintenance'
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
    print(ReportBudgetAssetMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-budget-asset-maintenance"
description: "Builds a structured summary report of budget asset maintenance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_budget_asset_maintenance", "rar_sha256": "6a3bf315aac0ddbf23517aea387fe24c9f571f788405bbffdcbf35f97c283b82", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_budget_asset_maintenance`. The original RAPP
agent is preserved byte-for-byte in `report_budget_asset_maintenance_agent.py` and in the RCI capsule.

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

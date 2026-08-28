---
name: "rar-cowork-cookbook-report-budget-asset-maintenance"
description: "Builds a structured summary report of budget asset maintenance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_budget_asset_maintenance", "rar_sha256": "0c04ed4689d6bab9eff37ad527ed35338ae6e63e4736aa552efb23963b509682", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_budget_asset_maintenance_agent.py` and embedded as the fenced Python below (sha256 0c04ed4689d6bab9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_budget_asset_maintenance_agent.py` first:

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
    "version": '2.0.1',
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

---
name: "rar-cowork-cookbook-report-budget-fixed-assets"
description: "Builds a structured summary report of budget fixed assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_budget_fixed_assets", "rar_sha256": "94fafb9d6466c4937baf62a1adc9d072b02db68172c38fcb934d3a3a67c6ca44", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_budget_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `report_budget_fixed_assets_agent.py` and in the RCI capsule.

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

Budget fixed assets Summary Report — Builds a structured summary report of budget fixed assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-budget-fixed-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_budget_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 94fafb9d6466c493…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_budget_fixed_assets_agent.py` first:

```bash
python3 report_budget_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_budget_fixed_assets_agent.py   # or on stdin
python3 report_budget_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget fixed assets Summary Report — Builds a structured summary report of budget fixed assets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-budget-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_budget_fixed_assets',
    "version": '2.0.1',
    "display_name": 'Budget fixed assets Summary Report',
    "description": 'Builds a structured summary report of budget fixed assets activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-budget-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-budget-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '035a7def79979a16',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/budget-fixed-assets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/report-budget-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportBudgetFixedAssets(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportBudgetFixedAssets'
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
    print(ReportBudgetFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-report-budget-fixed-assets"
description: "Builds a structured summary report of budget fixed assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_budget_fixed_assets", "rar_sha256": "048dc3382acd0174ad6fce2b6fe2ced8eed5683a0c1bf5322d72dfb84e9a091c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_budget_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 048dc3382acd0174…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_budget_fixed_assets_agent.py` first:

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
    "version": '2.0.0',
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

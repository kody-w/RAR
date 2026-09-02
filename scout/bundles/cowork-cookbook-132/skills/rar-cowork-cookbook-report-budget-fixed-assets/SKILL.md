---
name: "rar-cowork-cookbook-report-budget-fixed-assets"
description: "Builds a structured summary report of budget fixed assets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_budget_fixed_assets", "rar_sha256": "048dc3382acd0174ad6fce2b6fe2ced8eed5683a0c1bf5322d72dfb84e9a091c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_budget_fixed_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-budget-fixed-assets:d76bcb4dd33903be5bb5e1a42ce798bb827cb03ee150bed5b99784abfb7f82c5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_budget_fixed_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_budget_fixed_assets_agent.py` is
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

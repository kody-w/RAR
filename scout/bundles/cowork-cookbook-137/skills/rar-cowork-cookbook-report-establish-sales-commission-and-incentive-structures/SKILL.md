---
name: "rar-cowork-cookbook-report-establish-sales-commission-and-incentive-structures"
description: "Builds a structured summary report of establish sales commission and incentive structures activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_establish_sales_commission_and_incentive_structures", "rar_sha256": "fda6515ad660fe2b05bbc7ea7d252765e06fa0ec22bcaa1732e3736a9d02529a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_establish_sales_commission_and_incentive_structures`. The original RAPP
agent is preserved byte-for-byte in `report_establish_sales_commission_and_incentive_structures_agent.py` and in the RCI capsule.

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

Establish sales commission and incentive structures Summary Report — Builds a structured summary report of establish sales commission and incentive structures activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-establish-sales-commission-and-incentive-structures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_establish_sales_commission_and_incentive_structures_agent.py` and embedded as the fenced Python below (sha256 fda6515ad660fe2b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_establish_sales_commission_and_incentive_structures_agent.py` first:

```bash
python3 report_establish_sales_commission_and_incentive_structures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_establish_sales_commission_and_incentive_structures_agent.py   # or on stdin
python3 report_establish_sales_commission_and_incentive_structures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish sales commission and incentive structures Summary Report — Builds a structured summary report of establish sales commission and incentive structures activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-establish-sales-commission-and-incentive-structures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_establish_sales_commission_and_incentive_structures',
    "version": '2.0.1',
    "display_name": 'Establish sales commission and incentive structures Summary Report',
    "description": 'Builds a structured summary report of establish sales commission and incentive structures activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-establish-sales-commission-and-incentive-structures',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-establish-sales-commission-and-incentive-structures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f6ed50cb15f79afb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/establish-sales-commission-and-incentive-structures'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/report-establish-sales-commission-and-incentive-structures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportEstablishSalesCommissionAndIncentiveStructures(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportEstablishSalesCommissionAndIncentiveStructures'
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
    print(ReportEstablishSalesCommissionAndIncentiveStructures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

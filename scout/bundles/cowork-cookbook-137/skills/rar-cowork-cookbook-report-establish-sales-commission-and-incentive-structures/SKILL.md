---
name: "rar-cowork-cookbook-report-establish-sales-commission-and-incentive-structures"
description: "Builds a structured summary report of establish sales commission and incentive structures activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_establish_sales_commission_and_incentive_structures", "rar_sha256": "cafb0de750dd62746e655e30689b50bc4d9bbbd56d3d47dde8708042b719a775", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_establish_sales_commission_and_incentive_structures_agent.py` and embedded as the fenced Python below (sha256 cafb0de750dd6274…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_establish_sales_commission_and_incentive_structures_agent.py` first:

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
    "version": '2.0.0',
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

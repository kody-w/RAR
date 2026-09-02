---
name: "rar-cowork-cookbook-report-establish-sales-commission-and-incentive-structures"
description: "Builds a structured summary report of establish sales commission and incentive structures activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_establish_sales_commission_and_incentive_structures", "rar_sha256": "cafb0de750dd62746e655e30689b50bc4d9bbbd56d3d47dde8708042b719a775", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_establish_sales_commission_and_incentive_structures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-establish-sales-commission-and-incentive-structures:f206873ced247002c3c21d2b92377d696ee0071f2724a558eb7c027989275d01", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_establish_sales_commission_and_incentive_structures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_establish_sales_commission_and_incentive_structures_agent.py` is
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

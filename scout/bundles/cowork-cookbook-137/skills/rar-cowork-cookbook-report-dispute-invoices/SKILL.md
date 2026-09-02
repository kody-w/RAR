---
name: "rar-cowork-cookbook-report-dispute-invoices"
description: "Builds a structured summary report of dispute invoices activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_dispute_invoices", "rar_sha256": "4aad2bea060a1c404d4037d365c0a82c12e1a744a49868b434da66ae9f8762c6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_dispute_invoices_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-dispute-invoices:bf8bae0ec9d402d0e75a694b31657b0b5ed07c77b25777e73008c0f665149077", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_dispute_invoices`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_dispute_invoices_agent.py` is
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

Dispute invoices Summary Report — Builds a structured summary report of dispute invoices activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-dispute-invoices
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_dispute_invoices_agent.py` and embedded as the fenced Python below (sha256 4aad2bea060a1c40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_dispute_invoices_agent.py` first:

```bash
python3 report_dispute_invoices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_dispute_invoices_agent.py   # or on stdin
python3 report_dispute_invoices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Dispute invoices Summary Report — Builds a structured summary report of dispute invoices activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-dispute-invoices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_dispute_invoices',
    "version": '2.0.0',
    "display_name": 'Dispute invoices Summary Report',
    "description": 'Builds a structured summary report of dispute invoices activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-dispute-invoices',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-dispute-invoices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '433c69f430c9af40',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/dispute-invoices'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-dispute-invoices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportDisputeInvoices(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDisputeInvoices'
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
    print(ReportDisputeInvoices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

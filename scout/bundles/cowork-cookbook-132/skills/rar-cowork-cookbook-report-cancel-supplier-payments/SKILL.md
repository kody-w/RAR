---
name: "rar-cowork-cookbook-report-cancel-supplier-payments"
description: "Builds a structured summary report of cancel supplier payments activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_cancel_supplier_payments", "rar_sha256": "1f4ac4b3af5d751f978647499033ebad7036161aa046e09873081017a00b3258", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_cancel_supplier_payments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-cancel-supplier-payments:e6a7863ef845fc2591818d0c353ab6b9712bc05d8f0d606360d6258828f6c382", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_cancel_supplier_payments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_cancel_supplier_payments_agent.py` is
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

Cancel supplier payments Summary Report — Builds a structured summary report of cancel supplier payments activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-cancel-supplier-payments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_cancel_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 1f4ac4b3af5d751f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_cancel_supplier_payments_agent.py` first:

```bash
python3 report_cancel_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_cancel_supplier_payments_agent.py   # or on stdin
python3 report_cancel_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cancel supplier payments Summary Report — Builds a structured summary report of cancel supplier payments activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-cancel-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_cancel_supplier_payments',
    "version": '2.0.0',
    "display_name": 'Cancel supplier payments Summary Report',
    "description": 'Builds a structured summary report of cancel supplier payments activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-cancel-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-cancel-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'af81045b507299ca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/cancel-supplier-payments'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-cancel-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportCancelSupplierPayments(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCancelSupplierPayments'
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
    print(ReportCancelSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

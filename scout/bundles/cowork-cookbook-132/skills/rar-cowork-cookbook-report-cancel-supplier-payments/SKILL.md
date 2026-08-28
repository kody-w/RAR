---
name: "rar-cowork-cookbook-report-cancel-supplier-payments"
description: "Builds a structured summary report of cancel supplier payments activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_cancel_supplier_payments", "rar_sha256": "f0d4ecaa101a68d8a9c1714a5a77af1f62f1289b168bb5fa19071c517b71d53e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_cancel_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `report_cancel_supplier_payments_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_cancel_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 f0d4ecaa101a68d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_cancel_supplier_payments_agent.py` first:

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
    "version": '2.0.1',
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

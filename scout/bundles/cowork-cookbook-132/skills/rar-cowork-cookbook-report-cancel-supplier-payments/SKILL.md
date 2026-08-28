---
name: "rar-cowork-cookbook-report-cancel-supplier-payments"
description: "Builds a structured summary report of cancel supplier payments activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_cancel_supplier_payments", "rar_sha256": "1f4ac4b3af5d751f978647499033ebad7036161aa046e09873081017a00b3258", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

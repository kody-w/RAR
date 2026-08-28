---
name: "rar-cowork-cookbook-report-dispute-invoices"
description: "Builds a structured summary report of dispute invoices activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_dispute_invoices", "rar_sha256": "4aad2bea060a1c404d4037d365c0a82c12e1a744a49868b434da66ae9f8762c6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_dispute_invoices`. The original RAPP
agent is preserved byte-for-byte in `report_dispute_invoices_agent.py` and in the RCI capsule.

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

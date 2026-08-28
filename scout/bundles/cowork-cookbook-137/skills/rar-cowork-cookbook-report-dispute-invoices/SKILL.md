---
name: "rar-cowork-cookbook-report-dispute-invoices"
description: "Builds a structured summary report of dispute invoices activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_dispute_invoices", "rar_sha256": "9f645bd368718172c8ec379450fc53385632e1426d00232702d2565888791683", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_dispute_invoices_agent.py` and embedded as the fenced Python below (sha256 9f645bd368718172…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_dispute_invoices_agent.py` first:

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
    "version": '2.0.1',
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

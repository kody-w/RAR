---
name: "rar-cowork-cookbook-report-reconcile-ledger-and-subledger"
description: "Builds a structured summary report of reconcile ledger and subledger activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_reconcile_ledger_and_subledger", "rar_sha256": "439d19da4eea15a7cc306ee4685fbe67603780e17488a429e08283337b9c8ac9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_reconcile_ledger_and_subledger`. The original RAPP
agent is preserved byte-for-byte in `report_reconcile_ledger_and_subledger_agent.py` and in the RCI capsule.

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

Reconcile ledger and subledger Summary Report — Builds a structured summary report of reconcile ledger and subledger activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-reconcile-ledger-and-subledger
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_reconcile_ledger_and_subledger_agent.py` and embedded as the fenced Python below (sha256 439d19da4eea15a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_reconcile_ledger_and_subledger_agent.py` first:

```bash
python3 report_reconcile_ledger_and_subledger_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_reconcile_ledger_and_subledger_agent.py   # or on stdin
python3 report_reconcile_ledger_and_subledger_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile ledger and subledger Summary Report — Builds a structured summary report of reconcile ledger and subledger activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-reconcile-ledger-and-subledger
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_reconcile_ledger_and_subledger',
    "version": '2.0.1',
    "display_name": 'Reconcile ledger and subledger Summary Report',
    "description": 'Builds a structured summary report of reconcile ledger and subledger activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-reconcile-ledger-and-subledger',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-reconcile-ledger-and-subledger',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e179649b44aded3a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/reconcile-ledger-and-subledger'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-reconcile-ledger-and-subledger', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportReconcileLedgerAndSubledger(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReconcileLedgerAndSubledger'
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
    print(ReportReconcileLedgerAndSubledger().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

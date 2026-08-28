---
name: "rar-cowork-cookbook-report-reconcile-ledger-and-subledger"
description: "Builds a structured summary report of reconcile ledger and subledger activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_reconcile_ledger_and_subledger", "rar_sha256": "bdb39d7a4e5fa4ab7b8a0c6eb13f665a79ac89278772fd490305e152d7eadf21", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_reconcile_ledger_and_subledger_agent.py` and embedded as the fenced Python below (sha256 bdb39d7a4e5fa4ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_reconcile_ledger_and_subledger_agent.py` first:

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
    "version": '2.0.0',
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

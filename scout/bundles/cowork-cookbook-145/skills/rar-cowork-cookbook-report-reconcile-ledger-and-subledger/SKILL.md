---
name: "rar-cowork-cookbook-report-reconcile-ledger-and-subledger"
description: "Builds a structured summary report of reconcile ledger and subledger activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_reconcile_ledger_and_subledger", "rar_sha256": "bdb39d7a4e5fa4ab7b8a0c6eb13f665a79ac89278772fd490305e152d7eadf21", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_reconcile_ledger_and_subledger_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-reconcile-ledger-and-subledger:80f75bc06fa9766ffec55a75c82828cd78497384630593255b6f93b9e2b42185", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_reconcile_ledger_and_subledger`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_reconcile_ledger_and_subledger_agent.py` is
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

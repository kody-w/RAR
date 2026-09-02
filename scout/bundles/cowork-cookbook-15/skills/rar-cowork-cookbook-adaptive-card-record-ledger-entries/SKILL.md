---
name: "rar-cowork-cookbook-adaptive-card-record-ledger-entries"
description: "Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_record_ledger_entries", "rar_sha256": "47765e95b93ddfcb4dd0514e896f83c0bd59c31448b741aedcddd355ee8e4264", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_record_ledger_entries_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-record-ledger-entries:a9eb304dcddddd9fdec51983572897637d9cd3ce6dea9d5391088d18d04561ad", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_record_ledger_entries`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_record_ledger_entries_agent.py` is
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

Record ledger entries Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_record_ledger_entries_agent.py` and embedded as the fenced Python below (sha256 47765e95b93ddfcb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_record_ledger_entries_agent.py` first:

```bash
python3 adaptive_card_record_ledger_entries_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_record_ledger_entries_agent.py   # or on stdin
python3 adaptive_card_record_ledger_entries_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record ledger entries Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_record_ledger_entries',
    "version": '2.0.0',
    "display_name": 'Record ledger entries Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of record ledger entries status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-record-ledger-entries',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-record-ledger-entries',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '786ec6c04ed8c6a2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-ledger-entries'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/adaptive-card-record-ledger-entries', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardRecordLedgerEntries(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRecordLedgerEntries'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(AdaptiveCardRecordLedgerEntries().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

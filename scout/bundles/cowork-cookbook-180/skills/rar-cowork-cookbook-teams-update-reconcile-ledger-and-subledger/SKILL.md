---
name: "rar-cowork-cookbook-teams-update-reconcile-ledger-and-subledger"
description: "Drafts a Teams channel post on reconcile ledger and subledger status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_reconcile_ledger_and_subledger", "rar_sha256": "abaadad9fa7fd873c94b46622c766eeb219430b01967ecc0b4564cb290ca966e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_reconcile_ledger_and_subledger_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-reconcile-ledger-and-subledger:cf52086d152b08d8bbfeabd4ef79b387d4934452a8f54233a9212b1040085511", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_reconcile_ledger_and_subledger`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_reconcile_ledger_and_subledger_agent.py` is
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

Reconcile ledger and subledger Teams Channel Update — Drafts a Teams channel post on reconcile ledger and subledger status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-reconcile-ledger-and-subledger
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_reconcile_ledger_and_subledger_agent.py` and embedded as the fenced Python below (sha256 abaadad9fa7fd873…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_reconcile_ledger_and_subledger_agent.py` first:

```bash
python3 teams_update_reconcile_ledger_and_subledger_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_reconcile_ledger_and_subledger_agent.py   # or on stdin
python3 teams_update_reconcile_ledger_and_subledger_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile ledger and subledger Teams Channel Update — Drafts a Teams channel post on reconcile ledger and subledger status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-reconcile-ledger-and-subledger
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_reconcile_ledger_and_subledger',
    "version": '2.0.0',
    "display_name": 'Reconcile ledger and subledger Teams Channel Update',
    "description": 'Drafts a Teams channel post on reconcile ledger and subledger status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-reconcile-ledger-and-subledger',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-reconcile-ledger-and-subledger',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0f648109804ca146',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/reconcile-ledger-and-subledger'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-reconcile-ledger-and-subledger', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateReconcileLedgerAndSubledger(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateReconcileLedgerAndSubledger'
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
    print(TeamsUpdateReconcileLedgerAndSubledger().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

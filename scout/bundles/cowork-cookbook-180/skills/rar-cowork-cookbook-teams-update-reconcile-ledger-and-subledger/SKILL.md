---
name: "rar-cowork-cookbook-teams-update-reconcile-ledger-and-subledger"
description: "Drafts a Teams channel post on reconcile ledger and subledger status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_reconcile_ledger_and_subledger", "rar_sha256": "fd4efe29103038e7717a1dd2e825be686743bf53a88ccef438191dc95d69db67", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_reconcile_ledger_and_subledger`. The original RAPP
agent is preserved byte-for-byte in `teams_update_reconcile_ledger_and_subledger_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_reconcile_ledger_and_subledger_agent.py` and embedded as the fenced Python below (sha256 fd4efe29103038e7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_reconcile_ledger_and_subledger_agent.py` first:

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
    "version": '2.0.1',
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

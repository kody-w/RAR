---
name: "rar-cowork-cookbook-teams-update-reconcile-ledger-and-subledger"
description: "Drafts a Teams channel post on reconcile ledger and subledger status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_reconcile_ledger_and_subledger", "rar_sha256": "abaadad9fa7fd873c94b46622c766eeb219430b01967ecc0b4564cb290ca966e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

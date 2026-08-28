---
name: "rar-cowork-cookbook-scheduled-brief-reconcile-bank-accounts"
description: "Schedulable morning-brief email summarizing reconcile bank accounts for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_reconcile_bank_accounts", "rar_sha256": "6db35de472237918c2eb901df17e4b3cb2e6a8f7c521a7f8f34f1fe8a848d3a1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_reconcile_bank_accounts`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_reconcile_bank_accounts_agent.py` and in the RCI capsule.

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

Reconcile bank accounts Scheduled Email Brief — Schedulable morning-brief email summarizing reconcile bank accounts for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-reconcile-bank-accounts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_reconcile_bank_accounts_agent.py` and embedded as the fenced Python below (sha256 6db35de472237918…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_reconcile_bank_accounts_agent.py` first:

```bash
python3 scheduled_brief_reconcile_bank_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_reconcile_bank_accounts_agent.py   # or on stdin
python3 scheduled_brief_reconcile_bank_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile bank accounts Scheduled Email Brief — Schedulable morning-brief email summarizing reconcile bank accounts for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-reconcile-bank-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_reconcile_bank_accounts',
    "version": '2.0.1',
    "display_name": 'Reconcile bank accounts Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing reconcile bank accounts for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-reconcile-bank-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-reconcile-bank-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '69aaaf1ea9272d26',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/reconcile-bank-accounts'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-reconcile-bank-accounts', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ScheduledBriefReconcileBankAccounts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReconcileBankAccounts'
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
    print(ScheduledBriefReconcileBankAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

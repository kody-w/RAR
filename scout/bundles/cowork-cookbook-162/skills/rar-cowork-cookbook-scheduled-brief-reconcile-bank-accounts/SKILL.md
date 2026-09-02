---
name: "rar-cowork-cookbook-scheduled-brief-reconcile-bank-accounts"
description: "Schedulable morning-brief email summarizing reconcile bank accounts for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_reconcile_bank_accounts", "rar_sha256": "f5fef67f7b740414caa7c47dd3f8ff0d464922e4e76d62fdfcdc8feeda3b100c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_reconcile_bank_accounts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-reconcile-bank-accounts:d26d739705703b548f7e1c8f46eff5af850c55f246399059fa97e5b674dfbbb3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_reconcile_bank_accounts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_reconcile_bank_accounts_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_reconcile_bank_accounts_agent.py` and embedded as the fenced Python below (sha256 f5fef67f7b740414…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_reconcile_bank_accounts_agent.py` first:

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
    "version": '2.0.0',
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

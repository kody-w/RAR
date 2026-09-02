---
name: "rar-cowork-cookbook-bulk-update-reconcile-bank-accounts"
description: "Applies a bulk field update across reconcile bank accounts records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reconcile_bank_accounts", "rar_sha256": "84070826e2756dc50fa52b198ea9f1d1766c50a683dd012abfd425c722ee1b1f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_reconcile_bank_accounts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-reconcile-bank-accounts:f03eeda94a7d3a150e84d8d4749dc6841e68ad9e6489086ac18694be0e2b967e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_reconcile_bank_accounts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_reconcile_bank_accounts_agent.py` is
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

Reconcile bank accounts Bulk Field Update — Applies a bulk field update across reconcile bank accounts records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reconcile-bank-accounts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reconcile_bank_accounts_agent.py` and embedded as the fenced Python below (sha256 84070826e2756dc5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reconcile_bank_accounts_agent.py` first:

```bash
python3 bulk_update_reconcile_bank_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reconcile_bank_accounts_agent.py   # or on stdin
python3 bulk_update_reconcile_bank_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile bank accounts Bulk Field Update — Applies a bulk field update across reconcile bank accounts records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reconcile-bank-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reconcile_bank_accounts',
    "version": '2.0.0',
    "display_name": 'Reconcile bank accounts Bulk Field Update',
    "description": 'Applies a bulk field update across reconcile bank accounts records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-reconcile-bank-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reconcile-bank-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '57a634f9d84a6185',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-cash/reconcile-bank-accounts'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-reconcile-bank-accounts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateReconcileBankAccounts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReconcileBankAccounts'
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
    print(BulkUpdateReconcileBankAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

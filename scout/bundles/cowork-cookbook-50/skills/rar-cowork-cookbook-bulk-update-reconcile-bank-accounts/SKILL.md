---
name: "rar-cowork-cookbook-bulk-update-reconcile-bank-accounts"
description: "Applies a bulk field update across reconcile bank accounts records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reconcile_bank_accounts", "rar_sha256": "84070826e2756dc50fa52b198ea9f1d1766c50a683dd012abfd425c722ee1b1f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_reconcile_bank_accounts`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_reconcile_bank_accounts_agent.py` and in the RCI capsule.

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

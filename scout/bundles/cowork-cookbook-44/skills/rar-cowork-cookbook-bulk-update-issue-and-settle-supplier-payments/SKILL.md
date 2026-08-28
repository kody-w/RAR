---
name: "rar-cowork-cookbook-bulk-update-issue-and-settle-supplier-payments"
description: "Applies a bulk field update across issue and settle supplier payments records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_issue_and_settle_supplier_payments", "rar_sha256": "5aca417d2774ce8b7e56715735679e2f28ef75677b96ae322eb91f806bca0a08", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_issue_and_settle_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_issue_and_settle_supplier_payments_agent.py` and in the RCI capsule.

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

Issue and settle supplier payments Bulk Field Update — Applies a bulk field update across issue and settle supplier payments records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-issue-and-settle-supplier-payments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_issue_and_settle_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 5aca417d2774ce8b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_issue_and_settle_supplier_payments_agent.py` first:

```bash
python3 bulk_update_issue_and_settle_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_issue_and_settle_supplier_payments_agent.py   # or on stdin
python3 bulk_update_issue_and_settle_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue and settle supplier payments Bulk Field Update — Applies a bulk field update across issue and settle supplier payments records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-issue-and-settle-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_issue_and_settle_supplier_payments',
    "version": '2.0.1',
    "display_name": 'Issue and settle supplier payments Bulk Field Update',
    "description": 'Applies a bulk field update across issue and settle supplier payments records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-issue-and-settle-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-issue-and-settle-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '13acd1556819aad6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/issue-and-settle-supplier-payments'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-issue-and-settle-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateIssueAndSettleSupplierPayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateIssueAndSettleSupplierPayments'
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
    print(BulkUpdateIssueAndSettleSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

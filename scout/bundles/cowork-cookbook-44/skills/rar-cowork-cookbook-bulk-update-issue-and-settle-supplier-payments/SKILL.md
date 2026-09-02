---
name: "rar-cowork-cookbook-bulk-update-issue-and-settle-supplier-payments"
description: "Applies a bulk field update across issue and settle supplier payments records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_issue_and_settle_supplier_payments", "rar_sha256": "3038f849c47d552a545f21a27e18a0955127250a5efd02f2cf372746eabff168", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_issue_and_settle_supplier_payments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-issue-and-settle-supplier-payments:5a89c299341cbd7f9a0ac9cf552e59d1cfb7964d4960c6b5615896703124007d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_issue_and_settle_supplier_payments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_issue_and_settle_supplier_payments_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_issue_and_settle_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 3038f849c47d552a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_issue_and_settle_supplier_payments_agent.py` first:

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
    "version": '2.0.0',
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

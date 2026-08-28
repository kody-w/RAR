---
name: "rar-cowork-cookbook-bulk-update-issue-and-settle-supplier-payments"
description: "Applies a bulk field update across issue and settle supplier payments records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_issue_and_settle_supplier_payments", "rar_sha256": "3038f849c47d552a545f21a27e18a0955127250a5efd02f2cf372746eabff168", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

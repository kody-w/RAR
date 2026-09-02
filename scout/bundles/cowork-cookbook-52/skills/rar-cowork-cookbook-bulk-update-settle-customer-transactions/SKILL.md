---
name: "rar-cowork-cookbook-bulk-update-settle-customer-transactions"
description: "Applies a bulk field update across settle customer transactions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_settle_customer_transactions", "rar_sha256": "aaaf243d5eea2c2ef3a14e68025f2042839e05a38d748fcbbc821162baf5e79a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_settle_customer_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-settle-customer-transactions:614f60541e9fdc84168c625a7ff72b2284f2b87c230c63a71ca003e3ab5b9a1a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_settle_customer_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_settle_customer_transactions_agent.py` is
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

Settle customer transactions Bulk Field Update — Applies a bulk field update across settle customer transactions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-settle-customer-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_settle_customer_transactions_agent.py` and embedded as the fenced Python below (sha256 aaaf243d5eea2c2e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_settle_customer_transactions_agent.py` first:

```bash
python3 bulk_update_settle_customer_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_settle_customer_transactions_agent.py   # or on stdin
python3 bulk_update_settle_customer_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Settle customer transactions Bulk Field Update — Applies a bulk field update across settle customer transactions records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-settle-customer-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_settle_customer_transactions',
    "version": '2.0.0',
    "display_name": 'Settle customer transactions Bulk Field Update',
    "description": 'Applies a bulk field update across settle customer transactions records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-settle-customer-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-settle-customer-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '89b45043e126cedf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/settle-customer-transactions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-settle-customer-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateSettleCustomerTransactions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateSettleCustomerTransactions'
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
    print(BulkUpdateSettleCustomerTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

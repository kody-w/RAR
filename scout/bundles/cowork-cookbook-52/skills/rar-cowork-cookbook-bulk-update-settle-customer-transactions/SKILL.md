---
name: "rar-cowork-cookbook-bulk-update-settle-customer-transactions"
description: "Applies a bulk field update across settle customer transactions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_settle_customer_transactions", "rar_sha256": "17c04459a98e7ecc930ad8a5791747cf630a5ccdfdb6eced5b7515a13102078d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_settle_customer_transactions`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_settle_customer_transactions_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_settle_customer_transactions_agent.py` and embedded as the fenced Python below (sha256 17c04459a98e7ecc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_settle_customer_transactions_agent.py` first:

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
    "version": '2.0.1',
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

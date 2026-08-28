---
name: "rar-cowork-cookbook-bulk-update-settle-customer-transactions"
description: "Applies a bulk field update across settle customer transactions records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_settle_customer_transactions", "rar_sha256": "aaaf243d5eea2c2ef3a14e68025f2042839e05a38d748fcbbc821162baf5e79a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

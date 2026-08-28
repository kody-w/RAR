---
name: "rar-cowork-cookbook-scheduled-brief-settle-customer-transactions"
description: "Schedulable morning-brief email summarizing settle customer transactions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_settle_customer_transactions", "rar_sha256": "0beda0fb47b40e9a2f349fe217d14ded71ab64c48fed4c669945855fc79bb9e1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_settle_customer_transactions`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_settle_customer_transactions_agent.py` and in the RCI capsule.

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

Settle customer transactions Scheduled Email Brief — Schedulable morning-brief email summarizing settle customer transactions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-settle-customer-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_settle_customer_transactions_agent.py` and embedded as the fenced Python below (sha256 0beda0fb47b40e9a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_settle_customer_transactions_agent.py` first:

```bash
python3 scheduled_brief_settle_customer_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_settle_customer_transactions_agent.py   # or on stdin
python3 scheduled_brief_settle_customer_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Settle customer transactions Scheduled Email Brief — Schedulable morning-brief email summarizing settle customer transactions for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-settle-customer-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_settle_customer_transactions',
    "version": '2.0.0',
    "display_name": 'Settle customer transactions Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing settle customer transactions for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-settle-customer-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-settle-customer-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c719fdd5924f8a15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/settle-customer-transactions'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-settle-customer-transactions', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefSettleCustomerTransactions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefSettleCustomerTransactions'
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
    print(ScheduledBriefSettleCustomerTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

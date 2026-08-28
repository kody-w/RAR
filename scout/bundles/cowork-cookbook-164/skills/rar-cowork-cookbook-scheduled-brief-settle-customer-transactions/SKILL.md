---
name: "rar-cowork-cookbook-scheduled-brief-settle-customer-transactions"
description: "Schedulable morning-brief email summarizing settle customer transactions for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_settle_customer_transactions", "rar_sha256": "df49f0fe921ff27c1ee373fad899f89353e97d645ed64217f4fe9a29ab3dfdde", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_settle_customer_transactions_agent.py` and embedded as the fenced Python below (sha256 df49f0fe921ff27c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_settle_customer_transactions_agent.py` first:

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
    "version": '2.0.1',
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

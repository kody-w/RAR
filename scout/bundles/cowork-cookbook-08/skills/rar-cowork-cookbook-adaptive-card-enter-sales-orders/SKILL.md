---
name: "rar-cowork-cookbook-adaptive-card-enter-sales-orders"
description: "Produces a reusable Adaptive Card JSON snapshot of enter sales orders status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_enter_sales_orders", "rar_sha256": "00712e5246f026be096ea18cb83d261baec36943f9177d7124b807dc32032adf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_enter_sales_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-enter-sales-orders:38ed7a4b6e26a440677717138e83b4d9b70203c0fed5d0e4ffdb01ffd04800d6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_enter_sales_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_enter_sales_orders_agent.py` is
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

Enter sales orders Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of enter sales orders status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-enter-sales-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_enter_sales_orders_agent.py` and embedded as the fenced Python below (sha256 00712e5246f026be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_enter_sales_orders_agent.py` first:

```bash
python3 adaptive_card_enter_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_enter_sales_orders_agent.py   # or on stdin
python3 adaptive_card_enter_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enter sales orders Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of enter sales orders status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-enter-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_enter_sales_orders',
    "version": '2.0.0',
    "display_name": 'Enter sales orders Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of enter sales orders status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-enter-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-enter-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '19fd886bc8152542',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/enter-sales-orders'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-enter-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardEnterSalesOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardEnterSalesOrders'
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
    print(AdaptiveCardEnterSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

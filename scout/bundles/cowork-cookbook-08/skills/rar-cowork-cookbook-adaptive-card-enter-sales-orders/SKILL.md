---
name: "rar-cowork-cookbook-adaptive-card-enter-sales-orders"
description: "Produces a reusable Adaptive Card JSON snapshot of enter sales orders status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_enter_sales_orders", "rar_sha256": "00712e5246f026be096ea18cb83d261baec36943f9177d7124b807dc32032adf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_enter_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_enter_sales_orders_agent.py` and in the RCI capsule.

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

---
name: "rar-cowork-cookbook-adaptive-card-enter-sales-orders"
description: "Produces a reusable Adaptive Card JSON snapshot of enter sales orders status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_enter_sales_orders", "rar_sha256": "2b68c2ed5d731a0eeb9cbc0f2916ffc1da858ff2210fc82a968d45e64ddda480", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_enter_sales_orders_agent.py` and embedded as the fenced Python below (sha256 2b68c2ed5d731a0e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_enter_sales_orders_agent.py` first:

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
    "version": '2.0.1',
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

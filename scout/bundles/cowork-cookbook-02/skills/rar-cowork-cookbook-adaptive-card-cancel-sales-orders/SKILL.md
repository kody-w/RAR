---
name: "rar-cowork-cookbook-adaptive-card-cancel-sales-orders"
description: "Produces a reusable Adaptive Card JSON snapshot of cancel sales orders status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_cancel_sales_orders", "rar_sha256": "6feae232449c09bfc55913ce116f2e7c2b900ba25a91827e6bb6fc93f29fc8bc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_cancel_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_cancel_sales_orders_agent.py` and in the RCI capsule.

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

Cancel sales orders Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of cancel sales orders status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-cancel-sales-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_cancel_sales_orders_agent.py` and embedded as the fenced Python below (sha256 6feae232449c09bf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_cancel_sales_orders_agent.py` first:

```bash
python3 adaptive_card_cancel_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_cancel_sales_orders_agent.py   # or on stdin
python3 adaptive_card_cancel_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cancel sales orders Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of cancel sales orders status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-cancel-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_cancel_sales_orders',
    "version": '2.0.1',
    "display_name": 'Cancel sales orders Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of cancel sales orders status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-cancel-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-cancel-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1f24273d174a6ddd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/cancel-sales-orders'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/adaptive-card-cancel-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardCancelSalesOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCancelSalesOrders'
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
    print(AdaptiveCardCancelSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

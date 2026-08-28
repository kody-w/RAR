---
name: "rar-cowork-cookbook-adaptive-card-cross-dock-received-goods-to-outbound-orders"
description: "Produces a reusable Adaptive Card JSON snapshot of cross dock received goods to outbound orders status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_cross_dock_received_goods_to_outbound_orders", "rar_sha256": "2df8a7d7bf4260dddb566a6e8ce2755b9b16aeedc7307d29cbec1482bf75e319", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_cross_dock_received_goods_to_outbound_orders`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py` and in the RCI capsule.

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

Cross dock received goods to outbound orders Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of cross dock received goods to outbound orders status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-cross-dock-received-goods-to-outbound-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py` and embedded as the fenced Python below (sha256 2df8a7d7bf4260dd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py` first:

```bash
python3 adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py   # or on stdin
python3 adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock received goods to outbound orders Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of cross dock received goods to outbound orders status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-cross-dock-received-goods-to-outbound-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_cross_dock_received_goods_to_outbound_orders',
    "version": '2.0.1',
    "display_name": 'Cross dock received goods to outbound orders Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of cross dock received goods to outbound orders status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-cross-dock-received-goods-to-outbound-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-cross-dock-received-goods-to-outbound-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c7ed5fc7a32e624',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/cross-dock-received-goods-to-outbound-orders'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/adaptive-card-cross-dock-received-goods-to-outbound-orders', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardCrossDockReceivedGoodsToOutboundOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCrossDockReceivedGoodsToOutboundOrders'
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
    print(AdaptiveCardCrossDockReceivedGoodsToOutboundOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

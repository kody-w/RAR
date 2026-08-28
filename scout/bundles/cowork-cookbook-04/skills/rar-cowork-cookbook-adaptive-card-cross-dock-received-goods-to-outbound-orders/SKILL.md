---
name: "rar-cowork-cookbook-adaptive-card-cross-dock-received-goods-to-outbound-orders"
description: "Produces a reusable Adaptive Card JSON snapshot of cross dock received goods to outbound orders status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_cross_dock_received_goods_to_outbound_orders", "rar_sha256": "9134621f175ff36de5e4339f5c70540b40244d3a276317910803d3e369ff1e9f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py` and embedded as the fenced Python below (sha256 9134621f175ff36d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py` first:

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
    "version": '2.0.0',
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

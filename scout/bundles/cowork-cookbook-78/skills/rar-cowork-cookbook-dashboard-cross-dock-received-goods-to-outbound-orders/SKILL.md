---
name: "rar-cowork-cookbook-dashboard-cross-dock-received-goods-to-outbound-orders"
description: "Produces a self-contained interactive HTML dashboard for cross dock received goods to outbound orders - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_cross_dock_received_goods_to_outbound_orders", "rar_sha256": "871da6ba4ece8ad86fd8dfe348384cd089736bf2c0d918eb3e1247ef61428535", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_cross_dock_received_goods_to_outbound_orders`. The original RAPP
agent is preserved byte-for-byte in `dashboard_cross_dock_received_goods_to_outbound_orders_agent.py` and in the RCI capsule.

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

Cross dock received goods to outbound orders Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for cross dock received goods to outbound orders - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-cross-dock-received-goods-to-outbound-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_cross_dock_received_goods_to_outbound_orders_agent.py` and embedded as the fenced Python below (sha256 871da6ba4ece8ad8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_cross_dock_received_goods_to_outbound_orders_agent.py` first:

```bash
python3 dashboard_cross_dock_received_goods_to_outbound_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_cross_dock_received_goods_to_outbound_orders_agent.py   # or on stdin
python3 dashboard_cross_dock_received_goods_to_outbound_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock received goods to outbound orders Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for cross dock received goods to outbound orders - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-cross-dock-received-goods-to-outbound-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_cross_dock_received_goods_to_outbound_orders',
    "version": '2.0.1',
    "display_name": 'Cross dock received goods to outbound orders Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for cross dock received goods to outbound orders - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-cross-dock-received-goods-to-outbound-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-cross-dock-received-goods-to-outbound-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0069e88b3325b0af',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/cross-dock-received-goods-to-outbound-orders'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-cross-dock-received-goods-to-outbound-orders', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardCrossDockReceivedGoodsToOutboundOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCrossDockReceivedGoodsToOutboundOrders'
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
    print(DashboardCrossDockReceivedGoodsToOutboundOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

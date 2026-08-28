---
name: "rar-cowork-cookbook-dashboard-cross-dock-received-goods-to-outbound-orders"
description: "Produces a self-contained interactive HTML dashboard for cross dock received goods to outbound orders - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_cross_dock_received_goods_to_outbound_orders", "rar_sha256": "8dc9bac228f9389881c601b653a323ab341311184fb6acbda3b5361829ed2c76", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_cross_dock_received_goods_to_outbound_orders_agent.py` and embedded as the fenced Python below (sha256 8dc9bac228f93898…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_cross_dock_received_goods_to_outbound_orders_agent.py` first:

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
    "version": '2.0.0',
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

---
name: "rar-cowork-cookbook-dashboard-cross-dock-received-goods-to-outbound-orders"
description: "Produces a self-contained interactive HTML dashboard for cross dock received goods to outbound orders - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_cross_dock_received_goods_to_outbound_orders", "rar_sha256": "8dc9bac228f9389881c601b653a323ab341311184fb6acbda3b5361829ed2c76", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_cross_dock_received_goods_to_outbound_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-cross-dock-received-goods-to-outbound-orders:1e337a891d981ca76aaec8d44607f486902b2c7e9c6e0d198865eee301c47a35", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_cross_dock_received_goods_to_outbound_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_cross_dock_received_goods_to_outbound_orders_agent.py` is
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

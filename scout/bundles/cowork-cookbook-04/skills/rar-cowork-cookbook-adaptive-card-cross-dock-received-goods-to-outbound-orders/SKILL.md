---
name: "rar-cowork-cookbook-adaptive-card-cross-dock-received-goods-to-outbound-orders"
description: "Generates a read-only Adaptive Card JSON file showing cross-dock received-goods-to-outbound-order status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons; call when you need that card."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_cross_dock_received_goods_to_outbound_orders", "rar_sha256": "d500841466147da58382ad4fc0073fe8f5730cbf89a9f2c7139e4cbb65fdea1b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

Cross dock received goods to outbound orders Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing cross-dock received-goods-to-outbound-order status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons; call when you need that card.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "action_button_count": {
      "description": "How many action buttons to include (2-3).",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "kpi_tile_count": {
      "description": "How many KPI tiles to include (3-5), each with current value and trend arrow.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "output_filename": {
      "description": "Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-cross-dock-received-goods-to-outbound-orders-2026-05-24-card.json.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py` and embedded as the fenced Python below (sha256 d500841466147da5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py` first:

```bash
python3 adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py   # or on stdin
python3 adaptive_card_cross_dock_received_goods_to_outbound_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock received goods to outbound orders Status Adaptive Card — Generates a read-only Adaptive Card JSON file showing cross-dock received-goods-to-outbound-order status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons; call when you need that card.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "version": '3.0.2',
    "display_name": 'Cross dock received goods to outbound orders Status Adaptive Card',
    "description": 'Generates a read-only Adaptive Card JSON file showing cross-dock received-goods-to-outbound-order status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons; call when you need that card.',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b22f667e1274c106',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'action_button_count': 'How many action buttons to include (2-3).', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'kpi_tile_count': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-cross-dock-received-goods-to-outbound-orders-2026-05-24-card.json.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives any consuming app (Teams, Outlook, custom dashboard) a single canonical cross dock received goods to outbound orders status card so different surfaces always show the same numbers.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, produce an Adaptive Card JSON file 'adaptive-card-cross-dock-received-goods-to-outbound-orders-2026-05-24-card.json' that visualizes the current state of cross dock received goods to outbound orders. Include: header with title and timestamp, 3-5 KPI tiles with current value + trend arrow, a RAG indicator row, and 2-3 action buttons. The card should render correctly in Teams, Outlook Adaptive Card preview, and the Adaptive Cards designer. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Generates an Adaptive Card JSON file with current cross dock received goods to outbound orders KPIs and RAG indicators.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a read-only Adaptive Card JSON file showing cross-dock received-goods-to-outbound-order status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons; call when you need that card.', 'example_request': 'Make me an Adaptive Card showing cross-dock received goods to outbound order status for USMF.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-cross-dock-received-goods-to-outbound-orders-2026-05-24-card.json.', 'name': 'output_filename'}, {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'name': 'kpi_tile_count'}, {'description': 'How many action buttons to include (2-3).', 'name': 'action_button_count'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a caller wants a shareable Adaptive Card snapshot of cross-dock received goods to outbound order status for Teams, Outlook, or a dashboard.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class AdaptiveCardCrossDockReceivedGoodsToOutboundOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardCrossDockReceivedGoodsToOutboundOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'action_button_count': {'description': 'How many action buttons to include (2-3).', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'kpi_tile_count': {'description': 'How many KPI tiles to include (3-5), each with current value and trend arrow.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Adaptive Card JSON file to produce, e.g. adaptive-card-cross-dock-received-goods-to-outbound-orders-2026-05-24-card.json.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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

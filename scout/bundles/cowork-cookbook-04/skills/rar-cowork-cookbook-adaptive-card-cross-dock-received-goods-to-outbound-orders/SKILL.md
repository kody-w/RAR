---
name: "rar-cowork-cookbook-adaptive-card-cross-dock-received-goods-to-outbound-orders"
description: "Generates a read-only Adaptive Card JSON file showing cross-dock received-goods-to-outbound-order status from Dynamics 365 F&SCM, with KPI tiles, RAG row, and action buttons; call when you need that card."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_cross_dock_received_goods_to_outbound_orders", "rar_sha256": "d500841466147da58382ad4fc0073fe8f5730cbf89a9f2c7139e4cbb65fdea1b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

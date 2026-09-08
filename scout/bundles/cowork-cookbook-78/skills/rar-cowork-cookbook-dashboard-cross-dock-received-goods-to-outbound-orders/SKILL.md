---
name: "rar-cowork-cookbook-dashboard-cross-dock-received-goods-to-outbound-orders"
description: "Pulls cross-dock received-goods-to-outbound-orders data from Dynamics 365 F&SCM for a legal entity and fiscal period, and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the outp"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_cross_dock_received_goods_to_outbound_orders", "rar_sha256": "7eb6c888f7364f99469a3bdd785f49aafec8b5cd0195ae4854949dffd57433f9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

Cross dock received goods to outbound orders Interactive HTML Dashboard — Pulls cross-dock received-goods-to-outbound-orders data from Dynamics 365 F&SCM for a legal entity and fiscal period, and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the outp

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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "fiscal_period": {
      "description": "Fiscal period to report on; defaults to the most recent available.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-cross-dock-received-goods-to-outbound-orders-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_cross_dock_received_goods_to_outbound_orders_agent.py` and embedded as the fenced Python below (sha256 7eb6c888f7364f99…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_cross_dock_received_goods_to_outbound_orders_agent.py` first:

```bash
python3 dashboard_cross_dock_received_goods_to_outbound_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_cross_dock_received_goods_to_outbound_orders_agent.py   # or on stdin
python3 dashboard_cross_dock_received_goods_to_outbound_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Cross dock received goods to outbound orders Interactive HTML Dashboard — Pulls cross-dock received-goods-to-outbound-orders data from Dynamics 365 F&SCM for a legal entity and fiscal period, and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the outp

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
    "version": '3.0.3',
    "display_name": 'Cross dock received goods to outbound orders Interactive HTML Dashboard',
    "description": 'Pulls cross-dock received-goods-to-outbound-orders data from Dynamics 365 F&SCM for a legal entity and fiscal period, and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the outp',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f5d1d26160f240dd',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-cross-dock-received-goods-to-outbound-orders-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of cross dock received goods to outbound orders with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull cross dock received goods to outbound orders data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-cross-dock-received-goods-to-outbound-orders-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing cross dock received goods to outbound orders.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls cross-dock received-goods-to-outbound-orders data from Dynamics 365 F&SCM for a legal entity and fiscal period, and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the outp', 'example_request': 'Build me a cross-dock received goods to outbound orders HTML dashboard for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-cross-dock-received-goods-to-outbound-orders-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable cross-dock receipts-to-outbound-orders dashboard from D365 without giving the viewer D365 access. Read-only.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardCrossDockReceivedGoodsToOutboundOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCrossDockReceivedGoodsToOutboundOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-cross-dock-received-goods-to-outbound-orders-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardCrossDockReceivedGoodsToOutboundOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

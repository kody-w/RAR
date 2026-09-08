---
name: "rar-cowork-cookbook-dashboard-cross-dock-received-goods-to-outbound-orders"
description: "Pulls cross-dock received-goods-to-outbound-orders data from Dynamics 365 F&SCM for a legal entity and fiscal period, and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the outp"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_cross_dock_received_goods_to_outbound_orders", "rar_sha256": "7eb6c888f7364f99469a3bdd785f49aafec8b5cd0195ae4854949dffd57433f9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

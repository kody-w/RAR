---
name: "rar-cowork-cookbook-dashboard-enter-sales-orders"
description: "Pulls sales order data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_enter_sales_orders", "rar_sha256": "d712b589386277b0174d682bddd3a025b54f706c35ef1852e21690a440551c4f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_enter_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `dashboard_enter_sales_orders_agent.py` and in the RCI capsule.

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

Enter sales orders Interactive HTML Dashboard — Pulls sales order data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-enter-sales-orders
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
      "description": "Fiscal period to report on; defaults to the most recent period available.",
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
      "description": "Name of the generated HTML file, e.g. dashboard-enter-sales-orders-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_enter_sales_orders_agent.py` and embedded as the fenced Python below (sha256 d712b589386277b0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_enter_sales_orders_agent.py` first:

```bash
python3 dashboard_enter_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_enter_sales_orders_agent.py   # or on stdin
python3 dashboard_enter_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Enter sales orders Interactive HTML Dashboard — Pulls sales order data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-enter-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_enter_sales_orders',
    "version": '3.0.3',
    "display_name": 'Enter sales orders Interactive HTML Dashboard',
    "description": 'Pulls sales order data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to the output',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-enter-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-enter-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b9075d5013282704',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/enter-sales-orders'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-enter-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent period available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-enter-sales-orders-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of enter sales orders with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull enter sales orders data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-enter-sales-orders-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing enter sales orders.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls sales order data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to the output', 'example_request': 'Build an interactive HTML dashboard of sales orders for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent period available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-enter-sales-orders-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of sales order entry data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardEnterSalesOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardEnterSalesOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-enter-sales-orders-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardEnterSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

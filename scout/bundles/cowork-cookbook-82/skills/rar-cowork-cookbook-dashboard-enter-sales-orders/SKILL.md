---
name: "rar-cowork-cookbook-dashboard-enter-sales-orders"
description: "Pulls sales order data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_enter_sales_orders", "rar_sha256": "d712b589386277b0174d682bddd3a025b54f706c35ef1852e21690a440551c4f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

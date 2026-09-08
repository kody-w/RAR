---
name: "rar-cowork-cookbook-dashboard-process-customer-refunds"
description: "Pulls customer refund data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) t"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_process_customer_refunds", "rar_sha256": "5adf32de84e7f85d03da60908f174e56e960724c17e9ce470d4c09abbfba72db", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_process_customer_refunds`. The original RAPP
agent is preserved byte-for-byte in `dashboard_process_customer_refunds_agent.py` and in the RCI capsule.

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

Process customer refunds Interactive HTML Dashboard — Pulls customer refund data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) t

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-process-customer-refunds
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
      "description": "Name of the HTML file to produce, e.g. dashboard-process-customer-refunds-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_process_customer_refunds_agent.py` and embedded as the fenced Python below (sha256 5adf32de84e7f85d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_process_customer_refunds_agent.py` first:

```bash
python3 dashboard_process_customer_refunds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_process_customer_refunds_agent.py   # or on stdin
python3 dashboard_process_customer_refunds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer refunds Interactive HTML Dashboard — Pulls customer refund data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) t

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-process-customer-refunds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_process_customer_refunds',
    "version": '3.0.3',
    "display_name": 'Process customer refunds Interactive HTML Dashboard',
    "description": 'Pulls customer refund data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) t',
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
        "upstream_slug": 'dashboard-process-customer-refunds',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-process-customer-refunds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '702ee3fe66fbd3b5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-refunds'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/dashboard-process-customer-refunds', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-process-customer-refunds-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of process customer refunds with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull process customer refunds data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-process-customer-refunds-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing process customer refunds.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls customer refund data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator) t', 'example_request': 'Build me an interactive HTML refunds dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-process-customer-refunds-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of customer refunds from D365 for viewers who lack D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardProcessCustomerRefunds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardProcessCustomerRefunds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-process-customer-refunds-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardProcessCustomerRefunds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abObWLblX1HfF9GZ+bCvmCW5oiIagRiEBAgQCKUrnMzzIEZBdv33PkiycyjXq1cd/alvpn0lOGfPe619DL++2V0blfXbpzfNt4sFZ2dZHPn1wi68BV0OZZ2CX2XqgD8LtyzaOna6tqybtw9vnt+4dVy1cVmA7UqXZc3C7Zq2zMH+2g86IMKzW3sR1GW+YMbCzmO3WWAksWD/p0YfF0EJ9CwyP7SzhV+0cTs+1OZl04L9Lri0COLGBXcrv45L78OijfxiMdRx6zdgZ9OC5XZWFv4iLlq/tt027v0Frx8PQHETOaVde4sf27K1gWmRb3t+/QEszWKwQzO4hRvZddt8WDRl3dpO5i8ef39YqBQHlnmxawNXf1q0wFn/budV5jdvn37+24e3GHx++/Trm5vZDbj0xnzVptSl6zcN/QqD+ojCHKzMLkKwsBpBtAvwHXgE3M/BJc8PFq9vPzZ+FnxY/Od/poNdh81Pnz4Xi9fP57f5P7Ur5hgs2tJuWt9buHZlO3EGIve+oLLBHhsQuLari2d46rgI3587f5NUVou/zvd+fCp5D/32x89vJTDBnlP5+e2nBcjL57e6mz+/z1KqH396z8rBr3/86Tc5TeckvtvOwoDV719e319iwcLflsbB4oum7OiXLpDbuPKB8N/5N/88TX+Je4Xky3Pxj2X1YfF9ybM/fwX2PsvRAXK/LxbEAOx8e0/KuPjxpaMue7+wC9f/8ad/JtaNfDfN4qb9b8n9+Sn4WWs/vkLy04dH+v62gF6+fZP5z9VWoGD+HU/A8q/qvgXqn8l+ZPZPoueeaL7l8rvivrcB+uvi53/q23+14cMi+PzG+Blo2Hpuuk+LXx8l8vMP3m8Xf/jb34HofylGK7vafUj4kttFHPhN++XLzz80j8s//O3nH7oKVLFv51+6OvuezO/F9aHnDxF8rfrxj3uB/nORFuVQLL710OLXsvof9d/fF4adxd5v15tPi9934vwDLWYnvip9huB33dgAW38Xx5/e/g7ApwDedO7jNsCP//iPxTF267Ipg3ahuWUHwLMDaJr7s/F6FDcL8P+MGrUP4trEM9A914H6nzM8W1wGi1/+l/sA/I/uC/CX30B07pQZ1758xfcvT3xvfnlf6EByWcdhXACgVilF+VzY4YzdQGtV+41f9wCpnLH1P4KG/jh/AOC6+OVfC//ykPNejb88eCF+Yp9KCzPuNV3mv88emjMnPP1xAYP5d9/tgIqsnIkjiAFmfwCeN2UGqKGdo9GkcZYtvBggC4D3J+eAiH2ahf3yyy8OsOtz8QRqbPGkuGYJFnwzZ/HxI3AsyOIwaj8XvhuVix9+/fsPi/+9+K92PYTPOhTAGa98AAv3miwtQH91OVgGUgWSC8DjkY9f//4KLxBTAE4F2YuD2H9uBvWZ+t7XWGs89RElyIXjgxiD+OYVoDSA/ou4fV8IweKbvUDpfGvmh2jmWc+v/MLzC3cEUm3gzrdIFmW7aEARNsH4YdE1/kPrL05tP0zMQaPb7S+LI60ANioz8Nds5mMR2FwWgDyzb5XwvA6E1D80i+1XEe8Laa7IRWXXdhXV9ktHYD/zMk8Hr+1AuL0o/OFzMTOvP4fq0R7P8IBFIDLuK6Uf55yDWSUHWOA1X3U/1tgzZ+oP7qw/F82r9O16ToULqAAoDbvYmwnhL6+SaqKyy7xH/ICls6RXFrxXVh41+KL9P48/zUL481zybVJYfO5QGMEX/z/PTXNoKI5Tdxyl75jFTtJV65myeZSc7XxOn7MHs1OP9vxtpvmKW1/h+zOwANRfPf7lufKR6NeaJyR2NciLSqkP+aDKQEBnuY8mmIu6ruf2sT8XX3niAwjHAxRBHQDEAB01F/JXhfPdr5ZGIDDz999mhkfRgECBYIJCX1Sdk4EiDHzfc2w3BVbVcyO/0lzM0QZNPUSxG/3BqzmFoPCA/AUwIgatCbjk/Rt2P+9+Nf0PG5+j0bzlMTaCuvHrhwBghz8bOFfFELcAzuz2ObkDPz89hAA38qqdfXdAJ+UfXhf92r91cTMXyodXXP0KYPbH+ffT0/mqf69A84BggRapOhDdR1PNeJODYgE2AFwBhZXHBRgEQFBeQXgItPMZIQACvybVp8TH5ZdD/qMTZwb7unF2ZN7zKLZHW9jF+Hsg0b9XJkBePq946P1zpX3TNsuewRRUOujAb3ef08P7cwB4ThiLr3I//cPR6Md/7/T0oPTzHwvg0yJq26r5tFw+afgrC78DKFs+bW1+Y+SPL9L8+BU5Pr4g5w+Sn05/Wvx71v1BxKs7Pi2Qd/gdnm8dXtX1+gHBoD9urY/4fPdzofq/QS1QX+agvObUjWAE+MaLX5cAcgxrgGNg8ZMnm5leB4BWD2IAefhc/L7c53YD4FOE/gN9fgcDjwEBlP4zbd/4C9wqWqDbm0fK0H+fT2Kz+Y3/9qkAyPvhDaCr/986wc0slc9V3cwnPxB+AK5t7D++PUDi3s4f/3gqlh8f7Ox9wfgAkLLm95X34paZW3/XIE83gXsu0PBhZgLQ96AogZuz8rm57AZUKyjU2Z12rGb7n4e9eTx8Qv+XJ/T/o0Xs75nhwdqPgQBgz19A0wZ2l4EotuXDlN8zit0D8+f++67SBxl9eZLRP+pkZu76A18BBbcOdPmHhf8evi/O2pH9rtxvg/A/CjXB/DHL8cpPMxV/eEEa+A0OLx8W384hIISvk+GswS86cOj+eT4DzTl9bJk/gD3g17dN3/55w/Hf/vY9ux6492UuvWcB/dk6acYzgPdzGB/E+qhSYC5Q6XWu/3L8X/fzRxRGyY8w8RHF36M2z74fppc5ZQYo4Ds5f1yf+6r2/2TRPA/bYEB/2cOU7nMQXT4BYvmUvPyOVqD2QRaAcueA/pap3+JVPg6Qs4Egvu3z3zt+fQNNZM/zzauNXicQsBxg68dmnrqWAGuAQvD9iQrg3v/F2eQloYlsMBkDEYTtBRjq+WvcXwVrwoMxzybhDbwOkBXuE6S/IeEVirvIyt+4Pr6CPdyFN7bjBI69Qj0HyHuiy5d5uIxnq2aTQDA+AoDyf7sNLnkvd57mz7H6dhSa3X559eubQ+JgJY83AvX8oZcbxFmiK2c8XKALvL5ng9lVrB3DN221veq5FR1X2klqmtL2MPMQ0eGdTWKtE08Epkm1Kp0mWAhuu+B6WBW6whSk0Ow3PdxGLY7cBcKFnCMU5N4RVXj3dC3M8DyOsHq6Hgpbi1H4sjX2uZBimkYiPKSrraoug36Jmhh/uxJdti7O5bLnsB7vJqFcYdeyOE0YeofzstYLf9/jKK0zEwHF/Z2s173ekmLmHWh2xbrQijtp6iqTITaZsmsm+xbv06p5Vp3Q0SqkOor7kXHHne6SY25yuZHL+IVsdnEeHwopuntDaaxSBUkcjSFN3+JC13IdliE3bKOwSJEiu6rQuwN6rCBlrbvBai1ZNnv2mUIrN6wShetgiZFL+VIT0CYoyttltSGDJRSLm3tTUaWRDbYRENsuiy9L+1yTe4EKl5urp+rH5cBcxoPQIOMhwFpBIE209VcV6oRiI5JeGHLsjvXtbU5Hl2O+wqXLZGoJtjV6N2JM+XZomdUV2t2QNEvXYZwDYoPDTMicLWs6xS27yVh1XTsxdYYq4uZpsK4MaToa2VbbMil1hA5XdWCt2Mg6RWPEJbWjU3tDn7Nr7erSPizROkBPZK/JNtUMO/mCe1cZD9fsCq0Qwlge3Ly0jRLRte027/fhwRQSQ9kOnWbSktMJxTi5jOLe4Ta+D07BHKX1YSO5mxqGGyhZuScoY2vosjtdTTfYjZmcw5DRafWGiJfqKUjvWbqThFuT6FS639TLoUkIEUGPe2oQdsLeulfceFb50F/7o5M7JHtX8NVWvmjnq6Dcbh4qbnfHFWVZqT4eIFu/O2zfUQU07egBNcIb1x5trjMsxsxCZ0gzdHXLrBiumVhEQqQXETInM3p7F0cWEmkFv2lkNro3kMt6uT1cNOxe3CNPY9ZqvWaDVuDD2Nxj9D6VaGRVOdRoYysXUSLfUXbQBJmDuT7q1FQcmfYKX9VauhJWoCOUZtpqGleJPUhU7jDukq2WvFlxlGdpBLSaiJGHeKnd2PaKWQt4rpN4E1T8cju69Oqy61ZZOhmh7ZisdOU5LxeJHZKH5aQr1+58mhCol0zB2HbHRN3TBHlaQaHkWZl8WtpSifrqJdZWoslzlD2lK0fQGwwtxf1eKETVul40i8xO69PQW5bJn/Uk9H3D6QgCr3Kc96i8oCdr2I1ud6Hhgrzq19zneL3R13cyMrpDu952SW7mVZ6VXpGZvEHWTAOVlhntzXSnZ/RZJyp+8NUstaGp6y+yMK1Tg9Wi8oqiBjSpeYodhLsr1W1FZLisLzHknuWXgdjywkGTx41+PAccfj4dM/jM3W/b8w25k9dcyIJTVUNWE03bIzkR5wtOpxtcQfqrmmyHY9/bm3izVxEbvzSnPvYQObtbSb1lOuNKqlh7m8QUX9bFIJ5a0tdUAhtCGR0P2xQTqC0Kt0d4nSMrDQGI493OqqxR+5Qp6i7YyaiS9aSpnqwtpjewBAnNeIs6X2Smy9Xnjjy2DqGBYuJIT0wchTfb9CjpIHd4RZvoVkNkQcCaWm6FUDXz8zIKXOqiBdHJyZsmjlNJDEVONuqsxq6nDX8cnHY6m+fdWVV4qKenvMKI4n6JTvbJMVxvFQI39G3S8XBC32GdUoC7gaTZxrqnhw5J9N7fMn1xIdaI5RWxh7NcwokDhkw7ESTkGBeJEm5WeMa1Qk221M46yWW2OWEH2ErObhkPProaXSpvLHpX7KEDmwziIWY5ruQYut8uyYFOd1Z6Yu7CIEksFeUbx5GgjUct3UarBGi3t9WJoSeTC7RId3e2LubwejexWm2bGzsX3FNJJeN53cT7iMYbtNwK1qrvzpto2jWOVgtUeXD4VWKLaRZ0q7Fk3S3BRSyFwop5L30cM+LRqOWzXJqbVpCmtjJdtuHsPku2jLKSGmw/LoOLM6aWKGW3equo+4tSwiXs9lCitSqawKLCGqKYXy8Jdl2P6mFcRREK40N6RbbrQLk643iuoGVg3DiduAb5pR1TYry1yfE4LXNntxOuBNVCOor7lgELcX5Tb63Bbk/3smPXyqDzZ1bKijuJ52WLaayBNyMyJsd0jdf37aE0l2qiNXTr6ZHcVJHZ6bSeAOQwWCbO9+5WtIi8FjWTUbmdRFyLtcDuL5QtAp4QQxq+qKKs22RVnTAZinEasUrzalyIso76vSytlHadEXtMuuxNwr9VBbosjWsXROuTtDum4a0bblQ9WGlcH3OaL7hse4auIuYXDjk2cZjJh2x1pahQF7TIDjfV/nA6wgxz5LslLK9zPMK13YVHXGw83sP9OWoskUrJli+G4TAJfh0gxiWqa2cVhxSTHCirQ00DUrO+pbKQ7vDMTBtssIejeIyXG7fkT3eYOkdTtXfYMuIHsdxvbfY4pYh4Py6lewNtu14YnduQHAv3NOYkdVXvEGOENVYm1oHYhxZUbPvIHI1tzQ6H5uKrLKc1dxFljjo70Td+y7PZPkb3h9X1to+Y3WrQaCQS+UMqBK2brbMDKZ85cu8avlE7YA7id5RyL2BEgFV6ZaHbuzdabYR4nRDdKmOK6YmQzEHbM4WTUFYoxy5B3OypOtHArrjMYVGmIx+UWrHhTqEyWFrs0y1dtlafKYS4ihSI3dcIUx1HLQaNSfdlui6N9WE6Cw29xDfH6nyvglFExx2RnmWJPChoImikdDqwVL+8Bll0vJfKKOhqkYi6xGAOasWHanfKeHi6nkVvIzvcqbeOaxlBHasuws6hYfEkon1cDiglZpC06aU0E2jNw3h03ena0ZW9u3EsO1Nd36L9WZdhJN3deEyQw7PaGGhXWvsyXxe78lQxFreR83ja60e4chAhFYyQudy2En1uWmW779ZyTnW3QbChbV/WJ+IiwdhWjcpTbu9xxO3NdY0SW0o07VgPjtEFF5lBoqNrzEbNTu91SyVHs1BlJYOu6bA7Sc6eDDJOAWNQAMjHZffSbY1eiSYzrDVlCyxNa0NdpTedKKHx6Jz4hMwQ3aWwcNnkK2Ud6Jlxco7FybFtj3OoOwRv+x7u09vJarP1sbjwgrEz8QI60eb5equzezWSgdwT+EAHWn1AS+28lSa9Ltcn+roXU52ludbdXMRjV7npzEaYVPoWsls5kIXXJrNB73a2TY6IzBhbPXQFSrSj236f3yg0bKidq4sFfefXIcXhx+nqadt1LdeJrNPBvhGR5GgcaAy/ZYV2voHpdSvQSXrzz/U0hJo7+vn92I0kuzTbQUX2WZMNCIqqnCHlsHk7wxq/9XMqqeoMuy/di2PA9unAcQq720VRbC9LPGR6Usi6S50PYboTJADx4ilz9Xug39dLv5+QjcSCI4e3dJmAkHK8vXFCGhAWFZAiqbu9nBfMZTpAZmlg95TP8Wx/P6xGk82b2s13di3lgWQQF6RV15delnoxgCtLoa1uOFz36Y3dBiQ98a5NIYR2OOQyQaH7fYKdRXlXCsxSLEUmD9cFT2jMBAjpgEjnvTfmUhFpawVVokxJguPUrwJMG0DTaPTSzc+FvVKTgjn1y+ORT9MjTdxYOLhuCoTbxapWe2d7vRyQFg2cJKXNZLg14T6U7ZaHb/aYMpMdcgkh6Kd2TC6Wc0ucFLfd1bhhUvmMbHYwyiFydUNOcLvrIjfhh3NZ29XVNBooG1P/ZNctk7bNAPiqz0/ypg29ayvfuXjfaacMHOlUjEw2RRRz0LZWde3M3jJfo1c75N5qVHaD7evNEaUCnsJDuDtyJHPyOWsakdjww8pwq6gjTQ6j4KJGsEBNWoeqWurkEoq9dzR/pdtu4HteYxjiJlAcPggqXahgsqtGgltS20Pf3AW6Qm+bJDaxYJfU8kSJwd5QFVz0cGsMz25zoDUEOrJL1wnArMWxwZ4KFfkkQNN0u/A0UZodevIyPy8DSneOdMrkp72+t0/JOV/LlwvlRuoVIagI8ulBjEb86qLcRceLRMa3hmCLmLnEw766YFuRjdbqOMaORVrymHiaWJSGomVIoN5zBApIUDvdKSJOKjucTyibjVPId4ezQBhmrurO2jZu6wqj7hJs3JFY8JdQiN+ji4Ab47CJy0kjhRqhYt3xzGteCvhmr8nwxapMQ9NE2kDgTQcaIiYaMZEMJw2ODOzS16DqrVPe+UmTLqf8VBljl1gJifTd6It6Wg7dzi8CSMepm3JubJFX+aBcDvtO8h1ShKT+gof6qlqeUu9SiD06ehR9c9YR1+b3GM4prkXCydPjVMgV1s+3ZtHtdSzxzFN35dZwrPEHteE7qurOuipgWLVh7WGbxav11V8j9ZJDGAqcnC4oi09lnenD9sY30/XWdOfdHp0uagfftDOi7Pz9KYJ5+E6WU7NsUq/bI65NnF27dKKlVZRMIovbUI40/Vbb2H7DxUqZlJ6QuUqRNI6Ow3mISWqjDDTXM4O9A7WM1grC+SZiw3sIuxSOwhNtUV6DPiuTbvI83cq9CEcIjGfVjbddR3Y1JYaPlgzMcI3VwmS6hNWIjbOpgSOjljpMaM6X1U0+sI1ZNcF22YbtwQETqkxcO0PaLEvBRXby+tbrKxEwqMCIQmRW8vUO6VB5YvfuZmdI5+Weq8AYIoFh6oK6ywZMo1OHeMwSj+4oA2+yPEAzN8sw0mn8dsUVQ8wFS9YhV0pVWNDV482jyGwhCQOVcOy4lL8sOWrTyssmCJa4FZQHF9+77v2yXCdBVN3RzrqgowZ1PY/Ieb+z1+VoYHteDXqhMSWVZvIjBeWMrPahTiYmRQa6Ceh5OwpoxljjnYWPPM6nuSDKOH734NwludrPVa2Z3BVZWIV8GOvB87YkuquoLXIB/N8fOZe4K7HOT1Esh2vS28VGr8synmLN2ePOoV2ODsmT/mrVlNUe24mXdtrSl8S+XI8Rtz4qmnrrJf6wPGIcQe5lyDF953ITp5wPWNWVfUWVjaS3MhVqeU3jljW/OkrZsKzMxhLgkKt2oa8ok8xdvOy6trD7Tr03NorwOasWrjZaDdR4HIr0Uni5Rdnl1jAaN2moBdvoBpVMSEVN100ofT01nXM89Xf5IsK+YEKjkJ3VrIjNOwiSNcVUcTicduEVv+s0RLrrc1sa0UGa9vwmHbzc0iJ8HdtUKXkR49yhtc01qgyxuZW6ZriCcG7a4nJTMAqdEM65Wa3N5I5vAkCedZ9RnGnutfbkeraeYaGWXEifNyWDU2Q1dEqfVz3vnCtQfiLMazM04yqIDgSWgfNjtLY2pttMKuyNqYmDKd4NcfuQXzm5bFl4jOsc3q9C1uKP4hqVDqeLv3VWRFKVI6SBCCytuyic3bNzKU48SoS1D45xNBnXA27EyBHjs0JSsVQpShshqppZ0VQhydfNrVQartonJ9nzygYhxYohVs65Ow0IE+XEZQuj+gEmc1PJr+423pXXLt+tHWiw2JSBSIVMy1w979Rc2cKuezU2Z4fYn4JaZ1OjiNjeomCS6M2cT/yNYkvooUAcPWftaEWAM/glvfBKM01LO/OmCCVlcPZZbwr/flE6nJWY+LqzMDDAq+Re4ZwR2Rgr7xYdeGc8ONqGpLmygi0CkxFp6BRt5Xans7HXEi+DbrYFuJg6b4zrbbOTSLzdILURNFqJs3USMXlMrSF/gIw9jhM4gTjYSb0bWHYhNrQaCBU1aldTqGlvv7EcxAEos11z5SR6OVLAZdkn2DAY5iDalByrgW5waRDQSx7XkcqUy7MwLMPtiST7OxuKLJ0UJyNsRulQtoeLb8akunNdjdmYquVI9zUkToG3n/a3UUfq7a5ty1rYbOh7cuw3txoV+oO8bMtrQ03WRej0WKPFDKO8wgujzS3rnR2qIPB151xvo3kOsmmFDNhUbjg0C/Ks6tWwMrFWv5mBzTflze0wtdSR2DJVHKAZvLqexyzxzbxw7k1lEyS0N871wRKRFcAWoY8GtNnYYdXkxzsGHyj8uApsR5IVkz4QnNaphJrD9a52yIbBIpVjjNSNGEiqtz23TG4USWPGOJob2d2XgmhGpB72eyY8GyKfS9V25BDPZjPap5ye5wVb3QTSyEmXtl4ZMiABpD1uzr591qu8VKYl36IVMR6Q1Z1aO0tCGEWsBVWq5jFjUht2lYe7tcXpJ1kQVn0AXdaRi+ckt7yQh0N0sCO3LfFhA85mF7GavMJZunFf+JdrVp4G/4JcDt55Ga4yTOPF3QackXqSInCePa6yDj7Sk39k2DTporttEP2UoU7gGCy5uzZBTk8XxYyIldvcmLuyTmLtHpl5eNznE3wxu56ZTkRfN7RJIDJlbQSOO5kQwQtbsXHhcDf5SgsNZypCcenSjWDAACOvnrbczVgHjVqoWxS6FwpjekHrhwopeIzqMOxZsSqFJive6KOMDS6bOxvI9gVjbiJO5huXSqC4965BlNPLpSWvcUNOAo5nVkqq92EYJASYaqsKXpPtFR0Ng74bvNFubUwEBxrGwzb40VNNBuKLlXnXazDansR+O3UHvzM6fFO54Q6+H+7B8nhC6njtNjulb52lF+YMCk183+89OWvVdpkRxjI5thfJD/HwvO61u3AODzdDh47wYKgUuydvQhNLyAn1+GTEb1zPdXerucoUvgInWqmUUcpMmTjE/aI6KeExyr0Oz7whvKw8vnbWIyogk9dDbVBTPst3ouOvbc8pdv3kSntCJcQt2q2xGj6u0u7K4NkQY01l7IyjPMi2m8c4Km5qvroulxMWwzjjhs4RX3rwuNmZTrI9KA1cJ8radXmn1468cxDZXbs5TjiJJUOwUqJ8gNpTSFFv85PSr0/v3v6Nl9Hm5zz/zx4pPZ8MfX2j5PFg0re9Tw9dn/4do/724a12Y2DS89FZk3Xh6xHUnx6cffzXjxzn/ePzHa+vz7Wfz8pbO5xfgH6LCw9sqccvTZk93ikBO5yumd+YbL7a+vunq99Ugs9l7QH72/KLCy6+zW8zzi+K+F5st/7ra/h6kAg2vl5++oKRxBe/rmY3Xy8kAO+wd/gde/v7/wHjrByKxC4AAA== -->

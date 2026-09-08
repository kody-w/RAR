---
name: "rar-cowork-cookbook-customer-revenue-globe"
description: "Builds a standalone interactive 3D globe HTML file from customer master and trailing-12-month sales data, with one marker per customer sized by revenue and colored by region, plus a legend."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_revenue_globe", "rar_sha256": "27731f0f48e40a4a18c5d33dbfe1642abd09ecf033d9f3ad39585a5d2c698260", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/customer_revenue_globe`. The original RAPP
agent is preserved byte-for-byte in `customer_revenue_globe_agent.py` and in the RCI capsule.

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

Customer Revenue 3D Globe Visualization — Builds a standalone interactive 3D globe HTML file from customer master and trailing-12-month sales data, with one marker per customer sized by revenue and colored by region, plus a legend.

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
  Upstream entry : https://coworkcookbook.com/recipes/customer-revenue-globe
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
    "customer_master_source": {
      "description": "Customer master data with country and city per customer (Dynamics 365 F&SCM read access required).",
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
    "output_folder": {
      "description": "Folder path where the standalone HTML file is saved.",
      "type": "string"
    },
    "sales_source": {
      "description": "Trailing-12-month sales by customer used to size the markers.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_revenue_globe_agent.py` and embedded as the fenced Python below (sha256 27731f0f48e40a4a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_revenue_globe_agent.py` first:

```bash
python3 customer_revenue_globe_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_revenue_globe_agent.py   # or on stdin
python3 customer_revenue_globe_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer Revenue 3D Globe Visualization — Builds a standalone interactive 3D globe HTML file from customer master and trailing-12-month sales data, with one marker per customer sized by revenue and colored by region, plus a legend.

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
  Upstream entry : https://coworkcookbook.com/recipes/customer-revenue-globe
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/customer_revenue_globe',
    "version": '3.0.3',
    "display_name": 'Customer Revenue 3D Globe Visualization',
    "description": 'Builds a standalone interactive 3D globe HTML file from customer master and trailing-12-month sales data, with one marker per customer sized by revenue and colored by region, plus a legend.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'customer-revenue-globe',
        "upstream_url": 'https://coworkcookbook.com/recipes/customer-revenue-globe',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '43707d16e4a549a2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/customer-revenue-globe', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM read access', 'Output matches: One standalone interactive HTML file.'], 'confidence': 1.0, 'deliverable': 'One standalone interactive HTML file.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'customer_master_source': 'Customer master data with country and city per customer (Dynamics 365 F&SCM read access required).', 'output_folder': 'Folder path where the standalone HTML file is saved.', 'sales_source': 'Trailing-12-month sales by customer used to size the markers.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Turns the customer master and revenue tape into an exec-ready visual that makes geographic concentration risk and growth pockets immediately obvious.', 'expected_output': 'One standalone interactive HTML file.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM read access'], 'prompt': 'Read the customer master and trailing-12-month sales by customer. For each customer with a country and city, geocode the city to lat/lon. Produce a standalone HTML file that renders a 3D globe (using a web library like globe.gl) with a marker per customer, sized by revenue and colored by region. Include a side legend. Save the HTML to the output folder.', 'steps': ['Paste the prompt.', 'Open the saved HTML file in your browser to explore.'], 'tenant_caveat': "Validated end-to-end against a live Cowork tenant on 2026-05-23 with USMF 2017 sales data. Cowork ran all four plan steps and produced 'Customer-globe-2017.html' - a standalone interactive 3D globe (globe.gl via CDN) with 13 USMF customer markers sized/elevated by revenue and colored by US region (West/South/Midwest/Northeast). Total 2017 revenue $1,651,883; top customer Sunset Wholesales (Artesia Wells, TX) at $531,250. Cowork geocoded each city from known coordinates (the customer master had no stored lat/lon) and flagged a data inconsistency: US-009 'Owl Wholesales' has city=Phoenix with state=CO in the master; Cowork plotted Phoenix, AZ instead. Sourced from CustomersV3 + SalesInvoiceHeadersV4.TotalInvoiceAmount for invoice dates in calendar year 2017.", 'verified_against': 'm365.cloud.microsoft 2026-05-23', 'what_it_does': 'Visualizes customer revenue on a 3D globe as a standalone HTML file.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a standalone interactive 3D globe HTML file from customer master and trailing-12-month sales data, with one marker per customer sized by revenue and colored by region, plus a legend.', 'example_request': 'Make a 3D globe of my customers sized by trailing-12-month revenue and save the HTML to my output folder.', 'inputs': [{'description': 'Customer master data with country and city per customer (Dynamics 365 F&SCM read access required).', 'name': 'customer_master_source'}, {'description': 'Trailing-12-month sales by customer used to size the markers.', 'name': 'sales_source'}, {'description': 'Folder path where the standalone HTML file is saved.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants customer revenue plotted geographically on an interactive 3D globe from Dynamics 365 F&SCM customer and trailing-12-month sales data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Paste the prompt.', 'Open the saved HTML file in your browser to explore.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class CustomerRevenueGlobe(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CustomerRevenueGlobe'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'customer_master_source': {'description': 'Customer master data with country and city per customer (Dynamics 365 F&SCM read access required).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_folder': {'description': 'Folder path where the standalone HTML file is saved.', 'type': 'string'}, 'sales_source': {'description': 'Trailing-12-month sales by customer used to size the markers.', 'type': 'string'}},
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
    print(CustomerRevenueGlobe().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

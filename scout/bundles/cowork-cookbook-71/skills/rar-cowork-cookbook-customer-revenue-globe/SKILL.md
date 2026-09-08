---
name: "rar-cowork-cookbook-customer-revenue-globe"
description: "Builds a standalone interactive 3D globe HTML file from customer master and trailing-12-month sales data, with one marker per customer sized by revenue and colored by region, plus a legend."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_revenue_globe", "rar_sha256": "27731f0f48e40a4a18c5d33dbfe1642abd09ecf033d9f3ad39585a5d2c698260", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

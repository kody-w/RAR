---
name: "rar-cowork-cookbook-dashboard-build-a-quality-plan-for-a-product"
description: "Pulls quality plan data for a product from Dynamics 365 F&SCM (read-only) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product", "rar_sha256": "9b510079a69fdd361011e87474dfe6bc6a37ca5634b4f65e7dd54207feed6685", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product`. The original RAPP
agent is preserved byte-for-byte in `dashboard_build_a_quality_plan_for_a_product_agent.py` and in the RCI capsule.

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

Build a quality plan for a product Interactive HTML Dashboard — Pulls quality plan data for a product from Dynamics 365 F&SCM (read-only) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-build-a-quality-plan-for-a-product
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
      "description": "Name of the HTML file to write, e.g. dashboard-build-a-quality-plan-for-a-product-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, default Documents/Cowork/output/.",
      "type": "string"
    },
    "product": {
      "description": "The product whose quality plan data should be pulled.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_build_a_quality_plan_for_a_product_agent.py` and embedded as the fenced Python below (sha256 9b510079a69fdd36…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_build_a_quality_plan_for_a_product_agent.py` first:

```bash
python3 dashboard_build_a_quality_plan_for_a_product_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_build_a_quality_plan_for_a_product_agent.py   # or on stdin
python3 dashboard_build_a_quality_plan_for_a_product_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Build a quality plan for a product Interactive HTML Dashboard — Pulls quality plan data for a product from Dynamics 365 F&SCM (read-only) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the Cowork output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-build-a-quality-plan-for-a-product
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product',
    "version": '3.0.3',
    "display_name": 'Build a quality plan for a product Interactive HTML Dashboard',
    "description": 'Pulls quality plan data for a product from Dynamics 365 F&SCM (read-only) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the Cowork output folder.',
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
        "upstream_slug": 'dashboard-build-a-quality-plan-for-a-product',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-build-a-quality-plan-for-a-product',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4871dd987a102645',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/build-a-quality-plan-for-a-product'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-build-a-quality-plan-for-a-product', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-build-a-quality-plan-for-a-product-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, default Documents/Cowork/output/.', 'product': 'The product whose quality plan data should be pulled.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of build a quality plan for a product with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull build a quality plan for a product data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-build-a-quality-plan-for-a-product-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing build a quality plan for a product.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls quality plan data for a product from Dynamics 365 F&SCM (read-only) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the Cowork output folder.', 'example_request': 'Build a quality plan dashboard for USMF for the latest fiscal period and save it as an HTML file.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'The product whose quality plan data should be pulled.', 'name': 'product'}, {'description': 'Name of the HTML file to write, e.g. dashboard-build-a-quality-plan-for-a-product-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, default Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable quality plan dashboard built from D365 ERP data, with charts, a sortable table, and a RAG indicator, without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardBuildAQualityPlanForAProduct(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardBuildAQualityPlanForAProduct'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-build-a-quality-plan-for-a-product-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, default Documents/Cowork/output/.', 'type': 'string'}, 'product': {'description': 'The product whose quality plan data should be pulled.', 'type': 'string'}},
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
    print(DashboardBuildAQualityPlanForAProduct().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

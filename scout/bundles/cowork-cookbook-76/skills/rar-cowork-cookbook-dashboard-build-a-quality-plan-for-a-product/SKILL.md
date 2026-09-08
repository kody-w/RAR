---
name: "rar-cowork-cookbook-dashboard-build-a-quality-plan-for-a-product"
description: "Pulls quality plan data for a product from Dynamics 365 F&SCM (read-only) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file to the Cowork output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_build_a_quality_plan_for_a_product", "rar_sha256": "9b510079a69fdd361011e87474dfe6bc6a37ca5634b4f65e7dd54207feed6685", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

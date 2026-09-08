---
name: "rar-cowork-cookbook-dashboard-manage-supplier-pricing"
description: "Pulls supplier pricing data from Dynamics 365 ERP for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_supplier_pricing", "rar_sha256": "60fa05b1766feefd91e0e0345cfbced430b8f9076e7180fc4b1b17e347366583", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_supplier_pricing`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_supplier_pricing_agent.py` and in the RCI capsule.

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

Manage supplier pricing Interactive HTML Dashboard — Pulls supplier pricing data from Dynamics 365 ERP for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-supplier-pricing
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
      "description": "Name of the HTML file to save, e.g. dashboard-manage-supplier-pricing-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_supplier_pricing_agent.py` and embedded as the fenced Python below (sha256 60fa05b1766feefd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_supplier_pricing_agent.py` first:

```bash
python3 dashboard_manage_supplier_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_supplier_pricing_agent.py   # or on stdin
python3 dashboard_manage_supplier_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier pricing Interactive HTML Dashboard — Pulls supplier pricing data from Dynamics 365 ERP for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-supplier-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_supplier_pricing',
    "version": '3.0.3',
    "display_name": 'Manage supplier pricing Interactive HTML Dashboard',
    "description": 'Pulls supplier pricing data from Dynamics 365 ERP for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-supplier-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-supplier-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4059090f01df8a0b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-pricing'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/dashboard-manage-supplier-pricing', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to save, e.g. dashboard-manage-supplier-pricing-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage supplier pricing with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage supplier pricing data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-supplier-pricing-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage supplier pricing.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls supplier pricing data from Dynamics 365 ERP for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea', 'example_request': 'Build a supplier pricing dashboard from D365 for USMF for the latest fiscal period as an HTML file.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to save, e.g. dashboard-manage-supplier-pricing-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants supplier pricing from D365 rendered as a shareable browser dashboard for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageSupplierPricing(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageSupplierPricing'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to save, e.g. dashboard-manage-supplier-pricing-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file.', 'type': 'string'}},
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
    print(DashboardManageSupplierPricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

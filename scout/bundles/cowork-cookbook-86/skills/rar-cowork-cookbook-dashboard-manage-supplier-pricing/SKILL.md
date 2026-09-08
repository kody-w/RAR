---
name: "rar-cowork-cookbook-dashboard-manage-supplier-pricing"
description: "Pulls supplier pricing data from Dynamics 365 ERP for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_supplier_pricing", "rar_sha256": "60fa05b1766feefd91e0e0345cfbced430b8f9076e7180fc4b1b17e347366583", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

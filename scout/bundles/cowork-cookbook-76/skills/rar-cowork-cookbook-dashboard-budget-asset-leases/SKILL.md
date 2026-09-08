---
name: "rar-cowork-cookbook-dashboard-budget-asset-leases"
description: "Pulls budget asset lease data from Dynamics 365 F&SCM for a given legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_budget_asset_leases", "rar_sha256": "3b9304b3b59b8b7c3a6ad0d63b20fb89fd428f9480484db7934470544c7f731f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_budget_asset_leases`. The original RAPP
agent is preserved byte-for-byte in `dashboard_budget_asset_leases_agent.py` and in the RCI capsule.

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

Budget asset leases Interactive HTML Dashboard — Pulls budget asset lease data from Dynamics 365 F&SCM for a given legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-budget-asset-leases
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
      "description": "Name of the HTML file to write, e.g. dashboard-budget-asset-leases-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_budget_asset_leases_agent.py` and embedded as the fenced Python below (sha256 3b9304b3b59b8b7c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_budget_asset_leases_agent.py` first:

```bash
python3 dashboard_budget_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_budget_asset_leases_agent.py   # or on stdin
python3 dashboard_budget_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget asset leases Interactive HTML Dashboard — Pulls budget asset lease data from Dynamics 365 F&SCM for a given legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-budget-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_budget_asset_leases',
    "version": '3.0.3',
    "display_name": 'Budget asset leases Interactive HTML Dashboard',
    "description": 'Pulls budget asset lease data from Dynamics 365 F&SCM for a given legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-budget-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-budget-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '854faf6d22e2657d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/budget-asset-leases'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-budget-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-budget-asset-leases-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of budget asset leases with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull budget asset leases data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-budget-asset-leases-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing budget asset leases.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls budget asset lease data from Dynamics 365 F&SCM for a given legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output', 'example_request': 'Build a budget asset leases dashboard for USMF for the latest fiscal period as an HTML file.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-budget-asset-leases-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants budget asset lease data from D365 turned into a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardBudgetAssetLeases(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardBudgetAssetLeases'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-budget-asset-leases-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardBudgetAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-dashboard-budget-asset-leases"
description: "Pulls budget asset lease data from Dynamics 365 F&SCM for a given legal entity and fiscal period and saves a standalone interactive HTML dashboard (totals header, SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_budget_asset_leases", "rar_sha256": "3b9304b3b59b8b7c3a6ad0d63b20fb89fd428f9480484db7934470544c7f731f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

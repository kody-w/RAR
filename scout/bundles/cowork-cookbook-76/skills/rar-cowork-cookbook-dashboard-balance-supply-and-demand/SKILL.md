---
name: "rar-cowork-cookbook-dashboard-balance-supply-and-demand"
description: "Pulls balance supply and demand data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the Cowork output folde"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_balance_supply_and_demand", "rar_sha256": "dcd07c4f0fa8242696b282114b23316c668bbf34d6749208ce51525b622bd0af", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_balance_supply_and_demand`. The original RAPP
agent is preserved byte-for-byte in `dashboard_balance_supply_and_demand_agent.py` and in the RCI capsule.

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

Balance supply and demand Interactive HTML Dashboard — Pulls balance supply and demand data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the Cowork output folde

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-balance-supply-and-demand
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
      "description": "D365 legal entity to pull data for (e.g. USMF).",
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
      "description": "Name of the HTML file to write, e.g. dashboard-balance-supply-and-demand-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated file (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_balance_supply_and_demand_agent.py` and embedded as the fenced Python below (sha256 dcd07c4f0fa82426…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_balance_supply_and_demand_agent.py` first:

```bash
python3 dashboard_balance_supply_and_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_balance_supply_and_demand_agent.py   # or on stdin
python3 dashboard_balance_supply_and_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Balance supply and demand Interactive HTML Dashboard — Pulls balance supply and demand data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the Cowork output folde

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-balance-supply-and-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_balance_supply_and_demand',
    "version": '3.0.3',
    "display_name": 'Balance supply and demand Interactive HTML Dashboard',
    "description": 'Pulls balance supply and demand data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the Cowork output folde',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-balance-supply-and-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-balance-supply-and-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd4b94aeeb0cdb266',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/balance-supply-and-demand'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/dashboard-balance-supply-and-demand', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data for (e.g. USMF).', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-balance-supply-and-demand-2026-05-24.html.', 'output_folder': 'Destination folder for the generated file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of balance supply and demand with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull balance supply and demand data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-balance-supply-and-demand-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing balance supply and demand.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls balance supply and demand data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the Cowork output folde', 'example_request': 'Build me a balance supply and demand HTML dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull data for (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-balance-supply-and-demand-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 balance supply and demand data for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardBalanceSupplyAndDemand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardBalanceSupplyAndDemand'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data for (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-balance-supply-and-demand-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardBalanceSupplyAndDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

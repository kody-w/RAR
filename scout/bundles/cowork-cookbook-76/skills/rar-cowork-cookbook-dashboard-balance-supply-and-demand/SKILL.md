---
name: "rar-cowork-cookbook-dashboard-balance-supply-and-demand"
description: "Pulls balance supply and demand data from Dynamics 365 F&SCM for a legal entity and fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the Cowork output folde"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_balance_supply_and_demand", "rar_sha256": "dcd07c4f0fa8242696b282114b23316c668bbf34d6749208ce51525b622bd0af", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

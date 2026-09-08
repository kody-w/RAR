---
name: "rar-cowork-cookbook-dashboard-forecast-maintenance"
description: "Pulls forecast maintenance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_forecast_maintenance", "rar_sha256": "3593e3afe158ce967b18107d322322fd1a77c0c80428100da41beae3fcc89ee9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_forecast_maintenance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_forecast_maintenance_agent.py` and in the RCI capsule.

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

Forecast maintenance Interactive HTML Dashboard — Pulls forecast maintenance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-forecast-maintenance
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
      "description": "Name of the HTML file to write, e.g. dashboard-forecast-maintenance-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_forecast_maintenance_agent.py` and embedded as the fenced Python below (sha256 3593e3afe158ce96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_forecast_maintenance_agent.py` first:

```bash
python3 dashboard_forecast_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_forecast_maintenance_agent.py   # or on stdin
python3 dashboard_forecast_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast maintenance Interactive HTML Dashboard — Pulls forecast maintenance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-forecast-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_forecast_maintenance',
    "version": '3.0.3',
    "display_name": 'Forecast maintenance Interactive HTML Dashboard',
    "description": 'Pulls forecast maintenance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read',
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
        "upstream_slug": 'dashboard-forecast-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-forecast-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a2908c7988e8fe0d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/forecast-maintenance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-forecast-maintenance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-forecast-maintenance-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of forecast maintenance with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull forecast maintenance data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-forecast-maintenance-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing forecast maintenance.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls forecast maintenance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read', 'example_request': 'Build me a forecast maintenance HTML dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-forecast-maintenance-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable forecast maintenance dashboard from D365 data without the viewer needing D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardForecastMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardForecastMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-forecast-maintenance-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardForecastMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

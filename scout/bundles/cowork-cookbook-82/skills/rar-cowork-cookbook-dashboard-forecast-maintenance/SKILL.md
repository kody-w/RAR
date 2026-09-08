---
name: "rar-cowork-cookbook-dashboard-forecast-maintenance"
description: "Pulls forecast maintenance data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder, read"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_forecast_maintenance", "rar_sha256": "3593e3afe158ce967b18107d322322fd1a77c0c80428100da41beae3fcc89ee9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

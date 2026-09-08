---
name: "rar-cowork-cookbook-dashboard-report-on-production-sustainability-metrics"
description: "Pulls production sustainability metrics from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_on_production_sustainability_metrics", "rar_sha256": "eaba5ebb247141cc57d96d126195708827b45892c6fc12bf7001a4a0fa16802f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_report_on_production_sustainability_metrics`. The original RAPP
agent is preserved byte-for-byte in `dashboard_report_on_production_sustainability_metrics_agent.py` and in the RCI capsule.

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

Report on production sustainability metrics Interactive HTML Dashboard — Pulls production sustainability metrics from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-on-production-sustainability-metrics
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
      "description": "Name of the HTML file to write, e.g. dashboard-report-on-production-sustainability-metrics-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_on_production_sustainability_metrics_agent.py` and embedded as the fenced Python below (sha256 eaba5ebb247141cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_on_production_sustainability_metrics_agent.py` first:

```bash
python3 dashboard_report_on_production_sustainability_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_report_on_production_sustainability_metrics_agent.py   # or on stdin
python3 dashboard_report_on_production_sustainability_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on production sustainability metrics Interactive HTML Dashboard — Pulls production sustainability metrics from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-on-production-sustainability-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_report_on_production_sustainability_metrics',
    "version": '3.0.3',
    "display_name": 'Report on production sustainability metrics Interactive HTML Dashboard',
    "description": 'Pulls production sustainability metrics from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-report-on-production-sustainability-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-report-on-production-sustainability-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1668ebd70e7d72ae',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/report-on-production-sustainability-metrics'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-report-on-production-sustainability-metrics', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-report-on-production-sustainability-metrics-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of report on production sustainability metrics with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull report on production sustainability metrics data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-report-on-production-sustainability-metrics-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing report on production sustainability metrics.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls production sustainability metrics from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu', 'example_request': 'Build an interactive HTML dashboard of production sustainability metrics from D365 for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-report-on-production-sustainability-metrics-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants production sustainability metrics from D365 packaged as a browser-viewable HTML dashboard for people without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardReportOnProductionSustainabilityMetrics(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReportOnProductionSustainabilityMetrics'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-report-on-production-sustainability-metrics-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardReportOnProductionSustainabilityMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

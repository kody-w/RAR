---
name: "rar-cowork-cookbook-dashboard-report-on-production-sustainability-metrics"
description: "Pulls production sustainability metrics from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the outpu"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_on_production_sustainability_metrics", "rar_sha256": "eaba5ebb247141cc57d96d126195708827b45892c6fc12bf7001a4a0fa16802f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

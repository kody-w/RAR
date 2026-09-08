---
name: "rar-cowork-cookbook-dashboard-report-production-quality-non-conformance"
description: "Pulls production quality non-conformance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_production_quality_non_conformance", "rar_sha256": "8d1356db0434ad67cd96a52c59b2b21fe55e2ea1e4da40ca1c01e070dd307fab", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_report_production_quality_non_conformance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_report_production_quality_non_conformance_agent.py` and in the RCI capsule.

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

Report production quality non-conformance Interactive HTML Dashboard — Pulls production quality non-conformance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-production-quality-non-conformance
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
      "description": "Name of the HTML file to write, e.g. dashboard-report-production-quality-non-conformance-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_production_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 8d1356db0434ad67…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_production_quality_non_conformance_agent.py` first:

```bash
python3 dashboard_report_production_quality_non_conformance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_report_production_quality_non_conformance_agent.py   # or on stdin
python3 dashboard_report_production_quality_non_conformance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production quality non-conformance Interactive HTML Dashboard — Pulls production quality non-conformance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-production-quality-non-conformance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_report_production_quality_non_conformance',
    "version": '3.0.3',
    "display_name": 'Report production quality non-conformance Interactive HTML Dashboard',
    "description": 'Pulls production quality non-conformance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the',
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
        "upstream_slug": 'dashboard-report-production-quality-non-conformance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-report-production-quality-non-conformance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2e2195fbd864c98e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/report-production-quality-non-conformance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/dashboard-report-production-quality-non-conformance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-report-production-quality-non-conformance-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of report production quality non-conformance with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull report production quality non-conformance data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-report-production-quality-non-conformance-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing report production quality non-conformance.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls production quality non-conformance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the', 'example_request': 'Build me an interactive HTML dashboard of production quality non-conformances in USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-report-production-quality-non-conformance-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of production quality non-conformances from D365 for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardReportProductionQualityNonConformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReportProductionQualityNonConformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-report-production-quality-non-conformance-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardReportProductionQualityNonConformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

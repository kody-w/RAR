---
name: "rar-cowork-cookbook-dashboard-report-production-quality-non-conformance"
description: "Pulls production quality non-conformance data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_production_quality_non_conformance", "rar_sha256": "8d1356db0434ad67cd96a52c59b2b21fe55e2ea1e4da40ca1c01e070dd307fab", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

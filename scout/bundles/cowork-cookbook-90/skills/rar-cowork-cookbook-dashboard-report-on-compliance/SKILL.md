---
name: "rar-cowork-cookbook-dashboard-report-on-compliance"
description: "Pulls compliance report data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_on_compliance", "rar_sha256": "da0eeb2eb0d84f0d33cf804cf297ced099d79ab273655315fa530a966c766789", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_report_on_compliance`. The original RAPP
agent is preserved byte-for-byte in `dashboard_report_on_compliance_agent.py` and in the RCI capsule.

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

Report on compliance Interactive HTML Dashboard — Pulls compliance report data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-on-compliance
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
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-report-on-compliance-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (Cowork output folder).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_on_compliance_agent.py` and embedded as the fenced Python below (sha256 da0eeb2eb0d84f0d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_on_compliance_agent.py` first:

```bash
python3 dashboard_report_on_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_report_on_compliance_agent.py   # or on stdin
python3 dashboard_report_on_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on compliance Interactive HTML Dashboard — Pulls compliance report data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-on-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_report_on_compliance',
    "version": '3.0.3',
    "display_name": 'Report on compliance Interactive HTML Dashboard',
    "description": 'Pulls compliance report data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-report-on-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-report-on-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '13c0d675e29a18a2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/report-on-compliance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-report-on-compliance', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-report-on-compliance-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Cowork output folder).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of report on compliance with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull report on compliance data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-report-on-compliance-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing report on compliance.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls compliance report data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol', 'example_request': 'Build me a compliance dashboard HTML from D365 for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-report-on-compliance-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Cowork output folder).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone needs a shareable browser-viewable compliance dashboard from D365 ERP data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardReportOnCompliance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReportOnCompliance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-report-on-compliance-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Cowork output folder).', 'type': 'string'}},
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
    print(DashboardReportOnCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

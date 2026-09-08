---
name: "rar-cowork-cookbook-dashboard-report-on-compliance"
description: "Pulls compliance report data from Dynamics 365 F&SCM for a given legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_on_compliance", "rar_sha256": "da0eeb2eb0d84f0d33cf804cf297ced099d79ab273655315fa530a966c766789", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

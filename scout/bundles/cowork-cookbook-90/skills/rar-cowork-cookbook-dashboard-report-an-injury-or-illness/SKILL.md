---
name: "rar-cowork-cookbook-dashboard-report-an-injury-or-illness"
description: "Pulls injury/illness report data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder, read-on"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_an_injury_or_illness", "rar_sha256": "7d36b8635d7dbfccd8c571ad2e004268f37f374e17213a8898c9fab431ff5926", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_report_an_injury_or_illness`. The original RAPP
agent is preserved byte-for-byte in `dashboard_report_an_injury_or_illness_agent.py` and in the RCI capsule.

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

Report an injury or illness Interactive HTML Dashboard — Pulls injury/illness report data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder, read-on

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-an-injury-or-illness
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
      "description": "Name of the HTML file to produce, e.g. dashboard-report-an-injury-or-illness-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder the HTML file is saved to, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_report_an_injury_or_illness_agent.py` and embedded as the fenced Python below (sha256 7d36b8635d7dbfcc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_report_an_injury_or_illness_agent.py` first:

```bash
python3 dashboard_report_an_injury_or_illness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_report_an_injury_or_illness_agent.py   # or on stdin
python3 dashboard_report_an_injury_or_illness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report an injury or illness Interactive HTML Dashboard — Pulls injury/illness report data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder, read-on

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-report-an-injury-or-illness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_report_an_injury_or_illness',
    "version": '3.0.3',
    "display_name": 'Report an injury or illness Interactive HTML Dashboard',
    "description": 'Pulls injury/illness report data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder, read-on',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-report-an-injury-or-illness',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-report-an-injury-or-illness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '488dde4fff92821a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/report-an-injury-or-illness'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-report-an-injury-or-illness', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-report-an-injury-or-illness-2026-05-24.html.', 'output_folder': 'Folder the HTML file is saved to, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of report an injury or illness with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull report an injury or illness data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-report-an-injury-or-illness-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing report an injury or illness.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls injury/illness report data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder, read-on', 'example_request': 'Build an injury and illness dashboard from D365 for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-report-an-injury-or-illness-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder the HTML file is saved to, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of injury or illness reporting data from D365 without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardReportAnInjuryOrIllness(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardReportAnInjuryOrIllness'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-report-an-injury-or-illness-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder the HTML file is saved to, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardReportAnInjuryOrIllness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

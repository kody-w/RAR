---
name: "rar-cowork-cookbook-dashboard-report-an-injury-or-illness"
description: "Pulls injury/illness report data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (charts, sortable table, RAG indicator) to the output folder, read-on"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_report_an_injury_or_illness", "rar_sha256": "7d36b8635d7dbfccd8c571ad2e004268f37f374e17213a8898c9fab431ff5926", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

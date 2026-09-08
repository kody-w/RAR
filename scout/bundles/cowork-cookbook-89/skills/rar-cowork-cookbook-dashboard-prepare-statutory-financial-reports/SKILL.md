---
name: "rar-cowork-cookbook-dashboard-prepare-statutory-financial-reports"
description: "Pulls statutory financial reporting data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_prepare_statutory_financial_reports", "rar_sha256": "3dd552938a85142d8e3d192a6ad892fcb0333b332b1ff29ec018b25e4cc42180", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_prepare_statutory_financial_reports`. The original RAPP
agent is preserved byte-for-byte in `dashboard_prepare_statutory_financial_reports_agent.py` and in the RCI capsule.

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

Prepare statutory financial reports Interactive HTML Dashboard — Pulls statutory financial reporting data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-prepare-statutory-financial-reports
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
      "description": "D365 legal entity to pull from; defaults to USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-prepare-statutory-financial-reports-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_prepare_statutory_financial_reports_agent.py` and embedded as the fenced Python below (sha256 3dd552938a85142d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_prepare_statutory_financial_reports_agent.py` first:

```bash
python3 dashboard_prepare_statutory_financial_reports_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_prepare_statutory_financial_reports_agent.py   # or on stdin
python3 dashboard_prepare_statutory_financial_reports_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare statutory financial reports Interactive HTML Dashboard — Pulls statutory financial reporting data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-prepare-statutory-financial-reports
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_prepare_statutory_financial_reports',
    "version": '3.0.3',
    "display_name": 'Prepare statutory financial reports Interactive HTML Dashboard',
    "description": 'Pulls statutory financial reporting data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-prepare-statutory-financial-reports',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-prepare-statutory-financial-reports',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e65c872eadf45dd7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/prepare-statutory-financial-reports'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-prepare-statutory-financial-reports', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-prepare-statutory-financial-reports-2026-05-24.html.', 'output_folder': 'Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of prepare statutory financial reports with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull prepare statutory financial reports data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-prepare-statutory-financial-reports-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing prepare statutory financial reports.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls statutory financial reporting data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only.', 'example_request': 'Build me an interactive HTML dashboard of statutory financial reports for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-prepare-statutory-financial-reports-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants statutory financial report figures packaged as a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardPrepareStatutoryFinancialReports(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPrepareStatutoryFinancialReports'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-prepare-statutory-financial-reports-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the file; defaults to Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardPrepareStatutoryFinancialReports().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-dashboard-prepare-statutory-financial-reports"
description: "Pulls statutory financial reporting data for the most recent fiscal period from Dynamics 365 F&SCM (legal entity USMF) via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_prepare_statutory_financial_reports", "rar_sha256": "3dd552938a85142d8e3d192a6ad892fcb0333b332b1ff29ec018b25e4cc42180", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

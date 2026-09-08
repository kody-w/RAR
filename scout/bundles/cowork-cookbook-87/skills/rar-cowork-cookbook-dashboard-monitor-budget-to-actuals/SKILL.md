---
name: "rar-cowork-cookbook-dashboard-monitor-budget-to-actuals"
description: "Pulls budget-to-actuals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_budget_to_actuals", "rar_sha256": "3236df05c304a1deecc8082208274a41f3220626fc14d3f6e358367bd18ddfdd", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_budget_to_actuals`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_budget_to_actuals_agent.py` and in the RCI capsule.

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

Monitor budget to actuals Interactive HTML Dashboard — Pulls budget-to-actuals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-budget-to-actuals
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
      "description": "D365 legal entity to pull data from, e.g. USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-monitor-budget-to-actuals-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_budget_to_actuals_agent.py` and embedded as the fenced Python below (sha256 3236df05c304a1de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_budget_to_actuals_agent.py` first:

```bash
python3 dashboard_monitor_budget_to_actuals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_budget_to_actuals_agent.py   # or on stdin
python3 dashboard_monitor_budget_to_actuals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor budget to actuals Interactive HTML Dashboard — Pulls budget-to-actuals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-budget-to-actuals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_budget_to_actuals',
    "version": '3.0.3',
    "display_name": 'Monitor budget to actuals Interactive HTML Dashboard',
    "description": 'Pulls budget-to-actuals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;',
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
        "upstream_slug": 'dashboard-monitor-budget-to-actuals',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-budget-to-actuals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '711ab43511ca05be',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-budget-to-actuals'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/dashboard-monitor-budget-to-actuals', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull data from, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-monitor-budget-to-actuals-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of monitor budget to actuals with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull monitor budget to actuals data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-monitor-budget-to-actuals-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing monitor budget to actuals.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls budget-to-actuals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;', 'example_request': 'Build me a budget vs actuals HTML dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull data from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-monitor-budget-to-actuals-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable budget vs actuals dashboard from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMonitorBudgetToActuals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorBudgetToActuals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull data from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-monitor-budget-to-actuals-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardMonitorBudgetToActuals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

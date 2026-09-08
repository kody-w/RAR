---
name: "rar-cowork-cookbook-dashboard-monitor-budget-to-actuals"
description: "Pulls budget-to-actuals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_budget_to_actuals", "rar_sha256": "3236df05c304a1deecc8082208274a41f3220626fc14d3f6e358367bd18ddfdd", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

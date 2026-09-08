---
name: "rar-cowork-cookbook-dashboard-monitor-human-capital-expenses"
description: "Pulls human capital expense data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_human_capital_expenses", "rar_sha256": "5e6a0e0ae2bacf02b75be0127f44ca42f56df5e92f8d7e30ed1b704c56f4db12", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_monitor_human_capital_expenses`. The original RAPP
agent is preserved byte-for-byte in `dashboard_monitor_human_capital_expenses_agent.py` and in the RCI capsule.

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

Monitor human capital expenses Interactive HTML Dashboard — Pulls human capital expense data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-human-capital-expenses
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
      "description": "Name of the HTML file to write, e.g. dashboard-monitor-human-capital-expenses-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder the HTML file is saved to, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_monitor_human_capital_expenses_agent.py` and embedded as the fenced Python below (sha256 5e6a0e0ae2bacf02…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_monitor_human_capital_expenses_agent.py` first:

```bash
python3 dashboard_monitor_human_capital_expenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_monitor_human_capital_expenses_agent.py   # or on stdin
python3 dashboard_monitor_human_capital_expenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor human capital expenses Interactive HTML Dashboard — Pulls human capital expense data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-monitor-human-capital-expenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_monitor_human_capital_expenses',
    "version": '3.0.3',
    "display_name": 'Monitor human capital expenses Interactive HTML Dashboard',
    "description": 'Pulls human capital expense data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol',
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
        "upstream_slug": 'dashboard-monitor-human-capital-expenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-monitor-human-capital-expenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '434c073d5a7bb97b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/monitor-human-capital-expenses'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-monitor-human-capital-expenses', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-monitor-human-capital-expenses-2026-05-24.html.', 'output_folder': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of monitor human capital expenses with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull monitor human capital expenses data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-monitor-human-capital-expenses-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing monitor human capital expenses.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls human capital expense data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol', 'example_request': 'Build me an HTML dashboard of human capital expenses for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-monitor-human-capital-expenses-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants human capital expense figures from D365 packaged as a shareable browser dashboard for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardMonitorHumanCapitalExpenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardMonitorHumanCapitalExpenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-monitor-human-capital-expenses-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardMonitorHumanCapitalExpenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

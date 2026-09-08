---
name: "rar-cowork-cookbook-dashboard-monitor-human-capital-expenses"
description: "Pulls human capital expense data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fol"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_monitor_human_capital_expenses", "rar_sha256": "5e6a0e0ae2bacf02b75be0127f44ca42f56df5e92f8d7e30ed1b704c56f4db12", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-dashboard-set-employee-growth-goals"
description: "Pulls set employee growth goals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_set_employee_growth_goals", "rar_sha256": "9630ab31ba1b190952445ec0ae16778060f3d3c18a4d24c822e5e2bc424039a1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_set_employee_growth_goals`. The original RAPP
agent is preserved byte-for-byte in `dashboard_set_employee_growth_goals_agent.py` and in the RCI capsule.

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

Set employee growth goals Interactive HTML Dashboard — Pulls set employee growth goals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-employee-growth-goals
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
      "description": "Fiscal period to pull; defaults to the most recent available.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-set-employee-growth-goals-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (Documents/Cowork/output/).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_set_employee_growth_goals_agent.py` and embedded as the fenced Python below (sha256 9630ab31ba1b1909…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_set_employee_growth_goals_agent.py` first:

```bash
python3 dashboard_set_employee_growth_goals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_set_employee_growth_goals_agent.py   # or on stdin
python3 dashboard_set_employee_growth_goals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Set employee growth goals Interactive HTML Dashboard — Pulls set employee growth goals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-set-employee-growth-goals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_set_employee_growth_goals',
    "version": '3.0.3',
    "display_name": 'Set employee growth goals Interactive HTML Dashboard',
    "description": 'Pulls set employee growth goals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output',
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
        "upstream_slug": 'dashboard-set-employee-growth-goals',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-set-employee-growth-goals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '18b20c4362ccacc6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/set-employee-growth-goals'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-set-employee-growth-goals', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-set-employee-growth-goals-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of set employee growth goals with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull set employee growth goals data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-set-employee-growth-goals-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing set employee growth goals.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls set employee growth goals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output', 'example_request': 'Build me an HTML dashboard of employee growth goals from D365 for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-set-employee-growth-goals-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants employee growth goal data from D365 packaged as a shareable browser dashboard for viewers without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardSetEmployeeGrowthGoals(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardSetEmployeeGrowthGoals'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-set-employee-growth-goals-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardSetEmployeeGrowthGoals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

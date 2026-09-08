---
name: "rar-cowork-cookbook-dashboard-set-employee-growth-goals"
description: "Pulls set employee growth goals data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_set_employee_growth_goals", "rar_sha256": "9630ab31ba1b190952445ec0ae16778060f3d3c18a4d24c822e5e2bc424039a1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

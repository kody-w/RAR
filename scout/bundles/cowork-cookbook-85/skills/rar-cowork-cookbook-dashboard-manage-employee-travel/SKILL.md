---
name: "rar-cowork-cookbook-dashboard-manage-employee-travel"
description: "Pulls employee travel data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_employee_travel", "rar_sha256": "e64638e18474766cdf74cfc2f8008317dd17ed30603fc8fd9717a2350ecf30ed", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_employee_travel`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_employee_travel_agent.py` and in the RCI capsule.

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

Manage employee travel Interactive HTML Dashboard — Pulls employee travel data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-employee-travel
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-employee-travel-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_employee_travel_agent.py` and embedded as the fenced Python below (sha256 e64638e18474766c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_employee_travel_agent.py` first:

```bash
python3 dashboard_manage_employee_travel_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_employee_travel_agent.py   # or on stdin
python3 dashboard_manage_employee_travel_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage employee travel Interactive HTML Dashboard — Pulls employee travel data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-employee-travel
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_employee_travel',
    "version": '3.0.3',
    "display_name": 'Manage employee travel Interactive HTML Dashboard',
    "description": 'Pulls employee travel data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to the output',
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
        "upstream_slug": 'dashboard-manage-employee-travel',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-employee-travel',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bb9a2b2881e8e436',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/manage-employee-travel'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-manage-employee-travel', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-employee-travel-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage employee travel with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage employee travel data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-employee-travel-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage employee travel.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls employee travel data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to the output', 'example_request': 'Build me an interactive HTML dashboard of employee travel from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-employee-travel-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of employee travel data from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageEmployeeTravel(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageEmployeeTravel'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-employee-travel-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardManageEmployeeTravel().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-dashboard-manage-employee-travel"
description: "Pulls employee travel data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard with charts, a sortable table, and a RAG indicator to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_employee_travel", "rar_sha256": "e64638e18474766cdf74cfc2f8008317dd17ed30603fc8fd9717a2350ecf30ed", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-dashboard-assign-project-resources"
description: "Pulls assign project resources data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_assign_project_resources", "rar_sha256": "c10bd5bc97d69bfc7740de59911c984175448d8f5a712833e16cb1322c34406d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_assign_project_resources`. The original RAPP
agent is preserved byte-for-byte in `dashboard_assign_project_resources_agent.py` and in the RCI capsule.

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

Assign project resources Interactive HTML Dashboard — Pulls assign project resources data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fo

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-project-resources
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
      "description": "D365 legal entity to pull from, e.g. USMF.",
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
      "description": "Name of the HTML file to produce, e.g. dashboard-assign-project-resources-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the HTML file is saved, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_assign_project_resources_agent.py` and embedded as the fenced Python below (sha256 c10bd5bc97d69bfc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_assign_project_resources_agent.py` first:

```bash
python3 dashboard_assign_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_assign_project_resources_agent.py   # or on stdin
python3 dashboard_assign_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assign project resources Interactive HTML Dashboard — Pulls assign project resources data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fo

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_assign_project_resources',
    "version": '3.0.3',
    "display_name": 'Assign project resources Interactive HTML Dashboard',
    "description": 'Pulls assign project resources data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-assign-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-assign-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f2d0f01516a9ec44',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/assign-project-resources'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-assign-project-resources', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull from, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-assign-project-resources-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of assign project resources with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull assign project resources data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-assign-project-resources-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing assign project resources.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls assign project resources data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fo', 'example_request': 'Build an interactive HTML dashboard of assign project resources for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull from, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-assign-project-resources-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a shareable browser-viewable dashboard of assign project resources data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardAssignProjectResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAssignProjectResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull from, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-assign-project-resources-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardAssignProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

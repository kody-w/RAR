---
name: "rar-cowork-cookbook-dashboard-assign-project-resources"
description: "Pulls assign project resources data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output fo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_assign_project_resources", "rar_sha256": "c10bd5bc97d69bfc7740de59911c984175448d8f5a712833e16cb1322c34406d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

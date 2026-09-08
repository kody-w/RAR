---
name: "rar-cowork-cookbook-dashboard-control-project-scope"
description: "Pulls control project scope data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_control_project_scope", "rar_sha256": "31f9f215e7554557c58c0b8df729b248222c8c2da4c1a292ac00777d67c2ab1a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_control_project_scope`. The original RAPP
agent is preserved byte-for-byte in `dashboard_control_project_scope_agent.py` and in the RCI capsule.

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

Control project scope Interactive HTML Dashboard — Pulls control project scope data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-control-project-scope
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
      "description": "Name of the HTML file to write, e.g. dashboard-control-project-scope-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML file (Cowork output folder).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_control_project_scope_agent.py` and embedded as the fenced Python below (sha256 31f9f215e7554557…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_control_project_scope_agent.py` first:

```bash
python3 dashboard_control_project_scope_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_control_project_scope_agent.py   # or on stdin
python3 dashboard_control_project_scope_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Control project scope Interactive HTML Dashboard — Pulls control project scope data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-control-project-scope
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_control_project_scope',
    "version": '3.0.3',
    "display_name": 'Control project scope Interactive HTML Dashboard',
    "description": 'Pulls control project scope data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea',
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
        "upstream_slug": 'dashboard-control-project-scope',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-control-project-scope',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0d45d56fe436837f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/control-project-scope'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-control-project-scope', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-control-project-scope-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Cowork output folder).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of control project scope with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull control project scope data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-control-project-scope-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing control project scope.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls control project scope data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea', 'example_request': 'Build me a control project scope dashboard for USMF from the latest fiscal period as a shareable HTML file.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-control-project-scope-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Cowork output folder).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable dashboard of control project scope from D365 that can be shared with people who lack D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardControlProjectScope(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardControlProjectScope'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-control-project-scope-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Cowork output folder).', 'type': 'string'}},
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
    print(DashboardControlProjectScope().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

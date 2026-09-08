---
name: "rar-cowork-cookbook-dashboard-control-project-scope"
description: "Pulls control project scope data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder; rea"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_control_project_scope", "rar_sha256": "31f9f215e7554557c58c0b8df729b248222c8c2da4c1a292ac00777d67c2ab1a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

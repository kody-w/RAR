---
name: "rar-cowork-cookbook-dashboard-purchase-project-materials"
description: "Pulls purchase project materials data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_purchase_project_materials", "rar_sha256": "7e464884150de39841147fb69f9c5977b3cc9a519d5fc79a6b3cdc860dc9110f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_purchase_project_materials`. The original RAPP
agent is preserved byte-for-byte in `dashboard_purchase_project_materials_agent.py` and in the RCI capsule.

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

Purchase project materials Interactive HTML Dashboard — Pulls purchase project materials data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-purchase-project-materials
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
      "description": "Name of the HTML file to write, e.g. dashboard-purchase-project-materials-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_purchase_project_materials_agent.py` and embedded as the fenced Python below (sha256 7e464884150de398…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_purchase_project_materials_agent.py` first:

```bash
python3 dashboard_purchase_project_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_purchase_project_materials_agent.py   # or on stdin
python3 dashboard_purchase_project_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purchase project materials Interactive HTML Dashboard — Pulls purchase project materials data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-purchase-project-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_purchase_project_materials',
    "version": '3.0.3',
    "display_name": 'Purchase project materials Interactive HTML Dashboard',
    "description": 'Pulls purchase project materials data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output',
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
        "upstream_slug": 'dashboard-purchase-project-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-purchase-project-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '532027f00873758a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/purchase-project-materials'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/dashboard-purchase-project-materials', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-purchase-project-materials-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of purchase project materials with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull purchase project materials data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-purchase-project-materials-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing purchase project materials.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls purchase project materials data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output', 'example_request': 'Build an interactive HTML dashboard of purchase project materials for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-purchase-project-materials-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable dashboard of purchase project materials from D365 that can be shared with people who lack D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardPurchaseProjectMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardPurchaseProjectMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-purchase-project-materials-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardPurchaseProjectMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-dashboard-purchase-project-materials"
description: "Pulls purchase project materials data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, then saves a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_purchase_project_materials", "rar_sha256": "7e464884150de39841147fb69f9c5977b3cc9a519d5fc79a6b3cdc860dc9110f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

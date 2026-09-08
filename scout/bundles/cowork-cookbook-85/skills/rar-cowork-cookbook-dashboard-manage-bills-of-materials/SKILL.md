---
name: "rar-cowork-cookbook-dashboard-manage-bills-of-materials"
description: "Generates a standalone interactive HTML dashboard of bills of materials data pulled read-only from Dynamics 365 F&SCM for a legal entity and fiscal period, with charts, sortable table, and RAG indicator."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_bills_of_materials", "rar_sha256": "9ebd8c616baad91e05d1bf7080e6cbc272c8d43a337ca3d62c073a3b4dbaa9a9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_bills_of_materials`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_bills_of_materials_agent.py` and in the RCI capsule.

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

Manage bills of materials Interactive HTML Dashboard — Generates a standalone interactive HTML dashboard of bills of materials data pulled read-only from Dynamics 365 F&SCM for a legal entity and fiscal period, with charts, sortable table, and RAG indicator.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-bills-of-materials
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
      "description": "D365 legal entity to pull BOM data from (e.g. USMF).",
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
      "description": "Name of the HTML file to write, e.g. dashboard-manage-bills-of-materials-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder where the generated HTML file is saved (e.g. Documents/Cowork/output).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 9ebd8c616baad91e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_bills_of_materials_agent.py` first:

```bash
python3 dashboard_manage_bills_of_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_bills_of_materials_agent.py   # or on stdin
python3 dashboard_manage_bills_of_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage bills of materials Interactive HTML Dashboard — Generates a standalone interactive HTML dashboard of bills of materials data pulled read-only from Dynamics 365 F&SCM for a legal entity and fiscal period, with charts, sortable table, and RAG indicator.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-bills-of-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_bills_of_materials',
    "version": '3.0.3',
    "display_name": 'Manage bills of materials Interactive HTML Dashboard',
    "description": 'Generates a standalone interactive HTML dashboard of bills of materials data pulled read-only from Dynamics 365 F&SCM for a legal entity and fiscal period, with charts, sortable table, and RAG indicator.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-bills-of-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-bills-of-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6f6bbe024359751d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-bills-of-materials'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/dashboard-manage-bills-of-materials', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to pull BOM data from (e.g. USMF).', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-manage-bills-of-materials-2026-05-24.html.', 'output_folder': 'Folder where the generated HTML file is saved (e.g. Documents/Cowork/output).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage bills of materials with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage bills of materials data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-bills-of-materials-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage bills of materials.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Generates a standalone interactive HTML dashboard of bills of materials data pulled read-only from Dynamics 365 F&SCM for a legal entity and fiscal period, with charts, sortable table, and RAG indicator.', 'example_request': 'Build me a BOM dashboard HTML for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to pull BOM data from (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-manage-bills-of-materials-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the generated HTML file is saved (e.g. Documents/Cowork/output).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable BOM dashboard from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageBillsOfMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageBillsOfMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to pull BOM data from (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-manage-bills-of-materials-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the generated HTML file is saved (e.g. Documents/Cowork/output).', 'type': 'string'}},
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
    print(DashboardManageBillsOfMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

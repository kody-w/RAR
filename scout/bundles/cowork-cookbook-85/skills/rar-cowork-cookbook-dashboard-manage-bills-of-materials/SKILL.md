---
name: "rar-cowork-cookbook-dashboard-manage-bills-of-materials"
description: "Generates a standalone interactive HTML dashboard of bills of materials data pulled read-only from Dynamics 365 F&SCM for a legal entity and fiscal period, with charts, sortable table, and RAG indicator."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_bills_of_materials", "rar_sha256": "9ebd8c616baad91e05d1bf7080e6cbc272c8d43a337ca3d62c073a3b4dbaa9a9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

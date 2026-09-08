---
name: "rar-cowork-cookbook-dashboard-manage-work-assignments"
description: "Pulls manage work assignments data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_work_assignments", "rar_sha256": "db5d3b485814230d23206f540502430376b57fa65529b6f2a3c0c1a6cc64577c", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_work_assignments`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_work_assignments_agent.py` and in the RCI capsule.

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

Manage work assignments Interactive HTML Dashboard — Pulls manage work assignments data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-work-assignments
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
      "description": "Name of the HTML file to produce, e.g. dashboard-manage-work-assignments-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_work_assignments_agent.py` and embedded as the fenced Python below (sha256 db5d3b485814230d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_work_assignments_agent.py` first:

```bash
python3 dashboard_manage_work_assignments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_work_assignments_agent.py   # or on stdin
python3 dashboard_manage_work_assignments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage work assignments Interactive HTML Dashboard — Pulls manage work assignments data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-work-assignments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_work_assignments',
    "version": '3.0.3',
    "display_name": 'Manage work assignments Interactive HTML Dashboard',
    "description": 'Pulls manage work assignments data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-manage-work-assignments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-work-assignments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4749a388f67eece0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/manage-work-assignments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-manage-work-assignments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-manage-work-assignments-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML file (Documents/Cowork/output/).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage work assignments with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage work assignments data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-work-assignments-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage work assignments.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls manage work assignments data from Dynamics 365 F&SCM for a given legal entity and fiscal period, then writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder;', 'example_request': 'Build me an interactive HTML dashboard of manage work assignments for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-manage-work-assignments-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of manage work assignments from D365 that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageWorkAssignments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageWorkAssignments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-manage-work-assignments-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML file (Documents/Cowork/output/).', 'type': 'string'}},
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
    print(DashboardManageWorkAssignments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-dashboard-schedule-dock-appointments"
description: "Pulls schedule dock appointment data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_schedule_dock_appointments", "rar_sha256": "a21a2e26168a1e44e3c8142588f196d4f2a9a84f3f49598a654f42b4a82e9753", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_schedule_dock_appointments`. The original RAPP
agent is preserved byte-for-byte in `dashboard_schedule_dock_appointments_agent.py` and in the RCI capsule.

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

Schedule dock appointments Interactive HTML Dashboard — Pulls schedule dock appointment data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-schedule-dock-appointments
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
      "description": "Fiscal period to pull; defaults to the most recent available.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-schedule-dock-appointments-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_schedule_dock_appointments_agent.py` and embedded as the fenced Python below (sha256 a21a2e26168a1e44…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_schedule_dock_appointments_agent.py` first:

```bash
python3 dashboard_schedule_dock_appointments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_schedule_dock_appointments_agent.py   # or on stdin
python3 dashboard_schedule_dock_appointments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule dock appointments Interactive HTML Dashboard — Pulls schedule dock appointment data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-schedule-dock-appointments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_schedule_dock_appointments',
    "version": '3.0.3',
    "display_name": 'Schedule dock appointments Interactive HTML Dashboard',
    "description": 'Pulls schedule dock appointment data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder',
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
        "upstream_slug": 'dashboard-schedule-dock-appointments',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-schedule-dock-appointments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e268fd47591fc0ec',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/schedule-dock-appointments'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/dashboard-schedule-dock-appointments', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-schedule-dock-appointments-2026-05-24.html.', 'output_folder': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of schedule dock appointments with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull schedule dock appointments data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-schedule-dock-appointments-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing schedule dock appointments.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls schedule dock appointment data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder', 'example_request': 'Build me an interactive HTML dashboard of dock appointments for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-schedule-dock-appointments-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants dock appointment scheduling data turned into a shareable browser dashboard that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardScheduleDockAppointments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardScheduleDockAppointments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-schedule-dock-appointments-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardScheduleDockAppointments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

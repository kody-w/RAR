---
name: "rar-cowork-cookbook-dashboard-schedule-dock-appointments"
description: "Pulls schedule dock appointment data from Dynamics 365 F&SCM for a given legal entity and fiscal period, and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_schedule_dock_appointments", "rar_sha256": "a21a2e26168a1e44e3c8142588f196d4f2a9a84f3f49598a654f42b4a82e9753", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

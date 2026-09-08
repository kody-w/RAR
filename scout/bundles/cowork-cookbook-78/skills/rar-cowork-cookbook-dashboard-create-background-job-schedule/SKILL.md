---
name: "rar-cowork-cookbook-dashboard-create-background-job-schedule"
description: "Pulls create background job schedule data from Dynamics 365 F&SCM for a legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_background_job_schedule", "rar_sha256": "f6b4194e716d4ea8bd3c159bdd5c8c3bdb5e733068964d7e9780f3af4300db52", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_background_job_schedule`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_background_job_schedule_agent.py` and in the RCI capsule.

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

Create background job schedule Interactive HTML Dashboard — Pulls create background job schedule data from Dynamics 365 F&SCM for a legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule
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
      "description": "Name of the HTML file to produce, e.g. dashboard-create-background-job-schedule-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_background_job_schedule_agent.py` and embedded as the fenced Python below (sha256 f6b4194e716d4ea8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_background_job_schedule_agent.py` first:

```bash
python3 dashboard_create_background_job_schedule_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_background_job_schedule_agent.py   # or on stdin
python3 dashboard_create_background_job_schedule_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create background job schedule Interactive HTML Dashboard — Pulls create background job schedule data from Dynamics 365 F&SCM for a legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_background_job_schedule',
    "version": '3.0.3',
    "display_name": 'Create background job schedule Interactive HTML Dashboard',
    "description": 'Pulls create background job schedule data from Dynamics 365 F&SCM for a legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-create-background-job-schedule',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-background-job-schedule',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1ee9bab24f68b137',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/create-background-job-schedule'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-create-background-job-schedule', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-create-background-job-schedule-2026-05-24.html.', 'output_folder': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of create background job schedule with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull create background job schedule data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-create-background-job-schedule-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing create background job schedule.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls create background job schedule data from Dynamics 365 F&SCM for a legal entity and fiscal period and writes a standalone interactive HTML dashboard (totals header, inline SVG charts, sortable table, RAG indicator)', 'example_request': 'Build an HTML dashboard of create background job schedule data for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-create-background-job-schedule-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of D365 create background job schedule data without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardCreateBackgroundJobSchedule(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateBackgroundJobSchedule'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-create-background-job-schedule-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder where the HTML file is saved, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardCreateBackgroundJobSchedule().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

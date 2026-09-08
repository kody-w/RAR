---
name: "rar-cowork-cookbook-dashboard-create-and-schedule-services"
description: "Pulls create-and-schedule-services data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and returns a standalone interactive HTML dashboard file saved to the output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_and_schedule_services", "rar_sha256": "358919fbd05922cebcd58535c8c94c5848cd9f22db0db522c09be42f78cc53e3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_and_schedule_services`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_and_schedule_services_agent.py` and in the RCI capsule.

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

Create and schedule services Interactive HTML Dashboard — Pulls create-and-schedule-services data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and returns a standalone interactive HTML dashboard file saved to the output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-and-schedule-services
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
      "description": "Name of the HTML file to produce, e.g. dashboard-create-and-schedule-services-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the generated file, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_and_schedule_services_agent.py` and embedded as the fenced Python below (sha256 358919fbd05922ce…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_and_schedule_services_agent.py` first:

```bash
python3 dashboard_create_and_schedule_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_and_schedule_services_agent.py   # or on stdin
python3 dashboard_create_and_schedule_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and schedule services Interactive HTML Dashboard — Pulls create-and-schedule-services data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and returns a standalone interactive HTML dashboard file saved to the output folder.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-and-schedule-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_and_schedule_services',
    "version": '3.0.3',
    "display_name": 'Create and schedule services Interactive HTML Dashboard',
    "description": 'Pulls create-and-schedule-services data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and returns a standalone interactive HTML dashboard file saved to the output folder.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-create-and-schedule-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-and-schedule-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa6a76e9f0f09500',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-schedule-services'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-create-and-schedule-services', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-create-and-schedule-services-2026-05-24.html.', 'output_folder': 'Destination folder for the generated file, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of create and schedule services with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull create and schedule services data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-create-and-schedule-services-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing create and schedule services.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls create-and-schedule-services data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and returns a standalone interactive HTML dashboard file saved to the output folder.', 'example_request': 'Build me an interactive HTML dashboard of create and schedule services for USMF, latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-create-and-schedule-services-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the generated file, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable, self-contained HTML dashboard of create and schedule services data that a viewer can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardCreateAndScheduleServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateAndScheduleServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-create-and-schedule-services-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the generated file, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardCreateAndScheduleServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

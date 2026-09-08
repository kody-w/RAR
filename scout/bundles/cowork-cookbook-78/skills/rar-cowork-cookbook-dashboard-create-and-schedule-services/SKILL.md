---
name: "rar-cowork-cookbook-dashboard-create-and-schedule-services"
description: "Pulls create-and-schedule-services data from Dynamics 365 F&SCM (read-only) for a legal entity and fiscal period, and returns a standalone interactive HTML dashboard file saved to the output folder."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_and_schedule_services", "rar_sha256": "358919fbd05922cebcd58535c8c94c5848cd9f22db0db522c09be42f78cc53e3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

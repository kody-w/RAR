---
name: "rar-cowork-cookbook-dashboard-create-and-track-tasks-for-a-case"
description: "Pulls case task data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_and_track_tasks_for_a_case", "rar_sha256": "fc6ba7124bd4bf43e1f977764d9b7cfeeb7998a73ef73920cb20695acffd0c74", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_create_and_track_tasks_for_a_case`. The original RAPP
agent is preserved byte-for-byte in `dashboard_create_and_track_tasks_for_a_case_agent.py` and in the RCI capsule.

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

Create and track tasks for a case Interactive HTML Dashboard — Pulls case task data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-and-track-tasks-for-a-case
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
      "description": "Reporting period; defaults to the most recent fiscal period available.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query; defaults to USMF.",
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
      "description": "Name of the HTML file to write, e.g. dashboard-create-and-track-tasks-for-a-case-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the saved file, typically Documents/Cowork/output/ in OneDrive.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_create_and_track_tasks_for_a_case_agent.py` and embedded as the fenced Python below (sha256 fc6ba7124bd4bf43…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_create_and_track_tasks_for_a_case_agent.py` first:

```bash
python3 dashboard_create_and_track_tasks_for_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_create_and_track_tasks_for_a_case_agent.py   # or on stdin
python3 dashboard_create_and_track_tasks_for_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create and track tasks for a case Interactive HTML Dashboard — Pulls case task data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-create-and-track-tasks-for-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_create_and_track_tasks_for_a_case',
    "version": '3.0.3',
    "display_name": 'Create and track tasks for a case Interactive HTML Dashboard',
    "description": 'Pulls case task data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file, read-only.',
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
        "upstream_slug": 'dashboard-create-and-track-tasks-for-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-create-and-track-tasks-for-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3d8b4bf5b3c04f67',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/create-and-track-tasks-for-a-case'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-create-and-track-tasks-for-a-case', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-create-and-track-tasks-for-a-case-2026-05-24.html.', 'output_folder': 'Destination folder for the saved file, typically Documents/Cowork/output/ in OneDrive.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of create and track tasks for a case with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull create and track tasks for a case data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-create-and-track-tasks-for-a-case-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing create and track tasks for a case.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls case task data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file, read-only.', 'example_request': 'Build the case task dashboard from USMF for the latest fiscal period and save the HTML to my Cowork output folder.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-create-and-track-tasks-for-a-case-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the saved file, typically Documents/Cowork/output/ in OneDrive.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a browser-viewable dashboard of create-and-track-tasks-for-a-case D365 data that viewers can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardCreateAndTrackTasksForACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardCreateAndTrackTasksForACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-create-and-track-tasks-for-a-case-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the saved file, typically Documents/Cowork/output/ in OneDrive.', 'type': 'string'}},
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
    print(DashboardCreateAndTrackTasksForACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916eZPi1pbnV2GyI8Z2U5VaAEnUixcxWpAAIaENLbgcZe37gnbh8XefK8isst+r193umb+GqkxAuvfs53fOyavfXuyujcr65dOL6tvFgrOzLI78emEX3oIuh7JOwVuZOuBn4ZZFW8dO15Z18/LhxfMbt46rNi4LsF3qsqxZuHbjL1q7SRee3dqLoC7zBTMVdh67zWKFbRbs/1RpYfFj5od2tvCLNm6nxUUV2J8WQVkv2shf5GXTLmrfBTcXQdy4YF3l13HpLfrYfqx4k4uZ6e0UaVFlXRgXD5Ebu/ebhb1oWvDNzsrCX8RF69e228a9v9hrwglI1kROadceIJ/5HwAv2/tYFtn0CpTyRzuvMr95+fTzLx9eYvD55dNvL25mN+DSC/O+lQabWp8sPA2QTjWgcMOWNUkD9QGRzC5CsLqagGkL8B3ID7TLwSXPDxZv335s/Cz4sPj3f08Huw6bnz59LhZvr88v8z+lKx7qtqXdtL4HbFvZTpwBi70uyGywpwaI3nZ18VS4jovw9bnzG6WyWvx9vvfjk8lr6Lc/fn4pgQj27LfPLz8tgNk/v9Td/Pl1plL9+NNrVg5+/eNP3+g0nZP4bjsTA1K/fnn7/kYWLPy2NA4WX1RpR7/xAp6MKx8Q/4N+8+sp+hu5N5N8eS7+saw+LL5Pedbn70DeZ+w5gO73yQIbgJ0vr0kZFz++8ajL3i/swvV//OlfkXUj302zuGn/S3R/fhKOQPwAa72Z5KcPD/f9sli+6faV5r9mW4GA+SuagOXv7L4a6l/Rfnj2H0hncQGy5N2X3yX3vQ3Lvy9+/pe6/UcbPiyCzy+Mn4EUrG0n8z8tfnuEyM8/eN8u/vDL74D0f0pGLbvafVD4kttFHPhN++XLzz80j8s//PLzD10Foti38y9dnX2P5vfs+uDzJwu+rfrxz3sB/0uRFuVQLL7m0OK3svof9e+vC93OYu/b9ebT4o+ZOL+Wi1mJd6ZPE/whGxsg6x/s+NPL7wCBCqBN5z5uA/z4t39bCLFbl00ZtAvVLTsAlR1A0dyfhdeiuFmA/zNq1D6waxMDw76tA/E/e3iWuAwWv/4v94GiH903dIe+wuIX9wFuXwCCfmlnePsyA3rzBWToF/vLjPC/vi40wKKsY4C7AJ8VUpI+F3Y4QzZgX9V+49c9gCxnav2PYN/H+QNA4sWvf4HLlwfB12r69QHt8RMNFfowI2HTZf7rrLMR+cWbhi4oYP7oux3glZVz4ZgBvpkRvikzAP/tbJ8mjbNs4cUAa0Ahmx60gQ0/zcR+/fVXBwj4uXhC92rxrHANBBZ8FWfx8SPQMMjiMGo/F74blYsffvv9h8X/XvxHux7EZx4SKCVvHgISHtWzuAAZ1+VgGXAecDeAk4eHfvv9zc6ATAFKMvBnHMT+czOI2NT33o2u7smP6AZbOD4wHzB0XpV1C+rBIm5fF4dg8VVewHS+NVeMaK6znl/5hecX7gSo2kCdr5YsyhZU0zZugunDopurOuD6q1PbDxFzkPp2++tCoCVQn8oM/JrFfCwCm8siBub/GhLP64BI/UOzoN5JvC7EOUYXlV3bVVTbbzwC++kXUJfetwPi9qLwh8/FXJD92VSPhHmaBywClnHfXPpx9jloVXKADl7zzvuxxp6rqPaopvXnonlLBrueXeGC4gCYhl3szSXib28h1URll3kP+/nP9uTNC96bVx4x+OwGHpH0COVHB9Q8Ohr72RId/rEJ+dpJLD53KIysF/8/9E+zLUiOU3Ycqe2YxU7UFOvpo7l1nAV6dpuz0E9x4+YPbc07dL0j+Ocii0HA1dPfnisfnn1b80TFrgaOUEjlQR+EFfDRTPcR9XMU1/WcL/bn4r1UfAC6PXAROB5ABEihOXLfGc533yWNgJbz929twyNKgNbAMiCyF1XnZCDqAt/3nIfPo9kQ7+4sZtOBLB6i2I3+pNXsNRBpgP4CCBGDXATl5PUrfD/vvov+p43P7mje8ugcO5C49YMAkMOfBZw9OMQtwC+7fXbqQM9PDyJAjbxqZ90dkDpA0+dFv/ZvXdzE7QyTT7v6FUDrj/P7U9P5qj9WIFuAsUBOVB2w7iOLZoDJQe8DZABAAqIkjwvQCwCjvBnhQdDOZ0gAkPvWrD4pPi6/KeQ/Um8uYu8bZ0XmPXNf8EwCu5j+iBza98IE0MvnFQ++/xhpX7nNtGf0bAACAo7vd58NxOuzB3g2GYt3up/+aRT68a9NS4+qfvlzAHxaRG1bNZ8g6FmJ3wvxK8Au6Clr860of3yWy4+A08cHxnx8YMyjuNofZ9j4E4un9p8Wf03MP5F4S5NPC+QVfoXnW6e3MHt7AavQHynr43q++7lQ/G8gC9iXOYiz2YcT6AK+VsT3JaAshjXAMLD4WSGbubAOoJY/SgJwyOfij3E/5x2oOEU4x2lT/gEPHq0ByIGn/75WLnCraAFvb24vQ38e7R5ZAuazTwWA2g8vAFT9//pINxepfI7xZp4HQTYBTG1j//HtARljO3/880x8fnyws9cF4wN4ypo/xuFbaZlL6x/S5akr0NEFHD7MVQCgAAhRoOvMfE6199oy69RO1azEc/qb+8Un4n95Iv4/S6T4753Bc8XfQOIGdpcBA7blf1I+7B6oMGfkdxk/KtKXZ0X6Z76PWvOnogXY3Tp/xvY/SjCXsu+S/9ok/zNtA3Qi816v/DQX5Q9vWAfewWDzYfF1RgHWfJsaH4N+0YGB/Od5Pprd+9gyfwB7wNvXTV//zuH4L798T64HIH6ZQ/EZUP8onTgDHSgEs20f5fMRtUDcAYAT8LD/Gr4u/kKaf0RhFPsIbz6i69eozbPvW+tNqjIDJeI73vBn8H5OL88132DQnvv2Z2EHZN8ymCndZ4MKPeEDejKA5vbqXPhMDbLsO4IASR71BVTp2dTffPjNkuVj7JxlBpZvn38l+e0FZJo9N0BvufY2t4DlAI4/NnNnBgFUAgzB9yd+gHv/NxPNG6kmskEbDWgFLubYOIKuHW/tBOuVjwRbHMextbd1cBfUfAffbgkbX/kBvtqisOugMLbd2G4QeLCLrwG9JyB9mTvReBZvlg1YBbjV97/dBpe8N72eesxG+zpAzfq/qffbi4Otwcr9ujmQzxcNbREHAzJOV3N5x/wSl6mT0O3ZxnBzenXbcmw+9bLD7dO9qjGUHO/tewcn6E0sdHgMjuaOJffxUcrp4OjBG31rIeLFOZkpKgucyuM3GPPObdAXdLlJWgHXboapLvds6EbaHSfU7up5V4OvLt3uuCK61Kf6YpdDE8HeeAhH1tsNvCacEyIXWXWQ8CWCL4/wxPNCgqoAh8jpjo6aqHMFNybOKGG5maB3L4i35tLf44QWwnHX75LDmYTudZBEkLiqD+pSrzHTutGDeQu08RLfmbvgrxXejuhGQTCJO1grI4HjdpR7xS+uKH+kK8NyJ+K6xZC7QI1Zd3ZYLLPimhE9hAE2GpKze7TNhDJcR/W2+2rvbDG3N6u7J+1vymnEgtUehWHFtXZsEMqORVgVUevH2NAEBy4tzRlZbkveg/jUxJPJyytJjd0ji2GBvdmnUY2qO+siRZvUrciCQj3BTPuEM/mrIBKHFs8Pxyk/+GjWQvvYpfN7cFC2ptvANHJpDp0eWKbdTZ0Jxjv9nigrdTspOnI/oVa2VGVKRxm+gInTaCn8rs+yA0dvHSTPNdIux+OVKyuntaMexZsIV3WnzFGSFKMkI1bCRUFlp9fw6S4lRmadL0OqXRnFjVX+fCQrbXBPaRYmvYfulk5dbMzUPpWly22GkQloSDVP9lY4nWR0VKSNWkH85dDcaRN1k8NlcpLRvAr9Kj9tWWqp8Wogw/FtOgq0XCOyWdl7AjQc/YFZ7yxudzXu9FlQkmIVSONpEMXzht1p8T7p+Ea/rxFjw4Y23ZPpWTmOzFLcjo4ssB3BohA7jfKNugiOczm2t4FuGXkVHr0W1e3NruIF0IefO1a3785d1KsTtsMPl/VmDdGXCrlu7pGB5TcKQo/DqUasnmShtXKjj+u6PRgyetrH+jWVZIjnKuKaWZtVrt7tq1ZMAXZt8Z2+6aprojpZuka2Sa4mp72c09Jx/uFOk9RrezaCSt7v3DuI6hwbVUEh7rv95EnHFBpAciV6ZwXH/YEA2aYt6Y7Aj6tjZqmBb8iGwVatxdppd0MsZ2fmFcqpV0TAR0k3bqMy0qU07pzT4dikRlLuTeMoX2C7cc5ObvaQE7N6llV55WvbJgq33i3EVrvGrdgo88bkdmEU/gpT5gWLBWGL4OYSB8NH5CQtrNrunYUYs5quLnvoVdcR7pGMe6mDSSrfjGK/bJGKtbAuUeNlh5TN6ZrdjZhoMdfemchKPJ5WIMHg+DIxKKMdoesG5iwQkCvPR+xiI0xqVanqFm22SHs4FNcarZVKXxN3J2kAvFnXawahwz0sLe7qiIigUESwVCXZVCxbSI1LZ91UaQUpQgT3GMsqE1vAarVpanGjI2Q9JYk80phILU1i39z9npzEjg3Y6Xrs0Y3l9vvlUedbXB3RalJxneATnI/yta+KayJs1CyWTjvmvI8ZFgk4BFch30j5+KJ08R5Jd/u6C3ZdLmXI2vCjGlpJAiwCjLvzo+bK+xQy3cNBqzfKMtxJUZjftNBJXH24dEEzQMxhQEfGiMbDLcswR+ZZNoqkg4MvdTfELUOp6rQc4jhUqDhda3wAkjqjhuCO5h3CXRWKEogeTvnzrfCwnmo4IyPF+3LVJ3Hj1Wi63avnk8jz1JbQ2mUs1/u7zzBbmlAG7a4lt30GLXetyG0uMWK4wdQz6JFIjfyIKppMXDdlJHSDeidImleGS54ECairWbHarbWzV6qrNGxgd7/uTGlIm0PoXNG0Ra6STDNDzK0PaDlcu4gK4ZvFifgWusZlyYXDBVJJyFEPXVVQoSGiDb0fdjjnsdWhIpTTmejs/qCFakYf3JjeZJfwFMJCCDdxsxwHYx/6CkI3obrrm+AGl/HS9NtCrWJLtKzLhWkDr7azbbQ1ThTWrGVSd3NyB6rC0hrMi3IT1EsjSqsOD7h6u/R7XppSIdtbx+VJqJBdxtXF6uLqtwY+R8M4VHf43i6FQuKMU2i68DmPOG6HSoO57nq2AT8ERBwRou2hXGvU5j6pGSM2EJGfBPbgUlQbycdBQOoTUaajlw2dfN8e0iNRnGFuI0c3vltplA5wQcErmiNQxVqP+aVzESKpTjs7dUgyOKxpibeYmtoB1E1hnRVz4AX+LLq43h0tZ1MbVHaQ0OQAllWhdJ6G/Sky7jnqaMNmTVwHVMudFC0CpajtMVt1gROJU5u1Lb+Cl0SwQ/tzEeE6G1Kqw7TXzI2GnR+IZ53xjVrbLOV0GTFGWOqD3x9tlXD5ZcCj2iYibYtldtNm0pbUTeGP1x4hCm8SR2ady51UZudUSZi42jqqvNygB/NUlSZnbc+9oXdOkK3MQ0oOS9OCwKx96zYTA4cXmfUJphWaPdQMMgVToB2VCYRmBZg/2oxUlCm9Jmtb5C9A0tv1zu83HZKtu0NVOM3pwE9KS/KnhiKL01o06MGnm7heJ9vW3u0JxDvYcGqRyjLYwBeZTzjE4tLbvYB3Z1J2zWtnG32V16D8mXvKPnFk6Rpk0rG4joSNRd44jLL0XK+dq4Cy3B4aC2tq7EPn95p+6DeuHuIscpC3l+k6UTffuzS71MYwSMcOTJ10TmkhvM4wrn9wj+dSpNwe83aK5BfHBN/sigI0iTGv4oi5NOI91qeVhuyugqp2cZ6QdYgIYQYi7uKqsRkl5a5qhyGNmvR0P5QHRzekai9PFkw2Fxbyqq2tenEooQfNKJLGyhO76ASF1dXSSrBtWoLSuRcz0mywjqtW/XW3J3OND3m5IUx4cDdU7q65Dk3hZLc/Stp265n3CjvvzxCTXxwqK1RxY5ObHL0T8ImrdU616RNVhSlcWLF8ZbD9likozqjE82WHXS67KfRqZAc4OFd2iC0I03amftojvaIMsGx1KWEdo/HMIec93B4d/oqgSOJ7GiRejgXT7GhtENKjxdeRzGmQaiuScxFg5uiyt/NN3NbegbbZzZg2q+O9alpVjFzyGMeX4XSIb+lYQTHpyEU/5LvajI7yveMgAeqhSJEKNgrv3vHMV2N80hhIQ5dI7Fc8iawD8pghE0dJylFKqTYjjboKKleQVljBcqGGye01jY7hzhRv4U050GtgCC517f2O9Uf6iJs7FUfFSd1hxFZE+y7AQK3M16nMTMUNABV9k2mDAvULLffqlayZPMSAm9y9xaAqmbjcVcgrD73cnKVnsfWtOZlsPWjskThovX7fbLRMIkkhOd04cRPsV725PpLphKmbkbGOoDjffc28ORGTrkDAhVg1nnTBaNMGK42IEcWNRhy4007ZuupKUqJLuuLVcXM8K6mocNJ0ZpIKXvpBIi4JQBrTfc1zsCPXdTce9IjuhFVLN7ixQVVddb8EA5HH4C6yt9mt1wpwjjfqrWYMz+N63PaULajO2c7EW8XVT4e+53fubS1FBz8nK2PtHwXBYA5UEyhruqyEpL6ImAxLE6Mp/pkL+GRL9je9S5pa3omojG3Hi7Wbets6XZRap1njSg9rA57WYIaClL0Px1fP6pigbSrJsOOzAcUuh8hi5LFrlhJVUkLlVFZPusGvfC2rRhZJmpav5Ht0kWGURbDIsQbnamxAd7knUx679SaHxHoJXaABN7FzuswRPjpOjmwnDnc7wlZclDkV3SuzFvMp8RQ9SXm2JdqQ3ahGeEZqPjXvUh1chkDIOasAWCUenZCUD/VWMeiYxtfJfb/dyqCdYtFhIjcU6en6FJ5pi9rpLaNJeoXKg5Iy/dSVoblsGvpa5hNpnemDsgRzQHUYEfUAI3uBwwZ1d4g4izKLmKz0hDmOMKJZ55IMi7ilh0GWhs4wUAiD+QnjO20sVGhYpg4r3vG6UaA1M53ukhMm7q293NJ2TA693g9qMhgXp2UKW7qsjwbjEGkrZVSwyZowJGytaGKlk8Mx4BuByJWIv+on0L1WQaNLk2hgosqcDtJxV5+UWOuKDAxmaQfbQqz2+NFnKTw4oJ7WusRpfUqpqhTDaDktK8u9enoQCUfBa2IMMfi2PVR+VBHC/bZMagFMn+tgqfTUasUpuX65dFQ9WOmJPJUHMEJkiuYsu2y5rNLkghD6BrWSDkItG1Y0cX1BFY9O1+oNBkiu9qa49VVLQ1W2Kb2RVCAxPIprG49KsWkL665pgYIbF2Laa+LqeELKO8dSykF0BT7zDv0EjcS5SRu01B0zrwm+q/dNK7I6C4sBLUWwy3MjEqEsnSo7zjSxfWD6mCbT4THw91uR4qEgkdwTOVGiXws9rIurcLlJ6MzCk8pCDeEc+o2RQVYdZNlOT3lOVxCYVeTTlYwFr7ryTKJEdheKuki7zMHJbJ2k7dJlEoK5OOuaBe+SVgw9LS4LWYfvN1MsWGjQMI4vc3tfV8xFwQfMlajyHq8Pku6m+6t/g7QSLLjqHCzAm3bYk17q8V6qS5Z1ZznsttvIRoveaBCLXnKl7BSV/OacQGBwW9bIFr8yjlJLoIW+GfR6smukL6rAYFZun0+rDL924qVljHF7W28TopW6VpVFFwunPrikGHm/CrrtpTZ+GEJ5umumsmKQQ2EVoMmtytZBtZXGRBp6N31vOZhJ0Ji3mpVwQhTtUWlzCmPr8D5qe5mmZBA2E6dfQN2MO+V2alTQX1SxHx0ulOswGFJs9+w63VAQsT2GgT9c835p3kEW1vkGg8jWhUiPOLPozc/R3dbLV5lB3QRmGExGjfc7bJOoDHKiCq6jIGjbBoQlxTxcHzpIM4N1FxipvMLcGG7tbdfvVR2kLY75G95J0ytJ+ILiF5kg2ikDlXB4J6qbqFSty2/o9XlgbhdRlHZHMNiRbhorkwn60+2xEKIQrUr9JJlntESPW+syQbhz8cWM1+uyEPvwXoi+tYaUY7IM0b3q+5A16Z1nd3hmB4WHyqFqyTd8v3S3dXUaYTxOGBQKEWhoTw0mA7DDNwJs3gySjqHdxhlPy5tF1XgX3AsAWpEr+hBLZwxox5Wp3RM2C51OGOx11vxXdpHKSCGmWKJjIo/AhpPWbPvYyuMqEmvzcoiJyswiHb/esrpcmps6Y5Az39AA7k10vfZRb5LM7iIZghWRd8ho0OBsSiNl0mvvYGDjAbFU1kK58TStrlBZ7YOQU9SKKjlBgIe+P3a8IfPLiFuWOL0bvLNlK5uGtshcTCLGGUHgcY1yXi55K2sMAu/W3J3EwqbQz3S+di4xTlw00FsH2u2qSfJ+SoxTKpWMx8QaeoKPVNOeKZybMqeQBtVq9921vaD7JTZsMhctnaSqx4zAFA32lgGTmcVw1729W226kyGuTqg9Yblyr+++B5cT0crnLbnaGqyvBWMJPCF6BIogG+3oGKLfDxuL9w9CnTXMnb24PdWhkagba0GgHKOP4STv6qy/Wx7aIGyEYKSTF6INy6aZ6zus3F8ExLA3u8uI6iJmHiw7QgUw6WOnY4SdzROTnFekFfMACwTJ7luOupJQkmwMyxxLWp72knU+C7fuJuJcCOSb4ng7xKuGtK+eCQaKsfBzUYWge1NVW7f1tgR211cVO91xmNiileOuvS5MdaGXrvcIwaXUCJPIToR6o9+G7Vjcz7y9vG172sqZbImJfXClnMsARAWQdTyjvbq+d75vUHECZ8vSXq+rhrQI/ZpvIB3FSw+pdKdRyrVSt5o0podNeV7jjIKbAJHhE75vx+yE1AQUps7IHUAfb6TmJb252LBqsLUX0YJaLG/XLbo/lBUk6WNI8ePptlpNmprzIk/ccNKJtuJJ0emEw+EdfzL1JZuTZaqK3qqlxLUaq/Y1P42hN4xHHL4icbPyzHUljnBBRB0SVv0Npa/YLWq0nGq18zW466Yw+pMnObJWnvDorAj7XbxDzjSNGxDF4B7oh06dk/Ry6Y45BzfQDqL3e5yjYcdQlrl+xAQRlNCbryrbyqezU14r18jT1LgywbyHu22m0YaIOHbLsA4GDZmYVhXHjyNDCC56DZhra1lgCryuHaq2DGqoiA7mbN8nMMQSWpexs/PY7eD+Bos5u7OQ3J/Y/m426KAuMQWX0Sk1ZKjWKJaipxWiuuyGJ+i4Ki+TeOhUVKxVeHfEqfPad9Ge3UgBSDgL6Vt/zbXnvkri6C7nnoGIWLDWu4101vw+t0gOWqpCLXq1BscwodzkfVm4BFm05HjbjKB04lsYSsc9BymFX8hbIrpeTlFTHJjeqWNIP9cTHuB55m4Uj1NjZkSCzO3gZNh3JiJ4MIMwjYHXlz0IhAa94ANxQA6wZNA0hI+tnkO86cdV65zQ053ciOjKQQ0EHzbEnaEcOFW5TcjRlXDlkFUNNTDj2Pip6ChjiUoyOR64ztc7CoxK577dXZitDOZm0j0n3FpKO9SpveJcM9VlT4NGjahELbbviVacTK9OziE+CN5WuTKoLa5Nltw2wqnQPW21QwjsuL20FVaDYrd1JZ6Gxg49yjhOlHimX+wj5LiMyI2xR4M0ygfimHPOVLIrZ9Tdkb14GYzU7q2ToUuXdMpE8OGy3ED8dPT8Wq8pdi168VWfuhW3DbApx2jfKdYtmlncfcxDMekDnGAGYqSu280m3ZTdvUXWKHFfrjQ2gEAvAqK2aGm5JE+XuthWVXjDSJ6ZdMUj00viwX7PhOVt7ePjbUgP+6ShpCmX7zbFywgvVrjPnnxyOtWok2srZuO2u3Pf3fdOsqd0CNvgjby+dOW2x6N81TWGJ0pukZlNidur8dwHajdtMynW6Lu/zC6UNd7lqZyw/TI4+cAlyRLy/IN2RyaKwOPtMbjCFJhgytFDpliElkeY4ElnJ5yPjGJmdryE4WGDQwMjnHUAk6lAkuTf//4yn8O+Hwi+/HceeZsPiP6fnUU9j5TeH2N5HHr6tvfpwevTf0u6Xz681G4MZHuewjVZF74dYv3DGdzHv3CyOROans+WvR+oP0/qWzucn8d+iQuva9p6+tKU2ePRFrDD6Zr52c1mfrzXBe9/PMv9yns+0J3lb8svj0cB3zc/Hm3KfS8Ggr19Dd9OKMHut8euvqywzRe/rmal356JALquXuHX1cvv/weYuB3PQC8AAA== -->

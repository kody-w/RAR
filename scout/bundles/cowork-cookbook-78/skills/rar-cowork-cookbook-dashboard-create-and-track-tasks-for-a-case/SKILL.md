---
name: "rar-cowork-cookbook-dashboard-create-and-track-tasks-for-a-case"
description: "Pulls case task data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period via the Cowork D365 ERP plugin and saves a standalone interactive HTML dashboard file, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_create_and_track_tasks_for_a_case", "rar_sha256": "fc6ba7124bd4bf43e1f977764d9b7cfeeb7998a73ef73920cb20695acffd0c74", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-dashboard-assign-a-case"
description: "Pulls assign-a-case data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_assign_a_case", "rar_sha256": "55615b862f4a5a6eb581ff191d490e98e682e8e12f1c7dbec5fa18987999c65f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_assign_a_case`. The original RAPP
agent is preserved byte-for-byte in `dashboard_assign_a_case_agent.py` and in the RCI capsule.

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

Assign a case Interactive HTML Dashboard — Pulls assign-a-case data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-a-case
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
      "description": "Name of the generated HTML file, e.g. dashboard-assign-a-case-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the HTML file, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_assign_a_case_agent.py` and embedded as the fenced Python below (sha256 55615b862f4a5a6e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_assign_a_case_agent.py` first:

```bash
python3 dashboard_assign_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_assign_a_case_agent.py   # or on stdin
python3 dashboard_assign_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assign a case Interactive HTML Dashboard — Pulls assign-a-case data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_assign_a_case',
    "version": '3.0.3',
    "display_name": 'Assign a case Interactive HTML Dashboard',
    "description": 'Pulls assign-a-case data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.',
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
        "upstream_slug": 'dashboard-assign-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-assign-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16c32df7789ca745',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/assign-a-case'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-assign-a-case', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-assign-a-case-2026-05-24.html.', 'output_folder': 'Destination folder for the HTML file, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of assign a case with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull assign a case data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-assign-a-case-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing assign a case.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls assign-a-case data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only.', 'example_request': 'Build me an interactive HTML dashboard for assign a case from USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-assign-a-case-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the HTML file, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of assign-a-case D365 data that a viewer can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardAssignACase(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAssignACase'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-assign-a-case-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the HTML file, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardAssignACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

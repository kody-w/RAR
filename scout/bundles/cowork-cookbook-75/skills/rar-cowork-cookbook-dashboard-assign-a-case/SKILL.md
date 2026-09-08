---
name: "rar-cowork-cookbook-dashboard-assign-a-case"
description: "Pulls assign-a-case data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_assign_a_case", "rar_sha256": "55615b862f4a5a6eb581ff191d490e98e682e8e12f1c7dbec5fa18987999c65f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-dashboard-define-case-types-and-policies"
description: "Pulls define case types and policies data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and writes a standalone interactive HTML dashboard to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_case_types_and_policies", "rar_sha256": "71ef40d7effd37f8bfad0afc5f5695bc616d0359a17a5359fc977f7007fd3e97", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_case_types_and_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_case_types_and_policies_agent.py` and in the RCI capsule.

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

Define case types and policies Interactive HTML Dashboard — Pulls define case types and policies data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and writes a standalone interactive HTML dashboard to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-case-types-and-policies
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
      "description": "Name of the HTML file to write, e.g. dashboard-define-case-types-and-policies-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the saved HTML, typically Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_case_types_and_policies_agent.py` and embedded as the fenced Python below (sha256 71ef40d7effd37f8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_case_types_and_policies_agent.py` first:

```bash
python3 dashboard_define_case_types_and_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_case_types_and_policies_agent.py   # or on stdin
python3 dashboard_define_case_types_and_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define case types and policies Interactive HTML Dashboard — Pulls define case types and policies data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and writes a standalone interactive HTML dashboard to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-case-types-and-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_case_types_and_policies',
    "version": '3.0.3',
    "display_name": 'Define case types and policies Interactive HTML Dashboard',
    "description": 'Pulls define case types and policies data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and writes a standalone interactive HTML dashboard to the output folder; read-only.',
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
        "upstream_slug": 'dashboard-define-case-types-and-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-case-types-and-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd7c417d9526f3dfa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-case-types-and-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-define-case-types-and-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-define-case-types-and-policies-2026-05-24.html.', 'output_folder': 'Destination folder for the saved HTML, typically Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of define case types and policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull define case types and policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-define-case-types-and-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing define case types and policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls define case types and policies data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and writes a standalone interactive HTML dashboard to the output folder; read-only.', 'example_request': 'Build an interactive HTML dashboard of case types and policies from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-define-case-types-and-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the saved HTML, typically Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a browser-viewable dashboard of case types and policies data from D365 that recipients can open without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDefineCaseTypesAndPolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineCaseTypesAndPolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-define-case-types-and-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the saved HTML, typically Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDefineCaseTypesAndPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

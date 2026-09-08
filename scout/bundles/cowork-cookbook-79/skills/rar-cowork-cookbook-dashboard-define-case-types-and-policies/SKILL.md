---
name: "rar-cowork-cookbook-dashboard-define-case-types-and-policies"
description: "Pulls define case types and policies data for the most recent fiscal period from Dynamics 365 F&SCM via the ERP plugin and writes a standalone interactive HTML dashboard to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_case_types_and_policies", "rar_sha256": "71ef40d7effd37f8bfad0afc5f5695bc616d0359a17a5359fc977f7007fd3e97", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

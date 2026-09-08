---
name: "rar-cowork-cookbook-dashboard-develop-service-policies"
description: "Pulls develop service policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file with totals header, two inline SVG charts, sortable de"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_service_policies", "rar_sha256": "98ae8568890de5f257eb3246a9e7ff7b7b452e3ddb6779da636c342fd324d956", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_develop_service_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_develop_service_policies_agent.py` and in the RCI capsule.

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

Develop service policies Interactive HTML Dashboard — Pulls develop service policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file with totals header, two inline SVG charts, sortable de

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-service-policies
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
      "description": "Name of the HTML file to produce, e.g. dashboard-develop-service-policies-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Folder the HTML file is saved to, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_develop_service_policies_agent.py` and embedded as the fenced Python below (sha256 98ae8568890de5f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_develop_service_policies_agent.py` first:

```bash
python3 dashboard_develop_service_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_develop_service_policies_agent.py   # or on stdin
python3 dashboard_develop_service_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service policies Interactive HTML Dashboard — Pulls develop service policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file with totals header, two inline SVG charts, sortable de

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-develop-service-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_develop_service_policies',
    "version": '3.0.3',
    "display_name": 'Develop service policies Interactive HTML Dashboard',
    "description": 'Pulls develop service policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file with totals header, two inline SVG charts, sortable de',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-develop-service-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-develop-service-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0fd83918b48a883b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-develop-service-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to pull; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to produce, e.g. dashboard-develop-service-policies-2026-05-24.html.', 'output_folder': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of develop service policies with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull develop service policies data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-develop-service-policies-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing develop service policies.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls develop service policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file with totals header, two inline SVG charts, sortable de', 'example_request': 'Build me an interactive HTML dashboard of develop service policies for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to pull; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to produce, e.g. dashboard-develop-service-policies-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of develop service policies data from D365 without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDevelopServicePolicies(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDevelopServicePolicies'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to pull; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to produce, e.g. dashboard-develop-service-policies-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDevelopServicePolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

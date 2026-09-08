---
name: "rar-cowork-cookbook-dashboard-develop-service-policies"
description: "Pulls develop service policies data from Dynamics 365 F&SCM for a legal entity and most recent fiscal period, and writes a standalone interactive HTML dashboard file with totals header, two inline SVG charts, sortable de"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_develop_service_policies", "rar_sha256": "98ae8568890de5f257eb3246a9e7ff7b7b452e3ddb6779da636c342fd324d956", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

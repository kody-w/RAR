---
name: "rar-cowork-cookbook-dashboard-deploy-service-resources"
description: "Pulls deploy service resources data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_deploy_service_resources", "rar_sha256": "d6301071e488eb5512e5ce6c3130988dc170838f73c8eeeb7c14251b05dec3ac", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_deploy_service_resources`. The original RAPP
agent is preserved byte-for-byte in `dashboard_deploy_service_resources_agent.py` and in the RCI capsule.

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

Deploy service resources Interactive HTML Dashboard — Pulls deploy service resources data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder,

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-deploy-service-resources
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
      "description": "Name of the HTML file to write, e.g. dashboard-deploy-service-resources-2026-05-24.html.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_deploy_service_resources_agent.py` and embedded as the fenced Python below (sha256 d6301071e488eb55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_deploy_service_resources_agent.py` first:

```bash
python3 dashboard_deploy_service_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_deploy_service_resources_agent.py   # or on stdin
python3 dashboard_deploy_service_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Deploy service resources Interactive HTML Dashboard — Pulls deploy service resources data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder,

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-deploy-service-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_deploy_service_resources',
    "version": '3.0.3',
    "display_name": 'Deploy service resources Interactive HTML Dashboard',
    "description": 'Pulls deploy service resources data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder,',
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
        "upstream_slug": 'dashboard-deploy-service-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-deploy-service-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a97778b56df8cc86',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/manage-service-work/deploy-service-resources'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-deploy-service-resources', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Fiscal period to report on; defaults to the most recent available.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the HTML file to write, e.g. dashboard-deploy-service-resources-2026-05-24.html.', 'output_folder': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of deploy service resources with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull deploy service resources data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-deploy-service-resources-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing deploy service resources.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls deploy service resources data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder,', 'example_request': 'Build a deploy service resources HTML dashboard for USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Fiscal period to report on; defaults to the most recent available.', 'name': 'fiscal_period'}, {'description': 'Name of the HTML file to write, e.g. dashboard-deploy-service-resources-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants deploy service resources reported as a self-contained HTML dashboard viewable in a browser without D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardDeployServiceResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDeployServiceResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Fiscal period to report on; defaults to the most recent available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the HTML file to write, e.g. dashboard-deploy-service-resources-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Folder the HTML file is saved to, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardDeployServiceResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

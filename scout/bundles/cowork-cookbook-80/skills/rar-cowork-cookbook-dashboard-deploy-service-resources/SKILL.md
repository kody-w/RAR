---
name: "rar-cowork-cookbook-dashboard-deploy-service-resources"
description: "Pulls deploy service resources data from Dynamics 365 F&SCM for a given legal entity and fiscal period and writes a standalone interactive HTML dashboard (SVG charts, sortable table, RAG indicator) to the output folder,"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_deploy_service_resources", "rar_sha256": "d6301071e488eb5512e5ce6c3130988dc170838f73c8eeeb7c14251b05dec3ac", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

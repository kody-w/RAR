---
name: "rar-cowork-cookbook-dashboard-manage-service-truck-inventory"
description: "Pulls service truck inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_service_truck_inventory", "rar_sha256": "d3c0f532fd640e099a6e0ca7e2e89dce10c9622df7a03e4cd01af91cd3e87d66", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_manage_service_truck_inventory`. The original RAPP
agent is preserved byte-for-byte in `dashboard_manage_service_truck_inventory_agent.py` and in the RCI capsule.

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

Manage service truck inventory Interactive HTML Dashboard — Pulls service truck inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-service-truck-inventory
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
      "description": "D365 legal entity to query; the recipe uses USMF.",
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
      "description": "Name of the generated HTML file, e.g. dashboard-manage-service-truck-inventory-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the saved HTML, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_manage_service_truck_inventory_agent.py` and embedded as the fenced Python below (sha256 d3c0f532fd640e09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_manage_service_truck_inventory_agent.py` first:

```bash
python3 dashboard_manage_service_truck_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_manage_service_truck_inventory_agent.py   # or on stdin
python3 dashboard_manage_service_truck_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage service truck inventory Interactive HTML Dashboard — Pulls service truck inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder; read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-manage-service-truck-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_manage_service_truck_inventory',
    "version": '3.0.3',
    "display_name": 'Manage service truck inventory Interactive HTML Dashboard',
    "description": 'Pulls service truck inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder; read-only.',
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
        "upstream_slug": 'dashboard-manage-service-truck-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-manage-service-truck-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b448f0f90bac62e5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/manage-service-truck-inventory'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/dashboard-manage-service-truck-inventory', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query; the recipe uses USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-manage-service-truck-inventory-2026-05-24.html.', 'output_folder': 'Destination folder for the saved HTML, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of manage service truck inventory with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull manage service truck inventory data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-manage-service-truck-inventory-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing manage service truck inventory.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls service truck inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder; read-only.', 'example_request': 'Build me an interactive HTML dashboard of service truck inventory from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; the recipe uses USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-manage-service-truck-inventory-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the saved HTML, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable dashboard of service truck inventory from D365, without the viewer needing D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardManageServiceTruckInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardManageServiceTruckInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; the recipe uses USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-manage-service-truck-inventory-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the saved HTML, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardManageServiceTruckInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

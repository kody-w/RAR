---
name: "rar-cowork-cookbook-dashboard-manage-service-truck-inventory"
description: "Pulls service truck inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and saves a standalone interactive HTML dashboard file to the output folder; read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_manage_service_truck_inventory", "rar_sha256": "d3c0f532fd640e099a6e0ca7e2e89dce10c9622df7a03e4cd01af91cd3e87d66", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

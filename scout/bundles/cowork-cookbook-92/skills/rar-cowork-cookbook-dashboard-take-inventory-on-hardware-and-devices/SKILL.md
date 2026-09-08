---
name: "rar-cowork-cookbook-dashboard-take-inventory-on-hardware-and-devices"
description: "Pulls hardware and device inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_take_inventory_on_hardware_and_devices", "rar_sha256": "02e824f3ad8c28a6a0450b0b41a1512d6ad17d25916e109ff4771d313d9d0581", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_take_inventory_on_hardware_and_devices`. The original RAPP
agent is preserved byte-for-byte in `dashboard_take_inventory_on_hardware_and_devices_agent.py` and in the RCI capsule.

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

Take inventory on hardware and devices Interactive HTML Dashboard — Pulls hardware and device inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-take-inventory-on-hardware-and-devices
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
      "description": "Name of the generated HTML file, e.g. dashboard-take-inventory-on-hardware-and-devices-2026-05-24.html.",
      "type": "string"
    },
    "output_folder": {
      "description": "Destination folder for the HTML file, e.g. Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_take_inventory_on_hardware_and_devices_agent.py` and embedded as the fenced Python below (sha256 02e824f3ad8c28a6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_take_inventory_on_hardware_and_devices_agent.py` first:

```bash
python3 dashboard_take_inventory_on_hardware_and_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_take_inventory_on_hardware_and_devices_agent.py   # or on stdin
python3 dashboard_take_inventory_on_hardware_and_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Take inventory on hardware and devices Interactive HTML Dashboard — Pulls hardware and device inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.

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
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-take-inventory-on-hardware-and-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_take_inventory_on_hardware_and_devices',
    "version": '3.0.3',
    "display_name": 'Take inventory on hardware and devices Interactive HTML Dashboard',
    "description": 'Pulls hardware and device inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-take-inventory-on-hardware-and-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-take-inventory-on-hardware-and-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a08ed27df9f647dc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/take-inventory-on-hardware-and-devices'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-take-inventory-on-hardware-and-devices', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'fiscal_period': 'Reporting period; defaults to the most recent fiscal period available.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'output_filename': 'Name of the generated HTML file, e.g. dashboard-take-inventory-on-hardware-and-devices-2026-05-24.html.', 'output_folder': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Lets ops leadership share a live-looking view of take inventory on hardware and devices with executives and customers without granting D365 logins.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, pull take inventory on hardware and devices data for the most recent fiscal period available. Produce a standalone HTML file 'dashboard-take-inventory-on-hardware-and-devices-2026-05-24.html' that renders an interactive dashboard with: (a) a header with totals and 'data refreshed at' timestamp, (b) at least two inline SVG charts (bar, donut, or trend), (c) a sortable detail table beneath, (d) a colour-coded RAG indicator. Save the HTML to the output folder. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Builds a single-file HTML dashboard with inline SVG/d3 charts visualizing take inventory on hardware and devices.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Pulls hardware and device inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only.', 'example_request': 'Build me an interactive HTML dashboard of hardware and device inventory from D365 USMF for the latest fiscal period.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'name': 'fiscal_period'}, {'description': 'Name of the generated HTML file, e.g. dashboard-take-inventory-on-hardware-and-devices-2026-05-24.html.', 'name': 'output_filename'}, {'description': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.', 'name': 'output_folder'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a shareable browser-viewable inventory dashboard of hardware/devices from D365 without giving the viewer D365 access.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class DashboardTakeInventoryOnHardwareAndDevices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardTakeInventoryOnHardwareAndDevices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'fiscal_period': {'description': 'Reporting period; defaults to the most recent fiscal period available.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the generated HTML file, e.g. dashboard-take-inventory-on-hardware-and-devices-2026-05-24.html.', 'type': 'string'}, 'output_folder': {'description': 'Destination folder for the HTML file, e.g. Documents/Cowork/output/.', 'type': 'string'}},
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
    print(DashboardTakeInventoryOnHardwareAndDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-dashboard-take-inventory-on-hardware-and-devices"
description: "Pulls hardware and device inventory data from Dynamics 365 F&SCM (legal entity USMF) for the most recent fiscal period and writes a standalone interactive HTML dashboard file to the output folder, read-only."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_take_inventory_on_hardware_and_devices", "rar_sha256": "02e824f3ad8c28a6a0450b0b41a1512d6ad17d25916e109ff4771d313d9d0581", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

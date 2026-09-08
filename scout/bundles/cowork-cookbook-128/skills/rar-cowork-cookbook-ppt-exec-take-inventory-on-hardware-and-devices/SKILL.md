---
name: "rar-cowork-cookbook-ppt-exec-take-inventory-on-hardware-and-devices"
description: "Builds a read-only executive PowerPoint deck on hardware and device inventory from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_take_inventory_on_hardware_and_devices", "rar_sha256": "66fa3ea2bfb45747e8e3e63bd958c12eec5ab5a9d968adc9907397fa166006a2", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_take_inventory_on_hardware_and_devices`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_take_inventory_on_hardware_and_devices_agent.py` and in the RCI capsule.

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

Take inventory on hardware and devices Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on hardware and device inventory from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-take-inventory-on-hardware-and-devices
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
    "legal_entity": {
      "description": "Dynamics 365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the .pptx file to produce, e.g. ppt-exec-take-inventory-on-hardware-and-devices-2026-05-24.pptx.",
      "type": "string"
    },
    "review_period": {
      "description": "Reporting period and prior period for the trend comparison (e.g. monthly review).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_take_inventory_on_hardware_and_devices_agent.py` and embedded as the fenced Python below (sha256 66fa3ea2bfb45747…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_take_inventory_on_hardware_and_devices_agent.py` first:

```bash
python3 ppt_exec_take_inventory_on_hardware_and_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_take_inventory_on_hardware_and_devices_agent.py   # or on stdin
python3 ppt_exec_take_inventory_on_hardware_and_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Take inventory on hardware and devices Executive PowerPoint Deck — Builds a read-only executive PowerPoint deck on hardware and device inventory from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.

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
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-take-inventory-on-hardware-and-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_take_inventory_on_hardware_and_devices',
    "version": '3.0.3',
    "display_name": 'Take inventory on hardware and devices Executive PowerPoint Deck',
    "description": 'Builds a read-only executive PowerPoint deck on hardware and device inventory from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-take-inventory-on-hardware-and-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-take-inventory-on-hardware-and-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9a0ccdf00f2c6264',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/take-inventory-on-hardware-and-devices'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/ppt-exec-take-inventory-on-hardware-and-devices', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the .pptx file to produce, e.g. ppt-exec-take-inventory-on-hardware-and-devices-2026-05-24.pptx.', 'review_period': 'Reporting period and prior period for the trend comparison (e.g. monthly review).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Cuts deck prep time from hours to minutes for take inventory on hardware and devices reviews while ensuring the numbers in the slides match D365 to the cent.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build an executive PowerPoint deck on take inventory on hardware and devices for a 15-minute monthly review. Produce 'ppt-exec-take-inventory-on-hardware-and-devices-2026-05-24.pptx' with: (1) title slide, (2) headline KPIs, (3) trend chart vs prior period, (4) top issues / red flags, (5) recommended actions, (6) appendix - data sources and methodology. Include speaker-notes on each slide with talking points. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads take inventory on hardware and devices data and produces a 6-8 slide PowerPoint suitable for an executive review.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only executive PowerPoint deck on hardware and device inventory from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes.', 'example_request': "Build the exec PowerPoint on hardware and device inventory for USMF for this month's 15-minute review.", 'inputs': [{'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review).', 'name': 'review_period'}, {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-take-inventory-on-hardware-and-devices-2026-05-24.pptx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user needs an executive-ready hardware/device inventory deck from D365 ERP data for a short monthly review; requires the Cowork D365 ERP plugin.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PptExecTakeInventoryOnHardwareAndDevices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecTakeInventoryOnHardwareAndDevices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the .pptx file to produce, e.g. ppt-exec-take-inventory-on-hardware-and-devices-2026-05-24.pptx.', 'type': 'string'}, 'review_period': {'description': 'Reporting period and prior period for the trend comparison (e.g. monthly review).', 'type': 'string'}},
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
    print(PptExecTakeInventoryOnHardwareAndDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

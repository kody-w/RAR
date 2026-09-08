---
name: "rar-cowork-cookbook-ppt-exec-take-inventory-on-hardware-and-devices"
description: "Builds a read-only executive PowerPoint deck on hardware and device inventory from Dynamics 365 F&SCM data for a given legal entity, with KPI, trend, red-flag, action and appendix slides plus speaker notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_take_inventory_on_hardware_and_devices", "rar_sha256": "66fa3ea2bfb45747e8e3e63bd958c12eec5ab5a9d968adc9907397fa166006a2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

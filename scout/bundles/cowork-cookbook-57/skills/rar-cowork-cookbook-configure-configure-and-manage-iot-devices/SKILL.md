---
name: "rar-cowork-cookbook-configure-configure-and-manage-iot-devices"
description: "Applies a bulk IoT device configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_manage_iot_devices", "rar_sha256": "6f2036c96e562ffc1213692f66060ee68a35652811bc4dae58d9682819e0368e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_configure_and_manage_iot_devices`. The original RAPP
agent is preserved byte-for-byte in `configure_configure_and_manage_iot_devices_agent.py` and in the RCI capsule.

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

Configure and manage IoT devices Configuration Bulk Setup — Applies a bulk IoT device configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/aft

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-manage-iot-devices
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
    "approval": {
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per IoT device target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_configure_and_manage_iot_devices_agent.py` and embedded as the fenced Python below (sha256 6f2036c96e562ffc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_configure_and_manage_iot_devices_agent.py` first:

```bash
python3 configure_configure_and_manage_iot_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_configure_and_manage_iot_devices_agent.py   # or on stdin
python3 configure_configure_and_manage_iot_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage IoT devices Configuration Bulk Setup — Applies a bulk IoT device configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/aft

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-configure-and-manage-iot-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_configure_and_manage_iot_devices',
    "version": '3.0.3',
    "display_name": 'Configure and manage IoT devices Configuration Bulk Setup',
    "description": 'Applies a bulk IoT device configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/aft',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-configure-and-manage-iot-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-configure-and-manage-iot-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4260c47341eab79',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-iot-devices'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-configure-and-manage-iot-devices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per IoT device target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for configure and manage IoT devices, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per configure and manage IoT devices target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk IoT device configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/aft', 'example_request': 'Bulk-update our IoT device configs in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per IoT device target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update IoT device configuration records in D365 F&SCM from a spreadsheet, with row validation and an approval gate before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureConfigureAndManageIotDevices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureConfigureAndManageIotDevices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per IoT device target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureConfigureAndManageIotDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

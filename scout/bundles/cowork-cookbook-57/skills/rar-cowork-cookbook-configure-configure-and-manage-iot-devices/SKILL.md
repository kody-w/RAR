---
name: "rar-cowork-cookbook-configure-configure-and-manage-iot-devices"
description: "Applies a bulk IoT device configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/aft"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_configure_and_manage_iot_devices", "rar_sha256": "6f2036c96e562ffc1213692f66060ee68a35652811bc4dae58d9682819e0368e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

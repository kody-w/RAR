---
name: "rar-cowork-cookbook-bulk-update-configure-and-manage-iot-devices"
description: "Applies a bulk field update to IoT device records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_manage_iot_devices", "rar_sha256": "6e151e51a334277f5bb2428ed1433a68f188d7e84acb2065c243893ef787016f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_configure_and_manage_iot_devices`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_configure_and_manage_iot_devices_agent.py` and in the RCI capsule.

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

Configure and manage IoT devices Bulk Field Update — Applies a bulk field update to IoT device records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-iot-devices
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are written.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against; USMF sandbox by default.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to each record.",
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
    "record_ids": {
      "description": "List of IoT device record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_configure_and_manage_iot_devices_agent.py` and embedded as the fenced Python below (sha256 6e151e51a334277f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_configure_and_manage_iot_devices_agent.py` first:

```bash
python3 bulk_update_configure_and_manage_iot_devices_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_configure_and_manage_iot_devices_agent.py   # or on stdin
python3 bulk_update_configure_and_manage_iot_devices_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage IoT devices Bulk Field Update — Applies a bulk field update to IoT device records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation workboo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-iot-devices
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_configure_and_manage_iot_devices',
    "version": '3.0.3',
    "display_name": 'Configure and manage IoT devices Bulk Field Update',
    "description": 'Applies a bulk field update to IoT device records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation workboo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-configure-and-manage-iot-devices',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-configure-and-manage-iot-devices',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '60a75231a99df358',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-iot-devices'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-configure-and-manage-iot-devices', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are written.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of IoT device record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when configure and manage IoT devices records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to configure and manage IoT devices records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to IoT device records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation workboo', 'example_request': 'Bulk update the firmware version field on these 40 IoT device IDs in USMF sandbox - show me the dry-run first.', 'inputs': [{'description': 'List of IoT device record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are written.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of IoT device record IDs in a D365 sandbox, with a reviewable preview before commit.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateConfigureAndManageIotDevices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateConfigureAndManageIotDevices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are written.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of IoT device record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateConfigureAndManageIotDevices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

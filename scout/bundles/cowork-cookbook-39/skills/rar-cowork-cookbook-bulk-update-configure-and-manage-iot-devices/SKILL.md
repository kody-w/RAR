---
name: "rar-cowork-cookbook-bulk-update-configure-and-manage-iot-devices"
description: "Applies a bulk field update to IoT device records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook, pausing for approval, then a confirmation workboo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_configure_and_manage_iot_devices", "rar_sha256": "6e151e51a334277f5bb2428ed1433a68f188d7e84acb2065c243893ef787016f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

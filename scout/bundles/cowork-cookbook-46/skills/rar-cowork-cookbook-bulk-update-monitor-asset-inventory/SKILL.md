---
name: "rar-cowork-cookbook-bulk-update-monitor-asset-inventory"
description: "Applies a bulk field update to monitor asset inventory records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_asset_inventory", "rar_sha256": "d81b09732fa9b32358d6540c5f557a7afc99422fdd1c076d2c7889264850f2e4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_asset_inventory`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_asset_inventory_agent.py` and in the RCI capsule.

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

Monitor asset inventory Bulk Field Update — Applies a bulk field update to monitor asset inventory records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-asset-inventory
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
      "description": "Explicit approval after reviewing the dry-run preview workbook, before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against; defaults to USMF sandbox.",
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
      "description": "List of monitor asset inventory record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_asset_inventory_agent.py` and embedded as the fenced Python below (sha256 d81b09732fa9b323…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_asset_inventory_agent.py` first:

```bash
python3 bulk_update_monitor_asset_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_asset_inventory_agent.py   # or on stdin
python3 bulk_update_monitor_asset_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset inventory Bulk Field Update — Applies a bulk field update to monitor asset inventory records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-asset-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_asset_inventory',
    "version": '3.0.3',
    "display_name": 'Monitor asset inventory Bulk Field Update',
    "description": 'Applies a bulk field update to monitor asset inventory records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-asset-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-asset-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd46f9c064122ca0f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-inventory'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-monitor-asset-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of monitor asset inventory record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when monitor asset inventory records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to monitor asset inventory records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to monitor asset inventory records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a', 'example_request': 'Bulk update these monitor asset inventory record IDs in USMF sandbox to the new location value — show me the dry-run first.', 'inputs': [{'description': 'List of monitor asset inventory record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you have a list of monitor asset inventory record IDs and new field values to update in bulk, and want a dry-run preview and approval step before the write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateMonitorAssetInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorAssetInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of monitor asset inventory record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateMonitorAssetInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

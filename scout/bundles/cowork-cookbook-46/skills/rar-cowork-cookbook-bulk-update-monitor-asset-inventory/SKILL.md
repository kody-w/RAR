---
name: "rar-cowork-cookbook-bulk-update-monitor-asset-inventory"
description: "Applies a bulk field update to monitor asset inventory records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin, producing a dry-run preview workbook for approval before committing and a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_asset_inventory", "rar_sha256": "d81b09732fa9b32358d6540c5f557a7afc99422fdd1c076d2c7889264850f2e4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

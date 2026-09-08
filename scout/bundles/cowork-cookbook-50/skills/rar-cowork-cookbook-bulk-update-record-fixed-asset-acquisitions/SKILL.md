---
name: "rar-cowork-cookbook-bulk-update-record-fixed-asset-acquisitions"
description: "Applies a bulk field update to fixed asset acquisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pau"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_fixed_asset_acquisitions", "rar_sha256": "8f9175dfff80d03a2d47beafa35aef4d97a0f07e3783a69cb2ab232596934170", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_record_fixed_asset_acquisitions`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_record_fixed_asset_acquisitions_agent.py` and in the RCI capsule.

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

Record fixed asset acquisitions Bulk Field Update — Applies a bulk field update to fixed asset acquisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pau

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-fixed-asset-acquisitions
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
      "description": "D365 legal entity to run against; defaults to USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The field(s) and new value(s) to apply to those records.",
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
      "description": "List of fixed asset acquisition record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_record_fixed_asset_acquisitions_agent.py` and embedded as the fenced Python below (sha256 8f9175dfff80d03a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_record_fixed_asset_acquisitions_agent.py` first:

```bash
python3 bulk_update_record_fixed_asset_acquisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_record_fixed_asset_acquisitions_agent.py   # or on stdin
python3 bulk_update_record_fixed_asset_acquisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record fixed asset acquisitions Bulk Field Update — Applies a bulk field update to fixed asset acquisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pau

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-record-fixed-asset-acquisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_record_fixed_asset_acquisitions',
    "version": '3.0.3',
    "display_name": 'Record fixed asset acquisitions Bulk Field Update',
    "description": 'Applies a bulk field update to fixed asset acquisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pau',
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
        "upstream_slug": 'bulk-update-record-fixed-asset-acquisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-record-fixed-asset-acquisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '207648136b0ce6aa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/record-fixed-asset-acquisitions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-record-fixed-asset-acquisitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of fixed asset acquisition record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when record fixed asset acquisitions records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to record fixed asset acquisitions records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to fixed asset acquisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pau', 'example_request': 'Bulk update these fixed asset acquisition record IDs in USMF sandbox with the new values — show me the dry-run first.', 'inputs': [{'description': 'List of fixed asset acquisition record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many fixed asset acquisition records in D365 and want a before/after preview and approval step first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateRecordFixedAssetAcquisitions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRecordFixedAssetAcquisitions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of fixed asset acquisition record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateRecordFixedAssetAcquisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-bulk-update-record-fixed-asset-acquisitions"
description: "Applies a bulk field update to fixed asset acquisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook and approval pau"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_record_fixed_asset_acquisitions", "rar_sha256": "8f9175dfff80d03a2d47beafa35aef4d97a0f07e3783a69cb2ab232596934170", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

---
name: "rar-cowork-cookbook-bulk-update-reconcile-asset-subledger"
description: "Applies a bulk field update to reconcile asset subledger records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, an approval p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reconcile_asset_subledger", "rar_sha256": "8a4dc2e9ef14f0b5f97ec5170902b23ae66938f9c49c4b671383cb2268a75da6", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_reconcile_asset_subledger`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_reconcile_asset_subledger_agent.py` and in the RCI capsule.

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

Reconcile asset subledger Bulk Field Update — Applies a bulk field update to reconcile asset subledger records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, an approval p

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reconcile-asset-subledger
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
      "description": "D365 legal entity to run against; recipe uses USMF sandbox.",
      "type": "string"
    },
    "new_values": {
      "description": "The field value(s) to apply to those records.",
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
      "description": "List of reconcile asset subledger record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_reconcile_asset_subledger_agent.py` and embedded as the fenced Python below (sha256 8a4dc2e9ef14f0b5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_reconcile_asset_subledger_agent.py` first:

```bash
python3 bulk_update_reconcile_asset_subledger_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_reconcile_asset_subledger_agent.py   # or on stdin
python3 bulk_update_reconcile_asset_subledger_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile asset subledger Bulk Field Update — Applies a bulk field update to reconcile asset subledger records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, an approval p

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-reconcile-asset-subledger
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_reconcile_asset_subledger',
    "version": '3.0.3',
    "display_name": 'Reconcile asset subledger Bulk Field Update',
    "description": 'Applies a bulk field update to reconcile asset subledger records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, an approval p',
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
        "upstream_slug": 'bulk-update-reconcile-asset-subledger',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-reconcile-asset-subledger',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9f97589b0a3bc2d2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/reconcile-asset-subledger'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/bulk-update-reconcile-asset-subledger', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'new_values': 'The field value(s) to apply to those records.', 'record_ids': 'List of reconcile asset subledger record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when reconcile asset subledger records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to reconcile asset subledger records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to reconcile asset subledger records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, an approval p', 'example_request': 'Bulk update these reconcile asset subledger record IDs in USMF sandbox with this new value — show me the dry-run first.', 'inputs': [{'description': 'List of reconcile asset subledger record IDs to update.', 'name': 'record_ids'}, {'description': 'The field value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many reconcile asset subledger records at once in a D365 sandbox and want a before/after preview and approval step first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReconcileAssetSubledger(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReconcileAssetSubledger'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; recipe uses USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of reconcile asset subledger record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReconcileAssetSubledger().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

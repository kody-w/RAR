---
name: "rar-cowork-cookbook-bulk-update-reconcile-asset-subledger"
description: "Applies a bulk field update to reconcile asset subledger records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, with a dry-run preview workbook, an approval p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_reconcile_asset_subledger", "rar_sha256": "8a4dc2e9ef14f0b5f97ec5170902b23ae66938f9c49c4b671383cb2268a75da6", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

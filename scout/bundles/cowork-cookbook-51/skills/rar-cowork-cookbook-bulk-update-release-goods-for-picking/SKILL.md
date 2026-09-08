---
name: "rar-cowork-cookbook-bulk-update-release-goods-for-picking"
description: "Applies a bulk field update to release goods for picking records in Dynamics 365 F&SCM (legal entity USMF, sandbox), producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_release_goods_for_picking", "rar_sha256": "303075d5c25ba73d11a62ef7f9f4eca74b450faf44cb35794dec0bf755f51ace", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_release_goods_for_picking`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_release_goods_for_picking_agent.py` and in the RCI capsule.

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

Release goods for picking Bulk Field Update — Applies a bulk field update to release goods for picking records in Dynamics 365 F&SCM (legal entity USMF, sandbox), producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-release-goods-for-picking
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
      "description": "List of release goods for picking record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_release_goods_for_picking_agent.py` and embedded as the fenced Python below (sha256 303075d5c25ba73d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_release_goods_for_picking_agent.py` first:

```bash
python3 bulk_update_release_goods_for_picking_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_release_goods_for_picking_agent.py   # or on stdin
python3 bulk_update_release_goods_for_picking_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Release goods for picking Bulk Field Update — Applies a bulk field update to release goods for picking records in Dynamics 365 F&SCM (legal entity USMF, sandbox), producing a dry-run preview workbook for approval before committing and a confirmation workbook after.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-release-goods-for-picking
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_release_goods_for_picking',
    "version": '3.0.3',
    "display_name": 'Release goods for picking Bulk Field Update',
    "description": 'Applies a bulk field update to release goods for picking records in Dynamics 365 F&SCM (legal entity USMF, sandbox), producing a dry-run preview workbook for approval before committing and a confirmation workbook after.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-release-goods-for-picking',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-release-goods-for-picking',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cfaa4a326494fcb3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/release-goods-for-picking'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-release-goods-for-picking', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of release goods for picking record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when release goods for picking records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to release goods for picking records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to release goods for picking records in Dynamics 365 F&SCM (legal entity USMF, sandbox), producing a dry-run preview workbook for approval before committing and a confirmation workbook after.', 'example_request': 'Bulk update these release goods for picking IDs in USMF sandbox to the new value — show me the dry run first.', 'inputs': [{'description': 'List of release goods for picking record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across a known list of release-goods-for-picking record IDs in a D365 sandbox, with preview and approval.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateReleaseGoodsForPicking(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReleaseGoodsForPicking'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of release goods for picking record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateReleaseGoodsForPicking().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

---
name: "rar-cowork-cookbook-bulk-update-release-goods-for-picking"
description: "Applies a bulk field update to release goods for picking records in Dynamics 365 F&SCM (legal entity USMF, sandbox), producing a dry-run preview workbook for approval before committing and a confirmation workbook after."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_release_goods_for_picking", "rar_sha256": "303075d5c25ba73d11a62ef7f9f4eca74b450faf44cb35794dec0bf755f51ace", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

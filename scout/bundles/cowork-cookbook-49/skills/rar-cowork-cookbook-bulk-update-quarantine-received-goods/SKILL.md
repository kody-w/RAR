---
name: "rar-cowork-cookbook-bulk-update-quarantine-received-goods"
description: "Applies a bulk field update to quarantine received goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, pauses for approval, then a confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_quarantine_received_goods", "rar_sha256": "7b436a88ab48334628fa7569d8259c33f45a1eef82d74d862eac26d4a5c49eb1", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_quarantine_received_goods`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_quarantine_received_goods_agent.py` and in the RCI capsule.

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

Quarantine received goods Bulk Field Update — Applies a bulk field update to quarantine received goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, pauses for approval, then a confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-quarantine-received-goods
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
      "description": "Explicit approval after reviewing the dry-run preview workbook before changes are committed.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against (default USMF, sandbox).",
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
      "description": "List of quarantine received goods record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_quarantine_received_goods_agent.py` and embedded as the fenced Python below (sha256 7b436a88ab483346…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_quarantine_received_goods_agent.py` first:

```bash
python3 bulk_update_quarantine_received_goods_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_quarantine_received_goods_agent.py   # or on stdin
python3 bulk_update_quarantine_received_goods_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Quarantine received goods Bulk Field Update — Applies a bulk field update to quarantine received goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, pauses for approval, then a confirma

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-quarantine-received-goods
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_quarantine_received_goods',
    "version": '3.0.3',
    "display_name": 'Quarantine received goods Bulk Field Update',
    "description": 'Applies a bulk field update to quarantine received goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, pauses for approval, then a confirma',
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
        "upstream_slug": 'bulk-update-quarantine-received-goods',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-quarantine-received-goods',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '051b89ed85c32e87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-inbound-goods/quarantine-received-goods'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-quarantine-received-goods', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of quarantine received goods record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when quarantine received goods records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to quarantine received goods records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to quarantine received goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, pauses for approval, then a confirma', 'example_request': 'Bulk update these quarantine received goods records in USMF sandbox to the new status - show me a dry run first.', 'inputs': [{'description': 'List of quarantine received goods record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have a list of quarantine received goods record IDs and new field values to update in bulk, and want a dry-run preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateQuarantineReceivedGoods(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateQuarantineReceivedGoods'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (default USMF, sandbox).', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of quarantine received goods record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateQuarantineReceivedGoods().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

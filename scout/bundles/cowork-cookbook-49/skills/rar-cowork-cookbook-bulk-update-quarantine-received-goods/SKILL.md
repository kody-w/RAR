---
name: "rar-cowork-cookbook-bulk-update-quarantine-received-goods"
description: "Applies a bulk field update to quarantine received goods records in Dynamics 365 F&SCM (legal entity USMF, sandbox) via the Cowork D365 ERP plugin; returns a dry-run preview workbook, pauses for approval, then a confirma"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_quarantine_received_goods", "rar_sha256": "7b436a88ab48334628fa7569d8259c33f45a1eef82d74d862eac26d4a5c49eb1", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

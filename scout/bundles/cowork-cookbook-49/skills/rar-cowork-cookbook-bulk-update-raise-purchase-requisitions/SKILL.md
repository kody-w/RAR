---
name: "rar-cowork-cookbook-bulk-update-raise-purchase-requisitions"
description: "Applies a bulk field update to purchase requisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_raise_purchase_requisitions", "rar_sha256": "e1cd6accb8e0c3583fc6d599abc61b4fadf14441c4a0d635d43cf34424b20d03", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_raise_purchase_requisitions`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_raise_purchase_requisitions_agent.py` and in the RCI capsule.

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

Raise purchase requisitions Bulk Field Update — Applies a bulk field update to purchase requisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval b

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-raise-purchase-requisitions
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
      "description": "List of purchase requisition record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_raise_purchase_requisitions_agent.py` and embedded as the fenced Python below (sha256 e1cd6accb8e0c358…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_raise_purchase_requisitions_agent.py` first:

```bash
python3 bulk_update_raise_purchase_requisitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_raise_purchase_requisitions_agent.py   # or on stdin
python3 bulk_update_raise_purchase_requisitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Raise purchase requisitions Bulk Field Update — Applies a bulk field update to purchase requisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval b

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-raise-purchase-requisitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_raise_purchase_requisitions',
    "version": '3.0.3',
    "display_name": 'Raise purchase requisitions Bulk Field Update',
    "description": 'Applies a bulk field update to purchase requisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval b',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-raise-purchase-requisitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-raise-purchase-requisitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '141134ec6abfc682',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/procure-goods-and-services/raise-purchase-requisitions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-raise-purchase-requisitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of purchase requisition record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when raise purchase requisitions records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to raise purchase requisitions records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to purchase requisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval b', 'example_request': 'Bulk update these purchase requisitions in USMF sandbox to requester Jane Doe — show me the dry run first.', 'inputs': [{'description': 'List of purchase requisition record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change the same field(s) across many purchase requisition records at once and want a before/after preview and approval gate first.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateRaisePurchaseRequisitions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateRaisePurchaseRequisitions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against; defaults to USMF sandbox.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of purchase requisition record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateRaisePurchaseRequisitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

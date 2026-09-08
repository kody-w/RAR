---
name: "rar-cowork-cookbook-bulk-update-raise-purchase-requisitions"
description: "Applies a bulk field update to purchase requisition records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied list of record IDs and new values, producing a dry-run preview workbook for approval b"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_raise_purchase_requisitions", "rar_sha256": "e1cd6accb8e0c3583fc6d599abc61b4fadf14441c4a0d635d43cf34424b20d03", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

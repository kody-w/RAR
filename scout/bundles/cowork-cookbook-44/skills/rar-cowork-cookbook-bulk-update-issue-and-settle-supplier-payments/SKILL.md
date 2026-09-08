---
name: "rar-cowork-cookbook-bulk-update-issue-and-settle-supplier-payments"
description: "Applies a bulk field update to issue-and-settle supplier payment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, returning a dry-run preview workbook, then a confirmation workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_issue_and_settle_supplier_payments", "rar_sha256": "2470aa79f46d5c9e166ef62ae1c185ca798865e77e80a4766bc3eb696caf5561", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_issue_and_settle_supplier_payments`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_issue_and_settle_supplier_payments_agent.py` and in the RCI capsule.

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

Issue and settle supplier payments Bulk Field Update — Applies a bulk field update to issue-and-settle supplier payment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, returning a dry-run preview workbook, then a confirmation workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-issue-and-settle-supplier-payments
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
      "description": "D365 legal entity to run against; USMF sandbox by default.",
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
      "description": "List of issue-and-settle supplier payment record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_issue_and_settle_supplier_payments_agent.py` and embedded as the fenced Python below (sha256 2470aa79f46d5c9e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_issue_and_settle_supplier_payments_agent.py` first:

```bash
python3 bulk_update_issue_and_settle_supplier_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_issue_and_settle_supplier_payments_agent.py   # or on stdin
python3 bulk_update_issue_and_settle_supplier_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Issue and settle supplier payments Bulk Field Update — Applies a bulk field update to issue-and-settle supplier payment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, returning a dry-run preview workbook, then a confirmation workbo

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-issue-and-settle-supplier-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_issue_and_settle_supplier_payments',
    "version": '3.0.3',
    "display_name": 'Issue and settle supplier payments Bulk Field Update',
    "description": 'Applies a bulk field update to issue-and-settle supplier payment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, returning a dry-run preview workbook, then a confirmation workbo',
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
        "upstream_slug": 'bulk-update-issue-and-settle-supplier-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-issue-and-settle-supplier-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8bfe8b768ad0d43e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-accounts-payable/issue-and-settle-supplier-payments'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/bulk-update-issue-and-settle-supplier-payments', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against; USMF sandbox by default.', 'new_values': 'The field(s) and new value(s) to apply to those records.', 'record_ids': 'List of issue-and-settle supplier payment record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when issue and settle supplier payments records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to issue and settle supplier payments records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to issue-and-settle supplier payment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, returning a dry-run preview workbook, then a confirmation workbo', 'example_request': 'Bulk-update these supplier payment record IDs in USMF sandbox with the new value — show me the dry-run first.', 'inputs': [{'description': 'List of issue-and-settle supplier payment record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to those records.', 'name': 'new_values'}, {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'name': 'legal_entity'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to change a field on many issue-and-settle supplier payment records at once in a D365 sandbox and want a dry-run preview before committing.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateIssueAndSettleSupplierPayments(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateIssueAndSettleSupplierPayments'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook, before changes are committed.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against; USMF sandbox by default.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to those records.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of issue-and-settle supplier payment record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateIssueAndSettleSupplierPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->

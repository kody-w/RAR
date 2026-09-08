---
name: "rar-cowork-cookbook-bulk-update-issue-and-settle-supplier-payments"
description: "Applies a bulk field update to issue-and-settle supplier payment records in Dynamics 365 F&SCM (legal entity USMF, sandbox) from a caller-supplied ID list, returning a dry-run preview workbook, then a confirmation workbo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_issue_and_settle_supplier_payments", "rar_sha256": "2470aa79f46d5c9e166ef62ae1c185ca798865e77e80a4766bc3eb696caf5561", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

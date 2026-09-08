---
name: "rar-cowork-cookbook-bulk-update-settle-customer-transactions"
description: "Applies a bulk field update to settle customer transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_settle_customer_transactions", "rar_sha256": "5626452acec355bd30507e2c41bf5302ff6932f476ac82357c73ac49f1c67d19", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_settle_customer_transactions`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_settle_customer_transactions_agent.py` and in the RCI capsule.

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

Settle customer transactions Bulk Field Update — Applies a bulk field update to settle customer transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-settle-customer-transactions
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
      "description": "Explicit approval after reviewing the dry-run preview workbook.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; sandbox only.",
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
      "description": "List of settle customer transactions record IDs to update.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_settle_customer_transactions_agent.py` and embedded as the fenced Python below (sha256 5626452acec355bd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_settle_customer_transactions_agent.py` first:

```bash
python3 bulk_update_settle_customer_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_settle_customer_transactions_agent.py   # or on stdin
python3 bulk_update_settle_customer_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Settle customer transactions Bulk Field Update — Applies a bulk field update to settle customer transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes.

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
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-settle-customer-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_settle_customer_transactions',
    "version": '3.0.3',
    "display_name": 'Settle customer transactions Bulk Field Update',
    "description": 'Applies a bulk field update to settle customer transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-settle-customer-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-settle-customer-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c77b061721e06fef',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/settle-customer-transactions'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-settle-customer-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit approval after reviewing the dry-run preview workbook.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'new_values': 'The field(s) and new value(s) to apply to each record.', 'record_ids': 'List of settle customer transactions record IDs to update.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Avoids the click-by-click drudgery (and risk of inconsistency) when settle customer transactions records need a coordinated change - and the dry-run preview catches mistakes before they hit the system.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), apply a bulk field update to settle customer transactions records. Input format: I'll provide a list of record IDs and the new value(s). Produce a dry-run preview workbook showing every proposed change (before / after / status). Pause and ask for approval. After I approve, apply the changes and emit a confirmation workbook. WARNING: this recipe modifies data - sandbox only, and have a rollback plan.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads target record IDs + desired field values, previews changes, then applies them after explicit approval.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies a bulk field update to settle customer transactions records in Dynamics 365 F&SCM via the Cowork ERP plugin, producing a dry-run preview workbook for approval before committing changes.', 'example_request': 'Bulk update these settle customer transaction IDs in USMF sandbox with the new value — show me the dry run first.', 'inputs': [{'description': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'name': 'legal_entity'}, {'description': 'List of settle customer transactions record IDs to update.', 'name': 'record_ids'}, {'description': 'The field(s) and new value(s) to apply to each record.', 'name': 'new_values'}, {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to update many settle customer transactions records at once from a list of record IDs, with a reviewable preview before any data is written.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class BulkUpdateSettleCustomerTransactions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateSettleCustomerTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit approval after reviewing the dry-run preview workbook.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; sandbox only.', 'type': 'string'}, 'new_values': {'description': 'The field(s) and new value(s) to apply to each record.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'record_ids': {'description': 'List of settle customer transactions record IDs to update.', 'type': 'string'}},
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
    print(BulkUpdateSettleCustomerTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
